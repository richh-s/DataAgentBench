code = """# First check what variables we have access to
import sys
variables = dir()
print('Available variables:', [v for v in variables if not v.startswith('__')])

# Check if we can access the query result
if 'var_functions.query_db:5' in locals():
    print('Found query result variable')
    result_ref = locals()['var_functions.query_db:5']
    print('Type:', type(result_ref))
    print('Value (first 500 chars):', str(result_ref)[:500])"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
