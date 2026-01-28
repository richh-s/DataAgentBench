code = """import json, re

uc_path = var_call_mGsSzfpCDmC2t8Guo7pudB7f
with open(uc_path,'r',encoding='utf-8') as f:
    uc_recs = json.load(f)

all_path = var_call_o7MjA49BL1WAXlf6NUCFG4d2
with open(all_path,'r',encoding='utf-8') as f:
    all_recs = json.load(f)

def extract_pub_number(patents_info:str):
    m = re.search(r'pub\. number\s+([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)', patents_info)
    if not m:
        m = re.search(r'publication number\s+([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)', patents_info)
    return m.group(1) if m else None

def extract_assignee(patents_info:str):
    m = re.search(r'^(.*?)\s+holds\s+the\s+.*?\(.*?\),\s+with\s+publication number', patents_info)
    if m:
        return m.group(1).strip()
    for pat in [r'owned by\s+([^,\.]+)', r'assigned to\s+([^,\.]+)']:
        m = re.search(pat, patents_info)
        if m:
            return m.group(1).strip()
    m = re.search(r'^([^,]+?)\s+holds', patents_info)
    if m:
        return m.group(1).strip()
    return None

def primary_cpc_subclass(cpc_str:str):
    if not cpc_str:
        return None
    try:
        arr = json.loads(cpc_str)
    except Exception:
        return None
    # pick first==true else first element
    code=None
    for e in arr:
        if isinstance(e, dict) and e.get('first') is True and e.get('code'):
            code=e['code']
            break
    if code is None and arr:
        e=arr[0]
        if isinstance(e, dict):
            code=e.get('code')
    if not code:
        return None
    # subclass = letter+2digits after section/class, e.g., H01M10/0562 -> H01M
    m=re.match(r'^([A-HY]\d{2}[A-Z])', code)
    return m.group(1) if m else None

uc_pubnums=set(filter(None,(extract_pub_number(r.get('Patents_info','') or '') for r in uc_recs)))

pairs=set()
subclasses=set()
for r in all_recs:
    ass=extract_assignee(r.get('Patents_info','') or '')
    if not ass:
        continue
    if ass.strip().upper()=='UNIV CALIFORNIA':
        continue
    cit=r.get('citation')
    try:
        cits=json.loads(cit) if cit else []
    except Exception:
        continue
    cited_pubs=set()
    for c in cits:
        if isinstance(c, dict):
            pn=c.get('publication_number')
            if pn:
                cited_pubs.add(pn)
    if uc_pubnums.intersection(cited_pubs):
        sc=primary_cpc_subclass(r.get('cpc') or '')
        if sc:
            pairs.add((ass, sc))
            subclasses.add(sc)

import json as _json
print('__RESULT__:')
print(_json.dumps({'pair_count': len(pairs), 'assignee_count': len(set(a for a,_ in pairs)), 'subclass_count': len(subclasses), 'pairs_preview': sorted(list(pairs))[:20], 'subclasses': sorted(list(subclasses))}))"""

env_args = {'var_call_rx5W1jUyQT0P9qEJcsjzjH9I': ['publicationinfo'], 'var_call_fMEsFRgAHptD22vzpbFkWKRE': ['cpc_definition'], 'var_call_mGsSzfpCDmC2t8Guo7pudB7f': 'file_storage/call_mGsSzfpCDmC2t8Guo7pudB7f.json', 'var_call_csblGH9jl1APg8p4TKZUsQ7I': {'uc_pub_count': 114, 'sample_uc_pubnums': ['AU-2003247814-A1', 'AU-2003297741-A1', 'AU-2004253879-A1', 'AU-2005269556-A1', 'AU-2007297661-A1', 'AU-2008349842-A1', 'AU-2010214112-B2', 'AU-2015364602-B2', 'AU-2017356943-A1', 'AU-2019275518-B2']}, 'var_call_o7MjA49BL1WAXlf6NUCFG4d2': 'file_storage/call_o7MjA49BL1WAXlf6NUCFG4d2.json'}

exec(code, env_args)
