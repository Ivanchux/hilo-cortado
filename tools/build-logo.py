#!/usr/bin/env python3
"""Genera el logo y los iconos de Hilo Cortado.

Uso: python3 tools/build-logo.py CARPETA   (con logo_hilo_cortado.png sobre verde #00FF00 y icono_hilo_cortado.png cuadrado)
Escribe capturas/logo.png (transparente), icon-512.png, apple-touch-icon.png, favicon-32.png, favicon-16.png y favicon.ico.
Necesita Pillow y NumPy. Cualquiera de las dos imágenes puede faltar: se genera solo lo que haya.
"""
import sys, pathlib
import numpy as np
from PIL import Image, ImageDraw

root = pathlib.Path(__file__).resolve().parent.parent
src = pathlib.Path(sys.argv[1])

def key(img):
    a = np.asarray(img.convert('RGB')).astype(np.float32)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    spill = g - np.maximum(r, b)
    alpha = np.clip(1 - (spill - 40) / 90, 0, 1); alpha[spill < 40] = 1
    g2 = np.where(spill > 0, np.minimum(g, np.maximum(r, b) + 6), g)
    return Image.fromarray(np.dstack([r, g2, b, alpha * 255]).clip(0, 255).astype(np.uint8), 'RGBA')

logo = src / 'logo_hilo_cortado.png'
if logo.exists():
    im = key(Image.open(logo)); im = im.crop(im.getchannel('A').point(lambda v: 255 if v > 40 else 0).getbbox())
    im = im.resize((900, round(900 * im.height / im.width)), Image.LANCZOS)
    im.save(root / 'capturas' / 'logo.png', optimize=True); print('logo', im.size)

icon = src / 'icono_hilo_cortado.png'
if icon.exists():
    im = Image.open(icon).convert('RGB'); s = min(im.size); im = im.crop(((im.width - s) // 2, (im.height - s) // 2, (im.width + s) // 2, (im.height + s) // 2))
    def rounded(size, radius):
        x = im.resize((size, size), Image.LANCZOS).convert('RGBA'); m = Image.new('L', (size, size), 0)
        ImageDraw.Draw(m).rounded_rectangle([0, 0, size - 1, size - 1], radius=int(size * radius), fill=255); x.putalpha(m); return x
    rounded(512, .18).save(root / 'icon-512.png', optimize=True)
    im.resize((180, 180), Image.LANCZOS).save(root / 'apple-touch-icon.png', optimize=True)   # iOS aplica sus propias esquinas
    rounded(32, .16).save(root / 'favicon-32.png', optimize=True); rounded(16, .16).save(root / 'favicon-16.png', optimize=True)
    rounded(64, .16).save(root / 'favicon.ico', sizes=[(16, 16), (32, 32), (48, 48), (64, 64)]); print('iconos listos')
