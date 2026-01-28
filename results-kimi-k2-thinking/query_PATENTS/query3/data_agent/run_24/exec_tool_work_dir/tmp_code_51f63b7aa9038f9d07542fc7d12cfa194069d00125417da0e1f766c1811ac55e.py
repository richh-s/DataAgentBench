code = """import json

# Let's check if the variable is available as a string path
result_var = locals().get('var_functions.query_db:2')
print('----BEGIN PRINT FORMAT----')
print('__RESULT__:')
print(json.dumps({
    'var_type': str(type(result_var)),
    'var_value': str(result_var)[:200] if result_var else None,
    'available_keys': list(locals().keys())[:20]
}))
print('----END PRINT FORMAT----')"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition']}

exec(code, env_args)
