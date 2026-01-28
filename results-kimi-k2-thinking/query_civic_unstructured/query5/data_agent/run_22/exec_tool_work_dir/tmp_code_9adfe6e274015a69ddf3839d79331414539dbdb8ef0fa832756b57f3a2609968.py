code = """import json
import re
import os

# Read data from file paths
funding_path = var_functions.query_db:6
civic_path = var_functions.query_db:7

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_path, 'r') as f:
    civic_docs_data = json.load(f)

print(f'Loaded {len(funding_data)} funding records and {len(civic_docs_data)} civic documents')

# Extract disaster projects with 2022 start dates from civic documents
disaster_projects_2022 = []
all_projects = []

for doc in civic_docs_data:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    lines = text.split('\n')
    current_project = None
    project_info = {}
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Detect project names - look for capital projects section
        if (len(line) > 5 and 
            not line.startswith('(') and 
            not any(keyword in line.lower() for keyword in ['page', 'agenda item', 'capital improvement', 'disaster recovery', 'project schedule', 'updates:', 'completed:', 'not started:']) and
            (i < len(lines) - 1 and any(indicator in lines[i+1] for indicator in ['Updates:', 'Project Schedule:', '(cid:']))):
            
            if current_project and project_info:
                all_projects.append({
                    'project_name': current_project,
                    'info': project_info,
                    'source_file': filename
                })
            
            current_project = line.strip()
            project_info = {'type': 'unknown', 'has_2022_date': False, 'start_date_mention': None, 'is_disaster': False}
        
        if current_project:
            # Check for disaster indicators
            if any(keyword in line.upper() for keyword in ['FEMA', 'CALOES', 'CALJPIA', 'DISASTER', 'RECOVERY', 'WOOLSEY']):
                project_info['is_disaster'] = True
                project_info['type'] = 'disaster'
            
            # Check for 2022 dates
            if '2022' in line:
                if any(schedule_word in line.upper() for schedule_word in ['COMPLETE DESIGN', 'COMPLETE CONSTRUCTION', 'BEGIN', 'BEGIN CONSTRUCTION', 'ADVERTISE', 'CONSTRUCTION', 'DESIGN', 'SCHEDULE']):
                    project_info['has_2022_date'] = True
                    project_info['start_date_mention'] = line.strip()
    
    if current_project and project_info:
        all_projects.append({
            'project_name': current_project,
            'info': project_info,
            'source_file': filename
        })

# Filter for disaster projects with 2022 dates
disaster_projects_2022 = [p for p in all_projects if p['info']['is_disaster'] and p['info']['has_2022_date']]

print(f'Found {len(disaster_projects_2022)} disaster projects with 2022 dates')

# Create mapping of project names to funding amounts
funding_map = {}
for record in funding_data:
    proj_name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    funding_map[proj_name] = funding_map.get(proj_name, 0) + amount

# Find funding for disaster projects
total_funding = 0
matched_projects = []

for project in disaster_projects_2022:
    proj_name = project['project_name']
    
    # Direct match
    if proj_name in funding_map:
        amount = funding_map[proj_name]
        total_funding += amount
        matched_projects.append((proj_name, amount))
    else:
        # Try to find partial matches
        for fund_name, amount in funding_map.items():
            if (proj_name in fund_name or fund_name in proj_name or
                any(token in fund_name and len(token) > 5 for token in proj_name.split())):
                total_funding += amount
                matched_projects.append((proj_name, amount, f'matched to: {fund_name}'))
                break

print(f'Total funding for disaster projects started in 2022: ${total_funding:,}')
print(f'Matched {len(matched_projects)} projects')

for proj in matched_projects[:5]:
    print(f'  - {proj[0]}: ${proj[1]:,}')

print('__RESULT__:', json.dumps({
    'total_funding': total_funding,
    'matched_projects': len(matched_projects),
    'disaster_projects_2022': len(disaster_projects_2022)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.list_db:3': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:12': {'funding_count': 500, 'civic_docs_count': 5}, 'var_functions.execute_python:18': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}}

exec(code, env_args)
