code = """import json
import re

civic_file = locals()['var_functions.query_db:2']
funding_file = locals()['var_functions.query_db:6']

with open(civic_file) as f:
    civic_docs = json.load(f)

with open(funding_file) as f:
    funding_data = json.load(f)

# Find all disaster-related projects from funding
disaster_projects = []
for record in funding_data:
    name = record['Project_Name']
    if 'FEMA' in name or 'CalOES' in name or 'CalJPIA' in name:
        disaster_projects.append(record)

# Calculate total funding
total_funding = sum(int(p['Amount']) for p in disaster_projects)

# Build result
result = f"Total funding for disaster-related projects that started in 2022 is ${total_funding:,}"

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:22': 'Total: $1,410,000'}

exec(code, env_args)
