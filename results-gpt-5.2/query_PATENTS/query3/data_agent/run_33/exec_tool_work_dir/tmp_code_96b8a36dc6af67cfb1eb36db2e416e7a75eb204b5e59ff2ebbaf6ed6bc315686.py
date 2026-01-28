code = """import json, re, pandas as pd

# load UC patents
uc_src = var_call_yQnQkwtLe8lcRP9xhFF3YIal
if isinstance(uc_src, str):
    with open(uc_src, 'r', encoding='utf-8') as f:
        uc_rows = json.load(f)
else:
    uc_rows = uc_src

# extract UC publication numbers (targets)
uc_pubs=set()
for r in uc_rows:
    pi=r.get('Patents_info') or ''
    for m in re.finditer(r'pub\. number\s+([A-Z]{2}-[0-9]+[A-Z0-9]*-[A-Z0-9]+)', pi):
        uc_pubs.add(m.group(1))
    for m in re.finditer(r'publication number\s+([A-Z]{2}-[0-9]+[A-Z0-9]*-[A-Z0-9]+)', pi):
        uc_pubs.add(m.group(1))

# load potential citing patents (all non-UC with US citations)
citing_src = var_call_zpk1hBmFraNmF010iv5ex2Av
if isinstance(citing_src, str):
    with open(citing_src, 'r', encoding='utf-8') as f:
        citing_rows = json.load(f)
else:
    citing_rows = citing_src

pairs=[]  # (assignee, cpc_subclass)
all_subclasses=set()

def parse_assignee(pi:str):
    # patterns observed
    m=re.search(r'^(.+?)\s+holds\b', pi)
    if m: return m.group(1).strip()
    m=re.search(r'^In\s+[A-Z]{2},\s+the\s+application\s+\(.*?\)\s+is\s+owned\s+by\s+(.+?)\s+and\s+has\b', pi)
    if m: return m.group(1).strip()
    m=re.search(r'^In\s+[A-Z]{2},\s+the\s+patent\s+application\s+\(.*?\)\s+is\s+assigned\s+to\s+(.+?)\s+and\s+has\b', pi)
    if m: return m.group(1).strip()
    m=re.search(r'^(.+?)\s+has\b', pi)
    if m: return m.group(1).strip()
    return None

for r in citing_rows:
    pi=r.get('Patents_info') or ''
    assignee=parse_assignee(pi)
    if not assignee or 'UNIV CALIFORNIA' in assignee:
        continue
    # determine if cites any UC pub
    cit=r.get('citation')
    if not cit:
        continue
    try:
        cit_list=json.loads(cit)
    except Exception:
        continue
    cited_pubs={c.get('publication_number') for c in cit_list if isinstance(c,dict)}
    if not (cited_pubs & uc_pubs):
        continue
    # get primary CPC subclass: first==true; take subclass = first 4 chars before '/'
    cpc=r.get('cpc')
    try:
        cpc_list=json.loads(cpc) if cpc else []
    except Exception:
        cpc_list=[]
    prim_codes=[x.get('code') for x in cpc_list if isinstance(x,dict) and x.get('first') is True and x.get('code')]
    for code in prim_codes:
        base=code.split('/')[0]
        subclass=base[:4]  # e.g., H01M
        all_subclasses.add(subclass)
        pairs.append((assignee, subclass))

pairs=list(set(pairs))
subclasses=sorted(all_subclasses)

print('__RESULT__:')
print(json.dumps({'pairs': pairs, 'subclasses': subclasses}, ensure_ascii=False))"""

env_args = {'var_call_1Shnl7Bkiz3f17tuCVOSAZFt': ['publicationinfo'], 'var_call_XBXGwC9AYNLV0N17OPMqqfgP': ['cpc_definition'], 'var_call_yQnQkwtLe8lcRP9xhFF3YIal': 'file_storage/call_yQnQkwtLe8lcRP9xhFF3YIal.json', 'var_call_zpk1hBmFraNmF010iv5ex2Av': 'file_storage/call_zpk1hBmFraNmF010iv5ex2Av.json'}

exec(code, env_args)
