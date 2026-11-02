#!/usr/bin/env python3
"""Source-faithful, explicitly verified GOV.UK exemplar URL restoration.

An earlier GOV.UH build transformed GOV.UK illustrative URLs into GOV.UH
destinations even when the cited publication/service had never been issued
by UH. This repairs *only* the verified missing examples in the manifest.
No UH native service, correct UH URL, editorial body text or approved asset
is changed. This is a controlled migration overlay, not a new CMS.
"""
from pathlib import Path
from hashlib import sha256
import json,re,shutil,sys

if len(sys.argv)!=4:
    raise SystemExit("usage: restore.py BASE_PUBLIC MANIFEST_JSON OUT_PUBLIC")
base,manifest_path,out=map(Path,sys.argv[1:])
assert base.is_dir() and manifest_path.is_file() and not out.exists()
manifest=json.loads(manifest_path.read_text())
refs=manifest["references"]
assert len(refs)==128
assert len(list(base.rglob("*.html")))==157
assert len(list(p for p in base.rglob("*") if p.is_file()))==164
assert all(ref["status_verified"]==200 for ref in refs)

# Prioritise longer URL keys to avoid changing a short parent-path prefix.
sources=sorted(refs,key=lambda x:len(x["from"]),reverse=True)
shutil.copytree(base,out)
hits={r["from"]:0 for r in refs}
changed=[]
for page in out.rglob("*.html"):
    text=page.read_text()
    prior=text
    for entry in sources:
        old=entry["from"]
        new=entry["to"]
        # Only hyperlink destinations (not descriptive text, images, or script).
        # The next character must end the href or start its fragment/query.
        pat=r'(href=["\x27])'+re.escape(old)+r'(?=["\x27#?])'
        text,n=re.subn(pat,lambda m:m.group(1)+new,text)
        if n:hits[old]+=n
    if text!=prior:
        changed.append(str(page.relative_to(out)))
        page.write_text(text)
missing=[key for key,n in hits.items() if n==0]
assert not missing,("Unmatched audited links",missing)
assert all(val>0 for val in hits.values())

files=sorted(p for p in out.rglob("*") if p.is_file())
assert len(files)==164 and len(list(out.rglob("*.html")))==157
def digests(path):
    return {str(f.relative_to(path)):sha256(f.read_bytes()).digest()
            for f in path.rglob("*") if f.is_file()}
before,after=digests(base),digests(out)
assert before.keys()==after.keys()
assert {p for p in before if before[p]!=after[p]}==set(changed)
assert "assets/styles.css" not in changed
assert all("govuk-footer__copyright-logo" in p.read_text()
           for p in out.rglob("*.html") if "<title>Redirecting" not in p.read_text())

hasher=sha256()
for file in files:
    hasher.update(str(file.relative_to(out)).encode())
    hasher.update(b"\0")
    hasher.update(sha256(file.read_bytes()).digest())
digest=hasher.hexdigest()
receipt={
    "immutable_digest":digest,
    "source":"audit/verified-uk-example-links-20261102.json",
    "verified_targets":len(hits),
    "restored_hyperlink_occurrences":sum(hits.values()),
    "changed_html_pages":len(changed),
    "changed_pages":sorted(changed),
    "total_html_pages":157,
    "total_files":164,
    "base_digest":base.parent.name
}
(out.parent/"verified-uk-examples-receipt.json").write_text(
    json.dumps(receipt,indent=2))
print("VERIFIED_EXEMPLAR_LINKS_REPAIRED",json.dumps(
    {k:v for k,v in receipt.items() if k!="changed_pages"}))
