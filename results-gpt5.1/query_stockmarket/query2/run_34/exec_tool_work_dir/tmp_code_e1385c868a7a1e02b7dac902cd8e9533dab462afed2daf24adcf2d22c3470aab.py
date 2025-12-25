code = """import json
ets = var_call_286zlOyMMMGIRHNdFEMo4xKP
symbols = [row['Symbol'] for row in ets]
chunks = [symbols[i:i+200] for i in range(0, len(symbols), 200)]
result = json.dumps(chunks)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_LBl6dBoH38eJSNSqYM735HmY': 'file_storage/call_LBl6dBoH38eJSNSqYM735HmY.json', 'var_call_286zlOyMMMGIRHNdFEMo4xKP': 'file_storage/call_286zlOyMMMGIRHNdFEMo4xKP.json'}

exec(code, env_args)
