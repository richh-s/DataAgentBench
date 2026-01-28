code = """import json
# Read the large JSON result file produced by the previous query
with open(var_call_RjIW4gryMWhwa5L6eKLNoRE5, 'r') as f:
    data = json.load(f)
# data is a list of dicts like {"repo_name": "owner/repo"}
repo_names = [d['repo_name'] for d in data if 'repo_name' in d]
# dedupe and sort
repo_names = sorted(list(dict.fromkeys(repo_names)))
# print result in required format
print("__RESULT__:")
print(json.dumps(repo_names))"""

env_args = {'var_call_RjIW4gryMWhwa5L6eKLNoRE5': 'file_storage/call_RjIW4gryMWhwa5L6eKLNoRE5.json'}

exec(code, env_args)
