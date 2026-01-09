code = """import json, re, pandas as pd

# load all with citations
path = var_call_QjRqKDtIH0hHYIbWjeuk2JXl
with open(path,'r',encoding='utf-8') as f:
    citing_recs = json.load(f)

# helper parse assignee
def parse_assignee(patents_info:str):
    if not patents_info:
        return None
    # patterns
    m = re.search(r'^(.*?)\s+holds\b', patents_info)
    if m:
        return m.group(1).strip()
    m = re.search(r'is owned by\s+([^\n]+?)\s+and has', patents_info)
    if m:
        return m.group(1).strip()
    m = re.search(r'is assigned to\s+([^\n]+?)\s+and has', patents_info)
    if m:
        return m.group(1).strip()
    return None

# find UC cited pubs by looking for assignee UNIV CALIFORNIA in same table and map pub numbers
# We'll use already fetched cited_uc_recs mentioning UNIV CALIFORNIA, but pub extraction earlier failed.
# New extraction: look for 'pub. number ' and also 'pub. number' variants.

with open(var_call_32FcVDZfzFqhgKaVXxdtGrYO,'r',encoding='utf-8') as f:
    uc_recs = json.load(f)

uc_pubs=set()
for r in uc_recs:
    pi=r.get('Patents_info','') or ''
    m=re.search(r'pub\.? number\s+([A-Z]{2}-[0-9]+[A-Z0-9\-]*?)\b', pi)
    if m:
        uc_pubs.add(m.group(1))

# if still empty, attempt extract 'publication number'
if not uc_pubs:
    for r in uc_recs:
        pi=r.get('Patents_info','') or ''
        m=re.search(r'publication number\s+([A-Z]{2}-[0-9]+[A-Z0-9\-]*?)\b', pi)
        if m:
            uc_pubs.add(m.group(1))

# Build assignee -> set(primary subclass codes)
assignee_to_subclasses={}

for r in citing_recs:
    citations=r.get('citation')
    if not citations:
        continue
    try:
        cit_list=json.loads(citations) if isinstance(citations,str) else citations
    except Exception:
        continue
    # check if any citation pub in uc_pubs
    cited_match=False
    for c in cit_list:
        pub=c.get('publication_number') if isinstance(c,dict) else None
        if pub and pub in uc_pubs:
            cited_match=True
            break
    if not cited_match:
        continue
    assignee=parse_assignee(r.get('Patents_info','') or '')
    if not assignee:
        continue
    # exclude UNIV CALIFORNIA itself
    if 'UNIV CALIFORNIA' in assignee or 'UNIVERSITY OF CALIFORNIA' in assignee or 'REGENTS OF THE UNIVERSITY OF CALIFORNIA' in assignee:
        continue
    # primary CPC subclass from cpc where first==true; subclass is first 4 chars (e.g., A01B)
    cpc=r.get('cpc')
    try:
        cpc_list=json.loads(cpc) if isinstance(cpc,str) else cpc
    except Exception:
        cpc_list=[]
    prim_codes=[]
    for ent in cpc_list or []:
        if isinstance(ent,dict) and ent.get('first') is True:
            code=ent.get('code')
            if code:
                prim_codes.append(code)
    # fallback: none -> skip
    if not prim_codes:
        continue
    for code in prim_codes:
        subclass=code[:4]
        assignee_to_subclasses.setdefault(assignee,set()).add(subclass)

rows=[]
for a,subs in assignee_to_subclasses.items():
    for s in subs:
        rows.append({'citing_assignee':a,'cpc_subclass':s})

df=pd.DataFrame(rows)

print('__RESULT__:')
print(json.dumps({'uc_publications_count':len(uc_pubs),'citing_assignee_subclass_rows':len(rows),'data':df.sort_values(['citing_assignee','cpc_subclass']).to_dict(orient='records')[:200]}))"""

env_args = {'var_call_L9PcQ9ViTcmIoQKlufknTEOs': ['publicationinfo'], 'var_call_jFzSdOxWdZ8AEHUCyMFYMZEd': ['cpc_definition'], 'var_call_mMyUsI7E40mgWFzvNjfDjqs3': [], 'var_call_32FcVDZfzFqhgKaVXxdtGrYO': 'file_storage/call_32FcVDZfzFqhgKaVXxdtGrYO.json', 'var_call_95hw93XGxIWUFTNJWdRekCg4': {'uc_publications_count': 0, 'sample_uc_publications': []}, 'var_call_QjRqKDtIH0hHYIbWjeuk2JXl': 'file_storage/call_QjRqKDtIH0hHYIbWjeuk2JXl.json'}

exec(code, env_args)
