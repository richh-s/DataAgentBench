code = """import json, re, pandas as pd

# Load rows (may be a filepath if too large)
rows = var_call_3LJn53sRZEOxjIojCRtkURl4
if isinstance(rows, str):
    with open(rows, 'r', encoding='utf-8') as f:
        rows = json.load(f)

def extract_pub_numbers(citation_str):
    try:
        c = json.loads(citation_str) if citation_str else []
    except Exception:
        return []
    pubs = []
    for it in c if isinstance(c, list) else []:
        pn = it.get('publication_number')
        if pn:
            pubs.append(pn)
    return pubs

def extract_primary_subclass(cpc_str):
    # primary = entries with first==true; subclass = first 4 chars of code (letter+2 digits+letter) OR group like H01L etc
    try:
        cpcs = json.loads(cpc_str) if cpc_str else []
    except Exception:
        return []
    subs = []
    for it in cpcs if isinstance(cpcs, list) else []:
        if it.get('first') is True:
            code = it.get('code','')
            m = re.match(r'^([A-HY]\d{2}[A-Z])', code)
            if m:
                subs.append(m.group(1))
    # unique preserve order
    out=[]
    for s in subs:
        if s not in out:
            out.append(s)
    return out

# UC patents set + their primary subclasses
uc_pub_to_subs = {}
uc_pub_numbers = set()
for r in rows:
    pi = r.get('Patents_info','') or ''
    m = re.search(r'pub\. number\s+([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)', pi)
    if not m:
        m = re.search(r'pub\. number\s+([A-Z]{2}-[0-9A-Z]+)', pi)
    if m:
        pub = m.group(1)
        uc_pub_numbers.add(pub)
        uc_pub_to_subs[pub] = extract_primary_subclass(r.get('cpc'))

# Build query for citing patents that cite any UC pub
uc_list = sorted(list(uc_pub_numbers))
print('__RESULT__:')
print(json.dumps({'uc_count': len(uc_list), 'uc_pubs_sample': uc_list[:20]}))"""

env_args = {'var_call_S6TOUVGeExRHPcirAJHOn3zr': ['publicationinfo'], 'var_call_pUUCO2MgEYWzPHULdFRFjj0E': ['cpc_definition'], 'var_call_u9IVkBoB07nCmO06deR66Nrp': [], 'var_call_3LJn53sRZEOxjIojCRtkURl4': 'file_storage/call_3LJn53sRZEOxjIojCRtkURl4.json'}

exec(code, env_args)
