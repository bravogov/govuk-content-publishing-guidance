#!/usr/bin/env python3
"""Reproducible, narrowly scoped GOV.UH content-source fidelity release.
Compile the reviewed source with Eleventy before running. Reuse the canonical
immutable release for all other content and assets. Do not expand scope here.
"""
from pathlib import Path
from hashlib import sha256
from urllib.parse import urlsplit,unquote
from bs4 import BeautifulSoup
import json,shutil,sys
if len(sys.argv)!=4: raise SystemExit("usage: release.py BASE COMPILED OUTPUT_PUBLIC")
base,compiled,out=map(Path,sys.argv[1:])
changes=[
'index.html','writing-to-gov-uh-standards/index.html',
'publish-update-retire-content/index.html',
'formatting-content/index.html',
'formatting-content/text-formatting/index.html',
'formatting-content/text-formatting/headings/index.html',
'formatting-content/text-formatting/links/index.html',
'about-the-guidance/whats-new/index.html'
]
assert base.is_dir() and compiled.is_dir() and not out.exists()
assert len(list(base.rglob('*.html')))==157
shutil.copytree(base,out)
for rel in changes:
    compiled_file=compiled/rel
    assert compiled_file.exists(),rel
    s=compiled_file.read_text()
    added_css='<link rel="stylesheet" href="/assets/uh/guidance-header.css">'
    assert s.count(added_css)==1,rel
    s=s.replace(added_css,'')
    # The source still has upstream UK folder names for some nested pages.
    # Canonical GOV.UH live routes retain the adapted path for historical IDs.
    s=s.replace('href="/writing-to-gov-uk-standards/','href="/writing-to-gov-uh-standards/')
    s=s.replace('href="/writing-to-gov-uk-standards"','href="/writing-to-gov-uh-standards"')
    assert 'href="/writing-to-gov-uk-standards/' not in s,rel
    assert 'uh-crown-favicon.svg' in s and '/assets/styles.css' in s,rel
    (out/rel).write_text(s)
# Ensure the restored pages retain real internal targets.
link_problems=[]
for rel in changes:
    page=BeautifulSoup((out/rel).read_text(),'html.parser')
    for anchor in page.select('main a[href]'):
        href=anchor.get('href','')
        if not href.startswith('/') or href.startswith('//'):continue
        path=unquote(urlsplit(href).path).lstrip('/')
        if path and not ((out/path).is_file() or (out/path/'index.html').is_file() or (out/(path+'.html')).is_file()):
            link_problems.append((rel,href))
assert not link_problems,link_problems[:15]
assert 'How to create and update content for GOV.UH' in (out/'index.html').read_text()
assert 'Use the right heading level' in (out/'formatting-content/text-formatting/headings/index.html').read_text()
assert 'Include links to Whitehall Publisher content' in (out/'formatting-content/text-formatting/links/index.html').read_text()
assert (out/'formatting-content/text-formatting/links/index.html').read_text().count('x-govuk-sub-navigation__link')>=20
assert 'November 2026' in (out/'about-the-guidance/whats-new/index.html').read_text() and '2 November' in (out/'about-the-guidance/whats-new/index.html').read_text()
def digests(root):
    return {str(f.relative_to(root)):sha256(f.read_bytes()).hexdigest() for f in root.rglob('*') if f.is_file()}
original,updated=digests(base),digests(out)
assert set(original)==set(updated) and len(updated)==164
assert {x for x in original if original[x]!=updated[x]}==set(changes)
assert len(list(out.rglob('*.html')))==157
h=sha256()
for f in sorted(p for p in out.rglob('*') if p.is_file()):
    h.update(str(f.relative_to(out)).encode());h.update(b'\0');h.update(sha256(f.read_bytes()).digest())
digest=h.hexdigest()
manifest={'immutable_release_digest':digest,'baseline':base.parent.name,
          'source_commit':'5a96414727f42581ef12a504f48a4e40ddf6ca5b',
          'pages':157,'files':len(updated),'reviewed_page_changes':changes}
(out.parent/'manifest.json').write_text(json.dumps(manifest,indent=2))
print('SOURCE_FIDELITY_RELEASE_VALIDATED',json.dumps(manifest))
