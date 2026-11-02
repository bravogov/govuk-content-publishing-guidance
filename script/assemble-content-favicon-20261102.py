#!/usr/bin/env python3
"""Controlled GOV.UH publishing guidance release from live baseline and reviewed GitHub source.
This only changes favicon links, removes the three expressly voided corporate page types,
and corrects the publication-scheme link; content history is retained in GitHub/base release.
"""
from pathlib import Path
from hashlib import sha256
import re, shutil, json, sys
BASE=Path(sys.argv[1])
SRC=Path(sys.argv[2])
OUT=Path(sys.argv[3])
def must(x,reason):
    if not x: raise RuntimeError(reason)
must(BASE.is_dir() and SRC.is_dir() and not OUT.exists(),'baseline / GitHub source / candidate problem')
b=list(BASE.rglob('*.html'))
must(len(b)==159,'Unexpected baseline: '+str(len(b)))
svg=(SRC/'app/assets/uh/uh-crown-favicon.svg').read_bytes()
must(svg.startswith(b'<svg ') and len(svg)==2363,'Unexpected UH homepage favicon SVG')
source_corp=(SRC/'app/publish-update-retire-content/corporate-information/index.md').read_text()
source_pub=(SRC/'app/publish-update-retire-content/corporate-information/publication-scheme.md').read_text()
must(not any(x in source_corp for x in ['[Our energy use](', '[Procurement at [organisation name]](', '[Welsh language scheme](']),'voided types remain in source')
must('/corporate-information/procurement/' not in source_pub,'voided procurement link remains in publication scheme source')
cfg=(SRC/'eleventy.config.js').read_text()
must("shortcut: '/assets/uh/uh-crown-favicon.svg'" in cfg,'source config favicon not fixed')
shutil.copytree(BASE,OUT)
(OUT/'assets/uh/uh-crown-favicon.svg').write_bytes(svg)
voided=['our-energy-use','procurement','welsh-language-scheme']
for name in voided:
    page=OUT/f'publish-update-retire-content/corporate-information/{name}/index.html'
    if page.exists():
        page.unlink(); page.parent.rmdir()
fixed=[]
oldicons='<link rel="icon" href="/assets/uh/gov-uh-site-identity-logo.svg" sizes="any"><link rel="mask-icon" href="/assets/uh/gov-uh-site-identity-logo.svg" color="#1d70b8"><link rel="apple-touch-icon" href="/assets/uh/gov-uh-site-identity-logo.svg">'
newicons='<link rel="icon" href="/assets/uh/uh-crown-favicon.svg" sizes="any" type="image/svg+xml"><link rel="mask-icon" href="https://www.gov.uhrblx.com/uh-brand/uh-crown-mask-20261014.svg" color="#1d70b8"><link rel="apple-touch-icon" href="https://www.gov.uhrblx.com/uh-brand/uh-crown-touch-20261014.png">'
for f in OUT.rglob('*.html'):
    s=f.read_text()
    if s.count(oldicons)==1:
        s=s.replace(oldicons,newicons)
    else:
        # Some pages were originally HTML-minified and have reordered attributes.
        alt='<link href="/assets/uh/gov-uh-site-identity-logo.svg" rel="icon" sizes="any"/><link color="#1d70b8" href="/assets/uh/gov-uh-site-identity-logo.svg" rel="mask-icon"/><link href="/assets/uh/gov-uh-site-identity-logo.svg" rel="apple-touch-icon"/>'
        if s.count(alt)==1:
            s=s.replace(alt,newicons)
        else:
            must('<title>Redirecting' in s and 'rel="icon"' not in s, 'Unexpected head icon count '+str(f))
    for name in voided:
        dest='/publish-update-retire-content/corporate-information/'+name+'/'
        if dest not in s:continue
        # Native category sidebar, generated from original Eleventy navigation.
        pattern=r'\s*<li class="x-govuk-sub-navigation__section-item">\s*<a class="x-govuk-sub-navigation__link" href="'+re.escape(dest)+r'">[^<]*</a>\s*</li>'
        s,n=re.subn(pattern,'',s)
        # Corporate content list and site map.
        pattern=r'\s*<li><a href="'+re.escape(dest)+r'"(?: class="govuk-link")?>[^<]*</a></li>'
        s,m=re.subn(pattern,'',s)
        if dest in s and name=='procurement' and f.relative_to(OUT).as_posix()=='publish-update-retire-content/corporate-information/publication-scheme/index.html':
            previous='our [procurement procedures] (link to your <a href="'+dest+'" class="govuk-link">procurement page</a>)'
            current='* [procurement procedures] (link to the organisation’s actual published policies, contracts or procurement information, where applicable)'
            must(s.count(previous)==1,'Unexpected procurement cross-reference')
            s=s.replace(previous,current)
        must(dest not in s,'Voided corporate type remains in '+str(f)+': '+dest)
    f.write_text(s)
    fixed.append(str(f.relative_to(OUT)))
must(len(list(OUT.rglob('*.html')))==157,'Expected 157 HTML files (2 former pages removed, Welsh already absent)')
must(len(list(OUT.rglob('*')))>0,'empty output')
for f in OUT.rglob('*.html'):
    s=f.read_text()
    must('href="/assets/uh/uh-crown-favicon.svg"' in s or ('<title>Redirecting' in s and 'rel="icon"' not in s),'favicon absent '+str(f))
    must(not any('/corporate-information/'+x+'/' in s for x in voided),'stale void reference '+str(f))
must('Keep corporate information up to date' in (OUT/'publish-update-retire-content/corporate-information/index.html').read_text(),'prior approved guidance lost')
manifest={"repo_commit":"SOURCE_COMMIT_TO_SET","baseline":BASE.parent.name,"pages":157,"removed_corporate_pages":voided,"favicon":"homepage exact SVG","source_sections":["corporate-information/index.md","corporate-information/publication-scheme.md"],"file_count":len([f for f in OUT.rglob('*') if f.is_file()])}
(OUT.parent/'guidance-release-check.json').write_text(json.dumps(manifest,indent=2))
print('CANDIDATE_PASS',json.dumps(manifest))
