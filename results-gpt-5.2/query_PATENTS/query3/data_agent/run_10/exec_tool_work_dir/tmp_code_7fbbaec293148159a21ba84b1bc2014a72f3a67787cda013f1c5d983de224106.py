code = """import json, re

# load CPC definitions
cpc_path = var_call_7IGIUZlAUB6KKpkg7CvtV9if
with open(cpc_path,'r',encoding='utf-8') as f:
    cpc_defs = json.load(f)

title_by_symbol = {d['symbol']: d.get('titleFull') for d in cpc_defs if d.get('symbol')}

def subclass(code):
    if not code: return None
    code = code.strip()
    # remove spaces
    code = code.replace(' ','')
    # subclass is like A01B33/00? actually main group incl /00. We'll use first 4 + class+subclass digits
    # CPC subclass is 4 chars (section+class+subclass), e.g., H01M, C12Q
    return code[:4] if len(code)>=4 else code

# Load UC pubs
uc_path = var_call_efT0MFon4DlBI6omonZohoVs
with open(uc_path,'r',encoding='utf-8') as f:
    uc_recs = json.load(f)

pub_re = re.compile(r"pub\. number\s+([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)")
uc_pubnums=set()
for r in uc_recs:
    m=pub_re.search(r.get('Patents_info','') or '')
    if m:
        uc_pubnums.add(m.group(1))

# Load broad citer set
cite_path = var_call_Uim2b3zfpguEZmRiVsUWUsDi
with open(cite_path,'r',encoding='utf-8') as f:
    citer_recs = json.load(f)

# find records citing UC
citing=[]
for r in citer_recs:
    cit=r.get('citation')
    if not cit: continue
    try:
        arr=json.loads(cit)
    except Exception:
        continue
    cited=set([c.get('publication_number') for c in arr if isinstance(c,dict)])
    if cited & uc_pubnums:
        citing.append(r)

# parse assignee name from Patents_info: before 'holds the'
assignee=None
if citing:
    pi=citing[0].get('Patents_info','')
    assignee=pi.split(' holds the ')[0].strip()

# exclude UNIV CALIFORNIA itself
rows=[]
for r in citing:
    pi=r.get('Patents_info','')
    ass=pi.split(' holds the ')[0].strip()
    if 'UNIV CALIFORNIA' in ass.upper():
        continue
    # primary cpc: entries with first=true
    prim=[]
    try:
        cpcs=json.loads(r.get('cpc') or '[]')
        for e in cpcs:
            if isinstance(e,dict) and e.get('first') is True:
                prim.append(e.get('code'))
    except Exception:
        prim=[]
    # map to subclass titles: need title for subclass symbol; use exact match if exists else try /00 for group? Here request CPC subclass title.
    for code in prim:
        sc=subclass(code)
        title=title_by_symbol.get(sc)
        if title is None:
            # try find any symbol that matches subclass exactly in defs already handled; else None
            title=''
        rows.append({'citing_assignee': ass, 'cpc_subclass': sc, 'cpc_subclass_titleFull': title})

# unique
uniq=[]
seen=set()
for row in rows:
    key=(row['citing_assignee'], row['cpc_subclass'])
    if key in seen: continue
    seen.add(key)
    uniq.append(row)

print('__RESULT__:')
print(json.dumps(uniq))"""

env_args = {'var_call_efT0MFon4DlBI6omonZohoVs': 'file_storage/call_efT0MFon4DlBI6omonZohoVs.json', 'var_call_7IGIUZlAUB6KKpkg7CvtV9if': 'file_storage/call_7IGIUZlAUB6KKpkg7CvtV9if.json', 'var_call_csjqdJPUt2eWmapXV1UBKVpV': {'error': 'Need additional query to find citing patents; run query_db on publication_database with citation LIKE UC pubnums.'}, 'var_call_Uim2b3zfpguEZmRiVsUWUsDi': 'file_storage/call_Uim2b3zfpguEZmRiVsUWUsDi.json', 'var_call_Vl2XhmkHknjigtKxfxbo9IrD': {'uc_pubnums_count': 59, 'citing_records': 1}}

exec(code, env_args)
