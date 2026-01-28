code = """import json
import os

# Check what we have in storage
languages_data = locals()['var_functions.query_db:2']
print("Type of languages_data:", type(languages_data))
print("Value:", str(languages_data)[:200])

# Print result
result = {"data_type": str(type(languages_data))}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
