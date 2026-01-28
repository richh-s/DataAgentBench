code = """import json
# var_call_sYGEyX5JrMt2dOgtF3WlNf4f is available and contains the filepath to the JSON result
fp = var_call_sYGEyX5JrMt2dOgtF3WlNf4f
with open(fp, 'r', encoding='utf-8') as f:
    data = json.load(f)
# Extract unique (Name, Version) pairs
pairs = []
seen = set()
for r in data:
    name = r.get('Name')
    ver = r.get('Version')
    if (name, ver) not in seen:
        seen.add((name, ver))
        pairs.append({'Name': name, 'Version': ver})
# Output as JSON string
out = json.dumps(pairs)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_OEReunzHmE74cZY4WNSIkfET': ['packageinfo'], 'var_call_o5zSgoYFYlDqAiCwnnXLwH5B': ['project_info', 'project_packageversion'], 'var_call_sYGEyX5JrMt2dOgtF3WlNf4f': 'file_storage/call_sYGEyX5JrMt2dOgtF3WlNf4f.json'}

exec(code, env_args)
