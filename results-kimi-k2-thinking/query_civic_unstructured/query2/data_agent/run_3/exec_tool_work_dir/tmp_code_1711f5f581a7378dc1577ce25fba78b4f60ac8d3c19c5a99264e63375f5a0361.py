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

print('Found', len(funding_data), 'funding records')
print('Found', len(civic_data), 'civic documents')

# Extract completed park projects in 2022 from the text
completed_park_projects_2022 = []

for doc in civic_data:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or line.startswith('Page'):
            continue
            
        # Look for completion notices that mention 2022
        if 'completed' in line.lower() and '2022' in line:
            # Look backward for the project name (usually 2-5 lines back)
            for j in range(max(0, i-5), i):
                potential_name = lines[j].strip()
                if potential_name and len(potential_name) > 10:
                    # Check if it's park-related
                    if 'Park' in potential_name or 'park' in potential_name.lower():
                        completed_park_projects_2022.append({
                            'name': potential_name,
                            'context': line
                        })
                        break

print('\nFound', len(completed_park_projects_2022), 'park projects completed in 2022')
for p in completed_park_projects_2022:
    print('-', p['name'])

# Match with funding
matched = []
total = 0

for project in completed_park_projects_2022:
    proj_name = project['name'].upper().strip()
    
    # Direct match
    if proj_name in funding_dict:
        amount = funding_dict[proj_name]
        total += amount
        matched.append({'name': proj_name, 'amount': amount})
    else:
        # Try partial match (first 50 chars)
        proj_short = proj_name[:50]
        for funded_name, amount in funding_dict.items():
            if proj_short in funded_name or funded_name in proj_name:
                total += amount
                matched.append({'name': proj_name, 'matched': funded_name, 'amount': amount})
                break

print('\nMatched', len(matched), 'projects')
print('Total funding:', total)

result = {
    'total_funding_2022_park_completed': total,
    'matched_projects': matched,
    'count': len(matched)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.execute_python:10': {'funding_count': 500, 'civic_count': 5, 'funding_sample': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}], 'civic_sample': [{'filename': 'malibucity_agenda_03222023-2060.txt', 'text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil E'}, {'filename': 'malibucity_agenda__01262022-1835.txt', 'text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n10-27-21\nItem\n4.A.\n\nTo:\n\nChair Simmens and Members of the Public Works Commission\n\nPrepared by:\n\nTroy Spayd, Assistant Public Wor'}]}}

exec(code, env_args)
