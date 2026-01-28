code = """# Check what variables we have
import os
print('__RESULT__:')
print('variables_available:', list(locals().keys()))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
