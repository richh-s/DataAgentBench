code = """# Check what variables are available in the environment
import sys
print('__RESULT__:')
print(list(locals().keys()))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
