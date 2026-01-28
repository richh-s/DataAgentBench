code = """import json
with open(var_call_qmvmcRybdZcFdW5SX1SGgE7P, 'r') as f:
    data = json.load(f)
avail = set(data['available_symbols'])
candidates = ['SPY','IVV','VOO','VTI','VOO','GDX','GLD','IWM','QQQ']
found = [c for c in candidates if c in avail]
result = {'found_candidates': found}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_7unxnarEaWwSx7trThvVwizq': ['stockinfo'], 'var_call_WaEvCHYDu8q5PYvnJxAh1X2s': 'file_storage/call_WaEvCHYDu8q5PYvnJxAh1X2s.json', 'var_call_C9yV3KAORv9nL5ONxiYWO0Ud': 'file_storage/call_C9yV3KAORv9nL5ONxiYWO0Ud.json', 'var_call_qmvmcRybdZcFdW5SX1SGgE7P': 'file_storage/call_qmvmcRybdZcFdW5SX1SGgE7P.json'}

exec(code, env_args)
