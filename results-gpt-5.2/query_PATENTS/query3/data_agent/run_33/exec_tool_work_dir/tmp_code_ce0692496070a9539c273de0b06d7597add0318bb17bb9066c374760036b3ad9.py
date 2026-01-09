code = """import json, re

# UC pubs
uc_src = var_call_yQnQkwtLe8lcRP9xhFF3YIal
if isinstance(uc_src, str):
    with open(uc_src, 'r', encoding='utf-8') as f:
        uc_rows = json.load(f)
else:
    uc_rows = uc_src

uc_pubs=set()
for r in uc_rows:
    pi=r.get('Patents_info') or ''
    for m in re.finditer(r'(?:pub\. number|publication number)\s+([A-Z]{2}-[0-9]+[A-Z0-9]*-[A-Z0-9]+)', pi):
        uc_pubs.add(m.group(1))

# all rows with US- in citation
all_src = var_call_POoqrEqcjKIbyAAZthbJ2qkQ
if isinstance(all_src, str):
    with open(all_src, 'r', encoding='utf-8') as f:
        rows = json.load(f)
else:
    rows = all_src

# count how many cite UC pubs
hits=[]
for r in rows:
    if 'UNIV CALIFORNIA' in (r.get('Patents_info') or ''):
        continue
    cit=r.get('citation')
    if not cit:
        continue
    try:
        cl=json.loads(cit)
    except Exception:
        continue
    cited=set([c.get('publication_number') for c in cl if isinstance(c,dict)])
    inter=list(cited & uc_pubs)
    if inter:
        hits.append({'Patents_info': r.get('Patents_info'), 'uc_cited': inter[:5], 'n_uc_cited': len(inter)})

print('__RESULT__:')
print(json.dumps({'n_uc_pubs': len(uc_pubs), 'n_rows_checked': len(rows), 'n_hits': len(hits), 'sample_hits': hits[:5]}, ensure_ascii=False))"""

env_args = {'var_call_1Shnl7Bkiz3f17tuCVOSAZFt': ['publicationinfo'], 'var_call_XBXGwC9AYNLV0N17OPMqqfgP': ['cpc_definition'], 'var_call_yQnQkwtLe8lcRP9xhFF3YIal': 'file_storage/call_yQnQkwtLe8lcRP9xhFF3YIal.json', 'var_call_zpk1hBmFraNmF010iv5ex2Av': 'file_storage/call_zpk1hBmFraNmF010iv5ex2Av.json', 'var_call_l0AFL45eZ5Jdyp1xkvfBxfcE': {'pairs': [], 'subclasses': []}, 'var_call_WMJvbnsJ7iNdFg81pMCWFYHo': [], 'var_call_POoqrEqcjKIbyAAZthbJ2qkQ': 'file_storage/call_POoqrEqcjKIbyAAZthbJ2qkQ.json'}

exec(code, env_args)
