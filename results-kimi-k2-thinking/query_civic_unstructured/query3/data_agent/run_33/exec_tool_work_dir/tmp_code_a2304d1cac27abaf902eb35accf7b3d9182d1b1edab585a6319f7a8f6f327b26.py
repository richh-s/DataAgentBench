code = """import json
import re

# Load civic documents
civic_docs_path = locals()['var_functions.query_db:0']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Load funding data  
funding_path = locals()['var_functions.query_db:5']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Collect emergency/FEMA projects
emergency_projects = []
seen_projects = set()

# First pass: get all FEMA projects from funding database
for fund in funding_data:
    if 'fema' in fund['Project_Name'].lower():
        project = {
            'Project_Name': fund['Project_Name'],
            'Funding_Source': fund['Funding_Source'],
            'Amount': int(fund['Amount']),
            'Status': 'Not specified in civic docs'
        }
        emergency_projects.append(project)
        seen_projects.add(fund['Project_Name'].lower())

# Second pass: look for emergency/FEMA mentions in civic documents
doc_text = " ".join([doc['text'] for doc in civic_docs])
doc_lines = doc_text.split('\n')

for line in doc_lines:
    line_lower = line.lower().strip()
    if 'emergency' in line_lower or 'fema' in line_lower:
        # Skip short lines and headers
        if len(line) < 10 or any(x in line for x in ['Page', 'Agenda', 'Subject:', 'Prepared', 'Approved']):
            continue
            
        # Clean up the line
        clean_name = line.strip()
        
        # Check if we already have this project
        if clean_name.lower() in seen_projects:
            continue
            
        # Look for funding match
        funding_match = None
        for f in funding_data:
            if clean_name in f['Project_Name'] or f['Project_Name'] in clean_name:
                funding_match = f
                break
        
        if funding_match:
            amount = int(funding_match['Amount'])
            source = funding_match['Funding_Source']
        else:
            amount = 0
            source = 'Unknown'
        
        emergency_projects.append({
            'Project_Name': clean_name,
            'Funding_Source': source,
            'Amount': amount,
            'Status': 'Mentioned in civic docs'
        })
        seen_projects.add(clean_name.lower())

# Sort by amount descending
emergency_projects.sort(key=lambda x: x['Amount'], reverse=True)

print('__RESULT__:')
print(json.dumps(emergency_projects))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json'}

exec(code, env_args)
