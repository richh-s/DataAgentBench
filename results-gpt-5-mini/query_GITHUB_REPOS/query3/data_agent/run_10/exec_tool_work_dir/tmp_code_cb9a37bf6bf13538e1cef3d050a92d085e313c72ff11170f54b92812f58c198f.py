code = """import json
path = var_call_1i4P1uf3r6Q6nR4h0XMpoP4A
with open(path, 'r', encoding='utf-8') as f:
    sql = f.read()
print('__RESULT__:')
print(json.dumps(sql))"""

env_args = {'var_call_J100Hcf8cXp1CDcLYJbUDxF2': 'file_storage/call_J100Hcf8cXp1CDcLYJbUDxF2.json', 'var_call_1i4P1uf3r6Q6nR4h0XMpoP4A': 'file_storage/call_1i4P1uf3r6Q6nR4h0XMpoP4A.json'}

exec(code, env_args)
