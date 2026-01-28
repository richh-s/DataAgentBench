code = """# Let's check what variables are available in locals()
import json
import os

# Check available variables
available_vars = [k for k in locals().keys() if k.startswith('var_')]
print('__RESULT__:')
print(json.dumps(f"Available variables: {available_vars}"))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
