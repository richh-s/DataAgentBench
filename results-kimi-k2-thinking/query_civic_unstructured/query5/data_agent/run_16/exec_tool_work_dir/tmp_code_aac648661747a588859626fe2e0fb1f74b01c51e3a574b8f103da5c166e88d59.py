code = """import json
import re
import os

# Load funding data
funding_file = var_functions.query_db:30
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
civic_file = var_functions.query_db:31
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Identify disaster projects that started in 2022
disaster_projects_2022 = []

# Check funding data for projects with disaster keywords
for item in funding_data:
    project_name = item.get('Project_Name', '')
    amount = int(item.get('Amount', 0))
    
    # Check if disaster-related
    is_disaster = any(keyword in project_name.upper() for keyword in ['FEMA', 'CALOES', 'CALJPIA'])
    
    # Check if started in 2022 (either name contains 2022 or appears in civic docs with 2022)
    started_in_2022 = '2022' in project_name
    
    if is_disaster and started_in_2022:
        disaster_projects_2022.append({
            'name': project_name,
            'amount': amount
        })

# Also check civic documents for projects with 2022 and disaster keywords
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for line in lines:
        line = line.strip()
        if line and '2022' in line:
            # Check if disaster-related
            line_upper = line.upper()
            if any(keyword in line_upper for keyword in ['FEMA', 'CALOES', 'CALJPIA', 'DISASTER']):
                # Try to extract project name
                if line.endswith('Project') or 'FEMA Project' in line or 'CalOES Project' in line:
                    # Clean the name
                    clean_name = re.sub(r'\s*\([^)]*\)\s*$', '', line)
                    if clean_name:
                        # Find matching funding
                        for item in funding_data:
                            fund_name = item.get('Project_Name', '')
                            if clean_name in fund_name or fund_name in clean_name:
                                amount = int(item.get('Amount', 0))
                                disaster_projects_2022.append({
                                    'name': fund_name,
                                    'amount': amount
                                })

# Remove duplicates and calculate total
total = 0
unique_projects = {}

for proj in disaster_projects_2022:
    name = proj['name']
    if name not in unique_projects:
        unique_projects[name] = proj['amount']
        total += proj['amount']

result = {
    'total_funding': total,
    'project_count': len(unique_projects),
    'projects': [{'name': k, 'amount': v} for k, v in unique_projects.items()]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.list_db:1': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:24': {'test': 'hello'}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:27': 'file_storage/functions.query_db:27.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json'}

exec(code, env_args)
