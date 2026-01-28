code = """import json

funding_path = var_functions.query_db:6
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

civic_path = var_functions.query_db:5
with open(civic_path, 'r') as f:
    civic_data = json.load(f)

funding_projects = set(record['Project_Name'] for record in funding_data if int(record['Amount']) > 50000)

print('Funding projects count:', len(funding_projects))
print('__RESULT__:')
print(str(len(funding_projects)))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
