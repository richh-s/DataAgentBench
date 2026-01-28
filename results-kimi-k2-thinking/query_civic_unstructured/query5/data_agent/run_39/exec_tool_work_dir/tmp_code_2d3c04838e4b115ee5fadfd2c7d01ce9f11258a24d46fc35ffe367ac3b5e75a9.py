code = """import json

# Access the results from storage
funding_result = var_functions.query_db:2
civic_result = var_functions.query_db:6

# Load the JSON data from files
with open(funding_result, 'r') as f:
    funding_data = json.load(f)

with open(civic_result, 'r') as f:
    civic_docs = json.load(f)

print('Data loaded successfully')
print(f'Funding records: {len(funding_data)}')
print(f'Civic documents: {len(civic_docs)}')"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
