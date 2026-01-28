code = """import json
import os

# Try to read the funding data first to see what we have
funding_result_key = 'var_functions.query_db:12'
result = locals().get('var_functions.query_db:12')

print('__RESULT__:')
print(json.dumps(str(result)[:100]))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': 'Loaded 5 civic docs and 500 funding records', 'var_functions.list_db:24': ['civic_docs']}

exec(code, env_args)
