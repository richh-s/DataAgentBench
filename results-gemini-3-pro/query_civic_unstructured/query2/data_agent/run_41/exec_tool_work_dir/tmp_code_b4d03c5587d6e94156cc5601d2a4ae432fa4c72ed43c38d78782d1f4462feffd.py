code = """import json
import re

with open(locals()['var_function-call-4654103334756958724'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-4654103334756962095'], 'r') as f:
    funding_data = json.load(f)

projects = []
for doc in civic_docs:
    text = doc['text']
    lines = text.splitlines()
    for i, line in enumerate(lines):
        line = line.strip()
        # Use substring check to be safe
        if '(cid:190) Updates' in line or '(cid:190) Project Description' in line:
            # Look backwards for name
            j = i - 1
            while j >= 0 and not lines[j].strip():
                j -= 1
            if j >= 0:
                p_name = lines[j].strip()
                # Get text block
                block_lines = []
                k = i
                while k < len(lines):
                    l_strip = lines[k].strip()
                    if k > i and ('(cid:190) Updates' in l_strip or '(cid:190) Project Description' in l_strip):
                        # This might be the next project.
                        # But also check if there's a name before it?
                        # Assume yes.
                        break
                    block_lines.append(lines[k])
                    k += 1
                p_text = ' '.join(block_lines)
                
                is_completed_2022 = False
                if 'Construction was completed' in p_text and '2022' in p_text:
                    is_completed_2022 = True
                
                projects.append({'name': p_name, 'completed_2022': is_completed_2022})

total = 0
matched = []
unique_projects = set()
keywords = ['park', 'playground', 'recreation']

for p in projects:
    if p['completed_2022']:
        name_clean = p['name'].strip()
        if any(k in name_clean.lower() for k in keywords):
            unique_projects.add(name_clean)

for name in unique_projects:
    amount = 0
    for f in funding_data:
        if f['Project_Name'].strip().lower() == name.lower():
            amount = f['Amount']
            break
    if amount > 0:
        total += amount
        matched.append({'name': name, 'amount': amount})

print('__RESULT__:')
print(json.dumps({'total': total, 'projects': matched}))"""

env_args = {'var_function-call-4654103334756958724': 'file_storage/function-call-4654103334756958724.json', 'var_function-call-4654103334756962095': 'file_storage/function-call-4654103334756962095.json'}

exec(code, env_args)
