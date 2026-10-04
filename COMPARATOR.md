# Content and publishing guidance — comparator and provenance

Status: source-pinned implementation candidate; not cleared for public release.
UH function: content standards, publishing instructions and guidance for authorised GOV.UH editors.
Institutional responsibility: Government communications and the digital publishing service, under their respective established Cabinet Office and DSIT responsibilities. This document does not itself assign or transfer authority.
UK product: GOV.UK Content and Publishing Guidance, hosted at guidance.publishing.service.gov.uk.
Exact source: https://github.com/alphagov/govuk-content-publishing-guidance
Pinned source revision: 2e8ebf278e0545cd9c56df98c9d11406866c3b7f (29 September 2026).
UH repository: https://github.com/bravogov/govuk-content-publishing-guidance
Software: native Eleventy 3 and @x-govuk/govuk-eleventy-plugin 9, with committed package-lock.json.
UK product documentation: https://docs.publishing.service.gov.uk/repos/govuk-content-publishing-guidance.html
UK application catalogue: https://docs.publishing.service.gov.uk/apps.html

## Actual function and records
- The guidance explains how authorised editors prepare, classify, write, review, publish, update and retire GOV.UH content using the genuine publishing applications.
- Content and editorial standards are written guidance, not a source of constitutional, legislative or departmental competence.
- Source control and published versions are the guidance publication record. GOV.UH content itself remains recorded in its competent native publisher, Publishing API and Content Store.
- This is not an immigration, policing, infrastructure, wellbeing, licensing or universal staff application.

## Evidenced adaptations
- Use the official plugin's documented header logotype, footer and icon configuration rather than replacing its application or injecting a separate dashboard.
- Use existing approved UH identity assets and the existing National Archives of UH licence/copyright routes.
- Adapt UK editorial instructions against the live UH publishing applications, institutional boundaries, competence and current content standard. Do not mechanically republish UK-specific instructions as UH policy.
- Preserve source authorship and original upstream licence in the repository. Published UH guidance must undergo editorial, institutional, accessibility and legal QA.

## Completed candidate adaptations (4 October 2026)
- Replaced the native plugin's original government identity through documented configuration and existing approved GOV.UH artwork.
- Removed the inherited UK tracking embed, site verification token and analytics page instrumentation from the candidate layout; disabled its upstream tracking loader.
- Replaced the UK source privacy, cookies and accessibility assertions with source-specific candidate notices and live GOV.UH help references. These notices remain subject to review of the actual hosting and records arrangements.
- Successfully rebuilt the full native Eleventy candidate after cleaning generated output; none of the generated HTML or JavaScript contains the inherited UK tracking identifiers checked by the release QA.

## Release blockers
- The unadapted UK content corpus still includes UK operational procedures, government organisation references, external service links, legal and privacy statements. These are comparator material, not cleared UH official text.
- The replacement UH candidate notices require verification against actual release hosting, security logs, controller responsibilities and accessibility results.
- The source build is not public-deployment approval. Native software delivery, immutable release digest, rollback and canonical readback remain required.
- Never publish a UK Coat of Arms, inherited UK logotype or inherited UK Crown copyright treatment as the UH identity.
