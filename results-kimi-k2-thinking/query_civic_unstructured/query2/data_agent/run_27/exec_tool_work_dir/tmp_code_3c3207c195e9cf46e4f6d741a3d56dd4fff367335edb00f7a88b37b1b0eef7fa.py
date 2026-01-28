code = """import json, re

# Get stored file paths
civic_path = locals()['var_functions.query_db:16']
funding_path = locals()['var_functions.query_db:17']

# Load the data
civic_docs = json.loads(open(civic_path).read())
funding_records = json.loads(open(funding_path).read())

print('Loaded {0} documents and {1} funding records'.format(len(civic_docs), len(funding_records)))

# Find park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i]
        if '2022' in line and ('completed' in line.lower() or 'completion' in line.lower()):
            # Look for park name
            for j in range(max(0, i-5), min(len(lines), i+5)):
                nearby = lines[j].strip()
                if nearby and 'park' in nearby.lower() and len(nearby) > 5:
                    clean_name = nearby.replace('•', '').replace('◦', '').strip()
                    if clean_name not in park_projects:
                        park_projects.append(clean_name)

print('Found {0} park projects completed in 2022'.format(len(park_projects)))

# Calculate total funding
total = 0
for park in park_projects:
    park_key = park.lower().replace(' ', '').replace('-', '')
    for fund in funding_records:
        fund_key = fund['Project_Name'].lower().replace(' ', '').replace('-', '')
        if park_key in fund_key or fund_key in park_key:
            total += int(fund['Amount'])
            break

result = {'total_funding_dollars': total, 'project_count': len(park_projects)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json', 'var_functions.execute_python:56': {'test': 'success'}, 'var_functions.execute_python:66': {'status': 'success', 'docs_loaded': 5}, 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json'}

exec(code, env_args)
