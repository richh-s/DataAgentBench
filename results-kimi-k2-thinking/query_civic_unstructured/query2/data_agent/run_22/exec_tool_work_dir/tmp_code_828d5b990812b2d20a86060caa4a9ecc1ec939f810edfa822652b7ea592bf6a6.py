code = """import json
# Try to access the query results directly from variables
civic_docs = json.loads(var_functions.query_db_32)

print('__RESULT__:')
print(json.dumps({'count': len(civic_docs)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:56': [], 'var_functions.execute_python:60': {'has_civic_file': False, 'has_funding_file': False}}

exec(code, env_args)
