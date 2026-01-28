code = """import json
import re

# Load funding data
f_key = 'var_functions.query_db:6'
f_data = locals()[f_key]
if type(f_data) is str and f_data.endswith('.json'):
    with open(f_data, 'r') as f:
        f_data = json.load(f)

# Load civic docs data
c_key = 'var_functions.query_db:8'
c_data = locals()[c_key]
if type(c_data) is str and c_data.endswith('.json'):
    with open(c_data, 'r') as f:
        c_data = json.load(f)

# Build funding dictionary
f_dict = {}
for item in f_data:
    f_dict[item['Project_Name']] = int(item['Amount'])

# Find disaster projects from 2022
disaster_2022_projects = set()
for doc in c_data:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if line and (line.find('(FEMA') >= 0 or line.find('(CalOES') >= 0 or line.find('(CalJPIA') >= 0):
            # Check surrounding context for 2022
            context = '\n'.join(lines[max(0,i-5):min(len(lines),i+15)])
            if context.find('2022') >= 0:
                disaster_2022_projects.add(line)

# Calculate total funding
total = 0
for project in disaster_2022_projects:
    if project in f_dict:
        total += f_dict[project]
    else:
        # Try to match base name (without parentheses)
        base_match = re.search(r'^(.+?)\s*\([^)]*\)', project)
        if base_match:
            base_name = base_match.group(1)
            for funded in f_dict:
                if funded.find(base_name) >= 0 or base_name.find(funded) >= 0:
                    total += f_dict[funded]
                    break

result = {"total_funding": total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
