code = """import json
import pandas as pd

# Load data
with open(locals()['var_function-call-2604806260123295524'], 'r') as f:
    civic_docs = json.load(f)

projects = []
current_project = None
buffer_text = []
last_non_empty_line = ''
NEWLINE = chr(10)

for doc in civic_docs:
    lines = doc['text'].splitlines()
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        
        if 'Updates:' in line:
            if last_non_empty_line.strip().endswith(':'):
                if current_project:
                    buffer_text.append(line)
            else:
                if current_project:
                    current_project['text'] = NEWLINE.join(buffer_text)
                    projects.append(current_project)
                
                current_project = {'name': last_non_empty_line, 'text': ''}
                buffer_text = [line]
        else:
            if current_project:
                buffer_text.append(line)
            last_non_empty_line = stripped

    if current_project:
        current_project['text'] = NEWLINE.join(buffer_text)
        projects.append(current_project)
        current_project = None
        buffer_text = []

completed_2022 = []
for p in projects:
    text = p['text'].lower()
    p_lines = p['text'].split(NEWLINE)
    is_comp_2022 = False
    for line in p_lines:
        l_lower = line.lower()
        if 'completed' in l_lower and '2022' in l_lower:
            if 'design' in l_lower and 'construction' not in l_lower:
                continue
            is_comp_2022 = True
            break
    if is_comp_2022:
        completed_2022.append(p)

print('__RESULT__:')
print(json.dumps([p['name'] for p in completed_2022]))"""

env_args = {'var_function-call-2604806260123295524': 'file_storage/function-call-2604806260123295524.json', 'var_function-call-2604806260123292981': 'file_storage/function-call-2604806260123292981.json', 'var_function-call-11287208145778595060': {'total_funding': 21000, 'projects': ['Bluffs Park Shade Structure']}}

exec(code, env_args)
