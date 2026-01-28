code = """import json
import re

# Load the data
civic_data = json.load(open('/tmp/tmp1.json'))
funding_data = json.load(open('/tmp/tmp2.json'))

# Build funding map
funding = {}
for f in funding_data:
    funding[f['Project_Name']] = int(f['Amount'])

# Find projects
projects = []
for doc in civic_data:
    txt = doc.get('text', '')
    for line in txt.split('\n'):
        if 'Spring 2022' in line or '2022-Spring' in line:
            projects.append(txt)

print('Projects found:', len(projects))
print('Funding records:', len(funding))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json'}

exec(code, env_args)
