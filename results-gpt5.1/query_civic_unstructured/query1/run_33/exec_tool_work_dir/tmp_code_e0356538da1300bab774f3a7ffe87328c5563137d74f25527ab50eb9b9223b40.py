code = """import json, re
from collections import defaultdict

with open(var_call_eY0UXhPG3byqGDlQ4rK3M1vc, 'r') as f:
    funding_records = json.load(f)

funded_projects = {rec['Project_Name'] for rec in funding_records}

with open(var_call_TUXnfAcA2qtNchsZkHVh526G, 'r') as f:
    civic_docs = json.load(f)

text_corpus = ' '.join(doc['text'] for doc in civic_docs)

lines = re.split('\n+', text_corpus)

status_by_project = {}
current_section_type = None
current_status = None

for line in lines:
    stripped = line.strip()
    if not stripped:
        continue
    low = stripped.lower()

    if 'capital improvement projects' in low:
        if '(design' in low:
            current_section_type = 'capital'
            current_status = 'design'
        elif '(construction' in low:
            current_section_type = 'capital'
            current_status = 'completed'
        elif '(not started' in low:
            current_section_type = 'capital'
            current_status = 'not started'
        continue
    if 'disaster recovery projects' in low:
        if '(design' in low:
            current_section_type = 'disaster'
            current_status = 'design'
        elif '(construction' in low:
            current_section_type = 'disaster'
            current_status = 'completed'
        elif '(not started' in low:
            current_section_type = 'disaster'
            current_status = 'not started'
        continue

    if current_section_type and current_status and re.match('[A-Z0-9]', stripped):
        candidate = stripped
        if candidate not in funded_projects:
            if candidate.endswith(' Project') and candidate[:-8] in funded_projects:
                candidate = candidate[:-8]
            elif candidate.endswith(' Repairs') and candidate[:-8] in funded_projects:
                candidate = candidate[:-8]
        if candidate in funded_projects:
            status_by_project[candidate] = {'type': current_section_type, 'status': current_status}

count = sum(1 for p, meta in status_by_project.items() if meta['type']=='capital' and meta['status']=='design')

result = {'capital_design_projects_over_50000_count': count}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_eY0UXhPG3byqGDlQ4rK3M1vc': 'file_storage/call_eY0UXhPG3byqGDlQ4rK3M1vc.json', 'var_call_TUXnfAcA2qtNchsZkHVh526G': 'file_storage/call_TUXnfAcA2qtNchsZkHVh526G.json'}

exec(code, env_args)
