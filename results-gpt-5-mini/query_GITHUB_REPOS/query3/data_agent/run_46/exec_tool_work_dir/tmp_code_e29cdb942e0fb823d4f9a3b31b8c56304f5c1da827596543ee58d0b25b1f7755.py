code = """import json
# Load commits filtered by message conditions
with open(var_call_vlNBD1cd1aHT5gammgYda3w6, 'r') as f:
    commits = json.load(f)
# Load shell+apache repo list
with open(var_call_zfdzxeNfBMboGGBHePGhLH2q, 'r') as f:
    shell_repos = json.load(f)

shell_set = set(r.lower() for r in shell_repos)
count = 0
for c in commits:
    repo = c.get('repo_name', '').lower()
    if repo in shell_set:
        count += 1

print("__RESULT__:")
print(json.dumps(count))"""

env_args = {'var_call_RjIW4gryMWhwa5L6eKLNoRE5': 'file_storage/call_RjIW4gryMWhwa5L6eKLNoRE5.json', 'var_call_zfdzxeNfBMboGGBHePGhLH2q': 'file_storage/call_zfdzxeNfBMboGGBHePGhLH2q.json', 'var_call_vlNBD1cd1aHT5gammgYda3w6': 'file_storage/call_vlNBD1cd1aHT5gammgYda3w6.json'}

exec(code, env_args)
