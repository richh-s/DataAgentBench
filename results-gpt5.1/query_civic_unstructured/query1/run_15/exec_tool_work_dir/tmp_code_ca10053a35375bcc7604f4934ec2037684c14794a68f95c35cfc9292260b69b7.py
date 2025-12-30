code = """import re, json, os
import json as js

docs_ref = var_call_b3bIatIQCr4QoOHQOputYlEO

if isinstance(docs_ref, str):
    with open(docs_ref, 'r') as f:
        docs = js.load(f)
else:
    docs = docs_ref

projects = {}
pattern = re.compile(r"^[A-Z][A-Za-z0-9&.,'()\-/ ]+$")
current_status = None
current_type = None

for doc in docs:
    for line in doc.get('text','').split('\n'):
        line_stripped = line.strip()
        if not line_stripped:
            continue
        lower = line_stripped.lower()
        if 'capital improvement projects (design' in lower:
            current_status = 'design'
            current_type = 'capital'
            continue
        if 'capital improvement projects (construction' in lower:
            current_status = 'completed'
            current_type = 'capital'
            continue
        if 'capital improvement projects (not started' in lower:
            current_status = 'not started'
            current_type = 'capital'
            continue
        if current_status and pattern.match(line_stripped) and len(line_stripped.split())<10 and not line_stripped.endswith(':'):
            name = line_stripped
            projects[name] = {'Project_Name': name, 'status': current_status, 'type': current_type}

result = json.dumps(projects)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_SQzl7YcDEIWdVexrxuktrLXi': 'file_storage/call_SQzl7YcDEIWdVexrxuktrLXi.json', 'var_call_b3bIatIQCr4QoOHQOputYlEO': 'file_storage/call_b3bIatIQCr4QoOHQOputYlEO.json'}

exec(code, env_args)
