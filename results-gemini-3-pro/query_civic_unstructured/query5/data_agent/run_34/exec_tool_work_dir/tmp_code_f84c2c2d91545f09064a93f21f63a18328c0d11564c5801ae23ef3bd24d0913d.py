code = """import json
import pandas as pd
import re

funding_path = locals()['var_function-call-6570500424665690713']
docs_path = locals()['var_function-call-6570500424665692862']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)
    
with open(docs_path, 'r') as f:
    civic_docs = json.load(f)

projects = []
current_header = 'Unknown'
date_pattern = re.compile(r'Begin [cC]onstruction:\s*([A-Za-z0-9\s]+)')

for doc in civic_docs:
    lines = [l.strip() for l in doc['text'].split('\n') if l.strip()]
    
    for i, line in enumerate(lines):
        if 'Capital Improvement Projects' in line:
            current_header = 'Capital'
        elif 'Disaster Recovery Projects' in line:
            current_header = 'Disaster'
            
        if 'Updates:' in line or 'Project Description:' in line:
            if i > 0:
                possible_name = lines[i-1]
                if 'Capital Improvement Projects' in possible_name or 'Disaster Recovery Projects' in possible_name:
                    continue
                if 'Agenda' in possible_name or 'Page' in possible_name:
                    continue
                
                p_name = possible_name
                details_text = " ".join(lines[i:i+30])
                
                st_match = date_pattern.search(details_text)
                st_date = st_match.group(1).strip() if st_match else "Unknown"
                
                p_type = current_header
                if 'FEMA' in p_name or 'CalOES' in p_name or 'CalJPIA' in p_name:
                    p_type = 'Disaster'
                
                projects.append({
                    'Project_Name': p_name,
                    'Type': p_type,
                    'Start_Date': st_date
                })

target_projects = []
for p in projects:
    if p['Type'] == 'Disaster' and '2022' in p['Start_Date']:
        target_projects.append(p['Project_Name'])

# Remove duplicates if any
target_projects = list(set(target_projects))

df = pd.DataFrame(funding_data)
df['Amount'] = pd.to_numeric(df['Amount'])
total = df[df['Project_Name'].isin(target_projects)]['Amount'].sum()

print('__RESULT__:')
print(json.dumps({'total': int(total), 'projects': target_projects, 'debug': projects[:5]}))"""

env_args = {'var_function-call-2007247411734305584': ['Funding'], 'var_function-call-2007247411734305063': ['civic_docs'], 'var_function-call-6570500424665690713': 'file_storage/function-call-6570500424665690713.json', 'var_function-call-6570500424665692862': 'file_storage/function-call-6570500424665692862.json'}

exec(code, env_args)
