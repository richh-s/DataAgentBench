code = """import json
import os

# Load data from file paths
funding_path = locals()['var_functions.query_db:2']
civic_path = locals()['var_functions.query_db:0']

print("Loading funding data from:", funding_path)
print("Loading civic data from:", civic_path)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

print("Loaded", len(funding_data), "funding records")
print("Loaded", len(civic_docs), "civic documents")

# Find FEMA/emergency projects in funding
fema_projects = []
for record in funding_data:
    name = record.get('Project_Name', '')
    if 'FEMA' in name or 'fema' in name or 'emergency' in name.lower():
        fema_projects.append({
            'Project_Name': name,
            'Funding_Source': record.get('Funding_Source', ''),
            'Amount': int(record.get('Amount', 0))
        })

print("Found", len(fema_projects), "FEMA/emergency projects in funding")

# Extract status from documents
status_list = []
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if len(line) > 10:
            lower = line.lower()
            if any(kw in lower for kw in ['project', 'repairs', 'sirens', 'warning']):
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

# Match and create results
results = []
for fp in fema_projects:
    project_status = 'Unknown'
    for sp in status_list:
        if fp['Project_Name'].lower() in sp['name'].lower() or sp['name'].lower() in fp['Project_Name'].lower():
            project_status = sp['status']
            break
    
    results.append({
        'Project_Name': fp['Project_Name'],
        'Funding_Source': fp['Funding_Source'],
        'Amount': fp['Amount'],
        'Status': project_status
    })

# Output
output = json.dumps(results, indent=2)
print('__RESULT__:')
print(output)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}}

exec(code, env_args)
