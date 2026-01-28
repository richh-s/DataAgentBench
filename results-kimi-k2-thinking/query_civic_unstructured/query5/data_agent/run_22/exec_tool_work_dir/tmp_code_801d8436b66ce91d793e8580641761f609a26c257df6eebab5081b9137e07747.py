code = """import json, re

# Load data from stored results
f_path = locals()['var_functions.query_db:66']
c_path = locals()['var_functions.query_db:67']

with open(f_path, 'r') as f:
    funding = json.load(f)
with open(c_path, 'r') as f:
    civic_docs = json.load(f)

# Build funding map: project name to total funding amount
fund_map = {}
for r in funding:
    name = r.get('Project_Name', '')
    if name:
        amount = int(r.get('Amount', 0))
        fund_map[name] = fund_map.get(name, 0) + amount

print(f'Funding map contains {len(fund_map)} project entries')

# Extract project information from civic documents
disaster_projects_2022 = []
project_info = {}

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Skip empty lines and non-content lines
        if not line or line.startswith('(') or 'page' in line.lower() or 'agenda item' in line.lower():
            i += 1
            continue
        
        # Look for project headers (typically followed by project details)
        if i < len(lines) - 1:
            next_line = lines[i+1].strip()
            if 'Updates:' in next_line or 'Project Schedule:' in next_line or next_line.startswith('(cid:'):
                project_name = line
                
                # Initialize project tracking
                is_disaster = False
                has_2022_date = False
                date_info = []
                
                # Check following lines for disaster indicators and dates
                for j in range(i, min(i+15, len(lines))):
                    check_line = lines[j]
                    
                    # Check for disaster-related keywords
                    if any(keyword in check_line.upper() for keyword in ['FEMA', 'CALOES', 'CALJPIA', 'DISASTER', 'WOOLSEY', 'RECOVERY']):
                        is_disaster = True
                    
                    # Check for 2022 dates in project context
                    if '2022' in check_line:
                        # Look for schedule-related context
                        if any(schedule_indicator in check_line.upper() for schedule_indicator in 
                              ['COMPLETE DESIGN', 'BEGIN CONSTRUCTION', 'ADVERTISE', 'COMPLETE', 'BEGIN', 'CONSTRUCTION', 'DESIGN']):
                            has_2022_date = True
                            date_info.append(check_line.strip())
                
                # If it's a disaster project with 2022 date, add to list
                if is_disaster and has_2022_date and project_name:
                    disaster_projects_2022.append(project_name)
                    project_info[project_name] = {
                        'dates': date_info,
                        'source_file': doc.get('filename', '')
                    }
        
        i += 1

# Remove duplicates
unique_disaster_projects = list(set(disaster_projects_2022))
print(f'Found {len(unique_disaster_projects)} unique disaster projects with 2022 dates')

# Match with funding data and calculate total
total_funding = 0
matched_projects = []

for proj_name in unique_disaster_projects:
    # Direct match
    if proj_name in fund_map:
        amount = fund_map[proj_name]
        total_funding += amount
        matched_projects.append((proj_name, amount, 'exact'))
        continue
    
    # Try fuzzy matching with common suffixes
    matched = False
    for fund_name, amount in fund_map.items():
        # Check substring matches
        if proj_name.lower() in fund_name.lower() or fund_name.lower() in proj_name.lower():
            total_funding += amount
            matched_projects.append((proj_name, amount, f'matched to: {fund_name}'))
            matched = True
            break
        
        # Check for word similarity
        proj_words = set([w.lower() for w in re.findall(r'\\w+', proj_name) if len(w) > 5])
        fund_words = set([w.lower() for w in re.findall(r'\\w+', fund_name) if len(w) > 5])
        
        if proj_words and fund_words and len(proj_words.intersection(fund_words)) >= 2:
            total_funding += amount
            matched_projects.append((proj_name, amount, f'similar to: {fund_name}'))
            matched = True
            break

# Also check for explicitly named disaster projects with 2022 in their names
print('\\nChecking for 2022 disaster projects in funding data...')
for fund_name, amount in fund_map.items():
    if '2022' in fund_name and any(ind.upper() in fund_name.upper() for ind in ['FEMA', 'CALOES', 'CALJPIA', 'DISASTER', 'WOOLSEY']):
        print(f'Found 2022 disaster project: {fund_name} - ${amount:,}')
        if fund_name not in [p[0] for p in matched_projects]:
            total_funding += amount
            matched_projects.append((fund_name, amount, '2022_in_name'))

print(f'\\nTotal funding for disaster-related projects that started in 2022: ${total_funding:,}')
print(f'Number of projects matched: {len(set([p[0] for p in matched_projects]))}')

result = {
    'total_funding': total_funding,
    'disaster_projects_with_2022_start': len(unique_disaster_projects),
    'projects_matched_with_funding': len(set([p[0] for p in matched_projects]))
}

for i, (proj_name, amount, match_type) in enumerate(sorted(matched_projects, key=lambda x: x[1], reverse=True)[:10]):
    print(f'  {i+1}. {proj_name[:60]} - ${amount:,} ({match_type})')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.list_db:3': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:12': {'funding_count': 500, 'civic_docs_count': 5}, 'var_functions.execute_python:18': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}, 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:67': 'file_storage/functions.query_db:67.json', 'var_functions.execute_python:92': {'total_funding_for_disaster_related_projects': 1410000, 'number_of_disaster_projects': 27, 'sample_projects': ['Birdview Avenue Improvements (CalOES Project)', 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Clover Heights Storm Drain (FEMA Project)', 'Corral Canyon Culvert Repairs (FEMA Project)']}, 'var_functions.execute_python:96': {'total_disaster_related_funding': 1410000, 'projects': 27}}

exec(code, env_args)
