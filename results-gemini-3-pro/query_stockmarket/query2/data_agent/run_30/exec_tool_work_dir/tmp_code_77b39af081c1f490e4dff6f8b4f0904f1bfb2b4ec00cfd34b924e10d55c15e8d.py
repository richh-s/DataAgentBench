code = """import json
c = json.load(open('var_function-call-2542358163233930626.json'))
t = json.load(open('var_function-call-17634865684080335630.json'))
print('__RESULT__:')
print('"done"')"""

env_args = {'var_function-call-2542358163233930626': 'file_storage/function-call-2542358163233930626.json', 'var_function-call-17634865684080335630': 'file_storage/function-call-17634865684080335630.json', 'var_function-call-753327868909953960': 'test'}

exec(code, env_args)
