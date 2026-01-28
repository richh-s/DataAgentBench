code = """import json, re
rows = var_call_GuJJtOu8pLmuANvndaJguHlp
# rows is a list of dicts with rowid, Patents_info, cpc

def extract_assignee_simple(info):
    if not info:
        return None
    low = info.lower()
    keywords = ['is held by', 'held by', 'is assigned to', 'assigned to', 'is owned by', 'owned by']
    for kw in keywords:
        i = low.find(kw)
        if i >= 0:
            start = i + len(kw)
            tail = info[start:start+200]
            # split on common delimiters
            for sep in [' and has', ' and has pub', ' and has publication', ' and has publication no', ', ', '; ', '. ', ' with publication', ' and has publication number', ' and has publication no.']:
                if sep in tail:
                    tail = tail.split(sep)[0]
            tail = tail.split(' and ')[0]
            tail = tail.split(' has ')[0]
            return tail.strip().upper()
    return None

assignee_to_codes = {}
all_codes = set()
for rec in rows:
    info = rec.get('Patents_info','')
    assignee = extract_assignee_simple(info)
    if not assignee:
        continue
    if 'UNIV CALIFORNIA' in assignee:
        continue
    cpc_text = rec.get('cpc','[]')
    try:
        cpc_list = json.loads(cpc_text)
    except Exception:
        cpc_list = []
    primary_codes = set()
    for c in cpc_list:
        if isinstance(c, dict) and c.get('first'):
            code = c.get('code')
            if code:
                primary_codes.add(code)
    if not primary_codes:
        for c in cpc_list:
            if isinstance(c, dict) and c.get('code'):
                primary_codes.add(c.get('code'))
                break
    if not primary_codes:
        continue
    assignee_to_codes.setdefault(assignee, set()).update(primary_codes)
    all_codes.update(primary_codes)

res = {'assignee_to_codes': {k: sorted(list(v)) for k,v in assignee_to_codes.items()}, 'codes': sorted(list(all_codes))}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_uDiYoolU3jAQpH2wMff8iPIt': ['publicationinfo'], 'var_call_GlGC2BtHSHcOnyHn5dstNfTH': ['cpc_definition'], 'var_call_teNtoCHZkRPcqi3NXSIAqDMd': 'file_storage/call_teNtoCHZkRPcqi3NXSIAqDMd.json', 'var_call_SkSJcXss6ufl2IEdIhp2GI8L': ['AU-2003297741-A1', 'AU-2007297661-A1', 'AU-2008349842-A1', 'AU-2010214112-B2', 'AU-2015364602-B2', 'AU-2019275518-B2', 'AU-6535890-A', 'CA-2298540-A1', 'CA-2550552-A1', 'CA-2562038-C', 'CN-100339724-C', 'CN-102067370-B', 'CN-102584712-A', 'CN-103189548-A', 'EP-0826155-A4', 'EP-1212462-A1', 'EP-4284234-A1', 'HK-1250569-A1', 'ID-23426-A', 'IL-244029-A0', 'IL-274176-A', 'JP-2014224156-A', 'JP-S6163700-A', 'KR-20200041324-A', 'MX-2013002850-A', 'RO-70061-A', 'TW-201925402-A', 'US-11376346-B2', 'US-11546022-B2', 'US-11667770-B2', 'US-2006051790-A1', 'US-2006292670-A1', 'US-2017145219-A1', 'US-2017281687-A1', 'US-2018243924-A1', 'US-2019328740-A1', 'US-2020025859-A1', 'US-2021000566-A1', 'US-2021101879-A1', 'US-2022018060-A1', 'US-2022074631-A1', 'US-2023155090-A1', 'US-2023171142-A1', 'US-2023279470-A1', 'US-2023321419-A1', 'US-5304932-A', 'US-5547866-A', 'US-6750960-B2', 'US-6767662-B2', 'US-9061071-B2', 'WO-2010045542-A3', 'WO-2012162563-A2', 'WO-2017214343-A1', 'WO-2018026404-A3', 'WO-2020055916-A9', 'WO-2021102420-A1', 'WO-2023225482-A3', 'WO-2024044766-A3', 'WO-2024112568-A1'], 'var_call_CZD6HGEWIebNGzCkkBQs0BHE': 'file_storage/call_CZD6HGEWIebNGzCkkBQs0BHE.json', 'var_call_GuJJtOu8pLmuANvndaJguHlp': [{'rowid': '108314', 'Patents_info': 'The US patent application (no. US-201715785968-A) is held by BLOOM ENERGY CORP and has publication no. US-10615444-B2.', 'cpc': '[\n  {\n    "code": "H01M2004/8684",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/861",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/8642",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M8/2457",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2008/1293",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M8/1253",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/9016",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/8657",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/9066",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/8885",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M8/2425",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/8663",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/861",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/8652",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/8657",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/8684",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/8663",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M8/1253",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/8652",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M8/2457",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/9016",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/8657",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "Y02P70/56",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/8642",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/9066",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "Y02E60/525",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M2008/1293",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/8885",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M8/2425",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/861",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/9066",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M8/1253",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y02P70/50",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y02P70/50",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y02E60/50",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y02E60/50",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/8684",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/8642",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/8663",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/8652",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2008/1293",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}]}

exec(code, env_args)
