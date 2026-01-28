code = """import json
# The variable should be accessible directly
# Let's just try to see what variables are available
import sys
print('__RESULT__:')
print(json.dumps(str(list(locals().keys())[:10])))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
