code = """import json, re

# Load the data from the JSON files
with open('/tmp/tmp2p5k0y06.json') as f:
    funding_records = json.load(f)

with open('/tmp/tmpt3w8k1q3.json') as f:
    civic_docs = json.load(f)

# Build funding lookup for projects > $50k
funding_lookup = {}
for rec in funding_records:
    try:
        amount = int(rec['Amount'])
        funding_lookup[rec['Project_Name']] = amount
    except:
        continue

print('Funding projects count:', len(funding_lookup))
print('Civic docs count:', len(civic_docs))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:50': {'test': 'test'}, 'var_functions.query_db:56': 'file_storage/functions.query_db:56.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:62': 'file_storage/functions.query_db:62.json'}

exec(code, env_args)
