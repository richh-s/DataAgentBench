code = """import json
import re

# Load funding records
funding_path = locals()['var_functions.query_db:0']
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

# Load civic documents
civic_path = locals()['var_functions.query_db:14']
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Identify park keywords
park_keywords = ['park', 'bluffs', 'playground', 'arbors', 'walkway', 'shade', 'recreation']

# Extract projects completed in 2022 from civic documents
completed_2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
        
        # Check for completion in 2022
        if '2022' in line and ('completed' in line.lower() or 'completion' in line.lower()):
            # Look backwards for project name
            for j in range(max(0, i-10), i):
                prev_line = lines[j].strip()
                if prev_line and not prev_line.startswith('(') and not prev_line.startswith('•'):
                    completed_2022_projects.append(prev_line)
                    break

# Match with funding data for park projects
total_funding = 0
matched_park_projects = []

for funding in funding_records:
    project_name = funding.get('Project_Name', '')
    amount = int(funding.get('Amount', 0))
    
    # Check if it's a park project
    proj_lower = project_name.lower()
    if not any(kw in proj_lower for kw in park_keywords):
        continue
    
    # Check if completed in 2022
    for completed_project in completed_2022_projects:
        # Match project names (allow partial matching)
        if (project_name.lower() in completed_project.lower() or 
            completed_project.lower() in project_name.lower()):
            total_funding += amount
            matched_park_projects.append(project_name)
            break

# Also check for specific park projects mentioned as completed in 2022
print_matches = []

# Bluffs Park Shade Structure - completed November 2022
# Marie Canyon Green Streets - completed January 2023 (not 2022)
# Broad Beach Road Water Quality Repair - completed November 2022
# Point Dume Walkway Repairs - completed November 2022

for doc in civic_docs:
    text = doc.get('text', '').lower()
    
    if 'bluffs park shade structure' in text and 'november 2022' in text:
        for funding in funding_records:
            if 'Bluffs Park Shade Structure' in funding.get('Project_Name', ''):
                amount = int(funding.get('Amount', 0))
                total_funding += amount
                matched_park_projects.append(funding.get('Project_Name', ''))
                break
    
    if 'broad beach road water quality repair' in text and 'november 2022' in text:
        for funding in funding_records:
            if 'Broad Beach Road Water Quality Repair' in funding.get('Project_Name', ''):
                amount = int(funding.get('Amount', 0))
                total_funding += amount
                matched_park_projects.append(funding.get('Project_Name', ''))
                break
    
    if 'point dume walkway repairs' in text and 'november 2022' in text:
        for funding in funding_records:
            if 'Point Dume Walkway Repairs' in funding.get('Project_Name', ''):
                amount = int(funding.get('Amount', 0))
                total_funding += amount
                matched_park_projects.append(funding.get('Project_Name', ''))
                break

# Deduplicate and calculate
total_funding = 0
unique_projects = list(set(matched_park_projects))

for project in unique_projects:
    for funding in funding_records:
        if funding.get('Project_Name', '') == project:
            total_funding += int(funding.get('Amount', 0))
            break

print('__RESULT__:')
print(json.dumps({
    'total_funding_2022_park_projects': total_funding,
    'project_count': len(unique_projects),
    'projects': unique_projects
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:12': {'status': 'inspection_complete'}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'funding_records': 500, 'civic_docs': 5, 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}]}}

exec(code, env_args)
