code = """import json, re

civic_docs_file = locals()['var_functions.query_db:2']
funding_file = locals()['var_functions.query_db:6']

with open(civic_docs_file) as f:
    civic_docs = json.load(f)

with open(funding_file) as f:
    funding_data = json.load(f)

# Find all disaster-related projects in funding data
disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA']
total_funding = 0

for record in funding_data:
    project_name = record.get('Project_Name', '')
    if any(keyword in project_name for keyword in disaster_keywords):
        amount = int(record.get('Amount', 0))
        total_funding += amount

print('__RESULT__:')
print(json.dumps(f'Total: ${total_funding:,}'))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
