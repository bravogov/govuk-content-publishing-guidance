// Reject a substituted navigation button. Use the pinned GOV.UK Eleventy
// Plugin's native GOV.UK Frontend service-navigation macro and runtime.
// Comparator: alphagov/govuk-content-publishing-guidance at 2e8ebf2,
// https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/
// Source verification recorded 2026-10-04; app JS must be byte-identical.
import * as fs from 'node:fs';
import * as crypto from 'node:crypto';
import * as path from 'node:path';

const root = path.resolve('_site');
const html = fs.readFileSync(path.join(root, 'writing-to-gov-uh-standards/index.html'), 'utf8');
const css = fs.readFileSync(path.join(root, 'assets/styles.css'), 'utf8');
const js = fs.readFileSync(path.join(root, 'assets/application.js'));
const packageLock = JSON.parse(fs.readFileSync('package-lock.json','utf8'));
function assert(condition, message) { if (!condition) throw Error('NATIVE_NAVIGATION_GATE_FAIL: ' + message); }
assert(packageLock.packages['node_modules/@x-govuk/govuk-eleventy-plugin'].version === '9.0.2', 'Unexpected official GOV.UK Eleventy plugin version');
assert(packageLock.packages['node_modules/govuk-frontend'].version === '6.1.0', 'Unexpected GOV.UK Frontend version');
const expectedJs = '0cb1e3833fd731f433efa592acf290ff8bb87572cb4b448abcc06df429e64804';
assert(crypto.createHash('sha256').update(js).digest('hex') === expectedJs, 'Bundled JavaScript differs from actual GOV.UK publishing guidance');
assert(/<div class="govuk-service-navigation app-service-navigation" data-module="govuk-service-navigation">/.test(html), 'Missing native upstream service navigation');
assert(/<nav aria-label="Menu" class="govuk-service-navigation__wrapper">/.test(html), 'Missing upstream native navigation landmark');
assert(/<button type="button" class="govuk-service-navigation__toggle govuk-js-service-navigation-toggle" aria-controls="navigation" hidden="" aria-hidden="true">\s*Menu\s*<\/button>/.test(html), 'Menu toggle differs from official UK template');
assert(/<ul class="govuk-service-navigation__list" id="navigation">/.test(html), 'Menu target differs from upstream');
assert(css.includes('govuk-service-navigation__toggle'), 'Native GOV.UK Frontend service navigation CSS missing');
assert(!/govuh-menu-button|govuh-global-tools|govuh-navigation-menu|<button[^>]*>Menu[ ]*▼/.test(html), 'Found custom public site menu on publishing guidance');
assert(!/govuh-menu-button|govuh-global-menu-panel/.test(css), 'Custom menu styling prohibited');
for (const route of ['/writing-to-gov-uh-standards','/publish-update-retire-content','/formatting-content','/accounts-support']) {
 assert(html.includes('href="' + route + '"'), 'Missing real publishing route: '+route);
 assert(fs.existsSync(path.join(root, route.slice(1), 'index.html')), 'Navigation route has no real page: '+route);
}
console.log('NATIVE_GOVUK_GUIDANCE_NAVIGATION_PARITY=PASS; official pinned plugin, native macro, toggle, 4 published routes and byte-identical upstream JS');
