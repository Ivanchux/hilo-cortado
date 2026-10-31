# Hilo Cortado · prompts del logo y del icono (completos, para pegar tal cual)

Son dos imágenes y se piden por separado. Cada prompt es independiente: no hay que cambiar nada.

- **1 · Logo oficial** → guárdalo como `logo_hilo_cortado.png`. Va sobre **fondo verde liso `#00FF00`** (yo lo paso a transparente).
- **2 · Icono** → guárdalo como `icono_hilo_cortado.png`. Es un **cuadrado a sangre** (sin fondo verde): de ahí salen el favicon, el icono de 512 px y el de la pantalla de inicio del móvil.
- **3 · Icono, variante B (opcional)** → si prefieres la cara de Clavija en vez del símbolo. Adjunta `cara_clavija.png`.

Con ChatGPT, a veces el texto sale con una letra mal: si pasa, usa la frase del final y vuelve a generar (el nombre es **HILO CORTADO**, sin tildes ni signos).

---

## 1 · Logo oficial — `logo_hilo_cortado.png` (16:9)

```
Official logo lockup for a video game titled "HILO CORTADO" (Spanish for "Cut Thread"), a puppet-theatre beat 'em up. Wide 16:9 canvas with the logo centered and filling about 80% of the width, with an even margin. The title is set on two stacked lines, "HILO" on the first line and "CORTADO" on the second, spelled exactly H-I-L-O and C-O-R-T-A-D-O, in bold hand-carved wooden capital letters with painted gold-leaf edges, a warm honey-and-walnut wood tone, a thick dark-brown outline and soft cel shading, in the style of an old travelling puppet-theatre sign. A single bright red thread runs through the letters like a stitch, and in the middle it is sharply cut in two by a pair of silver tailor's scissors, with the two thread ends frayed and dangling. Above the title, small and centered, a wooden marionette control cross (a long horizontal bar with a shorter bar across it, with small brass eyelets) from which a few short red strings hang down onto the letters. The whole emblem is compact, symmetrical, high contrast and instantly readable even at a small size. Hand-painted illustration, warm light from the top left, deep red, aged gold and wood-brown palette, polished indie-game look, matching a painted puppet-theatre game. No other text, no tagline, no letters other than HILO CORTADO, no logos, no watermark, no cast shadow, no characters. Plain flat solid #00FF00 green background, nothing else.
```

## 2 · Icono — `icono_hilo_cortado.png` (cuadrado 1:1)

```
A square game icon, perfectly square 1:1, full-bleed (the artwork fills the entire square edge to edge, no transparent corners, no outer margin; the corners will be rounded later). Background: a deep red velvet theatre curtain with soft vertical folds, a thin aged-gold border line inset near the edges, a warm glow in the center. In the center, big and bold: a wooden marionette control cross (a long horizontal bar with a shorter bar across it, brass eyelets) near the top, and from it ONE single bright red thread hanging straight down the middle, which is sharply cut in two by a pair of silver tailor's scissors in the lower half, the two thread ends frayed. Very simple, large, chunky shapes with a thick dark-brown outline and flat saturated colors with soft cel shading, designed to stay perfectly readable at 16 by 16 pixels. The symbol is centered with a generous margin (about 14% on every side) and nothing touches the edges. Hand-painted, warm light from the top left, polished indie-game icon. No text, no letters, no numbers, no logos, no watermark, no cast shadow.
```

## 3 · Icono, variante B (opcional) — `icono_b_hilo_cortado.png`  (adjunta `cara_clavija.png`)

```
A square game icon, perfectly square 1:1, full-bleed (the artwork fills the entire square edge to edge, no transparent corners). Use the attached image as the exact reference for the character: it is the wooden marionette head of Clavija, the hero, with the red cap. Draw this head large and centered, in side profile facing right, in the same painted style as the reference, on a deep red velvet theatre curtain background with soft vertical folds and a thin aged-gold border line inset near the edges. A single bright red thread comes down from the top of the head and is sharply cut in half by a small pair of silver scissors at the top-right, the two ends frayed and dangling. Bold, simple, high-contrast shapes with a thick dark-brown outline, designed to stay readable at 16 by 16 pixels. The head fills about 70% of the square with an even margin. Warm light from the top left. No text, no letters, no logos, no watermark, no cast shadow.
```

---

## Si una imagen sale mal

Pega esto en la misma conversación y vuelve a generar, sin tocar el prompt:

```
Regenerate the same image. Keep everything identical except this one fix: spell the title exactly HILO CORTADO with no extra or missing letters and no other text anywhere, keep the exact layout and background requested, and keep the same hand-painted puppet-theatre style.
```

Cuando me pases las imágenes ejecuto `python3 tools/build-logo.py` (genera `capturas/logo.png`, los iconos y los favicons) y pongo el logo en el README.
