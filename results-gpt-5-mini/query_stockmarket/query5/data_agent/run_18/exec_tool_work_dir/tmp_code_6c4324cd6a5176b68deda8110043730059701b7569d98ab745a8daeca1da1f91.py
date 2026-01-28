code = """import json
paths = [var_call_p3wehT7WbD92Ab0NJaPpAfGD, var_call_Brv828NQIaemUxAB6OfCNpOc]
print('__RESULT__:')
print(json.dumps(paths))"""

env_args = {'var_call_p3wehT7WbD92Ab0NJaPpAfGD': 'file_storage/call_p3wehT7WbD92Ab0NJaPpAfGD.json', 'var_call_Brv828NQIaemUxAB6OfCNpOc': 'file_storage/call_Brv828NQIaemUxAB6OfCNpOc.json'}

exec(code, env_args)
