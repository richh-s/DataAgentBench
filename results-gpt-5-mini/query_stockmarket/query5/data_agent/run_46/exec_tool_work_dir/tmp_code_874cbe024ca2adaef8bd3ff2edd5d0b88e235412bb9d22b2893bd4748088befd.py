code = """import json
# var_call_0Fvjtx7UYryx92nSa40UHoDi contains the path to the JSON file with the stockinfo results
with open(var_call_0Fvjtx7UYryx92nSa40UHoDi, 'r') as f:
    data = json.load(f)
# Extract only Symbol and Company Description
out = [{"Symbol": r["Symbol"], "Company Description": r.get("Company Description") } for r in data]
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_0Fvjtx7UYryx92nSa40UHoDi': 'file_storage/call_0Fvjtx7UYryx92nSa40UHoDi.json'}

exec(code, env_args)
