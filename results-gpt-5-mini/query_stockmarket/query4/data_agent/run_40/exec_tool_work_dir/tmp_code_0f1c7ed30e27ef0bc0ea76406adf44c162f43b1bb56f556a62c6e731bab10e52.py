code = """import json, os
p = var_call_Z1LS9TfnT11V5aMqhG55TyCL
if isinstance(p, str) and os.path.exists(p):
    data = json.load(open(p, 'r'))
else:
    data = p
symbols = [r['Symbol'] for r in data]
# ensure unique
symbols = list(dict.fromkeys(symbols))
out = {"count": len(symbols), "symbols": symbols}
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_Z1LS9TfnT11V5aMqhG55TyCL': 'file_storage/call_Z1LS9TfnT11V5aMqhG55TyCL.json'}

exec(code, env_args)
