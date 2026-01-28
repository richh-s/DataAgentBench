code = """import json

# Get data from storage and check what they are
civic_result = locals()['var_functions.query_db:64']
funding_result = locals()['var_functions.query_db:10']

print('DEBUG: Civic docs result type:', type(civic_result))
print('DEBUG: Funding result type:', type(funding_result))
print('DEBUG: Civic docs length:', len(civic_result))
print('DEBUG: Funding length:', len(funding_result))

# If they're file paths, load them
if isinstance(civic_result, str) and civic_result.endswith('.json'):
    with open(civic_result, 'r') as f:
        civic_data = json.load(f)
    print('DEBUG: Loaded civic docs, type:', type(civic_data))
    print('DEBUG: Sample civic doc:', json.dumps(civic_data[0])[:100])

if isinstance(funding_result, str) and funding_result.endswith('.json'):
    with open(funding_result, 'r') as f:
        funding_data = json.load(f)
    print('DEBUG: Loaded funding, type:', type(funding_data))
    print('DEBUG: Sample funding:', json.dumps(funding_data[0]))

print('__RESULT__:')
print(json.dumps({'status': 'type_check_complete'}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.list_db:42': ['civic_docs'], 'var_functions.execute_python:52': {'debug': 'done'}, 'var_functions.execute_python:54': {'status': 'debug'}, 'var_functions.execute_python:58': {'status': 'debug_info_recorded'}, 'var_functions.execute_python:62': {'debug': 'path_identification'}, 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json'}

exec(code, env_args)
