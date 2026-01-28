code = """import json
import re

# Load funding data
funding_path = locals()['var_functions.query_db:24']
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

# Load civic documents  
civic_path = locals()['var_functions.query_db:26']
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Build funding map by project name
funding_map = {}
for rec in funding_records:
    proj_name = rec.get('Project_Name', '').strip()
    if proj_name:
        funding_map[proj_name] = int(rec.get('Amount', 0))

# Extract park projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    current_section = ''
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Track section (status)
        if 'Projects (Construction)' in line:
            current_section = 'completed'
        elif 'Projects (Design)' in line:
            current_section = 'design'
        elif 'Projects (Not Started)' in line:
            current_section = 'not_started'
            
        # Found a park project in construction section
        if current_section == 'completed' and 'park' in line.lower():
            # Skip headers/short lines
            if len(line) < 15 or line.isupper():
                continue
                
            # Look for 2022 completion in context
            context_start = max(0, i-2)
            context_end = min(len(lines), i+4)
            context = ' '.join(lines[context_start:context_end])
            
            if '2022' in context and ('completed' in context.lower() or 'complete' in context.lower()):
                park_projects_2022.append(line)

# Remove duplicates
park_projects_2022 = list(set(park_projects_2022))

# Find funding for these projects
total_funding = 0
funded_project_list = []

for park_project in park_projects_2022:
    # Exact match
    if park_project in funding_map:
        total_funding += funding_map[park_project]
        funded_project_list.append(park_project)
    else:
        # Partial match (funded name might be longer/more specific)
        for funded_name in funding_map:
            if park_project.lower() in funded_name.lower():
                total_funding += funding_map[funded_name]
                funded_project_list.append(funded_name)
                break

result = {
    'park_projects_2022': park_projects_2022,
    'funded_projects': funded_project_list,
    'total_funding': total_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:16': {'funding_records_count': 10, 'civic_docs_count': 5, 'funding_projects_count': 10}, 'var_functions.execute_python:20': {'civic_docs_count': 5, 'funding_data_type': "<class 'list'>"}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:28': {'funding_records_loaded': 500, 'civic_docs_loaded': 5}}

exec(code, env_args)
