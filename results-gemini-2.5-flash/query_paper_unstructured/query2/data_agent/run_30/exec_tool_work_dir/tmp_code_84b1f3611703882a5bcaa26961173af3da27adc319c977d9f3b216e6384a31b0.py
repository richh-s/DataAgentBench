code = """import json
with open(locals()['var_function-call-5858147982497012286'], 'r') as f:
    citations_2018 = json.load(f)
titles = [item['title'] for item in citations_2018]
print('__RESULT__:')
print(json.dumps(titles))"""

env_args = {'var_function-call-5858147982497012286': 'file_storage/function-call-5858147982497012286.json'}

exec(code, env_args)
