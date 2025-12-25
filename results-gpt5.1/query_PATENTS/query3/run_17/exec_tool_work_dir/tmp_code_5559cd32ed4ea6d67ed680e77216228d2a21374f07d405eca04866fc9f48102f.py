code = """import json, re, pandas as pd, pathlib

# Load citing records
path = pathlib.Path(var_call_oQlv2PLuWqLW7ywjZmCshQPA)
with open(path,'r') as f:
    citing = json.load(f)

# Load UC publication numbers (already a list)
uc_pubs = var_call_mdQIt4vXnhoL3ILCtztyaEuv
uc_set = set(uc_pubs)

records = []
for rec in citing:
    txt = rec.get('Patents_info','')
    m_assignee = re.search(r'assignee_harmonized: ([^,.;]+)', txt)
    assignee = m_assignee.group(1).strip() if m_assignee else None
    if not assignee or assignee.upper() == 'UNIV CALIFORNIA':
        continue
    cited_list = json.loads(rec.get('citation','[]')) if rec.get('citation') else []
    cites_uc = False
    for c in cited_list:
        pub = c.get('publication_number')
        if pub in uc_set:
            cites_uc = True
            break
    if not cites_uc:
        continue
    cpc_list = json.loads(rec.get('cpc','[]')) if rec.get('cpc') else []
    primary_codes = sorted({c['code'] for c in cpc_list if c.get('first') and c.get('inventive')})
    if not primary_codes:
        continue
    records.append({'assignee': assignee, 'primary_cpc_codes': primary_codes})

rows = []
seen = set()
for r in records:
    for code in r['primary_cpc_codes']:
        key = (r['assignee'], code)
        if key not in seen:
            seen.add(key)
            rows.append({'assignee': r['assignee'], 'cpc_code': code})

result = json.dumps(rows)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_EzMxUAYF0MisoIx0hDfWhVXV': [], 'var_call_iF1qIj6vf1p2PTLgvZ0dtWk1': 'file_storage/call_iF1qIj6vf1p2PTLgvZ0dtWk1.json', 'var_call_mdQIt4vXnhoL3ILCtztyaEuv': ['AU-2003297741-A1', 'AU-2007297661-A1', 'AU-2008349842-A1', 'AU-2010214112-B2', 'AU-2015364602-B2', 'AU-2019275518-B2', 'AU-6535890-A', 'CA-2298540-A1', 'CA-2550552-A1', 'CA-2562038-C', 'CN-100339724-C', 'CN-102067370-B', 'CN-102584712-A', 'CN-103189548-A', 'EP-0826155-A4', 'EP-1212462-A1', 'EP-4284234-A1', 'HK-1250569-A1', 'ID-23426-A', 'IL-244029-A0', 'IL-274176-A', 'JP-2014224156-A', 'JP-S6163700-A', 'KR-20200041324-A', 'MX-2013002850-A', 'RO-70061-A', 'TW-201925402-A', 'US-11376346-B2', 'US-11546022-B2', 'US-11667770-B2', 'US-2006051790-A1', 'US-2006292670-A1', 'US-2017145219-A1', 'US-2017281687-A1', 'US-2018243924-A1', 'US-2019328740-A1', 'US-2020025859-A1', 'US-2021000566-A1', 'US-2021101879-A1', 'US-2022018060-A1', 'US-2022074631-A1', 'US-2023155090-A1', 'US-2023171142-A1', 'US-2023279470-A1', 'US-2023321419-A1', 'US-5304932-A', 'US-5547866-A', 'US-6750960-B2', 'US-6767662-B2', 'US-9061071-B2', 'WO-2010045542-A3', 'WO-2012162563-A2', 'WO-2017214343-A1', 'WO-2018026404-A3', 'WO-2020055916-A9', 'WO-2021102420-A1', 'WO-2023225482-A3', 'WO-2024044766-A3', 'WO-2024112568-A1'], 'var_call_oQlv2PLuWqLW7ywjZmCshQPA': 'file_storage/call_oQlv2PLuWqLW7ywjZmCshQPA.json'}

exec(code, env_args)
