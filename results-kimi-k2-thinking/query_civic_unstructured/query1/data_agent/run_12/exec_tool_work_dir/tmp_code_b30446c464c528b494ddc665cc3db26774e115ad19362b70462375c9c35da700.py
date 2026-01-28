code = """import json
import os

# The variable names should be accessible directly
print('Checking available variables:')
print([var for var in dir() if var.startswith('var_')])

# Let's check what these variables contain
funding_data = var_functions.query_db:0
civic_data = var_functions.query_db:1

print('Type of funding_data:', type(funding_data))
print('Type of civic_data:', type(civic_data))
print('funding_data:', str(funding_data)[:200])
print('civic_data:', str(civic_data)[:200])"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json'}

exec(code, env_args)
