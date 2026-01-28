code = """import json
import pandas as pd

# Check what variables are available
available_vars = [name for name in locals().keys() if name.startswith('var_')]
print('__RESULT__:')
print(json.dumps({'available_vars': available_vars, 'storage_keys': list(locals().keys())}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json'}

exec(code, env_args)
