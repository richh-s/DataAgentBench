code = """full_result = var_functions.list_db:0
print('__RESULT__:')
print(full_result)"""

env_args = {'var_functions.list_db:0': ['checkin', 'business']}

exec(code, env_args)
