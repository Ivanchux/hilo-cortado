#!/usr/bin/env python3
"""Prepara el arte de Hilo Cortado a partir de las ilustraciones originales.

Uso: python3 tools/build-art.py CARPETA   (con estos nombres: fondo_bosque.png, fondo_ciudad.png, fondo_castillo.png,
     fondo_telar.png, marco.png, caras.png, textura_madera.png, textura_tela.png)
Escribe en img/: los decorados recortados (sin telón ni suelo), el marco con transparencia, una cara por marioneta
(con transparencia) y las dos texturas. Necesita Pillow y NumPy.
"""
import sys, pathlib
import numpy as np
from PIL import Image, ImageFilter

root = pathlib.Path(__file__).resolve().parent.parent
src = pathlib.Path(sys.argv[1]); out = root / 'img'; out.mkdir(exist_ok=True)

def key(im):
    a = np.asarray(im.convert('RGB')).astype(np.float32)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    spill = g - np.maximum(r, b)
    alpha = np.clip(1 - (spill - 40) / 90, 0, 1); alpha[spill < 40] = 1
    g2 = np.where(spill > 0, np.minimum(g, np.maximum(r, b) + 6), g)
    return Image.fromarray(np.dstack([r, g2, b, alpha * 255]).clip(0, 255).astype(np.uint8), 'RGBA')

