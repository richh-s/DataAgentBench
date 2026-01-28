code = """import json
import re

# Access the storage variables
funding_result_key = 'var_functions.query_db:6'
civic_result_key = 'var_functions.query_db:5'

# Check if they're file paths or actual data
funding_var = locals().get(funding_result_key)
civic_var = locals().get(civic_result_key)

print('Funding variable type:', type(funding_var))
print('Civic variable type:', type(civic_var))
print('Funding variable (first 200 chars):', str(funding_var)[:200])
print('Civic variable (first 200 chars):', str(civic_var)[:200])"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
