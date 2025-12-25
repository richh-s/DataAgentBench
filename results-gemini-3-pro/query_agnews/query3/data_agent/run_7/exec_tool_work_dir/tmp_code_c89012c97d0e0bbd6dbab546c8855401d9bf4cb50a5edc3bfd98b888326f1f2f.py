code = """import json
with open(locals()['var_function-call-12801721283441403514'], 'r') as f:
    ids = json.load(f)
print("__RESULT__:")
print(len(ids))"""

env_args = {'var_function-call-10971295442504843932': 'file_storage/function-call-10971295442504843932.json', 'var_function-call-12801721283441403514': 'file_storage/function-call-12801721283441403514.json'}

exec(code, env_args)
