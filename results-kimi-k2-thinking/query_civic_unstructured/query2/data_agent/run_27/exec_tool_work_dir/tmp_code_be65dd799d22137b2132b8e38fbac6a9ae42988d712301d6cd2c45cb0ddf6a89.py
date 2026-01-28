code = """import json, re

civic_docs_path = locals()['var_functions.query_db:16']
funding_path = locals()['var_functions.query_db:17']

with open(civic_docs_path) as f:
    civic_docs = json.load(f)
with open(funding_path) as f:
    funding_data = json.load(f)

print('Loaded files')

# Find park projects completed in 2022
projects_found = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i]
        if '2022' in line and ('completed' in line.lower() or 'completion' in line.lower()):
            
            # Look for park names nearby
            for j in range(max(0,i-5), min(len(lines), i+5)):
                context_line = lines[j].strip()
                if 'park' in context_line.lower() and len(context_line) > 5:
                    clean_name = context_line.replace('•','').replace('◦','').strip()
                    clean_name = re.sub(r'^[A-Z]\s+', '', clean_name)
                    if clean_name not in projects_found:
                        projects_found.append(clean_name)

print('Park projects:', len(projects_found))

# Sum up funding amounts
total_funding = 0
for park in projects_found:
    park_key = park.lower().replace(' ', '').replace('-', '')
    for fund in funding_data:
        fund_key = fund['Project_Name'].lower().replace(' ', '').replace('-', '')
        if park_key in fund_key or fund_key in park_key:
            total_funding += int(fund['Amount'])
            break

result = {'total_funding_dollars': total_funding}
print('__RESULT__:', json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json', 'var_functions.execute_python:56': {'test': 'success'}}

exec(code, env_args)
