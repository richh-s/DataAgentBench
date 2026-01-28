code = """import json, os

# Load the funding data from the stored file
funding_path = locals().get('var_functions.query_db:14')
print('Funding data path:', funding_path)

if isinstance(funding_path, str) and funding_path.endswith('.json'):
    with open(funding_path, 'r') as f:
        funding_data = json.load(f)
else:
    # Fallback for when data is directly in the variable
    funding_data = locals().get('var_functions.query_db:14', [])

print('Number of funding records:', len(funding_data))
print('Sample funding entries:')
for i in range(min(3, len(funding_data))):
    print(funding_data[i])
print('\n')

# Load civic documents data
civic_path = locals().get('var_functions.query_db:8')
print('Civic docs path:', civic_path)

if isinstance(civic_path, str) and civic_path.endswith('.json'):
    with open(civic_path, 'r') as f:
        civic_data = json.load(f)
else:
    civic_data = locals().get('var_functions.query_db:8', [])

print('Number of civic documents:', len(civic_data))
if civic_data:
    print('Sample civic document keys:', list(civic_data[0].keys()))
    print('First filename:', civic_data[0].get('filename'))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': ['civic_docs'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
