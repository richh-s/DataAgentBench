code = """import json, re
from pathlib import Path

# Load funding project names with Amount > 50000
funding_records = var_call_c2T4NjeCVMPgg7pGyeUBTpVF

# Load all civic docs text (file path string if large)
path = var_call_VuRfLYKgdjkgqZjos6Jw4zXq
if isinstance(path, str) and path.endswith('.json'):
    data = json.loads(Path(path).read_text())
else:
    data = path

texts = [d['text'] for d in data]
full_text = '\n'.join(texts)

# Define helper to find status/type for a given project name using heuristics

capital_design_projects = set()

for rec in funding_records:
    name = rec['Project_Name']
    # simple search: look for project name within some context and check for 'Capital Improvement Projects' and 'Design' or 'design'
    pattern = re.escape(name)
    for m in re.finditer(pattern, full_text, flags=re.IGNORECASE):
        start = max(0, m.start()-200)
        end = min(len(full_text), m.end()+200)
        ctx = full_text[start:end].lower()
        if 'capital improvement' in ctx and 'design' in ctx:
            capital_design_projects.add(name)
            break

result = len(capital_design_projects)

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_c2T4NjeCVMPgg7pGyeUBTpVF': 'file_storage/call_c2T4NjeCVMPgg7pGyeUBTpVF.json', 'var_call_VuRfLYKgdjkgqZjos6Jw4zXq': 'file_storage/call_VuRfLYKgdjkgqZjos6Jw4zXq.json'}

exec(code, env_args)
