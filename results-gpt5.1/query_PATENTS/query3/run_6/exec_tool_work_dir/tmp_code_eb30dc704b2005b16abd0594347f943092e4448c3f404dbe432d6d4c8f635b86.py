code = """import json, re
from collections import defaultdict

path = var_call_IysWgHR3srAmmw0kEhaukJQT
with open(path, 'r') as f:
    citing_recs = json.load(f)

assignee_re = re.compile(r'owned by ([A-Z0-9 .,&-]+?) and has pub\. number')

assignee_to_cpcs = defaultdict(set)

for r in citing_recs:
    m = assignee_re.search(r['Patents_info'])
    if not m:
        continue
    assignee = m.group(1).strip()
    if assignee == 'UNIV CALIFORNIA':
        continue
    # parse CPC JSON-like list
    try:
        cpc_list = json.loads(r['cpc'])
    except Exception:
        continue
    primary = None
    for entry in cpc_list:
        if entry.get('first'):
            primary = entry['code']
            break
    if primary:
        assignee_to_cpcs[assignee].add(primary)

# prepare list of unique primary CPC codes
all_cpcs = sorted({c for s in assignee_to_cpcs.values() for c in s})

result = json.dumps({"assignee_to_cpcs": {k: sorted(v) for k,v in assignee_to_cpcs.items()}, "cpc_codes": all_cpcs})
print('__RESULT__:')
print(result)"""

env_args = {'var_call_1K5l7r0nYbvnrpxZajkCjJDT': [], 'var_call_8FYofJPm9ETW7aZJWS67e67B': 'file_storage/call_8FYofJPm9ETW7aZJWS67e67B.json', 'var_call_kXqKR3Igxft9YN40QH28WWaT': ['AU-2003297741-A1', 'AU-2007297661-A1', 'AU-2008349842-A1', 'AU-2010214112-B2', 'AU-2015364602-B2', 'AU-2019275518-B2', 'AU-6535890-A', 'CA-2298540-A1', 'CA-2550552-A1', 'CA-2562038-C', 'CN-100339724-C', 'CN-102067370-B', 'CN-102584712-A', 'CN-103189548-A', 'EP-0826155-A4', 'EP-1212462-A1', 'EP-4284234-A1', 'HK-1250569-A1', 'ID-23426-A', 'IL-244029-A0', 'IL-274176-A', 'JP-2014224156-A', 'JP-S6163700-A', 'KR-20200041324-A', 'MX-2013002850-A', 'RO-70061-A', 'TW-201925402-A', 'US-11376346-B2', 'US-11546022-B2', 'US-11667770-B2', 'US-2006051790-A1', 'US-2006292670-A1', 'US-2017145219-A1', 'US-2017281687-A1', 'US-2018243924-A1', 'US-2019328740-A1', 'US-2020025859-A1', 'US-2021000566-A1', 'US-2021101879-A1', 'US-2022018060-A1', 'US-2022074631-A1', 'US-2023155090-A1', 'US-2023171142-A1', 'US-2023279470-A1', 'US-2023321419-A1', 'US-5304932-A', 'US-5547866-A', 'US-6750960-B2', 'US-6767662-B2', 'US-9061071-B2', 'WO-2010045542-A3', 'WO-2012162563-A2', 'WO-2017214343-A1', 'WO-2018026404-A3', 'WO-2020055916-A9', 'WO-2021102420-A1', 'WO-2023225482-A3', 'WO-2024044766-A3', 'WO-2024112568-A1'], 'var_call_IysWgHR3srAmmw0kEhaukJQT': 'file_storage/call_IysWgHR3srAmmw0kEhaukJQT.json'}

exec(code, env_args)
