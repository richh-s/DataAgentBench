code = """import json

# Check what type of data we have
result_data = var_functions.query_db:5
print('__RESULT__:')
print(json.dumps({
    'type': str(type(result_data)),
    'is_string': isinstance(result_data, str),
    'preview': str(result_data)[:200] if isinstance(result_data, str) else 'Not a string'
}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:2': ['commits', 'contents', 'files'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
