code = """import json

# Get the result from the previous query
result = locals().get('var_functions.query_db:0', [])
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'track_id': '4122'}]}

exec(code, env_args)
