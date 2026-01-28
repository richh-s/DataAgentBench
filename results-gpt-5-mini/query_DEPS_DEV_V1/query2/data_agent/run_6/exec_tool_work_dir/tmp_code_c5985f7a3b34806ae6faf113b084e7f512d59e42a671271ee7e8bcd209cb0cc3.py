code = """import json
# var_call_tYSqXN27S3qNNzfXJjqkaExN is available in the environment
data = None
# load from variable which contains the path to the JSON file
path = var_call_tYSqXN27S3qNNzfXJjqkaExN
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# extract unique (Name, Version) pairs where System == 'NPM'
pairs = []
seen = set()
for r in data:
    if r.get('System') == 'NPM':
        key = (r.get('Name'), r.get('Version'))
        if key not in seen:
            seen.add(key)
            pairs.append({'Name': key[0], 'Version': key[1]})

result = json.dumps(pairs)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_tYSqXN27S3qNNzfXJjqkaExN': 'file_storage/call_tYSqXN27S3qNNzfXJjqkaExN.json'}

exec(code, env_args)
