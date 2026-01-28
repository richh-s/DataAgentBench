code = """import json

funding_var = locals()['var_functions.query_db:2']
docs_var = locals()['var_functions.query_db:0']

print('__RESULT__:')
print(json.dumps({'funding_type': str(type(funding_var)), 'docs_type': str(type(docs_var))}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
