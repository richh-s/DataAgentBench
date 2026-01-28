code = """import json

funding_var = locals()['var_functions.query_db:2']
docs_var = locals()['var_functions.query_db:0']

print('Type of funding_var:', type(funding_var))
print('Type of docs_var:', type(docs_var))

# Check if they're lists or file paths
if isinstance(funding_var, str):
    print('Funding data is a file path string')
else:
    print('Funding data is a list with', len(funding_var), 'records')

if isinstance(docs_var, str):
    print('Docs data is a file path string')
else:
    print('Docs data is a list with', len(docs_var), 'documents')"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
