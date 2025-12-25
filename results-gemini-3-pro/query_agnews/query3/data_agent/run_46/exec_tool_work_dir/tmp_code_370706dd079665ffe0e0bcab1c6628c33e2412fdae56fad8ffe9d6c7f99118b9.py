code = """import json

with open(locals()['var_function-call-1308901072042740489'], 'r') as f:
    sql_results = json.load(f)

count = len(sql_results)
print("__RESULT__:")
print(count)"""

env_args = {'var_function-call-1308901072042740489': 'file_storage/function-call-1308901072042740489.json'}

exec(code, env_args)
