code = """import json, os

# Check available variables
for name in list(globals().keys()):
    if name.startswith('var_'):
        print(name)

# Check if the variables contain file paths or data
try:
    civic_var = globals()['var_functions.query_db:0']
    print('\nCivic docs variable type:', type(civic_var))
    print('Civic docs variable content (first 200 chars):', str(civic_var)[:200])
except:
    print('\nvar_functions.query_db:0 not found')

try:
    funding_var = globals()['var_functions.query_db:5']
    print('\nFunding variable type:', type(funding_var))
    print('Funding variable content (first 200 chars):', str(funding_var)[:200])
except:
    print('\nvar_functions.query_db:5 not found')

print('\n__RESULT__:', json.dumps({'status':'checked'}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
