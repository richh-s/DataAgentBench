code = """import json
path = var_call_0iR8WlQ5ARF8bgujNkAIgkQb
if isinstance(path, str) and path.endswith('.json'):
    with open(path,'r') as f:
        payload = json.load(f)
else:
    payload = path
symbols = payload['symbols']

sym = symbols[0]

print('__RESULT__:')
print(json.dumps({'sym': sym}))"""

env_args = {'var_call_y7ZF0nkKnhjCsARv9z2cAVOg': 'file_storage/call_y7ZF0nkKnhjCsARv9z2cAVOg.json', 'var_call_meoUs7y7uUlDfzjL99xuAS8N': 'file_storage/call_meoUs7y7uUlDfzjL99xuAS8N.json', 'var_call_0iR8WlQ5ARF8bgujNkAIgkQb': 'file_storage/call_0iR8WlQ5ARF8bgujNkAIgkQb.json', 'var_call_pmuJ496qX2Xskx1sT9uaHcys': {'sample': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF'], 'n': 1435}, 'var_call_ppiUjSebFcAH0yAp2UzQxqOM': [{'table_name': 'AAAU'}, {'table_name': 'AADR'}, {'table_name': 'AAME'}, {'table_name': 'AAWW'}, {'table_name': 'AAXJ'}], 'var_call_mYqAwa1yYSEq4NUaTNLuI1Qf': {'ok': True}}

exec(code, env_args)
