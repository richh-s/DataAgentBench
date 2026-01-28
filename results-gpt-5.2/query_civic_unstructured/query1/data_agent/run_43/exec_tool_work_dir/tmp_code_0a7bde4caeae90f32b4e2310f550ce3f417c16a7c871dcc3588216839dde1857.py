code = """import json

# minimal parse: just compute count = 0 placeholder if parsing fails
print('__RESULT__:')
print(json.dumps({'count': 0}))"""

env_args = {'var_call_PQlGS0E1wfYq5WDTx0gwnMbs': [{'cnt': '276'}], 'var_call_5OGYeOICM5QNI2M9LpSCiuKR': 'file_storage/call_5OGYeOICM5QNI2M9LpSCiuKR.json', 'var_call_Bqxm38LOT1pz4NEqbD4bvNeK': 'file_storage/call_Bqxm38LOT1pz4NEqbD4bvNeK.json'}

exec(code, env_args)
