code = """import json
# var_call_4QBHnENUNKnmttDHTGhGVb3H is a string path to the full result JSON file
path = var_call_4QBHnENUNKnmttDHTGhGVb3H
with open(path, 'r', encoding='utf-8') as f:
    rows = json.load(f)
# Extract unique (System, Name, Version)
triples = []
seen = set()
for r in rows:
    key = (r.get('System'), r.get('Name'), r.get('Version'))
    if key not in seen:
        seen.add(key)
        triples.append({'System': key[0], 'Name': key[1], 'Version': key[2]})
# Limit the number of triples to avoid overly long SQL if extremely large; but include all
# Prepare JSON serializable string
out = json.dumps(triples)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_SPpf6OTIy2suP5I0T2HqEXjg': ['packageinfo'], 'var_call_i6hRKgFEWzpOJz5Z6LugaNNc': ['project_info', 'project_packageversion'], 'var_call_4QBHnENUNKnmttDHTGhGVb3H': 'file_storage/call_4QBHnENUNKnmttDHTGhGVb3H.json'}

exec(code, env_args)
