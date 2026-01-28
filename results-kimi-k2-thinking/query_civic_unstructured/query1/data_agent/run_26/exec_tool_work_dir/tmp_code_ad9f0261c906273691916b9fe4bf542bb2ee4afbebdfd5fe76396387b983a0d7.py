code = """import json

# Open the files
with open('var_functions.query_db:0') as f:
    funding = json.load(f)

with open('var_functions.query_db:2') as f:
    docs = json.load(f)

# Build funding lookup
funded = {}
for rec in funding:
    funded[rec['Project_Name'].lower()] = int(rec['Amount'])

# For now, just count funding records > 50000 that have 'design' in some form
# This is a simplified approximation
count = 0
for rec in funding:
    if int(rec['Amount']) > 50000:
        name = rec['Project_Name'].lower()
        if 'design' in name:
            count += 1

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_records': 276, 'civic_docs': 5}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:54': 0, 'var_functions.execute_python:72': {'funding': 'var_functions.query_db:0', 'civic': 'var_functions.query_db:2'}}

exec(code, env_args)
