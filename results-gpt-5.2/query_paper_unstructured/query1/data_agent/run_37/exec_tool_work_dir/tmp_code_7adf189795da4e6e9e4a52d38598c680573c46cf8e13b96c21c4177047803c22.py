code = """import json, re

# load all filenames
path = var_call_r6QWCfP5lyQHfiZvNhBZpmgQ
with open(path, 'r', encoding='utf-8') as f:
    all_files = json.load(f)

titles = [rec['filename'].removesuffix('.txt') for rec in all_files]

food_titles = []
for t in titles:
    if re.search(r'food', t, flags=re.I):
        food_titles.append(t)

print('__RESULT__:')
print(json.dumps({'food_titles': food_titles, 'count': len(food_titles)}))"""

env_args = {'var_call_r6QWCfP5lyQHfiZvNhBZpmgQ': 'file_storage/call_r6QWCfP5lyQHfiZvNhBZpmgQ.json', 'var_call_55MoKbE7CVXtqCCRcMS1lJIY': [], 'var_call_db4rxScL1sMaOK6gsg2Q4tsE': 'file_storage/call_db4rxScL1sMaOK6gsg2Q4tsE.json'}

exec(code, env_args)
