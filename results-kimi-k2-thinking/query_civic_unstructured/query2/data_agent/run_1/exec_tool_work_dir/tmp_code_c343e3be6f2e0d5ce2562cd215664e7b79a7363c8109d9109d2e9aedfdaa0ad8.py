code = """import json
import re

funding_file = locals()['var_functions.query_db:24']
with open(funding_file, 'r') as f:
    funding = json.load(f)

civic_file = locals()['var_functions.query_db:26']
with open(civic_file, 'r') as f:
    civic = json.load(f)

# Build funding map
funding_map = {}
for rec in funding:
    name = rec.get('Project_Name', '').strip()
    if name:
        funding_map[name] = int(rec.get('Amount', 0))

# Extract park projects
park_projects = []

for doc in civic:
    txt = doc.get('text', '')
    lines = txt.split('\n')
    status = ''
    
    for i, line in enumerate(lines):
        line = line.strip()
        if 'Construction)' in line:
            status = 'completed'
        elif 'Design)' in line:
            status = 'design'
            
        if status == 'completed' and 'park' in line.lower() and len(line) > 10:
            # Look for 2022 completion
            has_2022 = False
            for j in range(max(0,i-3), min(len(lines), i+5)):
                if '2022' in lines[j] and ('complete' in lines[j].lower()):
                    has_2022 = True
                    break
            
            if has_2022:
                park_projects.append(line)

# Get funding
total = 0
for proj in park_projects:
    if proj in funding_map:
        total += funding_map[proj]

print('__RESULT__:')
print(json.dumps({'projects': park_projects, 'total_funding': total}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:16': {'funding_records_count': 10, 'civic_docs_count': 5, 'funding_projects_count': 10}, 'var_functions.execute_python:20': {'civic_docs_count': 5, 'funding_data_type': "<class 'list'>"}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:28': {'funding_records_loaded': 500, 'civic_docs_loaded': 5}}

exec(code, env_args)
