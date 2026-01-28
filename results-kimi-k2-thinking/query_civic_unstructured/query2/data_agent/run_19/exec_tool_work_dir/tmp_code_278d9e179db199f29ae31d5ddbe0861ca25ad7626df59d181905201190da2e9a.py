code = """import json
import re

# Load funding data
funding_path = locals()['var_functions.query_db:0']
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

# Load civic documents
civic_path = locals()['var_functions.query_db:14']
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Define park-related keywords
park_keywords = ['park', 'bluffs', 'playground', 'arbors', 'walkway', 'shade', 'recreation']

# Step 1: Find all park-related projects in funding data
park_funding_projects = []
for funding in funding_records:
    project_name = funding.get('Project_Name', '')
    if any(keyword in project_name.lower() for keyword in park_keywords):
        park_funding_projects.append({
            'name': project_name,
            'amount': int(funding.get('Amount', 0))
        })

# Step 2: Parse civic documents to find projects completed in 2022
completed_2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
            
        # Check if line mentions completion in 2022
        if '2022' in line and ('completed' in line.lower() or 'completion' in line.lower()):
            # Look backwards to find project name (up to 15 lines back)
            for j in range(max(0, i-15), i):
                prev_line = lines[j].strip()
                if prev_line and not prev_line.startswith('(') and not prev_line.startswith('—'):
                    # This might be a project name
                    completed_2022_projects.append(prev_line)
                    break

# Step 3: Find park projects that match between funding and civic docs
matched_park_projects = []
total_funding = 0

for park_proj in park_funding_projects:
    park_name = park_proj['name']
    
    # Check if this park project was completed in 2022
    for completed_proj in completed_2022_projects:
        # Match criteria: project names share key words
        park_words = set(park_name.lower().split())
        completed_words = set(completed_proj.lower().split())
        
        # Find intersection of meaningful words (exclude small words)
        meaningful_intersection = park_words.intersection(completed_words) - {'project', 'repair', 'improvements', 'improvement', 'and', 'the', 'at', 'of'}
        
        if len(meaningful_intersection) >= 2:  # At least 2 matching words
            matched_park_projects.append(park_name)
            total_funding += park_proj['amount']
            break
        elif park_name.lower() in completed_proj.lower() or completed_proj.lower() in park_name.lower():
            matched_park_projects.append(park_name)
            total_funding += park_proj['amount']
            break

# Step 4: Also check for explicit park project mentions in text
explicit_park_projects = [
    'Bluffs Park Shade Structure',
    'Broad Beach Road Water Quality Repair', 
    'Point Dume Walkway Repairs'
]

for proj in explicit_park_projects:
    for doc in civic_docs:
        text = doc.get('text', '').lower()
        proj_lower = proj.lower()
        
        if proj_lower in text and '2022' in text:
            for park_proj in park_funding_projects:
                if park_proj['name'].lower() in proj_lower or proj_lower in park_proj['name'].lower():
                    if park_proj['name'] not in matched_park_projects:
                        matched_park_projects.append(park_proj['name'])
                        total_funding += park_proj['amount']

# Deduplicate and finalize
unique_projects = list(set(matched_park_projects))

# Recalculate total funding for unique projects
total_funding = 0
for proj in unique_projects:
    for park_funding in park_funding_projects:
        if park_funding['name'] == proj:
            total_funding += park_funding['amount']
            break

result = {
    'total_funding_2022_park_projects': total_funding,
    'project_count': len(unique_projects),
    'projects': sorted(unique_projects)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:12': {'status': 'inspection_complete'}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'funding_records': 500, 'civic_docs': 5, 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}]}}

exec(code, env_args)
