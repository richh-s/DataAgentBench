code = """import json

# The result is stored as a file path string
result_var = locals().get('var_functions.query_db:2')
print('----BEGIN PRINT FORMAT----')
print('__RESULT__:')
print(json.dumps(str(result_var)))
print('----END PRINT FORMAT----')"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition']}

exec(code, env_args)
