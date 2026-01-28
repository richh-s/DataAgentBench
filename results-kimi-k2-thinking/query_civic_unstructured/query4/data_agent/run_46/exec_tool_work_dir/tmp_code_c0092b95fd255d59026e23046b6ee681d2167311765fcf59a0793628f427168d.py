code = """import json, re, os

civic_file = locals()['var_functions.query_db:2']
funding_file = locals()['var_functions.query_db:5']

with open(civic_file) as f:
    civic_docs = json.load(f)

with open(funding_file) as f:
    funding = json.load(f)

print('Loaded', len(civic_docs), 'civic documents and', len(funding), 'funding records')

# Extract projects with dates
def extract_projects_and_dates(docs):
    projects = []
    for doc in docs:
        text = doc.get('text', '')
        filename = doc.get('filename', '')
        lines = text.split('\n')
        
        for i in range(len(lines)):
            line = lines[i].strip()
            if not line or line.startswith('cid:'):
                continue
                
            # Look for date patterns in current or next line
            date_patterns = ['2022-Spring', '2022-Mar', '2022-Apr', '2022-May', 
                           'Spring 2022', 'Mar 2022', 'Apr 2022', 'May 2022',
                           '2022-03', '2022-04', '2022-05']
            
            has_date = False
            for pattern in date_patterns:
                if pattern in line or (i+1 < len(lines) and pattern in lines[i+1]):
                    has_date = True
                    break
            
            if has_date:
                # Find project name (look backwards up to 5 lines)
                project_name = None
                for j in range(i-1, max(-1, i-6), -1):
                    prev = lines[j].strip()
                    if prev and not prev.startswith('cid:') and len(prev) > 5:
                        # Clean name
                        name = re.sub(r'^[\u2022â€¢\-\*]+\s*', '', prev)
                        name = re.sub(r'^cid:\d+\s*', '', name)
                        name = re.sub(r'\s+', ' ', name).strip()
                        if name and 'Agenda' not in name and 'Report' not in name:
                            project_name = name
                            break
                
                if project_name:
                    projects.append({
                        'name': project_name,
                        'file': filename
                    })
    
    return projects

spring_projects = extract_projects_and_dates(civic_docs)
print('Found', len(spring_projects), 'Spring 2022 projects in text')

# Remove duplicates
unique_projects = []
seen = set()
for p in spring_projects:
    if p['name'] not in seen:
        seen.add(p['name'])
        unique_projects.append(p)

print('Unique projects:', len(unique_projects))
for p in unique_projects:
    print(' ', p['name'])

# Build funding map - sum amounts by project name
funding_map = {}
for record in funding:
    proj_name = record['Project_Name']
    amount = int(record['Amount'])
    funding_map[proj_name] = funding_map.get(proj_name, 0) + amount

print('Funding map has', len(funding_map), 'project names')

# Match projects with funding
matches = []
total_funding = 0

for project in unique_projects:
    proj_name = project['name']
    
    # Direct match
    if proj_name in funding_map:
        matches.append({
            'project': proj_name,
            'funding': funding_map[proj_name]
        })
        total_funding += funding_map[proj_name]
    else:
        # Try partial matching - check if project name is contained in funding name
        best_match = None
        best_amount = 0
        
        for fund_name, amount in funding_map.items():
            if proj_name in fund_name or fund_name in proj_name:
                best_match = fund_name
                best_amount = amount
                break
        
        if best_match:
            matches.append({
                'project': proj_name,
                'funding': best_amount,
                'matched_with': best_match
            })
            total_funding += best_amount

print('Matched', len(matches), 'projects with funding')
print('Total funding:', total_funding)

result = {
    'project_count': len(matches),
    'total_funding': total_funding,
    'matched_projects': matches
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.execute_python:14': {'civic_count': 5, 'funding_count': 500}, 'var_functions.execute_python:20': {'civic_file': 'var_functions.query_db:2', 'funding_file': 'var_functions.query_db:5'}, 'var_functions.execute_python:22': {'civic_path': 'file_storage/functions.query_db:2.json', 'funding_path': 'file_storage/functions.query_db:5.json', 'civic_exists': True, 'funding_exists': True}}

exec(code, env_args)
