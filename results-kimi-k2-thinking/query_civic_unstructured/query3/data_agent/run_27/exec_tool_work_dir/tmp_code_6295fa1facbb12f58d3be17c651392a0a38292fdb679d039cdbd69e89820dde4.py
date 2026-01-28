code = """import json
# Retrieve list_db result
list_result = locals().get('var_functions.list_db:0', [])
# Convert to JSON string
json_str = json.dumps(list_result)
print('__RESULT__:')
print(json_str)"""

env_args = {'var_functions.list_db:0': ['civic_docs']}

exec(code, env_args)
