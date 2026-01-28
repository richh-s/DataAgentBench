code = """import json
with open(var_call_ulODgnzxdmB7bWwddmb5TRy0, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_KWNLUv7QwTFzxckaFGtF9TlS, 'r') as f:
    tables = json.load(f)
mapping = {rec['Symbol']: rec['Company Description'] for rec in stockinfo}
available_symbols = sorted([s for s in mapping.keys() if s in tables])
res = {'available_symbols': available_symbols, 'num': len(available_symbols)}
print("__RESULT__:")
print(json.dumps(res))"""

env_args = {'var_call_ulODgnzxdmB7bWwddmb5TRy0': 'file_storage/call_ulODgnzxdmB7bWwddmb5TRy0.json', 'var_call_KWNLUv7QwTFzxckaFGtF9TlS': 'file_storage/call_KWNLUv7QwTFzxckaFGtF9TlS.json'}

exec(code, env_args)
