code = """import json, re, pandas as pd

path = var_call_QjRqKDtIH0hHYIbWjeuk2JXl
with open(path,'r',encoding='utf-8') as f:
    citing_recs = json.load(f)

def parse_assignee(patents_info):
    if not patents_info:
        return None
    m = re.search(r'^(.*?)\s+holds\b', patents_info)
    if m:
        return m.group(1).strip()
    m = re.search(r'is owned by\s+(.+?)\s+and has', patents_info)
    if m:
        return m.group(1).strip()
    m = re.search(r'is assigned to\s+(.+?)\s+and has', patents_info)
    if m:
        return m.group(1).strip()
    return None

with open(var_call_32FcVDZfzFqhgKaVXxdtGrYO,'r',encoding='utf-8') as f:
    uc_recs = json.load(f)

uc_pubs=set()
for r in uc_recs:
    pi=r.get('Patents_info','') or ''
    m=re.search(r'pub\.? number\s+([A-Z]{2}-[0-9]+[A-Z0-9\-]*?)\b', pi)
    if m:
        uc_pubs.add(m.group(1))
if not uc_pubs:
    for r in uc_recs:
        pi=r.get('Patents_info','') or ''
        m=re.search(r'publication number\s+([A-Z]{2}-[0-9]+[A-Z0-9\-]*?)\b', pi)
        if m:
            uc_pubs.add(m.group(1))

assignee_to_subclasses={}

for r in citing_recs:
    citations=r.get('citation')
    if not citations:
        continue
    try:
        cit_list=json.loads(citations) if isinstance(citations,str) else citations
    except Exception:
        continue
    if not any(isinstance(c,dict) and c.get('publication_number') in uc_pubs for c in cit_list):
        continue
    assignee=parse_assignee(r.get('Patents_info','') or '')
    if not assignee:
        continue
    if ('UNIV CALIFORNIA' in assignee) or ('UNIVERSITY OF CALIFORNIA' in assignee) or ('REGENTS OF THE UNIVERSITY OF CALIFORNIA' in assignee):
        continue
    cpc=r.get('cpc')
    try:
        cpc_list=json.loads(cpc) if isinstance(cpc,str) else cpc
    except Exception:
        cpc_list=[]
    prim_codes=[ent.get('code') for ent in (cpc_list or []) if isinstance(ent,dict) and ent.get('first') is True and ent.get('code')]
    if not prim_codes:
        continue
    for code in prim_codes:
        assignee_to_subclasses.setdefault(assignee,set()).add(code[:4])

rows=[{'citing_assignee':a,'cpc_subclass':s} for a,subs in assignee_to_subclasses.items() for s in sorted(subs)]
df=pd.DataFrame(rows)

print('__RESULT__:')
print(json.dumps({'uc_publications_count':len(uc_pubs),'citing_assignee_subclass_rows':len(rows),'data':df.sort_values(['citing_assignee','cpc_subclass']).to_dict(orient='records')}))"""

env_args = {'var_call_L9PcQ9ViTcmIoQKlufknTEOs': ['publicationinfo'], 'var_call_jFzSdOxWdZ8AEHUCyMFYMZEd': ['cpc_definition'], 'var_call_mMyUsI7E40mgWFzvNjfDjqs3': [], 'var_call_32FcVDZfzFqhgKaVXxdtGrYO': 'file_storage/call_32FcVDZfzFqhgKaVXxdtGrYO.json', 'var_call_95hw93XGxIWUFTNJWdRekCg4': {'uc_publications_count': 0, 'sample_uc_publications': []}, 'var_call_QjRqKDtIH0hHYIbWjeuk2JXl': 'file_storage/call_QjRqKDtIH0hHYIbWjeuk2JXl.json'}

exec(code, env_args)
