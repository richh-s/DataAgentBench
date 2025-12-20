code = """import json

with open(locals()['var_function-call-16212366058662656941'], 'r') as f:
    metadata = json.load(f)

print(f"Count: {len(metadata)}")
print(f"Sample: {metadata[:5]}")
print("__RESULT__:")
print(json.dumps({"count": len(metadata), "sample": metadata[:5]}))"""

env_args = {'var_function-call-16212366058662656941': 'file_storage/function-call-16212366058662656941.json'}

exec(code, env_args)
