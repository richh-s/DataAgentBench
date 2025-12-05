code = """import json, re, pandas as pd

with open(var_call_rWm2Cmud0IFfuaXolk88ya99, 'r') as f:
    business_data = json.load(f)

print('__RESULT__:')
print(json.dumps({'sample_keys': list(business_data[0].keys())}))"""

env_args = {'var_call_Bxs950sZ5rio9iVFYpZeb92a': 'file_storage/call_Bxs950sZ5rio9iVFYpZeb92a.json', 'var_call_PKusBbTTfo6UnBTeje8wlkuZ': 'file_storage/call_PKusBbTTfo6UnBTeje8wlkuZ.json', 'var_call_rWm2Cmud0IFfuaXolk88ya99': 'file_storage/call_rWm2Cmud0IFfuaXolk88ya99.json'}

exec(code, env_args)
