import { readFileSync } from 'node:fs';

// Stops an inherited UK policy or UK site ownership claim from being packaged as UH.
// Source review and competent approval remain necessary after these checks pass.
const blockers = new Map([
  ['app/privacy-notice.md', [
    /GOV\.UK content and publishing guidance/i,
    /data controller for GDS is DSIT/i,
    /guidance\.publishing\.service\.gov\.uk/i,
  ]],
  ['app/accessibility-statement.md', [
    /GOV\.UK Content and publishing guidance/i,
    /This website is run by the Government Digital Service/i,
    /last tested on 27 November 2025/i,
  ]],
  ['_includes/layouts/main.njk', [
    /GTM-W69GK5WH/,
    /google-site-verification/,
    /initialiseAnalytics\(/,
  ]],
  ['app/cookies.njk', [
    /we use Google Analytics software/i,
    /GOV\.UK content and publishing guidance/i,
  ]],
]);

const failures = [];
for (const [file, patterns] of blockers) {
  const content = readFileSync(new URL(`../${file}`, import.meta.url), 'utf8');
  for (const pattern of patterns) {
    if (pattern.test(content)) failures.push(`${file}: inherited UK content/configuration (${pattern.source})`);
  }
}
if (failures.length) {
  console.error('GOV.UH guidance build blocked pending approved replacement of inherited UK material:');
  failures.forEach((failure) => console.error(`- ${failure}`));
  process.exitCode = 1;
} else {
  console.log('Known UK identity and policy contamination checks passed; separate approval is still required.');
}
