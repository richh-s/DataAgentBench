code = """import json, re, pandas as pd
from collections import defaultdict

path = var_call_o3Ka1sHmCry71A83RmMtfhTp
with open(path, 'r') as f:
    data = json.load(f)

# Extract mapping: cited publication_number -> set of assignees who cite it (excluding UNIV CALIFORNIA)

cited_by_assignee = defaultdict(set)
patent_assignee = {}

for rec in data:
    info = rec.get('Patents_info','')
    # extract assignee_harmonized from text pattern "assignee_harmonized: <name>" if present, else look for "is owned by X" or similar
    m = re.search(r'assignee_harmonized:\s*([^;.,]+)', info)
    if m:
        assignee = m.group(1).strip()
    else:
        m2 = re.search(r'owned by ([A-Z0-9 &.,-]+)', info)
        if not m2:
            m2 = re.search(r'is assigned to ([A-Z0-9 &.,-]+)', info)
        if not m2:
            m2 = re.search(r'holds the [^,]+, with', info)
        assignee = m2.group(1).strip() if m2 else None
    # get this pub number
    m_pub = re.search(r'pub\. number ([A-Z0-9-]+)', info)
    if not m_pub:
        m_pub = re.search(r'publication number ([A-Z0-9-]+)', info)
    pubnum = m_pub.group(1) if m_pub else None
    if pubnum and assignee:
        patent_assignee[pubnum] = assignee

# Now build mapping for citations
for rec in data:
    info = rec.get('Patents_info','')
    # assignee of citing patent
    m = re.search(r'assignee_harmonized:\s*([^;.,]+)', info)
    if m:
        assignee_citing = m.group(1).strip()
    else:
        m2 = re.search(r'owned by ([A-Z0-9 &.,-]+)', info)
        if not m2:
            m2 = re.search(r'is assigned to ([A-Z0-9 &.,-]+)', info)
        assignee_citing = m2.group(1).strip() if m2 else None
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
        # if the cited patent is assigned to UNIV CALIFORNIA according to earlier mapping
        assignee_cited = patent_assignee.get(pub)
        if assignee_cited and assignee_cited.upper().startswith('UNIV CALIFORNIA'):
            cited_by_assignee[assignee_citing].add(pub)

result = {k: sorted(v) for k,v in cited_by_assignee.items()}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_AjHLjU0TdCpyY4jeFOAaFWV0': [], 'var_call_lNKrOqUlFQKmJl8yxBvC1qJ8': ['cpc_definition'], 'var_call_o3Ka1sHmCry71A83RmMtfhTp': 'file_storage/call_o3Ka1sHmCry71A83RmMtfhTp.json'}

exec(code, env_args)
