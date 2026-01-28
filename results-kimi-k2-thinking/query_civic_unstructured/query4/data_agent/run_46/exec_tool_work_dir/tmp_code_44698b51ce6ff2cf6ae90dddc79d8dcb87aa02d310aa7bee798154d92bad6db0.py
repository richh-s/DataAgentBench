code = """import json
import re

civic_path = locals()['var_functions.query_db:2']
funding_path = locals()['var_functions.query_db:5']

with open(civic_path) as f:
    civic_docs = json.load(f)

with open(funding_path) as f:
    funding = json.load(f)

print(f'Processing {len(civic_docs)} documents')

# Function to extract projects from text
def extract_projects(text):
    projects = []
    lines = text.split('\n')
    
    current_project = None
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or line.startswith('cid:'):
            continue
        
        # Detect category headers
        if 'Capital Improvement Projects (Design)' in line:
            category = 'design'
            continue
        elif 'Capital Improvement Projects (Construction)' in line:
            category = 'construction'
            continue
        elif 'Capital Improvement Projects (Not Started)' in line:
            category = 'not_started'
            continue
        elif 'Disaster Recovery Projects' in line:
            category = 'disaster'
            continue
        
        # Look for project names and dates
        if len(line) > 10 and not line.startswith('To:') and not line.startswith('Prepared'):
            # Check if this line or next few lines contain date info
            block = '\n'.join(lines[i:i+5])
            
            # Look for Spring 2022 or 2022 with spring months
            date_patterns = [
                r'Complete Design:\s*(Spring\s+2022|2022-Spring)',
                r'Complete Design:\s*(\w+\s+2022)',
                r'Begin Construction:\s*(Spring\s+2022|2022-Spring)',
                r'Project Schedule:\s*.*?Complete Design:\s*(\w+\s+2022)'
            ]
            
            project_date = None
            for pattern in date_patterns:
                match = re.search(pattern, block, re.IGNORECASE)
                if match:
                    project_date = match.group(1)
                    break
            
            if project_date and '2022' in project_date:
                # Check if it's a spring month
                is_spring = False
                date_upper = project_date.upper()
                
                if 'SPRING' in date_upper:
                    is_spring = True
                elif any(m in date_upper for m in ['MARCH', 'APRIL', 'MAY', 'MAR', 'APR', 'MAY']):
                    is_spring = True
                
                if is_spring:
                    # Extract project name (clean up)
                    name = re.sub(r'^[\u2022\-]+\s*', '', line)
                    name = re.sub(r'^cid:\d+\s*', '', name)
                    name = ' '.join(name.split())
                    
                    if name and 'Agenda' not in name and len(name) < 100:
                        projects.append({
                            'name': name,
                            'date': project_date
                        })
    
    return projects

# Extract all projects
all_spring_projects = []
for doc in civic_docs:
    projects = extract_projects(doc['text'])
    all_spring_projects.extend(projects)

print(f'Found {len(all_spring_projects)} potential Spring 2022 projects')

# Remove duplicates
duplicate_check = {}
unique_projects = []
for p in all_spring_projects:
    key = p['name']
    if key not in duplicate_check:
        duplicate_check[key] = True
        unique_projects.append(p)

print(f'After deduplication: {len(unique_projects)} projects')
for p in unique_projects:
    print(f"  {p['name']} - {p['date']}")

# Build funding map
funding_map = {}
for f in funding:
    name = f['Project_Name']
    amount = int(f['Amount'])
    funding_map[name] = funding_map.get(name, 0) + amount

# Match with funding
matched = []
total_funding = 0

for project in unique_projects:
    proj_name = project['name']
    
    if proj_name in funding_map:
        matched.append({
            'project': proj_name,
            'funding': funding_map[proj_name]
        })
        total_funding += funding_map[proj_name]
    else:
        # Try fuzzy matching
        for fund_name, amount in funding_map.items():
            if (proj_name in fund_name or fund_name in proj_name or
                re.sub(r'[^\w]', '', proj_name) in re.sub(r'[^\w]', '', fund_name)):
                matched.append({
                    'project': proj_name,
                    'funding': amount,
                    'matched_with': fund_name
                })
                total_funding += amount
                break

print(f'\nSuccessfully matched {len(matched)} projects with funding data')
print(f'Total funding: ${total_funding:,}')

result = {
    'project_count': len(matched),
    'total_funding': total_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.execute_python:14': {'civic_count': 5, 'funding_count': 500}, 'var_functions.execute_python:20': {'civic_file': 'var_functions.query_db:2', 'funding_file': 'var_functions.query_db:5'}, 'var_functions.execute_python:22': {'civic_path': 'file_storage/functions.query_db:2.json', 'funding_path': 'file_storage/functions.query_db:5.json', 'civic_exists': True, 'funding_exists': True}, 'var_functions.execute_python:36': {'project_count': 0, 'total_funding': 0}}

exec(code, env_args)
