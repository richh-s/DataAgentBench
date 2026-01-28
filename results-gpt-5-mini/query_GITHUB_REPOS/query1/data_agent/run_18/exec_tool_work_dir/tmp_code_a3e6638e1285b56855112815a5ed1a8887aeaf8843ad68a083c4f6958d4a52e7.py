code = """import json
print("__RESULT__:")
print(json.dumps({"test":1}))"""

env_args = {'var_call_LM3tvya7aOMgQs8YKYzKm8YV': 'file_storage/call_LM3tvya7aOMgQs8YKYzKm8YV.json', 'var_call_9JPe2QYsMLtUbCP1E5AsAkEn': 'file_storage/call_9JPe2QYsMLtUbCP1E5AsAkEn.json'}

exec(code, env_args)
