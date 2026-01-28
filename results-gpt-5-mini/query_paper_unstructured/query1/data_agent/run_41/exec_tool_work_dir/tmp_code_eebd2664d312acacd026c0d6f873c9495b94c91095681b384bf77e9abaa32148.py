code = """import json
path = var_call_y7sTqMxz8v6UcMHattxaO0rs
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

titles = []
for d in docs:
    fn = d.get('filename', '')
    if fn.lower().endswith('.txt'):
        titles.append(fn[:-4])
    else:
        titles.append(fn)

print("__RESULT__:")
print(json.dumps(titles))"""

env_args = {'var_call_y7sTqMxz8v6UcMHattxaO0rs': 'file_storage/call_y7sTqMxz8v6UcMHattxaO0rs.json'}

exec(code, env_args)
