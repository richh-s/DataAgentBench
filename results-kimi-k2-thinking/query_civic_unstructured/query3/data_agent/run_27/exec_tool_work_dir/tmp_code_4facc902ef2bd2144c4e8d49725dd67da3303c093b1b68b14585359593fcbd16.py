code = """# Retrieve list_db result
list_result = locals().get('var_functions.list_db:0')
print('__RESULT__:')
print(list_result)"""

env_args = {'var_functions.list_db:0': ['civic_docs']}

exec(code, env_args)
