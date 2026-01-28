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

# Identify projects related to emergency/FEMA
projects = []

# First, check funding data for FEMA projects
for f in funding_data:
    if 'fema' in f['Project_Name'].lower():
        projects.append({
            'Project_Name': f['Project_Name'],
            'Funding_Source': f['Funding_Source'],
            'Amount': int(f['Amount']),
            'Status': 'Not specified'
        })

# Check civic documents for emergency-related projects
for doc in civic_docs:
    text = doc['text'].lower()
    if 'emergency' in text or 'fema' in text:
        lines = doc['text'].split('\n')
        for line in lines:
            if 'emergency' in line.lower() or 'fema' in line.lower():
                clean_line = line.strip()
                if len(clean_line) > 5 and not clean_line.startswith('('):
                    # Find funding for this project
                    funding_match = None
                    for f in funding_data:
                        if clean_line in f['Project_Name'] or f['Project_Name'] in clean_line:
                            funding_match = f
                            break
                    
                    if funding_match:
                        amount = int(funding_match['Amount'])
                        source = funding_match['Funding_Source']
                    else:
                        amount = 0
                        source = 'Unknown'
                    
                    projects.append({
                        'Project_Name': clean_line,
                        'Funding_Source': source,
                        'Amount': amount,
                        'Status': 'From civic docs'
                    })

# Remove duplicates and sort
unique_projects = {}
for p in projects:
    key = p['Project_Name'].lower()
    if key not in unique_projects or p['Amount'] > 0:
        unique_projects[key] = p

final_projects = list(unique_projects.values())
final_projects.sort(key=lambda x: x['Amount'], reverse=True)

print('__RESULT__:')
print(json.dumps(final_projects))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json'}

exec(code, env_args)
