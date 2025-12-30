code = """import json
with open(locals()['var_function-call-11236365375082320521'], 'r') as f:
    citations_2020 = json.load(f)

titles = [item['title'] for item in citations_2020]
print('__RESULT__:')
print(json.dumps(titles))"""

env_args = {'var_function-call-11236365375082320521': 'file_storage/function-call-11236365375082320521.json'}

exec(code, env_args)
