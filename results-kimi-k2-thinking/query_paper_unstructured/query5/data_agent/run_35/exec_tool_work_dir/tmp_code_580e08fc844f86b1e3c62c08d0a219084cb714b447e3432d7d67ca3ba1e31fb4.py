code = """import json
import re

# Check what variables are available
all_vars = list(locals().keys())
print('__RESULT__:')
print(json.dumps({'available_vars': all_vars}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
