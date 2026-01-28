code = """import json
import re

# Load data
civic_docs_file = locals()['var_functions.query_db:2']
funding_file = locals()['var_functions.query_db:5']

with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

print(f'Civic docs: {len(civic_docs)}, Funding: {len(funding_data)}')

# Build funding map
funding_map = {}
for f in funding_data:
    name = f['Project_Name']
    amount = int(f['Amount'])
    funding_map[name] = funding_map.get(name, 0) + amount

# Search for Spring 2022 projects
spring_projects = set()

for doc in civic_docs:
    text = doc['text']
    # Look for Complete Design: or Begin Construction: lines with Spring 2022
    pattern = r'([A-Z][A-Za-z0-9 &\-\(\)]+?(?:Project|Improvements|Repairs|Drainage|Structure)).*?(?:Complete Design|Begin Construction).*?(?:Spring 2022|2022-Spring)'
    matches = re.findall(pattern, text, re.DOTALL)
    for proj in matches:
        clean = re.sub(r'^[\-\*\u2022]+', '', proj)
        clean = re.sub(r'^cid:\d+', '', clean)
        clean = ' '.join(clean.split())
        if clean and 'Agenda' not in clean:
            spring_projects.add(clean)

# Also look for numeric months
for doc in civic_docs:
    text = doc['text']
    pattern2 = r'([A-Z][A-Za-z0-9 &\-\(\)]+?(?:Project|Improvements|Repairs|Drainage|Structure)).*?(?:Complete Design|Begin Construction).*?(?:2022[-\s](?:Mar|Apr|May)|2022[-\s](?:03|04|05))'
    matches2 = re.findall(pattern2, text, re.DOTALL)
    for proj in matches2:
        clean = re.sub(r'^[\-\*\u2022]+', '', proj)
        clean = re.sub(r'^cid:\d+', '', clean)
        clean = ' '.join(clean.split())
        if clean and 'Agenda' not in clean:
            spring_projects.add(clean)

spring_list = list(spring_projects)
print('Spring projects found:', len(spring_list))
for proj in spring_list:
    print(' ', proj)

# Match with funding
matched = 0
total = 0
for proj in spring_list:
    for fund_name, amount in funding_map.items():
        proj_clean = re.sub(r'[^A-Za-z0-9]', '', proj).lower()
        fund_clean = re.sub(r'[^A-Za-z0-9]', '', fund_name).lower()
        if proj_clean in fund_clean or fund_clean in proj_clean:
            matched += 1
            total += amount
            break

result = {'count': matched, 'total_funding': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.execute_python:14': {'civic_count': 5, 'funding_count': 500}, 'var_functions.execute_python:20': {'civic_file': 'var_functions.query_db:2', 'funding_file': 'var_functions.query_db:5'}, 'var_functions.execute_python:22': {'civic_path': 'file_storage/functions.query_db:2.json', 'funding_path': 'file_storage/functions.query_db:5.json', 'civic_exists': True, 'funding_exists': True}, 'var_functions.execute_python:36': {'project_count': 0, 'total_funding': 0}}

exec(code, env_args)
