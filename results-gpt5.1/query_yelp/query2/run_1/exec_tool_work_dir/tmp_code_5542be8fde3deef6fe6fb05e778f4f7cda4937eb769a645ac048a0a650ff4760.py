code = """import json
with open(var_call_rWm2Cmud0IFfuaXolk88ya99, 'r') as f:
    business_data = json.load(f)

first = business_data[0]
second = business_data[1]

print('__RESULT__:')
print(json.dumps({'first': first, 'second': second}))"""

env_args = {'var_call_Bxs950sZ5rio9iVFYpZeb92a': 'file_storage/call_Bxs950sZ5rio9iVFYpZeb92a.json', 'var_call_PKusBbTTfo6UnBTeje8wlkuZ': 'file_storage/call_PKusBbTTfo6UnBTeje8wlkuZ.json', 'var_call_rWm2Cmud0IFfuaXolk88ya99': 'file_storage/call_rWm2Cmud0IFfuaXolk88ya99.json', 'var_call_c3QaRDkGeChs0yDmPTtLk4FC': {'sample_keys': ['business_id', 'description']}}

exec(code, env_args)
