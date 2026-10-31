# Hilo Cortado · prompts de ilustraciones (completos, uno por imagen)

Cada prompt se pega **tal cual**. Los 4 fondos son **16:9 (1792×1024 o similar)** y sin fondo verde; las 2 texturas son **cuadradas y repetibles**; el marco y las caras van sobre **fondo verde liso `#00FF00`**.

**Por qué no son hojas de animación.** Los personajes de Hilo Cortado son marionetas de piezas (cabeza, torso, brazos, piernas) que el juego mueve por código, y los hilos se cortan de verdad: un brazo cortado cuelga y la marioneta se desploma. Por eso el arte entra como **piezas y texturas** que se dibujan sobre ese esqueleto, y no como fotogramas. Así se conservan todas las mecánicas.

**Qué hará el juego con cada cosa**
- **Fondos (1 a 4):** sustituyen al decorado dibujado por código. Se repiten en espejo al desplazarse el escenario, para que no se vea la costura.
- **Texturas (5 y 6):** se aplican a la madera de brazos y piernas y a la ropa, teñidas con los colores de cada marioneta.
- **Marco (7):** el telón rojo, la cenefa dorada y las candilejas, con el hueco central en verde.
- **Caras (8):** la cabeza con su sombrero de cada marioneta, en lugar de las dibujadas por código.

**Orden recomendado:** 1, 2, 3, 4 (los fondos son lo que más cambia), luego 7, 5, 6 y 8.

---

## 1 · Acto I · El Bosque Pintado — `fondo_acto1.png`

```
Wide 16:9 painted theatre backdrop. A night forest made of cardboard cut-out trees on little wheels, layered in three depths (dark far hills, mid trees, big near trees), a large pale moon hanging from a visible thin string, a few painted stars, deep green and teal night colors with a moonlit glow. The trees must look like flat painted cardboard stage props, with small visible wooden supports at their bases. The bottom third of the image is where a wooden stage floor will be added by the game, so keep that lower part simple, calm and darker, with nothing important in it. Illustration style: a hand-made travelling puppet theatre of the 1800s. Painted canvas scenery flats, cardboard cut-outs, wooden stage, warm lamplight from candle footlights, rich deep red, aged gold, wood brown and dusk blue palette, slightly worn and handcrafted, soft clear dark-brown outlines, hand-painted digital illustration for a polished indie game. No text, no letters, no logos, no watermark, no characters, no people, original design.
```

## 2 · Acto II · La Ciudad de Tela — `fondo_acto2.png`

```
Wide 16:9 painted theatre backdrop. A town at dusk made of tall houses built from stitched patchwork fabric in dusty purple, blue, ochre and olive, visible seams and stitches, little glowing windows, hanging paper lanterns, clotheslines strung between the houses with small triangular bunting flags, a big warm orange sunset sky glowing behind the roofs. The houses look like flat painted canvas flats. The bottom third of the image is where a wooden stage floor will be added by the game, so keep that lower part simple, calm and darker, with nothing important in it. Illustration style: a hand-made travelling puppet theatre of the 1800s. Painted canvas scenery flats, cardboard cut-outs, wooden stage, warm lamplight from candle footlights, rich deep red, aged gold, wood brown and dusk blue palette, slightly worn and handcrafted, soft clear dark-brown outlines, hand-painted digital illustration for a polished indie game. No text, no letters, no logos, no watermark, no characters, no people, original design.
```

## 3 · Acto III · El Castillo de Tramoya — `fondo_acto3.png`

```
Wide 16:9 painted theatre backdrop. The inside of a painted stone castle hall: dark grey-blue stone walls with painted bricks, tall arched openings, hanging heraldic banners in dull red and gold, big canvas sacks of counterweight hanging from ropes, wooden pulleys and ropes, a few torches casting warm light. Moody, darker and heavier than the other acts, but still clearly painted canvas. The bottom third of the image is where a wooden stage floor will be added by the game, so keep that lower part simple, calm and darker, with nothing important in it. Illustration style: a hand-made travelling puppet theatre of the 1800s. Painted canvas scenery flats, cardboard cut-outs, wooden stage, warm lamplight from candle footlights, rich deep red, aged gold, wood brown and dusk blue palette, slightly worn and handcrafted, soft clear dark-brown outlines, hand-painted digital illustration for a polished indie game. No text, no letters, no logos, no watermark, no characters, no people, original design.
```

## 4 · Final · El telar (jefe final) — `fondo_telar.png`

```
Wide 16:9 theatre backdrop showing the bare backstage rigging loft of a puppet theatre, seen from the stage: dark old brick wall, tall wooden ladders, a high gridiron of beams, many ropes and thin strings hanging down, pulleys and iron wheels, a few sandbags hanging, dust in warm shafts of light. Almost black and brown, tense and bare, nothing painted or decorative, the raw machinery behind the show. The bottom third of the image is where a wooden stage floor will be added by the game, so keep that lower part simple, calm and darker, with nothing important in it. Illustration style: a hand-made travelling puppet theatre of the 1800s. Painted canvas scenery flats, cardboard cut-outs, wooden stage, warm lamplight from candle footlights, rich deep red, aged gold, wood brown and dusk blue palette, slightly worn and handcrafted, soft clear dark-brown outlines, hand-painted digital illustration for a polished indie game. No text, no letters, no logos, no watermark, no characters, no people, original design.
```

