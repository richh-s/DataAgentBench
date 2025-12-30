code = """import json
import re
import os

key_civic = 'var_function-call-6738799764007294516'
key_funding = 'var_function-call-6738799764007295879'

path_civic = locals()[key_civic]
path_funding = locals()[key_funding]

with open(path_civic, 'r') as f:
    civic_docs = json.load(f)

with open(path_funding, 'r') as f:
    funding_data = json.load(f)

extracted_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        is_title = False
        look_ahead_range = 5
        for j in range(1, look_ahead_range + 1):
            if i + j < len(lines):
                next_line = lines[i+j].strip()
                if 'Updates:' in next_line or 'Project Description:' in next_line or 'Project Updates:' in next_line:
                    is_title = True
                    break
        
        if is_title:
            if current_project:
                extracted_projects.append(current_project)
            current_project = {'name': line, 'text_lines': []}
        else:
            if current_project:
                current_project['text_lines'].append(line)
    
    if current_project:
        extracted_projects.append(current_project)

processed_projects = []
for proj in extracted_projects:
    full_text = " ".join(proj['text_lines'])
    
    start_match = re.search(r'Begin [cC]onstruction:?\s*([A-Za-z0-9\s,]+)', full_text)
    start_date_str = start_match.group(1).strip() if start_match else None
    
    started_in_2022 = False
    if start_date_str and '2022' in start_date_str:
        started_in_2022 = True
    
    is_disaster = False
    disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'Woolsey', 'Disaster', 'Recovery']
    
    if any(k.lower() in proj['name'].lower() for k in disaster_keywords):
        is_disaster = True
    if any(k in full_text for k in disaster_keywords):
        is_disaster = True
        
    processed_projects.append({
        'name': proj['name'],
        'started_in_2022': started_in_2022,
        'is_disaster': is_disaster,
        'start_date': start_date_str
    })

print('__RESULT__:')
print(json.dumps(processed_projects))"""

env_args = {'var_function-call-6738799764007294516': 'file_storage/function-call-6738799764007294516.json', 'var_function-call-6738799764007295879': 'file_storage/function-call-6738799764007295879.json'}

exec(code, env_args)
