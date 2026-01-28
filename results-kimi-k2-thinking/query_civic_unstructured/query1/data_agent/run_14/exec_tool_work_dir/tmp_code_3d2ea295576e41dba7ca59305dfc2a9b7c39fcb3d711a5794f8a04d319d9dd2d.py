code = """import json
import re

# Check what variables are available
available_vars = [key for key in globals().keys() if key.startswith('var_')]
print("__RESULT__:")
print(json.dumps(available_vars))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
