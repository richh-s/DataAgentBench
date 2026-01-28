code = """import json
import re

# Create a simpler approach to extract project information
# from the stored results

mongo_result = var_functions.query_db:9
funding_result = var_functions.query_db:10

print('__RESULT__:')
print('Starting analysis...')"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
