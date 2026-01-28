code = """# Check what variables are available in the storage
import json
print('__RESULT__:')
print(json.dumps(list(locals().keys())))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
