code = """import json
import os

funding_path = locals()['var_functions.query_db:2']
civic_path = locals()['var_functions.query_db:0']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

print('Funding count:', len(funding_data))
print('Civic count:', len(civic_docs))

fema_projects = []
for rec in funding_data:
    name = rec.get('Project_Name', '')
    if 'FEMA' in name or 'fema' in name or 'emergency' in name.lower():
        fema_projects.append({
            'Project_Name': name,
            'Funding_Source': rec.get('Funding_Source', ''),
            'Amount': int(rec.get('Amount', 0))
        })

print('FEMA projects found:', len(fema_projects))

status_list = []
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if len(line) > 10:
            lower_line = line.lower()
            keywords = ['project', 'repairs', 'sirens', 'warning']
            has_keyword = False
            for kw in keywords:
                if kw in lower_line:
                    has_keyword = True
                    break
            
            if has_keyword:
                status = None
                for j in range(i+1, min(i+4, len(lines))):
                    next_line = lines[j].lower()
                    if 'design' in next_line:
                        status = 'design'
                        break
                    elif 'completed' in next_line:
                        status = 'completed'
                        break
                    elif 'not started' in next_line:
                        status = 'not started'
                        break
                
                if status:
                    status_list.append({'name': line, 'status': status})

print('Status extracted for projects:', len(status_list))

results = []
for fp in fema_projects:
    matched_status = 'Unknown'
    for sp in status_list:
        fp_lower = fp['Project_Name'].lower()
        sp_lower = sp['name'].lower()
        if fp_lower in sp_lower or sp_lower in fp_lower:
            matched_status = sp['status']
            break
    
    results.append({
        'Project_Name': fp['Project_Name'],
        'Funding_Source': fp['Funding_Source'],
        'Amount': fp['Amount'],
        'Status': matched_status
    })

print('Final results:', len(results))
print('__RESULT__:')
print(json.dumps(results, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}}

exec(code, env_args)
