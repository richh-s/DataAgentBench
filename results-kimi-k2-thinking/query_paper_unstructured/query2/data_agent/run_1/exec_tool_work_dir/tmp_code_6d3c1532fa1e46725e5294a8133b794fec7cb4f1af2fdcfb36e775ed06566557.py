code = """import json, os

# Check what the variable contains
citation_result = var_functions.query_db:0
print('Type:', type(citation_result))
print('Content:', str(citation_result)[:500])"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
