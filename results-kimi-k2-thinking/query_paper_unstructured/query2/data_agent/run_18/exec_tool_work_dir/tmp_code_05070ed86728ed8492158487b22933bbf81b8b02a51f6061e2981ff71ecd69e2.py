code = """import json

# Get all available variables that start with var_
available_vars = [k for k in locals().keys() if k.startswith('var_')]
print('Available variables:', available_vars)

# If we have the citations data variable, try to use it
for var_name in available_vars:
    if 'query_db' in var_name and '20' in var_name:
        citations_data = locals()[var_name]
        print('Found citations data, type:', type(citations_data))
        if isinstance(citations_data, str) and citations_data.startswith('['):
            # It's a JSON string, parse it
            citations_data = json.loads(citations_data)
        print('Citations records:', len(citations_data))
        break

# Show what's in papers data variable
for var_name in available_vars:
    if 'query_db' in var_name and '22' in var_name:
        papers_data = locals()[var_name]
        print('Found papers data, type:', type(papers_data))
        break

result = {'status': 'checking_variables'}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
