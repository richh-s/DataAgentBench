code = """import re, json
from collections import defaultdict

text_preview = var_call_b3bIatIQCr4QoOHQOputYlEO

# If preview is a file path string, load full data
if isinstance(text_preview, str):
    import os, json as js
    with open(text_preview, 'r') as f:
        docs = js.load(f)
else:
    docs = text_preview

projects = {}
pattern = re.compile(r"^[A-Z][A-Za-z0-9&.,'()\-/ ]+$")

for doc in docs:
    for line in doc.get('text','').split('\n'):
        line_stripped = line.strip()
        if not line_stripped:
            continue
        # Identify section headers that indicate status
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
        # heuristic: project title lines under a known status section
        if 'current_status' in locals() and pattern.match(line_stripped) and len(line_stripped.split())<10 and not line_stripped.endswith(':'):
            name = line_stripped
            projects[name] = {'Project_Name': name, 'status': current_status, 'type': current_type}

result = json.dumps(projects)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_SQzl7YcDEIWdVexrxuktrLXi': 'file_storage/call_SQzl7YcDEIWdVexrxuktrLXi.json', 'var_call_b3bIatIQCr4QoOHQOputYlEO': 'file_storage/call_b3bIatIQCr4QoOHQOputYlEO.json'}

exec(code, env_args)
