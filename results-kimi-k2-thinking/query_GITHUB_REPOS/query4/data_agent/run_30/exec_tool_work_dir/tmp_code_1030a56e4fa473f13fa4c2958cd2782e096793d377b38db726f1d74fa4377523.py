code = """import json
import re

# Test accessing the variable
result = var_functions.query_db:0
print('__RESULT__:')
print(json.dumps({'type': str(type(result)), 'value': str(result)[:100]}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
