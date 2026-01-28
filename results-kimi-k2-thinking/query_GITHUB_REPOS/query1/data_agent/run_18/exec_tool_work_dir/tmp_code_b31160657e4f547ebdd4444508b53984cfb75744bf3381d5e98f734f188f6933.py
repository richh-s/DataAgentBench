code = """db_tables = var_functions.list_db:0
print('__RESULT__:')
print(db_tables)"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses']}

exec(code, env_args)
