code = """import re, json
from collections import defaultdict

# Load funding records
funding_records = var_call_Ew4FPBhw9esArvsNvY7TfgbY

# Build set of project names with funding > 50000
funding_projects = {rec['Project_Name'] for rec in funding_records}

# Load civic docs (preview or file path)
all_docs = var_call_YfcLmUn2eBVjZIqVlR4ePV1f

# If it's a file path (string), load json
if isinstance(all_docs, str):
    import pathlib, json as _json
    with open(all_docs, 'r') as f:
        all_docs = _json.load(f)

texts = [d['text'] for d in all_docs]
text = '\n'.join(texts)

# Very simple parsing based on headings in the example text
# We will infer type and status from section headers and list project names underneath until next header.

project_info = {}
current_section_type = None
current_status = None

for line in text.split('\n'):
    l = line.strip()
    if not l:
        continue
    lower = l.lower()
    if 'capital improvement projects' in lower:
        current_section_type = 'capital'
        if '(design)' in lower:
            current_status = 'design'
        elif '(construction)' in lower:
            current_status = 'completed'
        elif '(not started)' in lower:
            current_status = 'not started'
        continue
    # crude heuristic: lines that look like project names (no colon, not a sentence)
    if current_section_type and current_status and not l.endswith(':') and not l.lower().startswith('updates') and not l.lower().startswith('project') and len(l.split()) < 15:
        name = l.strip()
        # store only if in funding projects
        if name in funding_projects:
            project_info[name] = {
                'type': current_section_type,
                'status': current_status
            }

# Count projects that are capital, design, and have funding > 50000
count = sum(1 for name, info in project_info.items() if info['type']=='capital' and info['status']=='design')

import json as json_mod
result = json_mod.dumps(count)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_Ew4FPBhw9esArvsNvY7TfgbY': 'file_storage/call_Ew4FPBhw9esArvsNvY7TfgbY.json', 'var_call_YfcLmUn2eBVjZIqVlR4ePV1f': 'file_storage/call_YfcLmUn2eBVjZIqVlR4ePV1f.json'}

exec(code, env_args)
