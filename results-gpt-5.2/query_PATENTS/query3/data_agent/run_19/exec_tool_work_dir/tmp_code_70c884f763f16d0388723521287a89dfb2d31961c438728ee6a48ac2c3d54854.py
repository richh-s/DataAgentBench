code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str):
        # file path
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

citing_recs = load_records(var_call_gCtsGZNDafYsusAqCOrcY15R)
uc_recs = load_records(var_call_z4Bld5nhRj46hrtJBKpQYgRB)

# UC publication numbers set
uc_pubnums=set()
for r in uc_recs:
    txt=r.get('Patents_info','') or ''
    m=re.search(r'pub\. number\s+([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)', txt)
    if m:
        uc_pubnums.add(m.group(1))
    # also capture patterns 'pub. number XX-YYYY-Z'
    for m2 in re.finditer(r'\b[A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+\b', txt):
        # but restrict to those preceded by 'pub' maybe too hard; keep all? no.
        pass

# Build mapping citing assignee -> set of primary CPC subclass codes
pairs=set()
for r in citing_recs:
    pat_info=r.get('Patents_info','') or ''
    # extract assignee before 'holds' or 'is owned by' or 'is assigned to'
    assignee=None
    m=re.match(r'^(.*?)\s+holds\b', pat_info)
    if not m:
        m=re.match(r'^(.*?)\s+holds\b', pat_info)
    if not m:
        m=re.match(r'^(.*?)\s+is\s+owned\s+by\b', pat_info)
    if not m:
        m=re.match(r'^In\s+[A-Z]{2},\s+the\s+.*?\s+is\s+owned\s+by\s+(.*?)\s+and\s+has\b', pat_info)
    if not m:
        m=re.match(r'^In\s+[A-Z]{2},\s+the\s+.*?\s+is\s+assigned\s+to\s+(.*?)\s+and\s+has\b', pat_info)
    if not m:
        m=re.match(r'^(.*?)\s+holds\b', pat_info)
    if m:
        assignee=m.group(1).strip()
    else:
        m=re.search(r'\bis\s+assigned\s+to\s+(.*?)\s+and\s+has\b', pat_info)
        if m:
            assignee=m.group(1).strip()
    if not assignee:
        continue
    if 'UNIV CALIFORNIA' in assignee.upper():
        continue

    # parse citations list
    c=r.get('citation','[]')
    try:
        cits=json.loads(c) if isinstance(c,str) else c
    except Exception:
        continue
    cites_uc=False
    for cit in cits:
        pn=(cit or {}).get('publication_number','')
        if pn in uc_pubnums:
            cites_uc=True
            break
    if not cites_uc:
        continue

    # parse CPC and keep first==true; derive subclass (first 4 chars like H01M)
    cpc=r.get('cpc','[]')
    try:
        cpcs=json.loads(cpc) if isinstance(cpc,str) else cpc
    except Exception:
        cpcs=[]
    for e in cpcs:
        if isinstance(e, dict) and e.get('first') is True:
            code=e.get('code','')
            subclass=code[:4]
            if subclass:
                pairs.add((assignee, subclass))

pairs_sorted=sorted(pairs)
subclasses=sorted({p[1] for p in pairs_sorted})

print('__RESULT__:')
print(json.dumps({'pairs': pairs_sorted, 'subclasses': subclasses, 'uc_pubnums_count': len(uc_pubnums)}))"""

env_args = {'var_call_CHdfydOYns2nzKZv55IiN5Nt': ['publicationinfo'], 'var_call_e8HS6355ELEOpncpwgmL8axE': ['cpc_definition'], 'var_call_z4Bld5nhRj46hrtJBKpQYgRB': 'file_storage/call_z4Bld5nhRj46hrtJBKpQYgRB.json', 'var_call_gCtsGZNDafYsusAqCOrcY15R': 'file_storage/call_gCtsGZNDafYsusAqCOrcY15R.json'}

exec(code, env_args)