def quitar_filas(im, mask):
    """Rellena la zona enmascarada interpolando en horizontal, fila a fila, entre el cielo de cada lado (respeta el degradado vertical)."""
    a = np.asarray(im).astype(np.float32).copy(); rng = np.random.default_rng(2)
    for y in np.where(mask.any(1))[0]:
        xs = np.where(mask[y])[0]; x0, x1 = xs.min() - 1, xs.max() + 1
        l = a[y, max(x0 - 26, 0):x0 + 1].mean(0); r = a[y, x1:x1 + 27].mean(0)
        t = ((np.arange(x0 + 1, x1) - x0) / (x1 - x0))[:, None]; a[y, x0 + 1:x1] = l * (1 - t) + r * t
    f = np.asarray(Image.fromarray((mask * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(3))).astype(np.float32)[..., None] / 255
    sm = np.asarray(Image.fromarray(a.clip(0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(14))).astype(np.float32)
    out = np.asarray(im).astype(np.float32) * (1 - f) + (sm + rng.normal(0, 2.2, a.shape)) * f
    return Image.fromarray(out.clip(0, 255).astype(np.uint8))

def quitar(im, mask, iters=6000, f=4):
    """Rellena la zona enmascarada con el color de alrededor (difusión de Laplace). Se resuelve a 1/f de resolución para que converja
    y se reescala; solo cambia lo enmascarado. im: PIL RGB, mask: booleana."""
    a = np.asarray(im).astype(np.float32).copy()
    ys, xs = np.where(mask); y0, y1, x0, x1 = max(ys.min() - 10, 0), ys.max() + 11, max(xs.min() - 10, 0), xs.max() + 11
    sub = a[y0:y1, x0:x1]; m = mask[y0:y1, x0:x1]
    h, w = sub.shape[:2]; sh, sw = max(h // f, 4), max(w // f, 4)
    small = np.asarray(Image.fromarray(sub.clip(0, 255).astype(np.uint8)).resize((sw, sh), Image.BOX)).astype(np.float32)
    ms = np.asarray(Image.fromarray((m * 255).astype(np.uint8)).resize((sw, sh), Image.BOX)) > 8   # lo dudoso cuenta como enmascarado
    small[ms] = small[~ms].mean(0)
    for _ in range(iters):
        p = np.pad(small, ((1, 1), (1, 1), (0, 0)), mode='edge')
        small[ms] = ((p[:-2, 1:-1] + p[2:, 1:-1] + p[1:-1, :-2] + p[1:-1, 2:]) / 4)[ms]
    big = np.asarray(Image.fromarray(small.clip(0, 255).astype(np.uint8)).resize((w, h), Image.BICUBIC)).astype(np.float32)
    feather = np.asarray(Image.fromarray((m * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(4))).astype(np.float32)[..., None] / 255
    rng = np.random.default_rng(1)
    sub[:] = sub * (1 - feather) + (big + rng.normal(0, 2.2, big.shape)) * feather   # grano parecido al de la pintura
    return Image.fromarray(a.clip(0, 255).astype(np.uint8))

def disco(shape, cx, cy, r):
    yy, xx = np.ogrid[:shape[0], :shape[1]]
    return (xx - cx) ** 2 + (yy - cy) ** 2 <= r * r

# Decorados: se recorta solo el escenario (fuera telón, cenefa y suelo); fracciones x0, x1, y0, y1 de la imagen
CROPS = {'bosque': (.12, .88, .10, .81), 'ciudad': (.05, .95, .13, .81), 'castillo': (.06, .93, .14, .80), 'telar': (.03, .97, .04, .82)}
for k, (x0, x1, y0, y1) in CROPS.items():
    im = Image.open(src / f'fondo_{k}.png').convert('RGB'); W, H = im.size
    # la luna y el sol se quitan del decorado: repetido en espejo saldrían dos. La luna se dibuja por código.
    if k == 'bosque':
        mk = disco((H, W), W * .641, H * .251, 150); mk[int(H * .08):int(H * .14), int(W * .641) - 7:int(W * .641) + 8] = True; im = quitar_filas(im, mk)
    elif k == 'ciudad':
        a = np.asarray(im).astype(int); mk = disco((H, W), W * .477, H * .298, 72) & (a.sum(2) > 330); im = quitar(im, mk)
    c = im.crop((round(W * x0), round(H * y0), round(W * x1), round(H * y1)))
    h = 480; c = c.resize((round(c.width * h / c.height), h), Image.LANCZOS)
    c.save(out / f'fondo_{k}.jpg', quality=82, optimize=True, progressive=True); print('fondo', k, c.size)

# Marco del escenario: el hueco verde pasa a transparente
m = key(Image.open(src / 'marco.png')); m = m.resize((1440, round(1440 * m.height / m.width)), Image.LANCZOS)
m.save(out / 'marco.png', optimize=True); print('marco', m.size)

# Caras: hoja de 4 x 2 en este orden. Cada cabeza se separa por componentes conectados (los sombreros invaden las celdas vecinas)
NAMES = ['clavija', 'bramante', 'comparsa', 'alabardero', 'saltimbanqui', 'costurera', 'mozo', 'titiritero']
from collections import deque
from PIL import ImageFilter

def components(mask, step=4):
    """Etiqueta los componentes conectados de una máscara booleana (sobre una versión reducida y dilatada). Devuelve (etiquetas a tamaño completo, nº)."""
    small = Image.fromarray((mask * 255).astype(np.uint8)).resize((mask.shape[1] // step, mask.shape[0] // step), Image.BOX).point(lambda v: 255 if v > 20 else 0)
    small = small.filter(ImageFilter.MaxFilter(3)); sm = np.asarray(small) > 0
    lab = np.zeros(sm.shape, np.int32); n = 0
    for y, x in zip(*np.where(sm)):
        if lab[y, x]: continue
        n += 1; q = deque([(y, x)]); lab[y, x] = n
        while q:
            cy, cx = q.popleft()
            for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ny, nx = cy + dy, cx + dx
                if 0 <= ny < sm.shape[0] and 0 <= nx < sm.shape[1] and sm[ny, nx] and not lab[ny, nx]: lab[ny, nx] = n; q.append((ny, nx))
    full = np.kron(lab, np.ones((step, step), np.int32))
    out = np.zeros(mask.shape, np.int32); h, w = min(full.shape[0], mask.shape[0]), min(full.shape[1], mask.shape[1]); out[:h, :w] = full[:h, :w]
    return out, n
sheet = key(Image.open(src / 'caras.png')); W, H = sheet.size
al = np.asarray(sheet.getchannel('A')) > 40
lab, n = components(al)
sizes = np.array([((lab == i) & al).sum() for i in range(1, n + 1)]); big = [i + 1 for i in np.argsort(sizes)[::-1][:8]]
if len(big) != 8 or min(sizes[i - 1] for i in big) < 0.2 * max(sizes): raise SystemExit('no se han encontrado 8 cabezas separadas en caras.png')
cent = {i: tuple(np.argwhere((lab == i) & al).mean(0)) for i in big}   # (y, x)
rows = sorted(big, key=lambda i: cent[i][0]); order = sorted(rows[:4], key=lambda i: cent[i][1]) + sorted(rows[4:], key=lambda i: cent[i][1])
rgba = np.asarray(sheet).copy()
for name, i in zip(NAMES, order):
    m = (lab == i) & al
    ys, xs = np.where(m); y0, y1, x0, x1 = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
    piece = rgba[y0:y1, x0:x1].copy(); piece[..., 3] = np.where(m[y0:y1, x0:x1], piece[..., 3], 0)
    im = Image.fromarray(piece, 'RGBA'); s = 220 / im.height
    im = im.resize((round(im.width * s), 220), Image.LANCZOS)
    im.save(out / f'cara_{name}.png', optimize=True); print('cara', name, im.size)

# Texturas repetibles
for k in ('madera', 'tela'):
    t = Image.open(src / f'textura_{k}.png').convert('RGB').resize((192, 192), Image.LANCZOS)
    t.save(out / f'textura_{k}.jpg', quality=88, optimize=True); print('textura', k)
