code = """import json, re
from collections import defaultdict

path = var_call_IuILurzXY4TbuTNCjxYrQ9Ll
with open(path, 'r') as f:
    records = json.load(f)

assignee_citations = defaultdict(set)
for rec in records:
    info = rec.get('Patents_info','')
    m = re.search(r'assignee_harmonized: ([^,.;]+)', info)
    if not m:
        continue
    assignee = m.group(1).strip()
    if assignee.upper().startswith('UNIV CALIFORNIA'):
        continue
    cits = rec.get('citation','') or '[]'
    try:
        cits_list = json.loads(cits)
    except Exception:
        continue
    for c in cits_list:
        pub = c.get('publication_number','')
        if 'UNIV CALIFORNIA' in pub:
            assignee_citations[assignee].add(pub)

result = {k: sorted(v) for k,v in assignee_citations.items()}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_IuILurzXY4TbuTNCjxYrQ9Ll': 'file_storage/call_IuILurzXY4TbuTNCjxYrQ9Ll.json', 'var_call_tXNBbD5prgC8FsjmCRph5IPG': ['cpc_definition']}

exec(code, env_args)
