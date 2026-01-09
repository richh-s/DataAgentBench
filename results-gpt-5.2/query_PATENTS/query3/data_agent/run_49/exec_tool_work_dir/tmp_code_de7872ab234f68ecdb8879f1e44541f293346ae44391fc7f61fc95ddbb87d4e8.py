code = """import json, re
import pandas as pd

# load UC publications (assignee UNIV CALIFORNIA)
with open(var_call_59lcvJsIjZ1vcLpPvQ8cFHob,'r',encoding='utf-8') as f:
    uc_recs=json.load(f)

def extract_pubnum(info):
    for pat in [r'pub\. number\s+([A-Z]{2}-\d+-[A-Z0-9]+)', r'publication number\s+([A-Z]{2}-\d+-[A-Z0-9]+)']:
        m=re.search(pat, info)
        if m:
            return m.group(1)
    return None

uc_pubnums=set()
for r in uc_recs:
    p=extract_pubnum(r.get('Patents_info','') or '')
    if p:
        uc_pubnums.add(p)

# load all citing-candidate recs with citations
with open(var_call_OaoPEXpflIJ6vct6rGPk3PN9,'r',encoding='utf-8') as f:
    cite_recs=json.load(f)

# match citations
pairs=[]
for r in cite_recs:
    cit=r.get('citation')
    if not cit or cit=='[]':
        continue
    try:
        cit_list=json.loads(cit)
    except Exception:
        continue
    cited=set()
    for c in cit_list:
        pn=c.get('publication_number')
        if pn in uc_pubnums:
            cited.add(pn)
    if cited:
        # extract assignee from Patents_info (before ' holds' or 'In ')
        info=r.get('Patents_info','') or ''
        m=re.match(r'^(.*?)\s+holds\b', info)
        assignee=m.group(1).strip() if m else None
        if not assignee:
            m=re.search(r'is owned by\s+(.*?)\s+and has', info)
            assignee=m.group(1).strip() if m else None
        if not assignee:
            m=re.search(r'is assigned to\s+(.*?)\s+and has', info)
            assignee=m.group(1).strip() if m else None
        if not assignee:
            m=re.search(r'is assigned to\s+(.*?),\s+with publication', info)
            assignee=m.group(1).strip() if m else None
        if not assignee:
            assignee=info.split(' holds ')[0].strip() if ' holds ' in info else None
        # primary CPC: first==true entries
        cpc=r.get('cpc')
        primary=[]
        if cpc:
            try:
                cpc_list=json.loads(cpc)
                for ce in cpc_list:
                    if ce.get('first') is True:
                        code=ce.get('code')
                        if code:
                            primary.append(code)
            except Exception:
                pass
        for uc_pn in cited:
            for code in set(primary):
                pairs.append({'citing_assignee': assignee, 'primary_cpc': code})

# exclude UNIV CALIFORNIA itself
pairs=[p for p in pairs if p['citing_assignee'] and p['citing_assignee']!='UNIV CALIFORNIA']

# derive CPC subclass (first 4 chars letters+2 digits like A01B?) Actually subclass is 4 chars: section letter + class(2 digits)+subclass letter.
# CPC codes begin with e.g., H01M... subclass H01M.

def subclass(code):
    m=re.match(r'^([A-HY]\d\d[A-Z])', code)
    return m.group(1) if m else None

for p in pairs:
    p['cpc_subclass']=subclass(p['primary_cpc'])

pairs=[p for p in pairs if p['cpc_subclass']]

# unique assignee-subclass combos
uniq=sorted({(p['citing_assignee'], p['cpc_subclass']) for p in pairs})

print('__RESULT__:')
print(json.dumps({'n_pairs':len(pairs),'n_uniq':len(uniq),'uniq_sample':uniq[:50]}))"""

env_args = {'var_call_iHXHysJC3duFCWWnJW64v10h': ['publicationinfo'], 'var_call_jlHGhsPdB6yLdpu78t6zwQ84': ['cpc_definition'], 'var_call_59lcvJsIjZ1vcLpPvQ8cFHob': 'file_storage/call_59lcvJsIjZ1vcLpPvQ8cFHob.json', 'var_call_cHnpmjdlTkbewpaKyoAQJmfn': {'uc_pubnums_count': 0, 'uc_pubnums_sample': []}, 'var_call_sUHm40o9xxZWOiW1ZcJe76dg': {'example': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, 'var_call_6CbOtwWCqCuS4wKv3E6q79vg': {'found': 112, 'sample': ['US-2022074631-A1', 'TW-201925402-A', 'US-11421276-B2', 'AU-2019275518-B2', 'US-2017281687-A1', 'AU-2003247814-A1', 'AU-2017356943-A1', 'US-6237292-B1', 'US-7745569-B2', 'US-11072681-B2']}, 'var_call_OaoPEXpflIJ6vct6rGPk3PN9': 'file_storage/call_OaoPEXpflIJ6vct6rGPk3PN9.json'}

exec(code, env_args)
