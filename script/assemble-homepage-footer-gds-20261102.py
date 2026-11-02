#!/usr/bin/env python3
"""Apply the approved main-GOV.UH copyright slot consistently to the guidance
estate, and restore GDS/DSIT as the owner of writing standards.
Preserve the known-good public content until the full source-fidelity release.
"""
from pathlib import Path
from hashlib import sha256
import shutil,re,json,sys
base,compiled,source,out=map(Path,sys.argv[1:])
assert all(x.exists() for x in (base,compiled,source)) and not out.exists()
assert len(list(base.rglob('*.html')))==157
shutil.copytree(base,out)
pat=re.compile(r'<footer class="govuk-template__footer">[\s\S]*?</footer>')
template=(compiled/'index.html').read_text()
matched=pat.findall(template)
assert len(matched)==1
newfooter=matched[0].replace('Published by the United Hampshire Government.','Published by the Government Digital Service, part of the Department for Science, Innovation and Technology.')
assert 'govuk-footer__copyright-logo' in newfooter and '© UH Crown copyright' in newfooter
assert 'UH Open Government Licence v3.0' in newfooter
assert 'govuh-government-footer-arms' not in newfooter
footer_count=0
changed=[]
for file in out.rglob('*.html'):
    data=file.read_text()
    if not pat.search(data):
        assert '<title>Redirecting' in data,file
        continue
    assert len(pat.findall(data))==1,file
    result=pat.sub(lambda _:newfooter,data,count=1)
    if 'writing-to-gov-uh-standards/' in str(file):
        # GDS, part of DSIT, owns the content editorial work, not Platform Office.
        result=result.replace('The <abbr title="Platform Office">Platform Office</abbr> style guides covers style points for content.',
            'The Government Digital Service (<abbr title="Government Digital Service">GDS</abbr>), part of the Department for Science, Innovation and Technology (<abbr title="Department for Science, Innovation and Technology">DSIT</abbr>), maintains the style guides for content published on GOV.UH.')
        result=result.replace('Platform Office','GDS')
    if data!=result:changed.append(str(file.relative_to(out)))
    file.write_text(result)
    footer_count+=1
assert footer_count>=150 and len(changed)>=150,(footer_count,len(changed))
style=out/'assets/styles.css'
sty=style.read_text()
css=(source/'app/assets/styles.scss').read_text()
start=css.index('/* Match the approved GOV.UH homepage copyright-logo slot and artwork. */')
rule=css[start:]
assert '.govuk-footer__copyright-logo::before' in rule
assert 'uh-government-coat-of-arms-footer-20261016.webp' in rule
sty=sty.replace('.govuh-government-footer-arms{display:block;width:120px;height:120px;object-fit:contain;margin-bottom:10px}','')
assert rule not in sty
style.write_text(sty+'\n'+rule)
for f in out.rglob('*.html'):
    s=f.read_text()
    if pat.search(s):
        assert 'govuh-government-footer-arms' not in s,f
        assert 'govuk-footer__copyright-logo' in s,f
        assert '© UH Crown copyright' in s,f
        assert 'Published by the Government Digital Service' in s,f
for f in (out/'writing-to-gov-uh-standards').rglob('*.html'):
    assert 'Platform Office' not in f.read_text(),f
assert len(list(out.rglob('*.html')))==157
h=sha256()
allfiles=sorted(f for f in out.rglob('*') if f.is_file())
assert len(allfiles)==164
for f in allfiles:
    h.update(str(f.relative_to(out)).encode());h.update(b'\0');h.update(sha256(f.read_bytes()).digest())
digest=h.hexdigest()
manifest={'digest':digest,'base':base.parent.name,'html_pages':157,'html_footers_updated':footer_count,
         'files':164,'css_asset':'assets/styles.css','stylesheet_reference':'homepage approved copyright logo',
         'owner':'Government Digital Service (DSIT)',
         'source_commit':'5406dc1c097f1051d0d37244bdcedb10aed53bce'}
(out.parent/'manifest.json').write_text(json.dumps(manifest,indent=2))
print('VALIDATED_GUIDANCE_GDS_AND_FOOTER',json.dumps(manifest))
