code = """import json
import re

# Load data
funding_path = locals()['var_functions.query_db:0']
civic_path = locals()['var_functions.query_db:14']

with open(funding_path, 'r') as f:
    funding_records = json.load(f)

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

park_keywords = ['park', 'bluffs', 'playground', 'arbors', 'walkway', 'shade', 'recreation']

# Get all park project names from funding data
park_projects = []
for f in funding_records:
    name = f.get('Project_Name', '').lower()
    if any(kw in name for kw in park_keywords):
        park_projects.append(f.get('Project_Name', ''))

# Find which park projects were completed in 2022
completed_2022 = []
for doc in civic_docs:
    text = doc.get('text', '')
    if '2022' in text:
        lines = text.split('\n')
        for line in lines:
            if 'completed' in line.lower() or 'completion' in line.lower():
                for proj in park_projects:
                    if proj.lower() in line.lower():
                        completed_2022.append(proj)

# Check for specific mentions
for doc in civic_docs:
    text = doc.get('text', '').lower()
    if 'bluffs park shade structure' in text and 'november 2022' in text:
        completed_2022.append('Bluffs Park Shade Structure')
    if 'broad beach road water quality repair' in text and 'november 2022' in text:
        completed_2022.append('Broad Beach Road Water Quality Repair')
    if 'point dume walkway repairs' in text and 'november 2022' in text:
        completed_2022.append('Point Dume Walkway Repairs')

# Calculate total funding
total = 0
unique_projects = list(set(completed_2022))

for project in unique_projects:
    for funding in funding_records:
        if funding.get('Project_Name', '') == project:
            total += int(funding.get('Amount', 0))

result = {
    'total_funding_2022_park_projects': total,
    'project_count': len(unique_projects),
    'projects': unique_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:12': {'status': 'inspection_complete'}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'funding_records': 500, 'civic_docs': 5, 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}]}}

exec(code, env_args)
