code = """import json, re, os

civic_file = locals()['var_functions.query_db:2']
funding_file = locals()['var_functions.query_db:5']

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding = json.load(f)

print(f'Documents: {len(civic_docs)}, Funding: {len(funding)}')

# Extract project names from text that have Spring 2022 dates
spring_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        # Skip metadata lines
        if not line or line.startswith('cid:') or line.startswith('To:') or line.startswith('Prepared'):
            continue
            
        # Look for Spring 2022 patterns
        if '2022' in line and ('Spring' in line or 'Spring' in text[max(0, i-3):i+3]):
            # Look backwards for project name
            for j in range(i-1, max(-1, i-4), -1):
                prev_line = lines[j].strip()
                if prev_line and len(prev_line) > 5 and not prev_line.startswith('cid:'):
                    # Clean the project name
                    clean_name = re.sub(r'^[\-\*\u2022\u00e2\u20ac]+\s*', '', prev_line)
                    clean_name = re.sub(r'^cid:\d+\s*', '', clean_name)
                    clean_name = ' '.join(clean_name.split())
                    
                    # Validate it's a reasonable project name
                    if (clean_name and 'Agenda' not in clean_name and 'Report' not in clean_name 
                        and len(clean_name) < 150 and len(clean_name) > 3):
                        spring_projects.add(clean_name)
                        break

spring_list = list(spring_projects)
print(f'Found {len(spring_list)} potential Spring 2022 projects')

# Build funding map (aggregate amounts by project name)
funding_map = {}
for record in funding:
    name = record['Project_Name']
    amount = int(record['Amount'])
    funding_map[name] = funding_map.get(name, 0) + amount

# Match projects with funding
matched = []
total = 0

for project in spring_list:
    if project in funding_map:
        matched.append([project, funding_map[project]])
        total += funding_map[project]
    else:
        # Try substring matching
        found = False
        proj_clean = re.sub(r'[^A-Za-z0-9]', '', project).lower()
        for fund_name, amount in funding_map.items():
            fund_clean = re.sub(r'[^A-Za-z0-9]', '', fund_name).lower()
            if proj_clean in fund_clean or fund_clean in proj_clean:
                matched.append([project, amount, fund_name])
                total += amount
                found = True
                break

# Clean up result for JSON serialization
result = {
    'project_count': len(matched),
    'total_funding': total,
    'matched_projects': [[str(item[0]), int(item[1])] for item in matched]
}

output = json.dumps(result)
print('__RESULT__:')
print(output)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.execute_python:14': {'civic_count': 5, 'funding_count': 500}, 'var_functions.execute_python:20': {'civic_file': 'var_functions.query_db:2', 'funding_file': 'var_functions.query_db:5'}, 'var_functions.execute_python:22': {'civic_path': 'file_storage/functions.query_db:2.json', 'funding_path': 'file_storage/functions.query_db:5.json', 'civic_exists': True, 'funding_exists': True}, 'var_functions.execute_python:36': {'project_count': 0, 'total_funding': 0}}

exec(code, env_args)
