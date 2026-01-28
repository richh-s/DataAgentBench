code = """import json
import re

f_file = var_functions.query_db:6
with open(f_file) as f:
    funding = json.load(f)

c_file = var_functions.query_db:4
with open(c_file) as f:
    docs = json.load(f)

funding_dict = {item['Project_Name']: int(item['Amount']) for item in funding}

park_projects = []
park_terms = ['park', 'playground', 'bluffs', 'trancas', 'skate', 'shade', 'walkway']

for doc in docs:
    lines = doc['text'].split('\n')
    for i in range(len(lines)):
        line = lines[i]
        line_lower = line.lower()
        if '2022' in line:
            if 'completed' in line_lower or 'completion' in line_lower:
                for j in range(i-1, max(i-4, -1), -1):
                    proj = lines[j].strip()
                    if not proj or proj.startswith('('):
                        continue
                    low = proj.lower()
                    skip_terms = ['updates:', 'schedule:', 'advertise:', 'construction:']
                    if any(x in low for x in skip_terms):
                        continue
                    if any(term in low for term in park_terms):
                        clean = re.sub(r'^\d+\.\s*', '', proj)
                        clean = re.sub(r'\s*Project Schedule.*', '', clean)
                        clean = clean.strip()
                        if clean and len(clean) > 5:
                            park_projects.append(clean)
                            break

park_projects = list(dict.fromkeys(park_projects))

matched = []
total = 0

for proj in park_projects:
    if proj in funding_dict:
        amount = funding_dict[proj]
        matched.append({'project_name': proj, 'amount': amount})
        total += amount
    else:
        for funded, amount in funding_dict.items():
            if funded.lower() in proj.lower() or proj.lower() in funded.lower():
                matched.append({'project_name': funded, 'amount': amount})
                total += amount
                break

result = {'total_funding': total, 'matched_projects': matched, 'park_projects': park_projects}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
