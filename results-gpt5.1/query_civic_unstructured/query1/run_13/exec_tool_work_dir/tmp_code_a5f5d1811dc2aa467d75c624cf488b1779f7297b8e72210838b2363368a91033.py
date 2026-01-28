code = """import json, pathlib, re

funding_records = var_call_Ew4FPBhw9esArvsNvY7TfgbY
funding_projects = {rec['Project_Name'] for rec in funding_records}

all_docs = var_call_YfcLmUn2eBVjZIqVlR4ePV1f
if isinstance(all_docs, str):
    with open(all_docs, 'r') as f:
        all_docs = json.load(f)

texts = [d['text'] for d in all_docs]
text = '\n'.join(texts)

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
    if current_section_type and current_status and not l.endswith(':') and not l.lower().startswith('updates') and not l.lower().startswith('project') and len(l.split()) < 15:
        name = l.strip()
        if name in funding_projects:
            project_info[name] = {'type': current_section_type, 'status': current_status}

count = sum(1 for name, info in project_info.items() if info['type']=='capital' and info['status']=='design')

out = json.dumps(count)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_Ew4FPBhw9esArvsNvY7TfgbY': 'file_storage/call_Ew4FPBhw9esArvsNvY7TfgbY.json', 'var_call_YfcLmUn2eBVjZIqVlR4ePV1f': 'file_storage/call_YfcLmUn2eBVjZIqVlR4ePV1f.json'}

exec(code, env_args)
