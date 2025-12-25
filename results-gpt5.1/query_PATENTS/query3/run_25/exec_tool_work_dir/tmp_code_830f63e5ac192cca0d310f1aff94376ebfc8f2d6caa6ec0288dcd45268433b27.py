code = """import json, re, pandas as pd, os

uc_meta = var_call_2aY44VUDBIssKZfSEWn94oKu
uc_pubs = set(uc_meta['uc_publications'])

path_all = var_call_6DecUXPAsC3GDMwYCKGwODSs
with open(path_all, 'r') as f:
    all_data = json.load(f)

assignee_to_uc_cpc = {}

for rec in all_data:
    info = rec.get('Patents_info','')
    # skip UNIV CALIFORNIA assignees
    if 'UNIV CALIFORNIA' in info.upper() or 'UNIV OF CALIF' in info.upper() or 'REGENTS OF THE UNIVERSITY OF CALIFORNIA' in info.upper():
        continue
    # get assignee_harmonized: NAME pattern
    m = re.search(r'owned by ([^,]+)', info)
    if not m:
        m = re.search(r'holds the [A-Z]{2} patent filing .*?, with pub\. number', info)
    assignee = None
    m2 = re.search(r'^(.*?) holds the ', info)
    if m2:
        assignee = m2.group(1)
    if not assignee:
        m3 = re.search(r' is owned by ([^,]+)', info)
        if m3:
            assignee = m3.group(1)
    if not assignee:
        continue
    cit_raw = rec.get('citation') or '[]'
    try:
        cits = json.loads(cit_raw)
    except Exception:
        continue
    cited_uc = False
    for c in cits:
        pn = c.get('publication_number')
        if pn in uc_pubs:
            cited_uc = True
            break
    if not cited_uc:
        continue
    cpc_raw = rec.get('cpc') or '[]'
    try:
        cpcs = json.loads(cpc_raw)
    except Exception:
        continue
    prim_codes = [c['code'] for c in cpcs if c.get('first')]
    if not prim_codes and cpcs:
        prim_codes = [cpcs[0].get('code')]
    if not prim_codes:
        continue
    assignee_to_uc_cpc.setdefault(assignee, set()).update(prim_codes)

# convert sets to sorted lists
assignee_to_codes = {k: sorted(list(v)) for k,v in assignee_to_uc_cpc.items()}

import json as _json
out = _json.dumps(assignee_to_codes)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_r9o3TYrRDVmSSaniDTMva2bM': 'file_storage/call_r9o3TYrRDVmSSaniDTMva2bM.json', 'var_call_2aY44VUDBIssKZfSEWn94oKu': {'uc_publications': ['AU-2003297741-A1', 'AU-2007297661-A1', 'AU-2008349842-A1', 'AU-2010214112-B2', 'AU-2015364602-B2', 'AU-2019275518-B2', 'AU-6535890-A', 'CA-2298540-A1', 'CA-2550552-A1', 'CA-2562038-C', 'CN-100339724-C', 'CN-102067370-B', 'CN-102584712-A', 'CN-103189548-A', 'EP-0826155-A4', 'EP-1212462-A1', 'EP-4284234-A1', 'HK-1250569-A1', 'ID-23426-A', 'IL-244029-A0', 'IL-274176-A', 'JP-2014224156-A', 'JP-S6163700-A', 'KR-20200041324-A', 'MX-2013002850-A', 'RO-70061-A', 'TW-201925402-A', 'US-11376346-B2', 'US-11546022-B2', 'US-11667770-B2', 'US-2006051790-A1', 'US-2006292670-A1', 'US-2017145219-A1', 'US-2017281687-A1', 'US-2018243924-A1', 'US-2019328740-A1', 'US-2020025859-A1', 'US-2021000566-A1', 'US-2021101879-A1', 'US-2022018060-A1', 'US-2022074631-A1', 'US-2023155090-A1', 'US-2023171142-A1', 'US-2023279470-A1', 'US-2023321419-A1', 'US-5304932-A', 'US-5547866-A', 'US-6750960-B2', 'US-6767662-B2', 'US-9061071-B2', 'WO-2010045542-A3', 'WO-2012162563-A2', 'WO-2017214343-A1', 'WO-2018026404-A3', 'WO-2020055916-A9', 'WO-2021102420-A1', 'WO-2023225482-A3', 'WO-2024044766-A3', 'WO-2024112568-A1'], 'uc_pub_to_primary_cpc_example': {'US-2022074631-A1': ['F25B21/00', 'F25B21/00', 'F25B21/00'], 'TW-201925402-A': ['C09J9/02', 'C09J9/02', 'C09J9/02'], 'AU-2019275518-B2': ['A61K31/34', 'A61K31/351', 'A61K31/351', 'A61K31/357', 'A61K31/025'], 'JP-S6163700-A': ['C07K16/34', 'C07K16/34'], 'US-2017281687-A1': ['A61K35/28', 'A61K35/28', 'A61K35/28'], 'US-9061071-B2': ['A61K38/1767', 'A61K38/1767', 'A61K47/48261', 'A61K38/16'], 'EP-0826155-A4': ['G01T1/18', 'G01T1/18'], 'RO-70061-A': ['C07D295/26', 'C07D295/26'], 'WO-2021102420-A1': ['A61P35/00'], 'WO-2012162563-A2': ['C12Q1/6881', 'C12Q1/6806'], 'US-11376346-B2': ['A61L27/58', 'A61L27/3633', 'A61L27/3633'], 'CN-100339724-C': ['G01V3/12', 'G01V3/12'], 'US-2017145219-A1': ['C08B37/0024', 'C08B37/0024', 'C09D105/00', 'C09C1/3676'], 'KR-20200041324-A': ['C07F7/003', 'C07F7/003', 'C07F7/003', 'B01J20/226'], 'CN-103189548-A': ['C30B7/105', 'C30B7/105', 'C30B29/38'], 'CA-2298540-A1': ['C07K14/705', 'C07K14/705'], 'US-2021000566-A1': ['A61F9/009', 'A61B90/50', 'A61B90/50'], 'US-2006051790-A1': ['C12Q1/6883', 'C12Q1/6883'], 'US-2023171142-A1': ['G01S11/02', 'H04L27/265', 'H04L27/265'], 'WO-2018026404-A3': ['H04B1/38', 'H04B1/26']}}, 'var_call_6DecUXPAsC3GDMwYCKGwODSs': 'file_storage/call_6DecUXPAsC3GDMwYCKGwODSs.json'}

exec(code, env_args)
