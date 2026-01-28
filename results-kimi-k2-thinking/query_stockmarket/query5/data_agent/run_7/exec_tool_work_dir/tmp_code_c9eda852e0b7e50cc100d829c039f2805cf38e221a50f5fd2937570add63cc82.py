code = """import json, os
f1 = str(locals()['var_functions.query_db:0'])
f2 = str(locals()['var_functions.list_db:2'])
print('__RESULT__:') 
print(json.dumps({'p1': f1, 'p2': f2}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json'}

exec(code, env_args)
