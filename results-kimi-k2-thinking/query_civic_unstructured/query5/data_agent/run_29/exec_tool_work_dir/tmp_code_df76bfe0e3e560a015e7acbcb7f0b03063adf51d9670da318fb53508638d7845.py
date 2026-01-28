code = """import json
import re

civic_docs = locals()['var_functions.query_db:2']
funding_records = locals()['var_functions.query_db:5']

# Build funding dictionary
funding_dict = {}
for record in funding_records:
    name = record.get('Project_Name', '').lower()
    amount = int(record.get('Amount', 0))
    if name and amount > 0:
        funding_dict[name] = amount

# Find all disaster project names
all_disaster_names = []
for doc in civic_docs:
    text = doc.get('text', '')
    for line in text.split('\n'):
        line = line.strip()
        if len(line) > 5:
            lower_line = line.lower()
            if 'fema' in lower_line or 'caljpia' in lower_line or 'caloes' in lower_line:
                all_disaster_names.append(line)

# Filter for unique names and check for 2022
unique_disaster = list(set(all_disaster_names))
disaster_2022 = []

for proj_name in unique_disaster:
    for doc in civic_docs:
        text = doc.get('text', '')
        if proj_name in text and '2022' in text:
            disaster_2022.append(proj_name)
            break

# Match with funding
total = 0
matches = []

for proj in disaster_2022:
    proj_lower = proj.lower()
    if proj_lower in funding_dict:
        amount = funding_dict[proj_lower]
        total += amount
        matches.append({'project': proj, 'amount': amount})

result = json.dumps({'total_funding': total, 'projects': matches, 'count': len(disaster_2022)})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
