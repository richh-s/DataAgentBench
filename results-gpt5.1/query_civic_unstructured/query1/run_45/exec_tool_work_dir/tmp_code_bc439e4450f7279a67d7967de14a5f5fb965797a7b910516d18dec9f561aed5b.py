code = """import re, json, pandas as pd

funding = pd.DataFrame(var_call_Cx4W3fYvgp9PNQJHcF87E6Th)

if isinstance(var_call_fieBJRiJZceyYKqpiwU67wj6, str) and var_call_fieBJRiJZceyYKqpiwU67wj6.endswith('.json'):
    import json as _json
    with open(var_call_fieBJRiJZceyYKqpiwU67wj6, 'r') as f:
        docs = _json.load(f)
else:
    docs = var_call_fieBJRiJZceyYKqpiwU67wj6

project_status = {}

for doc in docs:
    text = doc.get('text','')
    m = re.search(r'Capital Improvement Projects \(Design\)(.*?)(Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects)', text, re.S)
    if not m:
        continue
    section = m.group(1)
    lines = [l.strip() for l in section.split('\n') if l.strip()]
    for line in lines:
        if '\u2022' in line or line.startswith('(cid:'):
            continue
        if 'Updates:' in line or 'Project Schedule' in line or 'Estimated Schedule' in line or 'Project Description' in line:
            continue
        if len(line.split()) <= 1 or len(line) > 100:
            continue
        name = line
        project_status[name] = 'design'

import pandas as pd

design_projects = pd.DataFrame({'Project_Name': list(project_status.keys()), 'status': ['design']*len(project_status)})

merged = funding.merge(design_projects, on='Project_Name', how='inner')
count = int(len(merged))

result = json.dumps(count)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_Cx4W3fYvgp9PNQJHcF87E6Th': 'file_storage/call_Cx4W3fYvgp9PNQJHcF87E6Th.json', 'var_call_fieBJRiJZceyYKqpiwU67wj6': 'file_storage/call_fieBJRiJZceyYKqpiwU67wj6.json'}

exec(code, env_args)
