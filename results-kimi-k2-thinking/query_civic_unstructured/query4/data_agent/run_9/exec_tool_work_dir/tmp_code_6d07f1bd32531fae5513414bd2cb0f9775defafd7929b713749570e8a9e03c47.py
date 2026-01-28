code = """import json
import re

# Load data
civic_docs_file = locals()['var_functions.query_db:32']
if isinstance(civic_docs_file, str) and civic_docs_file.endswith('.json'):
    with open(civic_docs_file, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_docs_file

funding_file = locals()['var_functions.query_db:33']
if isinstance(funding_file, str) and funding_file.endswith('.json'):
    with open(funding_file, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = funding_file

# Find Spring 2022 projects
docs_with_spring_2022 = []
for doc in civic_docs:
    text = doc.get('text', '')
    if '2022' in text and ('Spring' in text or 'spring' in text or 'March' in text or 'April' in text or 'May' in text):
        docs_with_spring_2022.append(doc)

project_names = []
for doc in docs_with_spring_2022:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        # Look for lines that might be project names (not headers)
        line = line.strip()
        if len(line) > 10 and line[0].isupper():
            if not any(skip in line for skip in ['Agenda', 'Page', 'RECOMMENDED', 'DISCUSSION:', 'To:', 'Prepared by:']):
                # Check if 2022 appears within next few lines
                next_text = ' '.join(lines[i:i+10])
                if '2022' in next_text and any(season in next_text for season in ['Spring', 'spring', 'March', 'April', 'May']):
                    project_names.append(line)

# Get unique projects
unique_projects = list(set(project_names))

# Match with funding
funding_dict = {}
for fund in funding_data:
    name = fund.get('Project_Name', '')
    amount = int(fund.get('Amount', 0))
    funding_dict[name] = amount

# Try to find funding matches
matched_projects = []
total_funding = 0

for project in unique_projects[:50]:  # Limit to avoid timeout
    found_funding = False
    for fund_name, amount in funding_dict.items():
        # Simple matching: if project name is part of funding name or vice versa
        if project in fund_name or fund_name in project:
            matched_projects.append({
                'project': project,
                'funding': fund_name,
                'amount': amount
            })
            total_funding += amount
            found_funding = True
            break
    
    if not found_funding:
        matched_projects.append({
            'project': project,
            'funding': None,
            'amount': 0
        })

result = {
    'total_projects_found': len(unique_projects),
    'projects_with_funding': len([p for p in matched_projects if p['amount'] > 0]),
    'total_funding': total_funding,
    'sample_projects': matched_projects[:10]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.execute_python:8': {'civic_docs_count': 5, 'funding_records_count': 5, 'funding_sample': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:21': [{'total_records': '500'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:33': 'file_storage/functions.query_db:33.json'}

exec(code, env_args)
