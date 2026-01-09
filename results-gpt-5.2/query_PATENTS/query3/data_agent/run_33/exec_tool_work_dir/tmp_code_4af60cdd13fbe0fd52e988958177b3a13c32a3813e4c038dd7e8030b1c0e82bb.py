code = """import json, re

def parse_assignee(pi:str):
    m=re.search(r'^(.+?)\s+holds\b', pi)
    if m: return m.group(1).strip()
    m=re.search(r'^(.+?)\s+is\s+assigned\s+to\s+(.+?)\s+and\s+has\b', pi)
    if m: return m.group(2).strip()
    m=re.search(r'^The\s+US\s+application.*?\s+is\s+owned\s+by\s+(.+?)\s+and\s+has\b', pi)
    if m: return m.group(1).strip()
    m=re.search(r'^The\s+US\s+patent\s+application.*?\s+is\s+held\s+by\s+(.+?)\s+and\s+has\b', pi)
    if m: return m.group(1).strip()
    return None

# Load full hits rows by re-filtering from all citations
all_src = var_call_POoqrEqcjKIbyAAZthbJ2qkQ
if isinstance(all_src, str):
    with open(all_src, 'r', encoding='utf-8') as f:
        rows = json.load(f)
else:
    rows = all_src

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

pairs=set()
subclasses=set()
for r in rows:
    pi=r.get('Patents_info') or ''
    if 'UNIV CALIFORNIA' in pi:
        continue
    cit=r.get('citation')
    if not cit:
        continue
    try:
        cl=json.loads(cit)
    except Exception:
        continue
    cited=set([c.get('publication_number') for c in cl if isinstance(c,dict)])
    if not (cited & uc_pubs):
        continue
    assignee=parse_assignee(pi)
    if not assignee or 'UNIV CALIFORNIA' in assignee:
        continue
    cpc=r.get('cpc')
    try:
        cpc_list=json.loads(cpc) if cpc else []
    except Exception:
        cpc_list=[]
    prim_codes=[x.get('code') for x in cpc_list if isinstance(x,dict) and x.get('first') is True and x.get('code')]
    for code in prim_codes:
        subclass=code.split('/')[0][:4]
        pairs.add((assignee, subclass))
        subclasses.add(subclass)

print('__RESULT__:')
print(json.dumps({'pairs': sorted(list(pairs)), 'subclasses': sorted(list(subclasses))}, ensure_ascii=False))"""

env_args = {'var_call_1Shnl7Bkiz3f17tuCVOSAZFt': ['publicationinfo'], 'var_call_XBXGwC9AYNLV0N17OPMqqfgP': ['cpc_definition'], 'var_call_yQnQkwtLe8lcRP9xhFF3YIal': 'file_storage/call_yQnQkwtLe8lcRP9xhFF3YIal.json', 'var_call_zpk1hBmFraNmF010iv5ex2Av': 'file_storage/call_zpk1hBmFraNmF010iv5ex2Av.json', 'var_call_l0AFL45eZ5Jdyp1xkvfBxfcE': {'pairs': [], 'subclasses': []}, 'var_call_WMJvbnsJ7iNdFg81pMCWFYHo': [], 'var_call_POoqrEqcjKIbyAAZthbJ2qkQ': 'file_storage/call_POoqrEqcjKIbyAAZthbJ2qkQ.json', 'var_call_ExZhvZ0JkwRvzm2ygYfUgMTL': {'n_uc_pubs': 112, 'n_rows_checked': 77562, 'n_hits': 4, 'sample_hits': [{'Patents_info': 'The US patent filing (application number US-4007205-A) is assigned to CALIFORNIA INST OF TECHN and has publication number US-2005165588-A1.', 'uc_cited': ['US-6237292-B1'], 'n_uc_cited': 1}, {'Patents_info': 'The US patent application (no. US-201715785968-A) is held by BLOOM ENERGY CORP and has publication no. US-10615444-B2.', 'uc_cited': ['US-6767662-B2'], 'n_uc_cited': 1}, {'Patents_info': 'The US application (ID US-201414520615-A) is owned by CRYSTAL IS INC and has publication no. US-9447521-B2.', 'uc_cited': ['US-2010025717-A1'], 'n_uc_cited': 1}, {'Patents_info': 'SCHOWALTER LEO J holds the US application (number US-2000608-A), with publication number US-9437430-B2.', 'uc_cited': ['US-2010025717-A1'], 'n_uc_cited': 1}]}}

exec(code, env_args)
