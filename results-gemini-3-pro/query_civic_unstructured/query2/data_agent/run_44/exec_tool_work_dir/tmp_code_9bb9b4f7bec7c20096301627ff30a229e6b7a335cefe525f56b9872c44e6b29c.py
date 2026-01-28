code = """import json
import pandas as pd

with open(locals()['var_function-call-2604806260123295524'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-2604806260123292981'], 'r') as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)

projects = []
current_project = None
buffer_text = []
last_non_empty_line = ''

for doc in civic_docs:
    lines = doc['text'].splitlines()
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        
        # Check for marker
        # We assume any line containing "Updates:" is a potential marker
        if 'Updates:' in line:
            # Heuristic: Previous line should not end with colon (e.g. "Subject:")
            if last_non_empty_line.strip().endswith(':'):
                if current_project:
                    buffer_text.append(line)
            else:
                # Potential new project
                if current_project:
                    current_project['text'] = '\n'.join(buffer_text)
                    projects.append(current_project)
                
                current_project = {'name': last_non_empty_line, 'text': ''}
                buffer_text = [line]
        else:
            if current_project:
                buffer_text.append(line)
            last_non_empty_line = stripped

    if current_project:
        current_project['text'] = '\n'.join(buffer_text)
        projects.append(current_project)
        current_project = None
        buffer_text = []

completed_parks = []
for p in projects:
    name = p['name']
    text = p['text'].lower()
    full_text = (name + ' ' + p['text']).lower()
    
    is_park = False
    if 'park' in full_text and 'parking' not in full_text:
        is_park = True
    if 'playground' in full_text:
        is_park = True
        
    is_comp_2022 = False
    p_lines = p['text'].split('\n')
    for line in p_lines:
        l_lower = line.lower()
        if 'completed' in l_lower and '2022' in l_lower:
            if 'design' in l_lower and 'construction' not in l_lower:
                continue
            is_comp_2022 = True
            break
            
    if is_park and is_comp_2022:
        completed_parks.append(name)

completed_parks = list(set(completed_parks))

total = 0
found_projects = []

for name in completed_parks:
    clean_name = name.strip()
    match = funding_df[funding_df['Project_Name'].str.strip() == clean_name]
    if match.empty:
        match = funding_df[funding_df['Project_Name'].str.strip().str.lower() == clean_name.lower()]
    
    if not match.empty:
        total += match['Amount'].sum()
        found_projects.append(clean_name)

print('__RESULT__:')
print(json.dumps({'total_funding': int(total), 'projects': found_projects}))"""

env_args = {'var_function-call-2604806260123295524': 'file_storage/function-call-2604806260123295524.json', 'var_function-call-2604806260123292981': 'file_storage/function-call-2604806260123292981.json'}

exec(code, env_args)
