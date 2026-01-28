code = """import json, os

# Access the stored result
civic_docs_data = locals().get('var_functions.query_db:2')

print('Type:', type(civic_docs_data))
if civic_docs_data:
    if isinstance(civic_docs_data, list):
        print('Length:', len(civic_docs_data))
        if civic_docs_data:
            print('Sample keys:', list(civic_docs_data[0].keys())[:5])
    elif isinstance(civic_docs_data, str):
        print('String length:', len(civic_docs_data))
        print('Preview:', civic_docs_data[:200])

result = {'check': 'complete'}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': {'status': 'error', 'message': "[Errno 2] No such file or directory: '/tmp/tmpub7z9f6a.json'"}, 'var_functions.execute_python:14': {'available_vars': ['var_functions.query_db:2', 'var_functions.query_db:5']}, 'var_functions.execute_python:18': {'step': 'inspection'}}

exec(code, env_args)
