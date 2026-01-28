code = """import json
import re

# Load data
f_path = locals()['var_functions.query_db:2']
c_path = locals()['var_functions.query_db:3']

with open(f_path, 'r') as f:
    funding = json.load(f)

with open(c_path, 'r') as f:
    civic = json.load(f)

# Build funding dict
funding_dict = {}
for item in funding:
    name = item['Project_Name'].upper().strip()
    amount = int(item['Amount'])
    funding_dict[name] = amount

# Find completed park projects in 2022
park_projects = []

for doc in civic:
    text = doc.get('text', '')
    if '2022' in text:
        lines = text.split('\n')
        for i in range(len(lines)):
            line = lines[i].lower()
            if 'completed' in line or 'completion' in line:
                # Look around this line for park project names
                for j in range(max(0, i-6), min(len(lines), i+6)):
                    proj_line = lines[j].strip()
                    if proj_line and 'park' in proj_line.lower() and len(proj_line) < 150:
                        if proj_line not in park_projects:
                            park_projects.append(proj_line)

# Match with funding
total = 0
matched = []

for proj in park_projects:
    proj_upper = proj.upper()
    if proj_upper in funding_dict:
        amount = funding_dict[proj_upper]
        total += amount
        matched.append([proj, amount])

result = {
    'total_funding': total,
    'project_count': len(matched),
    'projects': [{'name': m[0], 'amount': m[1]} for m in matched]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.execute_python:10': {'funding_count': 500, 'civic_count': 5, 'funding_sample': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}], 'civic_sample': [{'filename': 'malibucity_agenda_03222023-2060.txt', 'text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil E'}, {'filename': 'malibucity_agenda__01262022-1835.txt', 'text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n10-27-21\nItem\n4.A.\n\nTo:\n\nChair Simmens and Members of the Public Works Commission\n\nPrepared by:\n\nTroy Spayd, Assistant Public Wor'}]}}

exec(code, env_args)
