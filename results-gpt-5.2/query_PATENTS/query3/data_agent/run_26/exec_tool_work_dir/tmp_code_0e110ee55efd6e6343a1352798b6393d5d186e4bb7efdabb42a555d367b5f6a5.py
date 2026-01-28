code = """import json, re

all_rows = var_call_utMC9UsVtwENeM1POJp7bJQV
if isinstance(all_rows, str):
    with open(all_rows, 'r', encoding='utf-8') as f:
        all_rows = json.load(f)

uc_rows = var_call_3LJn53sRZEOxjIojCRtkURl4
if isinstance(uc_rows, str):
    with open(uc_rows, 'r', encoding='utf-8') as f:
        uc_rows = json.load(f)

# UC pub -> primary subclass codes
uc_pub_to_subs = {}
uc_pubs=set()

def extract_primary_subclass(cpc_str):
    try:
        cpcs = json.loads(cpc_str) if cpc_str else []
    except Exception:
        return []
    subs=[]
    for it in cpcs if isinstance(cpcs, list) else []:
        if it.get('first') is True:
            code=it.get('code','')
            m=re.match(r'^([A-HY]\d{2}[A-Z])', code)
            if m:
                subs.append(m.group(1))
    out=[]
    for s in subs:
        if s not in out:
            out.append(s)
    return out

for r in uc_rows:
    pi=r.get('Patents_info','') or ''
    m=re.search(r'pub\. number\s+([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)', pi)
    if not m:
        continue
    pub=m.group(1)
    uc_pubs.add(pub)
    uc_pub_to_subs[pub]=extract_primary_subclass(r.get('cpc'))

# find citing assignees and the UC subclasses they cite
assignee_to_subs = {}
for r in all_rows:
    cit=r.get('citation')
    if not cit:
        continue
    try:
        cits=json.loads(cit)
    except Exception:
        continue
    hit_subs=set()
    for it in cits if isinstance(cits, list) else []:
        pn=it.get('publication_number')
        if pn and pn in uc_pub_to_subs:
            for s in uc_pub_to_subs[pn]:
                hit_subs.add(s)
    if not hit_subs:
        continue
    pi=r.get('Patents_info','') or ''
    # assignee is before ' holds' or 'In US, the application ... is owned by'
    m=re.match(r'^(.+?)\s+holds\b', pi)
    if not m:
        m=re.search(r'is owned by\s+(.+?)\s+and has', pi)
    assignee=(m.group(1).strip() if m else None)
    if not assignee:
        continue
    if assignee.upper()=='UNIV CALIFORNIA':
        continue
    assignee_to_subs.setdefault(assignee,set()).update(hit_subs)

subs_sorted=sorted({s for subs in assignee_to_subs.values() for s in subs})
assignees_sorted=sorted(assignee_to_subs)

print('__RESULT__:')
print(json.dumps({'assignee_count': len(assignees_sorted), 'subclasses': subs_sorted, 'assignees_sample': assignees_sorted[:30]}))"""

env_args = {'var_call_S6TOUVGeExRHPcirAJHOn3zr': ['publicationinfo'], 'var_call_pUUCO2MgEYWzPHULdFRFjj0E': ['cpc_definition'], 'var_call_u9IVkBoB07nCmO06deR66Nrp': [], 'var_call_3LJn53sRZEOxjIojCRtkURl4': 'file_storage/call_3LJn53sRZEOxjIojCRtkURl4.json', 'var_call_HrV5YecrJPI7rOVPNYo8unhw': {'uc_count': 59, 'uc_pubs_sample': ['AU-2003297741-A1', 'AU-2007297661-A1', 'AU-2008349842-A1', 'AU-2010214112-B2', 'AU-2015364602-B2', 'AU-2019275518-B2', 'AU-6535890-A', 'CA-2298540-A1', 'CA-2550552-A1', 'CA-2562038-C', 'CN-100339724-C', 'CN-102067370-B', 'CN-102584712-A', 'CN-103189548-A', 'EP-0826155-A4', 'EP-1212462-A1', 'EP-4284234-A1', 'HK-1250569-A1', 'ID-23426-A', 'IL-244029-A0']}, 'var_call_yTFkyx1scojLnrERgs9KIjJD': 'file_storage/call_yTFkyx1scojLnrERgs9KIjJD.json', 'var_call_utMC9UsVtwENeM1POJp7bJQV': 'file_storage/call_utMC9UsVtwENeM1POJp7bJQV.json'}

exec(code, env_args)
