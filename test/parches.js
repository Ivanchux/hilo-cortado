// Navegador (Chromium sin interfaz): dificultad, guardado, sonido, pantalla completa, pausa al perder el foco,
// iframe con almacenamiento bloqueado y táctil. Uso: node test/parches.js   (necesita `playwright`)
const { chromium } = require('playwright');
const http = require('http'), fs = require('fs'), path = require('path');
(async () => {
  const srv = http.createServer((q, r) => { const f = q.url.split('?')[0]; const p = path.join(process.cwd(), f === '/' ? 'index.html' : f); fs.readFile(p, (e, d) => { if (e) { r.writeHead(404); r.end(); } else { r.writeHead(200, { 'content-type': p.endsWith('.html') ? 'text/html; charset=utf-8' : 'application/octet-stream' }); r.end(d); } }); }).listen(0);
  const url = 'http://127.0.0.1:' + srv.address().port + '/';
  const b = await chromium.launch(); let ok = 0, bad = 0; const errs = [], ext = [];
  const check = (c, m) => { if (c) ok++; else { bad++; console.log('FALLO:', m); } };
  const watch = pg => { pg.on('pageerror', e => errs.push(String(e))); pg.on('console', m => m.type() === 'error' && errs.push(m.text())); pg.on('request', r => { if (!r.url().startsWith(url)) ext.push(r.url()); }); };

  // 1) Contexto normal: dificultad, partida, récord y ajustes guardados
  {
    const ctx = await b.newContext({ viewport: { width: 960, height: 540 } }); const pg = await ctx.newPage(); watch(pg);
    await pg.goto(url + '?test=1'); await pg.waitForTimeout(500);
    const G = () => pg.evaluate(() => ({ idx: HC.Game.diffIdx, diff: HC.Game.diff, cred: HC.Game.credits, st: HC.Game.st }));
    check((await G()).idx === 1, 'dificultad inicial Normal');
    await pg.waitForTimeout(2000);
    check(await pg.evaluate(() => Object.keys(CUERPOS).length === 10 && Object.keys(CUERPOS).every(bodyReady)), 'las piezas ilustradas de los diez personajes cargan');
    check(await pg.evaluate(() => Object.keys(ART.ok).length > 90 && Object.values(ART.ok).every(Boolean)), 'todo el arte ilustrado carga sin fallos');
    await pg.keyboard.down('ArrowLeft'); await pg.waitForTimeout(80); await pg.keyboard.up('ArrowLeft');
    // en TEST el bucle no corre: avanzamos fotogramas a mano
    await pg.evaluate(() => { HC.key('KeyA', true); HC.step(2); HC.key('KeyA', false); HC.step(2); });
    check((await G()).idx === 0, 'A cambia a Fácil');
    await pg.evaluate(() => { HC.key('KeyD', true); HC.step(2); HC.key('KeyD', false); HC.step(2); HC.key('KeyD', true); HC.step(2); HC.key('KeyD', false); HC.step(2); });
    check((await G()).idx === 2, 'D dos veces -> Difícil');
    await pg.evaluate(() => HC.Game.newGame(1)); check((await G()).diff === 1.2 && (await G()).cred === 2, 'Difícil: daño ×1,2 y 2 intentos');
    await pg.evaluate(() => { HC.Game.diffIdx = 0; HC.Game.newGame(1); }); check((await G()).diff === 0.65 && (await G()).cred === 5, 'Fácil: daño ×0,65 y 5 intentos');
    await pg.evaluate(() => { HC.Game.diffIdx = 1; HC.Game.newGame(1); }); check((await G()).diff === 0.9, 'Normal 1 jugador: ×0,9');
    await pg.evaluate(() => { HC.Game.newGame(2); }); check((await G()).diff === 1, 'Normal 2 jugadores: ×1');
    // récord
    await pg.evaluate(() => { HC.Game.newGame(1); HC.Game.players[0].score = 4321; HC.Game.st = 'play'; HC.Game.toTitle(); });
    const best = await pg.evaluate(() => JSON.parse(localStorage.getItem('hilocortado.v1')).best);
    check(best['1-1'] && best['1-1'].score === 4321 && best['1-1'].act === 1, 'récord guardado por dificultad y jugadores');
    await pg.evaluate(() => { HC.Game.newGame(1); HC.Game.players[0].score = 100; HC.Game.st = 'play'; HC.Game.toTitle(); });
    check((await pg.evaluate(() => JSON.parse(localStorage.getItem('hilocortado.v1')).best['1-1'].score)) === 4321, 'un récord peor no sustituye al mejor');
    // sonido y calma, y que se recuerdan al recargar
    await pg.evaluate(() => { HC.Game.toggleSound(); HC.Game.toggleReduce(); });
    await pg.evaluate(() => { HC.Game.diffIdx = 2; HC.Game.cycleDiff(0); });
    await pg.reload(); await pg.waitForTimeout(500);
    const st = await pg.evaluate(() => ({ sound: document.getElementById('btn-snd').getAttribute('aria-pressed'), red: document.getElementById('btn-red').getAttribute('aria-pressed'), idx: HC.Game.diffIdx }));
    check(st.sound === 'false' && st.red === 'true' && st.idx === 2, 'ajustes recordados tras recargar: ' + JSON.stringify(st));
    // botón de sonido y pantalla completa
    await pg.click('#btn-snd'); check((await pg.getAttribute('#btn-snd', 'aria-pressed')) === 'true', 'botón Sonido');
    check(await pg.locator('#btn-fs').isVisible(), 'botón de pantalla completa visible');
    await pg.click('#btn-fs'); await pg.waitForTimeout(300); check(await pg.evaluate(() => !!document.fullscreenElement), 'botón entra en pantalla completa');
    await pg.keyboard.press('f'); await pg.waitForTimeout(300); check(await pg.evaluate(() => !document.fullscreenElement), 'F sale de pantalla completa');
    // pausa al perder el foco
    await pg.evaluate(() => { HC.start({ players: 1, bots: [true] }); HC.step(30); window.dispatchEvent(new Event('blur')); });
    check((await G()).st === 'paused', 'pierde el foco -> pausa');
    await ctx.close();
  }
  // 2) iframe con almacenamiento bloqueado: arranca y se puede jugar
  {
    const ctx = await b.newContext({ viewport: { width: 960, height: 540 } });
    await ctx.addInitScript(() => { Object.defineProperty(window, 'localStorage', { get() { throw new Error('bloqueado'); } }); });
    const pg = await ctx.newPage(); watch(pg);
    fs.writeFileSync('.iframe-test.html', '<!doctype html><body style="margin:0"><iframe src="index.html?test=1" style="width:960px;height:540px;border:0" allow="fullscreen"></iframe>');
    await pg.goto(url + '.iframe-test.html'); await pg.waitForTimeout(800);
    const f = pg.frames().find(x => x !== pg.mainFrame());
    await f.evaluate(() => { HC.start({ players: 1, bots: [true], seed: 3 }); HC.step(600); });
    check(await f.evaluate(() => HC.Game.st === 'play' && HC.Game.time > 500), 'iframe con localStorage bloqueado: se juega');
    await f.evaluate(() => { HC.Game.players[0].score = 50; HC.Game.toTitle(); }); check(true, 'volver al título sin almacenamiento no falla');
    fs.unlinkSync('.iframe-test.html'); await ctx.close();
  }
  // 3) Móvil táctil: tocar la dificultad la cambia; en vertical sale el aviso
  {
    const ctx = await b.newContext({ viewport: { width: 844, height: 390 }, hasTouch: true, isMobile: true }); const pg = await ctx.newPage(); watch(pg);
    await pg.goto(url); await pg.waitForTimeout(700);
    const cdp = await ctx.newCDPSession(pg);
    const tap = async (x, y) => { await cdp.send('Input.dispatchTouchEvent', { type: 'touchStart', touchPoints: [{ x, y, id: 0 }] }); await pg.waitForTimeout(80); await cdp.send('Input.dispatchTouchEvent', { type: 'touchEnd', touchPoints: [] }); await pg.waitForTimeout(250); };
    const idx = () => pg.evaluate(() => (typeof HC !== 'undefined' ? 0 : -1));
    // sin ?test=1 no hay HC: leemos el guardado
    const saved = () => pg.evaluate(() => JSON.parse(localStorage.getItem('hilocortado.v1') || '{"diff":1}').diff);
    const r = await pg.locator('canvas').boundingBox(); const px = (lx, ly) => [r.x + lx / 960 * r.width, r.y + ly / 540 * r.height];
    await tap(...px(960 / 2 + 150, 352)); check(await saved() === 2, 'tocar a la derecha de la dificultad -> Difícil');
    await tap(...px(960 / 2 - 150, 352)); await tap(...px(960 / 2 - 150, 352)); check(await saved() === 0, 'tocar dos veces a la izquierda -> Fácil');
    check(await pg.locator('#rot').isVisible() === false, 'horizontal: sin aviso de girar');
    await pg.setViewportSize({ width: 390, height: 844 }); await pg.waitForTimeout(300);
    check(await pg.locator('#rot').isVisible(), 'vertical: aviso de girar');
    await ctx.close();
  }
  console.log(`navegador: ${ok} correctas, ${bad} fallos · errores de consola: ${errs.length} · peticiones externas: ${ext.length}`); if (errs.length) console.log(errs);
  await b.close(); srv.close(); process.exit(bad || errs.length || ext.length ? 1 : 0);
})();
