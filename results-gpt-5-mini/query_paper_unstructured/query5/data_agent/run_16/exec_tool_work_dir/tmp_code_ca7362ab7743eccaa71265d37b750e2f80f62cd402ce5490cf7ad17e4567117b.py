code = """import json
fp = var_call_mALohj97VQIHLtJCzMrobCxP
with open(fp, 'r', encoding='utf-8') as f:
    data = json.load(f)
filenames = [rec['title'] + '.txt' for rec in data]
print("__RESULT__:")
print(json.dumps(filenames))"""

env_args = {'var_call_mALohj97VQIHLtJCzMrobCxP': 'file_storage/call_mALohj97VQIHLtJCzMrobCxP.json'}

exec(code, env_args)
