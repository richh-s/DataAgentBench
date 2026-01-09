code = """import json, re

# Load UC pubs
uc_path = var_call_efT0MFon4DlBI6omonZohoVs
with open(uc_path,'r',encoding='utf-8') as f:
    uc_recs = json.load(f)

pub_re = re.compile(r"pub\. number\s+([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)")
ass_re = re.compile(r"owned by (.+?) and has pub\. number|assigned to (.+?) and has publication number|holds the [A-Z]{2} patent filing .*?, with pub\. number|holds the US patent application .*?, with publication number", re.IGNORECASE)

uc_pubnums=set()
for r in uc_recs:
    m=pub_re.search(r.get('Patents_info','') or '')
    if m:
        uc_pubnums.add(m.group(1))

# Load broad citing set
cite_path = var_call_Uim2b3zfpguEZmRiVsUWUsDi
with open(cite_path,'r',encoding='utf-8') as f:
    citer_recs = json.load(f)

# parse citations and filter to those that cite UC pubnums
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

result = {"uc_pubnums_count": len(uc_pubnums), "citing_records": len(citing)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_efT0MFon4DlBI6omonZohoVs': 'file_storage/call_efT0MFon4DlBI6omonZohoVs.json', 'var_call_7IGIUZlAUB6KKpkg7CvtV9if': 'file_storage/call_7IGIUZlAUB6KKpkg7CvtV9if.json', 'var_call_csjqdJPUt2eWmapXV1UBKVpV': {'error': 'Need additional query to find citing patents; run query_db on publication_database with citation LIKE UC pubnums.'}, 'var_call_Uim2b3zfpguEZmRiVsUWUsDi': 'file_storage/call_Uim2b3zfpguEZmRiVsUWUsDi.json'}

exec(code, env_args)