## 5 · Textura de madera — `textura_madera.png` (cuadrada 1:1)

```
A perfectly seamless tileable square texture of light pine wood planks seen from the front, visible vertical grain, a few small knots, subtle worn edges and tiny cracks, warm honey color, even lighting without shadows or vignette, no objects, the pattern must repeat without visible seams in all four directions. Hand-painted look, matching a handmade puppet theatre. No text, no letters, no logos, no watermark.
```

## 6 · Textura de tela — `textura_tela.png` (cuadrada 1:1)

```
A perfectly seamless tileable square texture of coarse linen and burlap cloth with a visible woven thread pattern and a few tiny stitched seams, warm cream beige color, even lighting without shadows or vignette, no objects, the pattern must repeat without visible seams in all four directions. Hand-painted look, matching a handmade puppet theatre. No text, no letters, no logos, no watermark.
```

## 7 · Marco del escenario — `marco_proscenio.png` (16:9)

```
A theatre proscenium frame seen from the audience, wide 16:9, perfectly symmetrical. On the left and right edges, thick deep-red velvet curtains with heavy folds, each about 4% of the image width; across the top, a deep-red scalloped valance with gold fringe and a small golden ornament in the middle shaped like a puppet control cross (a horizontal bar with a vertical bar), about 6% of the image height; along the bottom, a dark wooden stage lip about 10% of the image height with a row of small candle footlights glowing warm orange-yellow, evenly spaced. EVERYTHING INSIDE the frame (the whole central opening) is one completely flat solid #00FF00 green with nothing on it, so it can be removed. Illustration style: a hand-made travelling puppet theatre of the 1800s. Painted canvas scenery flats, cardboard cut-outs, wooden stage, warm lamplight from candle footlights, rich deep red, aged gold, wood brown and dusk blue palette, slightly worn and handcrafted, soft clear dark-brown outlines, hand-painted digital illustration for a polished indie game. No text, no letters, no logos, no watermark, no characters, no people, original design. Plain flat solid #00FF00 green in the central opening, no other text, no logos, no watermark.
```

## 8 · Las ocho caras de las marionetas — `caras.png` (16:9)

Una sola hoja con las ocho cabezas, **4 columnas × 2 filas**, todas del mismo tamaño y alineadas. Cada cabeza va **de perfil mirando a la derecha**, con su sombrero puesto, sin cuello ni cuerpo.

```
A character head sheet for wooden puppets, 8 heads in a perfectly aligned grid of 4 columns by 2 rows on a 16:9 canvas, same scale for all, equal spacing, nothing overlapping or cut off, each head in side profile facing right, wearing its hat, no neck and no body, carved and painted wood with visible grain, round glass-bead eyes, rosy painted cheeks, hand-painted detail. In reading order: 1 CLAVIJA: light pine wood, a faded red cap with a short peak, friendly young face; 2 BRAMANTE: dark walnut wood, a dark green beret, a little rough and kind; 3 COMPARSA: tan wood, a brown conical hat with small bells, plain simple face; 4 ALABARDERO: pale wood, a polished steel morion helmet with a crest, stern face; 5 SALTIMBANQUI: pale wood, a long pointed magenta hat, a narrow face, mischievous smile; 6 COSTURERA: pale wood, a cream cloth bonnet, a pinched, sharp face; 7 MOZO DE TRAMOYA: reddish-brown wood, a red kerchief tied over the head, a big heavy square face; 8 EL TITIRITERO: smooth bone-white porcelain mask face with a thin painted red smile and black hollow eyes, wearing a very wide black felt hat, sinister. Illustration style: a hand-made travelling puppet theatre of the 1800s. Painted canvas scenery flats, cardboard cut-outs, wooden stage, warm lamplight from candle footlights, rich deep red, aged gold, wood brown and dusk blue palette, slightly worn and handcrafted, soft clear dark-brown outlines, hand-painted digital illustration for a polished indie game. No text, no letters, no logos, no watermark, no characters, no people, original design. Plain flat solid #00FF00 green background in every cell, no ground, no shadows, no text, no letters, no logos, no watermark.
```

---

## Si una imagen sale mal

No hace falta editar el prompt. Pega esto en la misma conversación y vuelve a generar:

```
Regenerate the same image. Keep everything identical except this one fix: respect the exact layout, composition and proportions that were requested (including the empty flat green areas or the calm dark lower third where asked), and keep the same hand-painted puppet-theatre style.
```

Cuando me pases los archivos con esos nombres los integro con un respaldo: si falta alguno, el juego sigue usando el dibujo por código de esa parte.
