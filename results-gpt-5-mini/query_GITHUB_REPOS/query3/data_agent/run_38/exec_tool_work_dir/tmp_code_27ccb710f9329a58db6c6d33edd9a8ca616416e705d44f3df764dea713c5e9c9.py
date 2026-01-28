code = """import json
# var_call_6aN3CzElB6ohUyLRkF7mru3h is provided by the previous query_db call
data = None
try:
    # If the storage variable is a file path (string), read it
    if isinstance(var_call_6aN3CzElB6ohUyLRkF7mru3h, str):
        with open(var_call_6aN3CzElB6ohUyLRkF7mru3h, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = var_call_6aN3CzElB6ohUyLRkF7mru3h
except Exception as e:
    # fallback: try to use it directly
    data = var_call_6aN3CzElB6ohUyLRkF7mru3h

repo_names = []
if isinstance(data, list):
    for rec in data:
        if isinstance(rec, dict) and 'repo_name' in rec:
            repo_names.append(rec['repo_name'])
# dedupe and sort
repo_names = sorted(list(dict.fromkeys(repo_names)))

print("__RESULT__:")
print(json.dumps(repo_names))"""

env_args = {'var_call_6aN3CzElB6ohUyLRkF7mru3h': 'file_storage/call_6aN3CzElB6ohUyLRkF7mru3h.json'}

exec(code, env_args)
