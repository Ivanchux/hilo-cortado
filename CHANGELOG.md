# Registro de cambios

## 1.3 · Arte ilustrado
- **Marionetas ilustradas.** Los diez personajes (Clavija, Bramante, Comparsa, Alabardero, Saltimbanqui, Costurera, Mozo, Titiritero y los jefes Mozo Mayor y Madre Tijera) se dibujan con piezas ilustradas (torso, brazo, antebrazo con mano, muslo, espinilla, bota y complementos) rotadas entre las articulaciones. Se conserva todo el sistema de hilos: un brazo cortado cuelga y la marioneta desplomada queda hecha un montón de piezas. Las piezas del lado lejano se oscurecen, y hay destello al golpear y variante quemada.
- **Decorados ilustrados** para los tres actos y el telar del jefe, repetidos en espejo sin costura; **marco del escenario** (telón, cenefa y candilejas), **caras**, **texturas** de madera y tela en el suelo, y **armas y objetos** ilustrados (tijeras, tijerona, alabarda, mazo, vela, bastón, carrete, ovillo, caja, cesto y tonel).
- Todo con **respaldo por código**: si una imagen falta, esa parte se dibuja como antes. El juego sigue a 60 fps.
- **Animación:** aplastamiento y estiramiento al saltar y aterrizar, polvo al arrancar la carrera, al derrapar al cambiar de sentido y al correr.
- La luna del Acto I se dibuja por código (en el decorado se repetía en espejo).
- `tools/build-art.py` y `tools/build-cuerpos.py` preparan las ilustraciones; `docs/PROMPTS_CUERPOS.md` tiene los prompts con los que se generaron. Capturas, GIF y banner rehechos. La prueba de navegador comprueba ahora que todo el arte carga.

## 1.2 · Música por acto
- **Cada acto tiene su música.** El Acto I conserva la de siempre; el Acto II (La Ciudad de Tela) suena a feria en modo mayor y el Acto III (El Castillo de Tramoya) es más lento y oscuro, en menor armónico. Las melodías se generan con semilla a partir de los acordes, así que suenan igual en cada partida. El jefe y el título no cambian.
- Al continuar tras perder, la música vuelve a ser la del acto en el que estás (antes volvía siempre a la del Acto I).
- `docs/PROMPTS_ILUSTRACIONES.md`: prompts para ilustrar los decorados, las texturas, el marco del escenario y las caras de las marionetas.

## 1.1 · Parches para publicar
- **Dificultad** Fácil, Normal y Difícil, que se elige en el título (teclado, mando o tocando) y cambia el daño recibido y los intentos extra.
- **Mejores marcas** por dificultad y número de jugadores, y los ajustes de sonido, calma y dificultad, guardados en el navegador (con `try/catch`: el juego funciona igual si el almacenamiento falla).
- Botones de **sonido**, **calma** (menos temblor y destellos) y **pantalla completa** (`F`), y la calma se activa sola si el sistema pide reducir movimiento.
- El juego se **pausa al perder el foco** de la ventana.
- **Aviso de girar el móvil** cuando está en vertical.
- `tools/build-dist.mjs`, carpeta `itch/` y `test/parches.js`.

## Presentación
- Banner propio de cada juego, hecho con su arte (no una captura con panel).
- README con banner, badges, índice, capturas, GIFs en PC y móvil (con controles táctiles), estructura y licencia.
- Iconos de la página (favicon, 512 px y pantalla de inicio) y metaetiquetas para compartir el enlace.

## 1.0 · Primera versión
- Tres actos con tres jefes: El Mozo Mayor, La Madre Tijera y El Titiritero.
- Combate por hilos: brazos, piernas y cabeza se cortan por separado.
- Golpes, agarres, mangual, molinete y armas.
- Uno o dos jugadores, con teclado, mando y controles táctiles.
- Música y efectos con Web Audio.
