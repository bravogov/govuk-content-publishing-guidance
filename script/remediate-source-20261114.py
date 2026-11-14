from pathlib import Path
from urllib.parse import urlparse
from collections import Counter,defaultdict
import re,json
ROOT=Path('/srv/uhde/candidates/govuh-guidance-estate-correction-20261114')
APP=ROOT/'app'
status=json.loads((ROOT/'audit-uk-links-20261114.json').read_text())
changes=Counter(); broken=defaultdict(list)
for f in list(APP.rglob('*.md')) + list(APP.rglob('*.njk')):
    old=f.read_text(encoding='utf-8')
    new=old
    if 'GOV.UK' in new:
        changes['GOV.UK_mentions_repaired']+=new.count('GOV.UK')
        new=new.replace('GOV.UK','GOV.UH')
    if 'guidance.publishing.service.gov.uk' in new:
        changes['old_guidance_host_fixed']+=new.count('guidance.publishing.service.gov.uk')
        new=new.replace('guidance.publishing.service.gov.uk','guidance.publishing.service.gov.uhrblx.com')
    if f.name=='ask-short-url.md':
        changes['short_url_Platform_Office_fixed']+=new.count('Platform Office')
        new=new.replace('Platform Office','GDS')
        new=new.replace('talk to GDS','talk to the Government Digital Service (GDS)')
        new=new.replace('Submit your request at least 2 weeks before you need it. GDS might not be able to meet your deadline if they do not get the full 2 weeks\' notice.','Allow at least 2 weeks where practicable. State any deadline and explain the consequences if it cannot be met.')
    if f.name=='identify-user-needs.md':
        new=new.replace('User needs are the needs that our users have when they come to GOV.UH. People visit GOV.UH to help them fulfil a certain task, like apply for a driving licence or find out how to vote.','User needs describe what people are trying to do when they use GOV.UH. People come to GOV.UH to complete a task, access a service or find reliable information, for example to find out how to vote.')
        new=new.replace('someone who wants to work in the UK','someone who wants to work in United Hampshire')
        new=new.replace('a person who has reached state pension age','a person seeking information about an applicable pension scheme')
        new=new.replace('someone applying for a child\'s passport','someone applying for an identity document')
        new=new.replace('Carer\'s Allowance','a relevant support payment')
        new=new.replace('why the need is in [proposition for GOV.UH](https://www.gov.uk/government/publications/govuk-proposition/govuk-proposition)','why the content is appropriate for GOV.UH and the responsible publishing organisation')
    if f.name=='worldwide.md':
        new=new.replace("* 'Welsh language scheme' (for organisations providing services in Wales)\n",'')
    if f.name=='a-to-z-style-guide.md':
        # Remove UK-only constitutional definitions as text, rather than misstate UH institutions.
        new=re.sub(r'(?ms)^### (?:Great Britain|MS|MSP|north Wales|Senedd Cymru \(Welsh Parliament\)|Welsh Government|Welsh exotic animal disease contingency plan|Welsh Parliament)\n.*?(?=^### |\Z)','',new)
        new=new.replace('Use title case for \'Welsh Government\' and \'Scottish Government\' because it\'s the full title.','Use title case for the established full title of a government, such as \'Hampshire County Government\'.')
        new=new.replace('Lower case unless used in the full title, like the National Assembly for Wales (Legislative Competence) (Social Welfare) Order 2008.','Lower case unless used in the verified full title of an instrument.')
        new=new.replace('Title case if used as the full title: the National Assembly for Wales (Legislative Competence) (Social Welfare) Order 2008.','Use title case when quoting the verified full title of an instrument.')
        new=new.replace('Use lower case for the north, the south of England, the south-west, north-east Scotland, south Wales, the west, western Europe, the far east, south-east Asia.','Use lower case for compass directions, such as the north, the south of England, the west and western Europe.')
    # Map known-live GOV.UH equivalents; for others remove misleading clickable UK targets.
    # This targets Markdown links, not legitimate textual discussions of UK practice.
    def uk_link(m):
        label,url=m.group(1),m.group(2)
        rec=status.get(url)
        if rec and rec['status']==200 and rec['effective'].startswith('https://www.gov.uhrblx.com/'):
            changes['verified_UH_destination']+=1
            return '['+label+']('+rec['effective']+')'
        changes['unavailable_UK_link_removed']+=1
        broken[str(f.relative_to(APP))].append({'label':label,'uk':url,'uh_candidate':rec['dest'] if rec else None,'http':rec['status'] if rec else None})
        return label
    new=re.sub(r'\[([^\]\n]+)\]\((https://www\.gov\.uk/[^\)\s]+)\)',uk_link,new)
    # Where raw GOV.UK URLs remain, remove the hyperlink rather than send GOV.UH users to UK-specific instructions.
    def bare_uk(m):
        url=m.group(0);changes['raw_UK_url_removed']+=1
        broken[str(f.relative_to(APP))].append({'uk':url,'reason':'bare URL without verified equivalent'})
        return '[UK reference not available on GOV.UH]'
    new=re.sub(r'https://www\.gov\.uk/[^\s\)\]<>"\']+',bare_uk,new)
    if new!=old:
        f.write_text(new,encoding='utf-8')
        changes['edited_pages']+=1
( ROOT/'audit-unavailable-uk-destinations-20261114.json').write_text(json.dumps(broken,indent=2,ensure_ascii=False))
( ROOT/'audit-source-edits-20261114.json').write_text(json.dumps(changes,indent=2))
print('SOURCE_EDITS',dict(changes))
print('UNAVAILABLE_DESTINATION_PAGES',len(broken),'LINKS',sum(map(len,broken.values())))
