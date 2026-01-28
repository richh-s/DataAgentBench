code = """import json

# Check what's in the variable
result = var_functions.query_db:5
print('Type:', type(result))
print('Value preview:', str(result)[:200])

# If it's a file path, load it
if isinstance(result, str) and ('.json' in result or '/' in result or '\\' in result):
    print('Detected as file path, loading...')
    with open(result, 'r') as f:
        data = json.load(f)
    print('Loaded data, type:', type(data))
    print('Length:', len(data))
    print('First item preview:', str(data[0])[:300])
else:
    print('Not a file path, using directly')
    data = result
    print('Data type:', type(data))
    if isinstance(data, list):
        print('Length:', len(data))
        if len(data) > 0:
            print('First item preview:', str(data[0])[:300])"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['cpc_definition'], 'var_functions.query_db:8': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}]}

exec(code, env_args)
