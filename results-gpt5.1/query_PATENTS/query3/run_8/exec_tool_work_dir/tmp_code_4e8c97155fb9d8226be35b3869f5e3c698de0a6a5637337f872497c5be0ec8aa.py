code = """import json, re, pandas as pd
from collections import defaultdict

path = var_call_o3Ka1sHmCry71A83RmMtfhTp
with open(path, 'r') as f:
    data = json.load(f)

cited_by_assignee = defaultdict(set)
patent_assignee = {}

for rec in data:
    info = rec.get('Patents_info','')
    assignee = None
    m = re.search(r'assignee_harmonized:\s*([^;.,]+)', info)
    if m:
        assignee = m.group(1).strip()
    else:
        m2 = re.search(r'owned by ([A-Z0-9 &.,-]+)', info)
        if not m2:
            m2 = re.search(r'is assigned to ([A-Z0-9 &.,-]+)', info)
        if m2:
            assignee = m2.group(1).strip()
    m_pub = re.search(r'pub\. number ([A-Z0-9-]+)', info)
    if not m_pub:
        m_pub = re.search(r'publication number ([A-Z0-9-]+)', info)
    pubnum = m_pub.group(1) if m_pub else None
    if pubnum and assignee:
        patent_assignee[pubnum] = assignee

for rec in data:
    info = rec.get('Patents_info','')
    assignee_citing = None
    m = re.search(r'assignee_harmonized:\s*([^;.,]+)', info)
    if m:
        assignee_citing = m.group(1).strip()
    else:
        m2 = re.search(r'owned by ([A-Z0-9 &.,-]+)', info)
        if not m2:
            m2 = re.search(r'is assigned to ([A-Z0-9 &.,-]+)', info)
        if m2:
            assignee_citing = m2.group(1).strip()
    if not assignee_citing or assignee_citing.upper().startswith('UNIV CALIFORNIA'):
        continue
    cites = rec.get('citation','[]') or '[]'
    try:
        cites_list = json.loads(cites)
    except Exception:
        continue
    for c in cites_list:
        pub = c.get('publication_number')
        if not pub:
            continue
        assignee_cited = patent_assignee.get(pub)
        if assignee_cited and assignee_cited.upper().startswith('UNIV CALIFORNIA'):
            cited_by_assignee[assignee_citing].add(pub)

result = {k: sorted(v) for k,v in cited_by_assignee.items()}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_AjHLjU0TdCpyY4jeFOAaFWV0': [], 'var_call_lNKrOqUlFQKmJl8yxBvC1qJ8': ['cpc_definition'], 'var_call_o3Ka1sHmCry71A83RmMtfhTp': 'file_storage/call_o3Ka1sHmCry71A83RmMtfhTp.json'}

exec(code, env_args)
