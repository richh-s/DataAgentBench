code = """import json, re, os

# Load data from the file paths provided in storage
civic_docs_path = locals()['var_functions.query_db:16']
funding_path = locals()['var_functions.query_db:17']

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

print('Loaded files successfully')

# Find all park-related projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i]
        # Check for completion date in 2022
        if '2022' in line and ('completed' in line.lower() or 'completion' in line.lower()):
            # Look for project name in nearby lines
            for j in range(max(0, i-5), min(len(lines), i+5)):
                project_line = lines[j].strip()
                if project_line and 'park' in project_line.lower() and len(project_line) > 5:
                    # Clean the project name
                    clean_name = project_line.replace('•', '').replace('◦', '').strip()
                    clean_name = re.sub(r'^[A-Z]\.?\s+', '', clean_name)
                    if clean_name and clean_name not in park_projects:
                        park_projects.append(clean_name)
                        break

print('Found park projects completed in 2022:', len(park_projects))

# Calculate total funding
total_funding = 0
for park in park_projects:
    park_simple = park.lower().replace(' ', '').replace('-', '')
    for fund in funding_data:
        fund_simple = fund['Project_Name'].lower().replace(' ', '').replace('-', '')
        if park_simple in fund_simple or fund_simple in park_simple:
            total_funding += int(fund['Amount'])
            break

result = {'total_funding_dollars': total_funding, 'project_count': len(park_projects)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json', 'var_functions.execute_python:56': {'test': 'success'}, 'var_functions.execute_python:66': {'status': 'success', 'docs_loaded': 5}, 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json'}

exec(code, env_args)
