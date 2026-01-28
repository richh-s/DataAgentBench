code = """import json

# Check what variables are available in locals()
all_vars = list(locals().keys())
print('All local variables:', all_vars[:20])  # Show first 20

# Look for variables that contain our query results
query_vars = [v for v in all_vars if 'query_db' in str(v)]
print('Query-related variables:', query_vars)

# Try to find the citations and papers data
for var_name in all_vars:
    if '20' in str(var_name) or 'citation' in str(var_name).lower():
        try:
            data = locals()[var_name]
            print(f'Potential citations data in {var_name}:', type(data))
            if isinstance(data, str) and len(data) > 100:
                print('Data preview:', data[:100])
        except:
            pass

result = {'status': 'variable_check_complete'}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:28': {'status': 'checking_variables'}}

exec(code, env_args)
