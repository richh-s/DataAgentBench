code = """import json
import re

# Load data
mongo_file = str(globals()['var_functions.query_db:5'])
funding_file = str(globals()['var_functions.query_db:20'])

with open(mongo_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Create funding map
funding_map = {}
for rec in funding_records:
    funding_map[rec['Project_Name'].strip()] = int(rec['Amount'])

# Find Spring 2022 projects
spring_2022_refs = []
for doc in civic_docs:
    text = doc.get('text', '')
    if '2022' in text and ('Spring' in text or 'spring' in text):
        # Extract relevant lines
        lines = text.split('\n')
        for line in lines:
            if '2022' in line and ('Spring' in line or 'spring' in line or 'Mar' in line or 'Apr' in line or 'May' in line):
                spring_2022_refs.append({'line': line, 'filename': doc.get('filename')})

# Match with funding
matched_projects = []
total_funding = 0

for ref in spring_2022_refs:
    # Check each funded project
    for fund_name, amount in funding_map.items():
        if fund_name in ref['line']:
            matched_projects.append({'name': fund_name, 'funding': amount})
            total_funding += amount
            break

result = {'project_count': len(matched_projects), 'total_funding': total_funding}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:14': ['Funding'], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:28': {'status': 'loaded', 'civic_docs': 5, 'funding_records': 500}}

exec(code, env_args)
