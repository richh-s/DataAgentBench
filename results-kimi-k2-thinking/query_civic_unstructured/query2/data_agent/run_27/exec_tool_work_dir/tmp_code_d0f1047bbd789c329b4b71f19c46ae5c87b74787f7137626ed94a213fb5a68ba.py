code = """import json, re

# Load data files
civic_docs_path = locals()['var_functions.query_db:16']
funding_path = locals()['var_functions.query_db:17']

with open(civic_docs_path) as f:
    civic_docs = json.load(f)
with open(funding_path) as f:
    funding_data = json.load(f)

print('Loaded files')

# Find park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc['text']
    
    # Split into lines
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i]
        # Check for 2022 completion
        if '2022' in line and ('completed' in line.lower() or 'completion' in line.lower()):
            # Look for park names in context
            for j in range(max(0,i-5), min(len(lines), i+5)):
                context = lines[j].strip()
                if 'park' in context.lower() and len(context) > 5:
                    # Clean name
                    clean = context.replace('•','').replace('◦','').strip()
                    if clean not in park_projects:
                        park_projects.append(clean)

print('Park projects:', len(park_projects))

# Calculate funding
total = 0
for park in park_projects:
    park_key = park.lower().replace(' ', '')
    for fund in funding_data:
        fund_key = fund['Project_Name'].lower().replace(' ', '')
        if park_key in fund_key or fund_key in park_key:
            total += int(fund['Amount'])

result = {'total_funding': total}
print('__RESULT__:', json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json'}

exec(code, env_args)
