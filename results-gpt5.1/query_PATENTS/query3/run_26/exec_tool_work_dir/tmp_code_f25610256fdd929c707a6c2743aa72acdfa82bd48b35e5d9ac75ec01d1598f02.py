code = """import json, re, pandas as pd, os

path = var_call_aVVFld85vBkhbryth5wyUIVH
with open(path, 'r') as f:
    data = json.load(f)

# Extract publication_number and assignee from Patents_info
records = []
for row in data:
    info = row.get('Patents_info','')
    m_pub = re.search(r'pub\. number ([A-Z]{2}-[0-9A-Z]+-[A0-9]+)', info)
    pub_num = m_pub.group(1) if m_pub else None
    m_assignee = re.search(r'assigned to ([^.,]+)|owned by ([^.,]+)|holds the .* patent filing .* is owned by ([^.,]+)', info)
    assignee = None
    if m_assignee:
        assignee = next((g for g in m_assignee.groups() if g), None)
    records.append({
        'pub_num': pub_num,
        'assignee': assignee,
        'Patents_info': info,
        'cpc': row.get('cpc',''),
        'citation': row.get('citation','')
    })

# Build map of publication_number -> assignee from all patents
# Need all patents, not just UNIV CALIFORNIA, to find who cites them later

print('__RESULT__:')
print(json.dumps(records))"""

env_args = {'var_call_5UUhZm9dAbLI9F6cfNna9uWh': [], 'var_call_NKoCzB2FUSYum4cLg5VjS7lY': ['cpc_definition'], 'var_call_aVVFld85vBkhbryth5wyUIVH': 'file_storage/call_aVVFld85vBkhbryth5wyUIVH.json'}

exec(code, env_args)
