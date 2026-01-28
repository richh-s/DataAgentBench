code = """import json

# Check what variables are available
available_vars = [k for k in locals().keys() if k.startswith('var_')]
print('Available variables:', available_vars)

# Access the query result file path
result_file = locals()['var_functions.query_db:5']
print('Result file path:', result_file[:100] if isinstance(result_file, str) else str(result_file)[:100])"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
