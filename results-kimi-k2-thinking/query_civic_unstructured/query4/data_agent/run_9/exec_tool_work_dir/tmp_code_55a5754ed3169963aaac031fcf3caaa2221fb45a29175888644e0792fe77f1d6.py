code = """import json
import re

# Load data
civic_docs = locals()['var_functions.query_db:32']
funding_data = locals()['var_functions.query_db:33']

if isinstance(civic_docs, str) and civic_docs.endswith('.json'):
    with open(civic_docs, 'r') as f:
        civic_docs = json.load(f)

if isinstance(funding_data, str) and funding_data.endswith('.json'):
    with open(funding_data, 'r') as f:
        funding_data = json.load(f)

# Build funding lookup
funding_lookup = {}
for record in funding_data:
    name = record['Project_Name']
    amount = int(record['Amount'])
    funding_lookup[name] = amount
    
    base_name = name.split('(')[0].strip()
    if base_name != name:
        funding_lookup[base_name] = funding_lookup.get(base_name, 0) + amount

# Find Spring 2022 projects
spring_projects = []
project_set = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find sections with Spring 2022
    for line in text.split('\n'):
        if '2022' in line and any(season in line for season in ['Spring', 'spring', 'March', 'April', 'May']):
            # Look for project names before this line
            idx = text.find(line)
            preceding_text = text[max(0, idx-500):idx]
            
            # Extract capitalized project names from preceding text
            for match in re.finditer(r'\n([A-Z][a-zA-Z &\-]+)', preceding_text):
                project_name = match.group(1).strip()
                if len(project_name) > 10 and project_name not in project_set:
                    if not any(pattern in project_name for pattern in ['Agenda', 'Page', 'To:', 'From:', 'Prepared', 'Approved']):
                        spring_projects.append(project_name)
                        project_set.add(project_name)

# Match with funding and calculate totals
matched = []
total_funding = 0

for project in spring_projects:
    found = False
    for fund_name, amount in funding_lookup.items():
        if project in fund_name or fund_name in project:
            if len(project) > 15:
                matched.append({'project': project, 'amount': amount})
                total_funding += amount
                found = True
                break
    
    if not found and project in funding_lookup:
        amount = funding_lookup[project]
        matched.append({'project': project, 'amount': amount})
        total_funding += amount

result = {
    'count': len(matched),
    'total_funding': total_funding,
    'projects': matched
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.execute_python:8': {'civic_docs_count': 5, 'funding_records_count': 5, 'funding_sample': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:21': [{'total_records': '500'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:33': 'file_storage/functions.query_db:33.json'}

exec(code, env_args)
