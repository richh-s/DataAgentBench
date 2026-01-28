code = """import json

# Check what variables are available
available = [k for k in locals().keys() if 'query_db' in str(k)]
result = {'available_vars': available}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': {'paper_docs_count': 5, 'citations_count': 1405}}

exec(code, env_args)
