# Registro de cambios

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
