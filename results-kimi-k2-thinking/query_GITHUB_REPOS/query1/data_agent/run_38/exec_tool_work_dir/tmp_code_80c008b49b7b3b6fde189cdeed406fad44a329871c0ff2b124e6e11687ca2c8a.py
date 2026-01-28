code = """import json

# List tables from previous result
tables = locals()['var_functions.list_db:0']
print('tables found:', tables)"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses']}

exec(code, env_args)
