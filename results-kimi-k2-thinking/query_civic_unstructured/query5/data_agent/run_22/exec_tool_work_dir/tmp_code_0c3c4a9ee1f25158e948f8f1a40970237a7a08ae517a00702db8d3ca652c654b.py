code = """import json
import re

with open(locals()['var_functions.query_db:66'], 'r') as f:
    funding = json.load(f)

with open(locals()['var_functions.query_db:67'], 'r') as f:
    civic_docs = json.load(f)

# Build funding map for all projects
fund_map = {}
for r in funding:
    name = r.get('Project_Name', '')
    if name:
        fund_map[name] = fund_map.get(name, 0) + int(r.get('Amount', 0))

# Analyze civic documents to find disaster projects with 2022 dates
disaster_projects_2022 = []
project_2022_dates = {}

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    # Look for project sections
    for i in range(len(lines) - 1):
        line = lines[i].strip()
        if not line or line.startswith('(') or 'page' in line.lower():
            continue
            
        # Check if this line is a project name
        next_line = lines[i+1].strip() if i+1 < len(lines) else ''
        if 'Updates:' in next_line or 'Project Schedule:' in next_line or next_line.startswith('(cid:'):
            project_name = line
            
            # Check if disaster-related
            is_disaster = False
            
            # Check following lines for disaster indicators and 2022 dates
            for j in range(i, min(i+15, len(lines))):
                check_line = lines[j].upper()
                
                # Check for disaster indicators
                if any(indicator in check_line for indicator in [
                    'FEMA', 'CALOES', 'CALJPIA', 'DISASTER', 'RECOVERY', 'WOOLSEY'
                ]):
                    is_disaster = True
                    
                # Check for 2022 dates in schedule context
                if '2022' in check_line:
                    if any(schedule_word in check_line for schedule_word in [
                        'DESIGN', 'CONSTRUCTION', 'BEGIN', 'COMPLETE', 'ADVERTISE', 'SCHEDULE'
                    ]):
                        project_2022_dates[project_name] = project_2022_dates.get(project_name, [])
                        project_2022_dates[project_name].append(check_line.strip())
            
            if is_disaster and project_name in project_2022_dates:
                disaster_projects_2022.append(project_name)

# Remove duplicates
disaster_projects_2022 = list(set(disaster_projects_2022))

print(f'Found {len(disaster_projects_2022)} disaster projects with 2022 dates:')
for proj in disaster_projects_2022[:10]:
    print(f'  - {proj}')
    if proj in project_2022_dates:
        print(f'     Dates: {project_2022_dates[proj][:2]}')

# Calculate funding for disaster projects started in 2022
total_funding = 0
matched_projects = []
unmatched_projects = []

for disaster_proj in disaster_projects_2022:
    found_match = False
    # Check for direct match with variations
    possible_names = [
        disaster_proj,
        disaster_proj + ' (FEMA Project)',
        disaster_proj + ' (FEMA/CalOES Project)',
        disaster_proj + ' (CalOES Project)',
        disaster_proj + ' (CalJPIA Project)'
    ]
    
    for name_variation in possible_names:
        if name_variation in fund_map:
            total_funding += fund_map[name_variation]
            matched_projects.append((disaster_proj, name_variation, fund_map[name_variation]))
            found_match = True
            break
    
    if not found_match:
        # Try fuzzy matching
        for fund_name, amount in fund_map.items():
            if disaster_proj in fund_name or fund_name in disaster_proj:
                total_funding += amount
                matched_projects.append((disaster_proj, fund_name, amount))
                found_match = True
                break
    
    if not found_match:
        unmatched_projects.append(disaster_proj)

print(f'\nMatched {len(matched_projects)} projects with funding')
print(f'Could not match {len(unmatched_projects)} projects')

for proj, fund_name, amt in matched_projects[:10]:
    print(f'  {proj[:50]} -> ${amt:,}')

# Also include disaster-related projects from funding with 2022 in name
for fund_name, amount in fund_map.items():
    if '2022' in fund_name and any(ind in fund_name.upper() for ind in ['FEMA', 'CALOES', 'CALJPIA', 'DISASTER', 'WOOLSEY']):
        total_funding += amount
        matched_projects.append((fund_name, fund_name, amount))

result = {
    'total_funding_for_disaster_projects_in_2022': total_funding,
    'number_of_disaster_projects_identified': len(disaster_projects_2022),
    'number_of_projects_matched_with_funding': len(matched_projects),
    'sample_matched_projects': [(p[:50], a) for _, p, a in matched_projects[:10]]
}

print('__RESULT__:')
print(json.dumps(result, default=str))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.list_db:3': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:12': {'funding_count': 500, 'civic_docs_count': 5}, 'var_functions.execute_python:18': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}, 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:67': 'file_storage/functions.query_db:67.json', 'var_functions.execute_python:92': {'total_funding_for_disaster_related_projects': 1410000, 'number_of_disaster_projects': 27, 'sample_projects': ['Birdview Avenue Improvements (CalOES Project)', 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Clover Heights Storm Drain (FEMA Project)', 'Corral Canyon Culvert Repairs (FEMA Project)']}}

exec(code, env_args)
