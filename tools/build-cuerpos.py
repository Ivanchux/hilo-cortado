#!/usr/bin/env python3
"""Recorta las hojas de piezas de las marionetas y la hoja de objetos.

Uso: python3 tools/build-cuerpos.py CARPETA
La carpeta debe tener cuerpo_<personaje>.png (8 piezas en una cuadrícula de 4 x 2: torso, brazo, antebrazo con mano, muslo,
espinilla, bota y dos complementos) y objetos.png (12 objetos en una cuadrícula de 4 x 3).
Escribe img/cuerpos/<personaje>_<pieza>.png, img/objetos/<objeto>.png y, dentro de index.html (entre los marcadores /*CUERPOS*/ y /*FIN-CUERPOS*/), las medidas y los puntos de giro de cada pieza.
"""
import json, sys, pathlib
from collections import deque
import numpy as np
from PIL import Image, ImageFilter

root = pathlib.Path(__file__).resolve().parent.parent
src = pathlib.Path(sys.argv[1])
PARTS = ['torso', 'uarm', 'farm', 'thigh', 'shin', 'boot', 'a1', 'a2']
OBJS = ['tijeras', 'tijerona', 'alabarda', 'mazo', 'vela', 'baston', 'carrete', 'ovillo', 'caja', 'cesto', 'tonel', 'cruceta']
MAXSIDE = {'torso': 190, 'uarm': 170, 'farm': 190, 'thigh': 180, 'shin': 170, 'boot': 150, 'a1': 200, 'a2': 200}

def key(img):
    a = np.asarray(img.convert('RGB')).astype(np.float32)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    spill = g - np.maximum(r, b)
    alpha = np.clip(1 - (spill - 40) / 90, 0, 1); alpha[spill < 40] = 1
    g2 = np.where(spill > 0, np.minimum(g, np.maximum(r, b) + 6), g)
    return Image.fromarray(np.dstack([r, g2, b, alpha * 255]).clip(0, 255).astype(np.uint8), 'RGBA')

def components(mask, step=4):
    small = Image.fromarray((mask * 255).astype(np.uint8)).resize((mask.shape[1] // step, mask.shape[0] // step), Image.BOX).point(lambda v: 255 if v > 20 else 0)
    sm = np.asarray(small.filter(ImageFilter.MaxFilter(3))) > 0
    lab = np.zeros(sm.shape, np.int32); n = 0
    for y, x in zip(*np.where(sm)):
        if lab[y, x]: continue
        n += 1; q = deque([(y, x)]); lab[y, x] = n
        while q:
            cy, cx = q.popleft()
            for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ny, nx = cy + dy, cx + dx
                if 0 <= ny < sm.shape[0] and 0 <= nx < sm.shape[1] and sm[ny, nx] and not lab[ny, nx]: lab[ny, nx] = n; q.append((ny, nx))
    full = np.kron(lab, np.ones((step, step), np.int32)); out = np.zeros(mask.shape, np.int32)
    h, w = min(full.shape[0], mask.shape[0]), min(full.shape[1], mask.shape[1]); out[:h, :w] = full[:h, :w]
    return out, n

def cells(sheet, cols, rows):
    """Devuelve {índice de celda: imagen RGBA recortada} (varias piezas en la misma celda se unen)."""
    im = key(Image.open(sheet)); H, W = im.height, im.width
    al = np.asarray(im.getchannel('A')) > 40; lab, n = components(al); rgba = np.asarray(im)
    acc = {}
    for i in range(1, n + 1):
        m = (lab == i) & al
        if m.sum() < 400: continue
        cy, cx = np.argwhere(m).mean(0); idx = min(int(cy // (H / rows)), rows - 1) * cols + min(int(cx // (W / cols)), cols - 1)
        acc[idx] = acc.get(idx, np.zeros_like(al)) | m
    res = {}
    for idx, m in acc.items():
        ys, xs = np.where(m); y0, y1, x0, x1 = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
        piece = rgba[y0:y1, x0:x1].copy(); piece[..., 3] = np.where(m[y0:y1, x0:x1], piece[..., 3], 0)
        res[idx] = Image.fromarray(piece, 'RGBA')
    return res

def peg(im, top=True):
    """Centro del pivote del extremo de arriba (o de abajo): x e y como fracción del tamaño."""
    a = np.asarray(im.getchannel('A')) > 40; h, w = a.shape; band = max(2, int(h * .05))
    rows = a[:band] if top else a[-band:]; xs = np.where(rows.any(0))[0]
    if len(xs) == 0: return .5, (.07 if top else .93)
    r = (xs.max() - xs.min() + 1) / 2
    py = float(np.clip(r / h, .03, .12)); return round(float(xs.mean() / w), 3), round(py if top else 1 - py, 3)

def fit(im, side):
    s = side / max(im.size); return im.resize((max(1, round(im.width * s)), max(1, round(im.height * s))), Image.LANCZOS)

meta = {'cuerpos': {}, 'objetos': {}}
(root / 'img' / 'cuerpos').mkdir(parents=True, exist_ok=True); (root / 'img' / 'objetos').mkdir(parents=True, exist_ok=True)
for f in sorted(src.glob('cuerpo_*.png')):
    char = f.stem[len('cuerpo_'):]; meta['cuerpos'][char] = {}
    got = cells(f, 4, 2)
    for idx, name in enumerate(PARTS):
        if idx not in got: continue
        im = fit(got[idx], MAXSIDE[name]); px, py = peg(im, True); bx, by = peg(im, False)
        im.save(root / 'img' / 'cuerpos' / f'{char}_{name}.png', optimize=True)
        meta['cuerpos'][char][name] = {'w': im.width, 'h': im.height, 'px': px, 'py': py, 'bx': bx, 'by': by}
    print(char, sorted(meta['cuerpos'][char]))
got = cells(src / 'objetos.png', 4, 3)
for idx, name in enumerate(OBJS):
    if idx not in got: continue
    im = fit(got[idx], 170); im.save(root / 'img' / 'objetos' / f'{name}.png', optimize=True); meta['objetos'][name] = {'w': im.width, 'h': im.height}
print('objetos', sorted(meta['objetos']))
html = (root / 'index.html').read_text(encoding='utf-8')
block = '/*CUERPOS*/\n// Generado por tools/build-cuerpos.py: medidas y puntos de giro (fracciones) de las piezas ilustradas y de los objetos\nconst CUERPOS = ' + json.dumps(meta['cuerpos'], separators=(',', ':')) + ';\nconst OBJETOS = ' + json.dumps(meta['objetos'], separators=(',', ':')) + ';\n/*FIN-CUERPOS*/'
if '/*CUERPOS*/' in html: html = html[:html.index('/*CUERPOS*/')] + block + html[html.index('/*FIN-CUERPOS*/') + len('/*FIN-CUERPOS*/'):]
else: raise SystemExit('Faltan los marcadores /*CUERPOS*/ y /*FIN-CUERPOS*/ en index.html')
(root / 'index.html').write_text(html, encoding='utf-8')
print('index.html actualizado')
