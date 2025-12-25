code = """import json
symbols = ["AGMH", "ALACU"]
q_parts = []
for s in symbols:
    q_parts.append("SELECT '" + s + "' as S, COUNT(*) FROM \"" + s + "\"")
q = " UNION ".join(q_parts)
print("__RESULT__:")
print(json.dumps(q))"""

env_args = {'var_function-call-5715290877284323167': 'file_storage/function-call-5715290877284323167.json', 'var_function-call-18378532918632794193': 'file_storage/function-call-18378532918632794193.json', 'var_function-call-9687647277801400069': 'file_storage/function-call-9687647277801400069.json', 'var_function-call-7849848251971865444': 'test'}

exec(code, env_args)
