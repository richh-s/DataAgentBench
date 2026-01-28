code = """import json, re

uc_path = var_call_j55SyTVQyBw0aAybXsyxCaAM
with open(uc_path, 'r', encoding='utf-8') as f:
    uc_rows=json.load(f)

# Extract all pub numbers patterns (more general): XX-<alphanum>-<kind>
pat = re.compile(r"\b([A-Z]{2}-[0-9]{4,}[0-9A-Z]*-[A-Z][0-9A-Z]?)\b")

uc_pubs=set()
for r in uc_rows:
    txt=r.get('Patents_info','') or ''
    for m in pat.findall(txt):
        uc_pubs.add(m)

cit_path = var_call_KJ7mredPpIpCLZFg4dHYGs9s
with open(cit_path,'r',encoding='utf-8') as f:
    citing_rows=json.load(f)

# Build set of all cited pub_numbers in DB
cited=set()
for r in citing_rows:
    cstr=r.get('citation')
    if not cstr or cstr.strip() in ('','[]'): continue
    try:
        cites=json.loads(cstr)
    except: continue
    for c in cites:
        if isinstance(c,dict):
            pn=c.get('publication_number')
            if pn:
                cited.add(pn)

# Find intersection
inter = sorted(list(set(uc_pubs).intersection(cited)))
print('__RESULT__:')
print(json.dumps({'uc_pubs_count': len(uc_pubs), 'cited_unique_count': len(cited), 'intersection_count': len(inter), 'intersection_sample': inter[:20]}))"""

env_args = {'var_call_RXZxPa6ek2GtXCBDhmGKF66H': ['publicationinfo'], 'var_call_xRaFlt6HbwpuEGgcKr0x8ZXF': ['cpc_definition'], 'var_call_j55SyTVQyBw0aAybXsyxCaAM': 'file_storage/call_j55SyTVQyBw0aAybXsyxCaAM.json', 'var_call_zqNKJTMEJLBC8OYNvbOYtOK0': {'uc_pub_count': 59}, 'var_call_KJ7mredPpIpCLZFg4dHYGs9s': 'file_storage/call_KJ7mredPpIpCLZFg4dHYGs9s.json', 'var_call_gTbEbPoeoJQcPiupxFUywacn': {'pairs': [], 'pair_count': 0, 'assignee_count': 0}, 'var_call_zfz41NofEzSTuL1G6p8oWKRs': {'uc_pub_sample': ['AU-2003297741-A1', 'AU-2007297661-A1', 'AU-2008349842-A1', 'AU-2010214112-B2', 'AU-2015364602-B2', 'AU-2019275518-B2', 'AU-6535890', 'CA-2298540-A1', 'CA-2550552-A1', 'CA-2562038', 'CN-100339724', 'CN-102067370', 'CN-102584712', 'CN-103189548', 'EP-0826155-A4', 'EP-1212462-A1', 'EP-4284234-A1', 'HK-1250569-A1', 'ID-23426', 'IL-244029-A0'], 'match_count_5000': 0, 'match_sample': []}}

exec(code, env_args)
