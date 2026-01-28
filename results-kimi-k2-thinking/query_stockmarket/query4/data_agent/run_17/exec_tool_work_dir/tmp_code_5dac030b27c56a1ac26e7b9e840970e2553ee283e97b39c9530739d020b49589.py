code = """import json
# Retrieve the stored result
result_key = 'var_functions.query_db:2'
if result_key in locals():
    symbols_data = locals()[result_key]
    print('Found in locals')
else:
    print('Not found in locals')
    # Try to see what keys are present
    print('Available keys:', list(locals().keys()))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
