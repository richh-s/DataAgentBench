code = """import json, os, re

# Load data
funding_path = locals()['var_functions.query_db:12']
civic_path = locals()['var_functions.query_db:14']

with open(funding_path) as f:
    funding = json.load(f)

with open(civic_path) as f:
    civic_docs = json.load(f)

# Find all disaster-related projects (FEMA/CalOES/CalJPIA)
disaster_funding = []
for rec in funding:
    name = rec['Project_Name'].lower()
    if '(fema' in name or '(caloes' in name or '(caljpia' in name:
        disaster_funding.append(int(rec['Amount']))

# Check if civic documents mention 2022 and disaster
has_2022_disaster = False
for doc in civic_docs:
    text = doc['text']
    if '2022' in text and ('FEMA' in text or 'CalOES' in text or 'fire' in text.lower()):
        has_2022_disaster = True
        break

# If we found 2022 disaster projects, sum all disaster funding
total_funding = sum(disaster_funding) if has_2022_disaster and disaster_funding else 0

print('__RESULT__:')
print(json.dumps({'total_funding': total_funding}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:9': {'success': True, 'num_docs': 5}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'funding_total': 500, 'civic_docs_total': 5, 'disaster_funding_count': 27}}

exec(code, env_args)
