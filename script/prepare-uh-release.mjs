// Release packaging for the native upstream Eleventy build.
// Retains GOV.UK open-source implementation but never publishes UK identity assets.
import * as fs from 'node:fs';
import * as path from 'node:path';

const root = path.resolve('_site');
const cssPath = path.join(root, 'assets/styles.css');
const css = fs.readFileSync(cssPath, 'utf8');
const ukCrest = '/assets/images/govuk-crest.svg';
const occurrences = css.split(ukCrest).length - 1;
if (occurrences !== 3) throw Error('Unexpected upstream crest CSS: ' + occurrences);
if (/GDS Transport|\/assets\/fonts\//.test(css)) throw Error('Restricted font still referenced');
fs.writeFileSync(cssPath, css.replaceAll(ukCrest, '/assets/uh/uh-header-crown-approved.png'));
const manifestPath = path.join(root, 'assets/manifest.json');
fs.writeFileSync(manifestPath, JSON.stringify({
  name: 'GOV.UH content and publishing guidance',
  short_name: 'GOV.UH guidance',
  icons: [
    { src: 'uh/uh-header-crown-approved.png', type: 'image/png', sizes: 'any' },
    { src: 'uh/gov-uh-site-identity-logo.svg', type: 'image/svg+xml', sizes: 'any', purpose: 'monochrome' }
  ]
}, null, 2) + '\n');
const all = [];
function visit(dir) {
  for (const f of fs.readdirSync(dir, {withFileTypes:true})) {
    const p = path.join(dir,f.name);
    if (f.isDirectory()) visit(p);
    else all.push(p);
  }
}
visit(root);
for (const f of all.filter(f => f.endsWith('.html') || f.endsWith('.css') || f.endsWith('manifest.json'))) {
  const body = fs.readFileSync(f, 'utf8');
  if (/guidance\.publishing\.service\.gov\.uk|surveys\.publishing\.service\.gov\.uk|\/assets\/images\/govuk-crest\.svg|govuk-footer__crown[\s\S]{0,300}govuk-crest\.svg|GDS Transport/.test(body))
    throw Error('UK identity or service reference in ' + f);
}
fs.rmSync(path.join(root,'assets/uh/uh-footer-coat-of-arms.webp'),{force:true});
for (const item of ['images','fonts']) fs.rmSync(path.join(root,'assets',item),{recursive:true,force:true});
console.log('UH_RELEASE_ASSETS_PASS: original UK icons and restricted font files excluded; approved identity used');
