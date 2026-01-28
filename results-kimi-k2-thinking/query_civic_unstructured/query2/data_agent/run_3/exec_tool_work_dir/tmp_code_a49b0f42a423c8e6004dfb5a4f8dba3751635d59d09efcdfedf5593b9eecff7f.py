code = """import json
import re

# Load the data
funding_path = locals()['var_functions.query_db:2']
civic_path = locals()['var_functions.query_db:3']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_path, 'r') as f:
    civic_data = json.load(f)

# Create funding lookup dictionary
funding_dict = {}
for item in funding_data:
    name = item['Project_Name'].upper().strip()
    amount = int(item['Amount'])
    funding_dict[name] = amount

# Extract completed park projects in 2022
completed_park_projects = []

for doc in civic_data:
    text = doc.get('text', '')
    # Simple heuristic: find lines mentioning both completion and 2022
    # and check nearby text for park references
    
    for i, line in enumerate(text.split('\n')):
        line_lower = line.lower()
        if 'completed' in line_lower and '2022' in line:
            # Look back up to 5 lines for project name
            lines = text.split('\n')
            for j in range(max(0, i-5), i):
                candidate = lines[j].strip()
                if candidate and len(candidate) > 5 and ('park' in candidate.lower() or 'Park' in candidate):
                    completed_park_projects.append(candidate)
                    break

# Remove duplicates
completed_park_projects = list(set(completed_park_projects))

# Match with funding
total_funding = 0
matched_projects = []

for project_name in completed_park_projects:
    proj_upper = project_name.upper().strip()
    
    # Direct match
    if proj_upper in funding_dict:
        amount = funding_dict[proj_upper]
        total_funding += amount
        matched_projects.append({'name': project_name, 'amount': amount})
    else:
        # Partial match
        for funded_name, amount in funding_dict.items():
            if proj_upper in funded_name or funded_name in proj_upper:
                total_funding += amount
                matched_projects.append({'name': project_name, 'funded_as': funded_name, 'amount': amount})
                break

# Prepare result
result = {
    'total_funding': total_funding,
    'project_count': len(matched_projects),
    'projects': matched_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.execute_python:10': {'funding_count': 500, 'civic_count': 5, 'funding_sample': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}], 'civic_sample': [{'filename': 'malibucity_agenda_03222023-2060.txt', 'text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil E'}, {'filename': 'malibucity_agenda__01262022-1835.txt', 'text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n10-27-21\nItem\n4.A.\n\nTo:\n\nChair Simmens and Members of the Public Works Commission\n\nPrepared by:\n\nTroy Spayd, Assistant Public Wor'}]}}

exec(code, env_args)
