[Reading 81 lines from start (total: 81 lines, 0 remaining)]

#!/usr/bin/env python3
"""Assemble a controlled GOV.UH guidance edition from the verified immutable
live baseline and three reviewed source-authored pages. Never modify the live edition.
All unchanged files must be byte-identical to the baseline."""
from pathlib import Path
import hashlib, json, re, shutil, sys
BASE=Path('/var/www/govuh-native-guidance/releases/short-url-a49874413a364852822adc486db96911f1606278/public')
CAND=Path('/srv/uhde/candidates/govuh-corporate-guidance-20261101/_site')
OUT=Path('/srv/uhde/candidates/govuh-corporate-guidance-20261101/release/public')
assert BASE.is_dir() and CAND.is_dir()
def check(test,msg):
 if not test: raise RuntimeError(msg)
def take(f):return f.read_text(encoding='utf-8')
def setonce(s,needle,value,where):
 check(s.count(needle)==1,f'{where}: expected exactly one match, found {s.count(needle)}')
 return s.replace(needle,value,1)
def block(s,first,end):
 a=s.find(first);check(a>=0,'beginning section not found: '+first)
 b=s.find(end,a);check(b>a,'ending section not found: '+end)
 return s[a:b]
check(len(list(BASE.rglob('*.html')))==159,'unexpected previous live page count')
check(len([f for f in BASE.rglob('*') if f.is_file()])==165,'unexpected previous live file count')
if OUT.exists():shutil.rmtree(OUT)
shutil.copytree(BASE,OUT)
changed={}
# Canonical corporate page: add source-built substantive sections, retain the existing editor instructions.
rel='publish-update-retire-content/corporate-information/index.html'
old=take(OUT/rel);new=take(CAND/rel)
extra=block(new,'<h2 id="confirm-the-content-with-the-responsible-organisation"', '<h2 id="add-or-edit-a-corporate-information-page"')
check('Keep corporate information up to date' in extra,'missing review guidance')
extra=extra.replace('/writing-to-gov-uk-standards/','/writing-to-gov-uh-standards/')
old=setonce(old,'<h2 id="add-or-edit-a-corporate-information-page"',extra+'<h2 id="add-or-edit-a-corporate-information-page"','corporate insertion')
toc='<li><a href="#confirm-the-content-with-the-responsible-organisation">Confirm the content with the responsible organisation</a></li><li><a href="#keep-corporate-information-up-to-date">Keep corporate information up to date</a></li>'
# Native content list may not have TOC on landing page; do not invent it.
welsh='<li><a href="/publish-update-retire-content/corporate-information/welsh-language-scheme/" class="govuk-link">Welsh language scheme</a></li>'
old=setonce(old,welsh,'','Welsh navigation')
(OUT/rel).write_text(old,encoding='utf-8');changed[rel]='source-compiled corporate content and review guidance'
# Review existing content: import source-built section into canonical existing writing standards.
rel='writing-to-gov-uh-standards/plan-manage-content/manage-existing-govuk-content/index.html'
old=take(OUT/rel)
new=take(CAND/'writing-to-gov-uk-standards/plan-manage-content/manage-existing-govuk-content/index.html')
extra=block(new,'<h2 id="keep-content-accurate-between-scheduled-reviews"', '<h2 id="check-your-content-is-working-for-users"')
extra=extra.replace('/writing-to-gov-uk-standards/','/writing-to-gov-uh-standards/')
old=setonce(old,'<h2 id="check-your-content-is-working-for-users"',extra+'<h2 id="check-your-content-is-working-for-users"','review insertion')
toc='<li><a href="#keep-content-accurate-between-scheduled-reviews">Keep content accurate between scheduled reviews</a></li>'
old=setonce(old,'<li><a href="#check-your-content-is-working-for-users">',toc+'<li><a href="#check-your-content-is-working-for-users">','review TOC')
(OUT/rel).write_text(old,encoding='utf-8');changed[rel]='source-compiled periodic review guidance and TOC'
# Personal information charter: amend exactly the outdated provisions in the established live page.
rel='publish-update-retire-content/corporate-information/personal-information-charter/index.html'
old=take(OUT/rel)
check(old.count('Data Protection Act 1998')==2,'unexpected prior DPA wording')
old=old.replace('Data Protection Act 1998','United Hampshire Realm Data Protection Act 2026')
old=setonce(old,
'<p class="govuk-body">Contact your organisation’s data protection officer if you’re not sure which parts of the page you should include.</p>',
'<p class="govuk-body">Check the organisation’s current data protection policies, its responsible controller and the applicable United Hampshire Realm Data Protection Act 2026 requirements. Refer questions to its genuinely appointed data protection officer or other competent source of legal and data protection advice. Do not publish an unverified officer’s name or contact details.</p>',
'data protection competence')
old=setonce(old,
'<p class="govuk-body">View <a href="https://www.gov.uhrblx.com/government/organisations/charity-commission/about/personal-information-charter" class="govuk-link">a good example of a ‘Personal information charter’ page</a>.</p>',
'<p class="govuk-body">Before linking an example, check that its published edition, organisation and statutory references are current. Do not copy another organisation’s data processing or subject access arrangements without checking that they apply.</p>',
'unsupported example')
(OUT/rel).write_text(old,encoding='utf-8');changed[rel]='precise legal and actual DPO references'
# Safety, provenance, and byte-for-byte non-target preservation.
a={str(f.relative_to(BASE)):hashlib.sha256(f.read_bytes()).hexdigest() for f in BASE.rglob('*') if f.is_file()}
b={str(f.relative_to(OUT)):hashlib.sha256(f.read_bytes()).hexdigest() for f in OUT.rglob('*') if f.is_file()}
check(set(a)==set(b),'output file set changed')
delta={p for p in a if a[p]!=b[p]}
check(delta==set(changed),f'unexpected changed file set: {delta ^ set(changed)}')
check(sum(1 for x in OUT.rglob('*.html'))==159,'page count diverged')
check(all(not (OUT/x).read_text().count('Data Protection Act 1998') for x in changed),'obsolete law remains')
check(not any('govuk-crest.svg' in (OUT/x).read_text() for x in changed),'UK crest reference in changed pages')
check(not any('GDS Transport' in (OUT/x).read_text() for x in changed),'restricted font reference in changed pages')
check(not (OUT/'publish-update-retire-content/corporate-information/welsh-language-scheme/index.html').exists(),'Welsh source exposed')
check('Keep content accurate between scheduled reviews' in take(OUT/'writing-to-gov-uh-standards/plan-manage-content/manage-existing-govuk-content/index.html'),'review absent')
check('Confirm the content with the responsible organisation' in take(OUT/'publish-update-retire-content/corporate-information/index.html'),'corporate source absent')
manifest=dict(source_commit='ac13bf8a23f1fe4d6c97fd04791066c1d7956527',
 baseline_directory=BASE.parent.name, baseline_sha256=a, changed_files=changed,
 output_files=len(b), html_count=159)
# Manifest outside public root, so byte-consistency and published file counts remain stable.
(Path(OUT.parent)/'change-manifest.json').write_text(json.dumps(manifest,indent=2,sort_keys=True))
print('GUIDANCE_CANDIDATE_PASS 159 HTML, 165 files, changed exactly 3 authored pages')
for x in changed:print('CHANGED',x,b[x])

[executed on device: vps-0c7c0252 (73306686-c479-4f6d-8dec-135b7db0d40b)]