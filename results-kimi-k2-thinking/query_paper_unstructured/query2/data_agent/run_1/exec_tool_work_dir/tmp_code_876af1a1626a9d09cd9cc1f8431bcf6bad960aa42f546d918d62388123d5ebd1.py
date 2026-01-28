code = """import json
# Try to access the result from the previous querysql_result = globals().get('var_functions.query_db:0') or locals().get('var_functions.query_db:0')
print('__RESULT__:')
print(json.dumps(str(type(sql_result))))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
