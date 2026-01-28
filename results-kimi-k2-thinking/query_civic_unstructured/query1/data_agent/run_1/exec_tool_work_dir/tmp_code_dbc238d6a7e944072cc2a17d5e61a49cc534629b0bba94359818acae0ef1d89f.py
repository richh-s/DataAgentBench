code = """import json
import re

funding_file = locals()['var_functions.query_db:0']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

civic_file = locals()['var_functions.query_db:2']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

project_funding = {}
for record in funding_data:
    name = record['Project_Name']
    amount = int(record['Amount'])
    if amount > 50000:
        project_funding[name] = amount

design_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        if len(line) < 10 or len(line) > 150:
            continue
            
        if line[0].isupper():
            indicators = ['Project', 'Improvements', 'Repair', 'Replacement', 'Construction', 'Resurfacing', 'Drainage', 'Road', 'Park', 'Bridge', 'Culvert', 'Wall', 'Signs', 'Study']
            
            if any(indicator in line for indicator in indicators):
                if line in project_funding:
                    context = ' '.join(lines[max(0, i-8):min(len(lines), i+12)])
                    
                    if 'design' in context.lower() and 'complete design' not in context.lower():
                        design_projects.append({'name': line, 'funding': project_funding[line]})
                else:
                    for funded_name in project_funding:
                        if funded_name.startswith(line) or line.startswith(funded_name.split(' (')[0]):
                            context = ' '.join(lines[max(0, i-8):min(len(lines), i+12)])
                            
                            if 'design' in context.lower() and 'complete design' not in context.lower():
                                design_projects.append({'name': funded_name, 'funding': project_funding[funded_name]})

unique_projects = []
seen = set()
for p in design_projects:
    if p['name'] not in seen:
        unique_projects.append(p)
        seen.add(p['name'])

print('__RESULT__:')
print(json.dumps({'count': len(unique_projects)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_records': 276, 'civic_documents': 5}}

exec(code, env_args)
