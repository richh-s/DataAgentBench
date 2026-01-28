code = """import json
import re

civic_file = locals()['var_functions.query_db:2']
funding_file = locals()['var_functions.query_db:5']

with open(civic_file) as f:
    civic_docs = json.load(f)

with open(funding_file) as f:
    funding = json.load(f)

print('Loaded', len(civic_docs), 'documents and', len(funding), 'funding records')

# Find project names followed by Spring 2022 dates
spring_projects = {}

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        # Look for Spring 2022 dates
        if '2022' in line and ('Spring' in line or 'Spring' in text[max(0, i-3):i+1]):
            # Check if this line has a date
            date_match = None
            if 'Complete Design:' in line or 'Begin Construction:' in line:
                date_match = line
            
            if date_match:
                # Look backwards for project name
                for j in range(i-1, max(-1, i-5), -1):
                    prev_line = lines[j].strip()
                    if prev_line and len(prev_line) > 10 and not prev_line.startswith('cid:'):
                        # Clean project name
                        clean_name = re.sub(r'^[\u2022\-\*\u2022]+\s*', '', prev_line)
                        clean_name = re.sub(r'^cid:\d+\s*', '', clean_name)
                        clean_name = ' '.join(clean_name.split())
                        
                        if clean_name and 'Agenda' not in clean_name and len(clean_name) < 100:
                            spring_projects[clean_name] = True
                            break

spring_project_list = list(spring_projects.keys())
print('Spring 2022 projects found:', len(spring_project_list))
for proj in spring_project_list:
    print(' ', proj)

# Build funding map
funding_map = {}
for record in funding:
    proj_name = record['Project_Name']
    amount = int(record['Amount'])
    funding_map[proj_name] = funding_map.get(proj_name, 0) + amount

# Match projects with funding
matched_projects = []
matched_funding = 0

for project in spring_project_list:
    if project in funding_map:
        matched_projects.append({'project': project, 'funding': funding_map[project]})
        matched_funding += funding_map[project]
    else:
        # Try substring matching
        for fund_name, amount in funding_map.items():
            if (project in fund_name or fund_name in project or
                re.sub(r'[^\w]', '', project) in re.sub(r'[^\w]', '', fund_name)):
                matched_projects.append({'project': project, 'funding': amount, 'matched_with': fund_name})
                matched_funding += amount
                break

print('Matched', len(matched_projects), 'projects with total funding of', matched_funding)

result = {
    'project_count': len(matched_projects),
    'total_funding': matched_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.execute_python:14': {'civic_count': 5, 'funding_count': 500}, 'var_functions.execute_python:20': {'civic_file': 'var_functions.query_db:2', 'funding_file': 'var_functions.query_db:5'}, 'var_functions.execute_python:22': {'civic_path': 'file_storage/functions.query_db:2.json', 'funding_path': 'file_storage/functions.query_db:5.json', 'civic_exists': True, 'funding_exists': True}, 'var_functions.execute_python:36': {'project_count': 0, 'total_funding': 0}}

exec(code, env_args)
