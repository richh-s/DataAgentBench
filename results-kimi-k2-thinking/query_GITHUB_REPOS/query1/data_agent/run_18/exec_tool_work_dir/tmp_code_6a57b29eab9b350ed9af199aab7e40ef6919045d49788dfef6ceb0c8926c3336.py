code = """import json
tables = locals()['var_functions.list_db:0']
print('__RESULT__:')
print(json.dumps(tables))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses']}

exec(code, env_args)
