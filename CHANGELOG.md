# Registro de cambios

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
