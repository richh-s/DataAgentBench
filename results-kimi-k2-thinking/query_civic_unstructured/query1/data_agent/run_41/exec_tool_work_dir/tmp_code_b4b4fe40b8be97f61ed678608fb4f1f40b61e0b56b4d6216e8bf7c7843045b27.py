code = """import json

funding_result = locals()['var_functions.query_db:32']
civic_key = 'var_functions.query_db:6'
civic_result = locals()[civic_key]

print('Funding result type:', type(funding_result))
print('Civic result type:', type(civic_result))

if isinstance(civic_result, str) and civic_result.endswith('.json'):
    with open(civic_result, 'r') as f:
        civic_data = json.load(f)
    print('Loaded civic data from file, records:', len(civic_data))
else:
    civic_data = civic_result
    print('Civic data is already loaded, records:', len(civic_data))

print('First document keys:', list(civic_data[0].keys()))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
