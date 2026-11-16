// Renders every SVG in <svg_dir> to a PNG in <png_dir>.
// Usage: node render.js <svg_dir> <png_dir> [scale]
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

(async () => {
  const [svgDir, pngDir, scaleArg] = process.argv.slice(2);
  const scale = Number(scaleArg || 2);
  fs.mkdirSync(pngDir, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({
    viewport: { width: 2000, height: 1414 },
    deviceScaleFactor: scale,
  });
  for (const file of fs.readdirSync(svgDir).filter((f) => f.endsWith('.svg')).sort()) {
    const svg = fs.readFileSync(path.join(svgDir, file), 'utf8');
    await page.setContent(
      `<html><body style="margin:0;background:#fff">${svg}</body></html>`
    );
    await page.evaluate(() => document.fonts.ready);
    const out = path.join(pngDir, file.replace(/\.svg$/, '.png'));
    await page.screenshot({ path: out, clip: { x: 0, y: 0, width: 2000, height: 1414 } });
    console.log('rendered', out);
  }
  await browser.close();
})();
