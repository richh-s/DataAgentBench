code = """import json, pandas as pd

a = var_functions.query_db:0
m = var_functions.query_db:2

print('__RESULT__:')
print('Articles type:', type(a))
print('Metadata type:', type(m))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
