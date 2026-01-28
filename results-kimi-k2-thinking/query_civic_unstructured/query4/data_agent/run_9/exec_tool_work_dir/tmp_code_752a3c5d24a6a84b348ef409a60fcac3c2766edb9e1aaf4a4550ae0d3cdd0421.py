code = """import json
import re

# Read data
civic_result = locals()['var_functions.query_db:32']
funding_result = locals()['var_functions.query_db:33']

# Handle file paths
if isinstance(civic_result, str) and '.json' in civic_result:
    with open(civic_result, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_result

if isinstance(funding_result, str) and '.json' in funding_result:
    with open(funding_result, 'r') as f:
        funding = json.load(f)
else:
    funding = funding_result

# Build funding map
funding_map = {}
for item in funding:
    name = item['Project_Name']
    amount = int(item['Amount'])
    funding_map[name] = amount
    # Also store without parentheses
    clean_name = name.split('(')[0].strip()
    if clean_name != name:
        funding_map[clean_name] = funding_map.get(clean_name, 0) + amount

spring_2022_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.splitlines()
    
    for i in range(len(lines)):
        line = lines[i].strip()
        # Skip if too short or obvious header
        if len(line) < 10: continue
        if 'Page' in line or 'Agenda' in line or 'To:' in line: continue
        
        # Check for 2022 and spring months
        has_2022 = line.find('2022') >= 0
        has_spring = any(x in line for x in ['Spring', 'spring', 'March', 'April', 'May'])
        
        if has_2022 and has_spring:
            # Look back at previous lines for project name
            for j in range(max(0, i-8), i):
                prev_line = lines[j].strip()
                if len(prev_line) > 10 and prev_line[0].isupper():
                    if 'Page' not in prev_line and 'Agenda' not in prev_line and 'Subject' not in prev_line:
                        spring_2022_projects.add(prev_line)

# Match with funding
matched_projects = []
total_funding = 0

for project in spring_2022_projects:
    amount = 0
    # Direct match
    if project in funding_map:
        amount = funding_map[project]
    else:
        # Partial match
        for fund_name, fund_amount in funding_map.items():
            if project in fund_name or fund_name in project:
                amount = fund_amount
                break
    
    if amount > 0:
        matched_projects.append({'name': project, 'funding': amount})
        total_funding += amount

result = {
    'project_count': len(matched_projects),
    'total_funding': total_funding,
    'projects': matched_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.execute_python:8': {'civic_docs_count': 5, 'funding_records_count': 5, 'funding_sample': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:21': [{'total_records': '500'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:33': 'file_storage/functions.query_db:33.json'}

exec(code, env_args)
