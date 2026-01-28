code = """import json, re, os

print('Starting analysis...')

# Load data from file paths
with open(locals()['var_functions.query_db:66']) as f:
    funding = json.load(f)
with open(locals()['var_functions.query_db:67']) as f:
    civic_docs = json.load(f)

print(f'Loaded {len(funding)} funding records and {len(civic_docs)} civic documents')

# Step 1: Build comprehensive funding map
fund_map = {}
for r in funding:
    name = r.get('Project_Name', '')
    if name:
        amount = int(r.get('Amount', 0))
        fund_map[name] = fund_map.get(name, 0) + amount

print(f'Funding map contains {len(fund_map)} unique project names')

# Step 2: Extract disaster projects with 2022 start dates
disaster_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines) - 1):
        curr_line = lines[i].strip()
        next_line = lines[i+1].strip() if i+1 < len(lines) else ''
        
        # Skip empty or non-project lines
        if not curr_line or curr_line.startswith('(') or 'page' in curr_line.lower():
            continue
            
        # Check if this is a project header (next line has project details)
        if 'Updates:' in next_line or 'Project Schedule:' in next_line:
            project_name = curr_line
            is_disaster = False
            has_2022 = False
            
            # Check following lines for indicators
            for j in range(i+1, min(i+15, len(lines))):
                check_line = lines[j].upper()
                
                # Look for disaster indicators
                disaster_indicators = ['FEMA', 'CALOES', 'CALJPIA', 'DISASTER', 'WOOLSEY', 'RECOVERY']
                for ind in disaster_indicators:
                    if ind in check_line:
                        is_disaster = True
                        break
                
                # Look for 2022 dates with schedule information
                if '2022' in check_line:
                    schedule_words = ['DESIGN', 'CONSTRUCTION', 'BEGIN', 'COMPLETE', 'ADVERTISE', 'SCHEDULE']
                    for word in schedule_words:
                        if word in check_line:
                            has_2022 = True
                            break
            
            if is_disaster and has_2022 and project_name:
                disaster_projects.append(project_name)

# Remove duplicates
disaster_projects = list(set(disaster_projects))
print(f'Found {len(disaster_projects)} disaster projects with 2022 dates:')
for p in disaster_projects[:5]:
    print(f'  - {p}')

# Step 3: Calculate funding total
total_funding = 0
matched_projects = []
unmatched_projects = []

for proj in disaster_projects:
    matched = False
    for fund_proj, amount in fund_map.items():
        # Direct match or substring match
        if proj == fund_proj or proj in fund_proj or fund_proj in proj:
            total_funding += amount
            matched_projects.append((proj, amount))
            matched = True
            break
    
    if not matched:
        unmatched_projects.append(proj)

print(f'\nMatched with funding: {len(matched_projects)}')
print(f'Without funding match: {len(unmatched_projects)}')
print(f'\nTotal funding: ${total_funding:,}')

# Show matched projects with their funding
print('\nProjects with funding:')
for proj, amt in matched_projects[:10]:
    print(f'  {proj}: ${amt:,}')

result = {
    'total_funding_for_disaster_projects_started_2022': total_funding,
    'number_of_disaster_projects_found': len(disaster_projects),
    'number_of_projects_with_funding_match': len(matched_projects),
    'sample_d projects': disaster_projects[:3]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.list_db:3': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:12': {'funding_count': 500, 'civic_docs_count': 5}, 'var_functions.execute_python:18': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}, 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:67': 'file_storage/functions.query_db:67.json'}

exec(code, env_args)
