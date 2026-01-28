code = """import json
# Load query results from storage files
with open(var_call_CXtGwFrZu0CwEx7E08dUQNdH, 'r') as f:
    langs = json.load(f)
with open(var_call_MZ6k9QPWlyJI9Uk6ZT9Ezapw, 'r') as f:
    licenses = json.load(f)
with open(var_call_hEev8Bv7nsgeFoPMBiTAT6Bx, 'r') as f:
    commits = json.load(f)

shell_repos = set(r['repo_name'] for r in langs if 'repo_name' in r)
apache_repos = set(r['repo_name'] for r in licenses if 'repo_name' in r)
valid_repos = shell_repos.intersection(apache_repos)

count = 0
for c in commits:
    rn = c.get('repo_name')
    if rn in valid_repos:
        count += 1

import json as _json
print("__RESULT__:")
print(_json.dumps(count))"""

env_args = {'var_call_CXtGwFrZu0CwEx7E08dUQNdH': 'file_storage/call_CXtGwFrZu0CwEx7E08dUQNdH.json', 'var_call_MZ6k9QPWlyJI9Uk6ZT9Ezapw': 'file_storage/call_MZ6k9QPWlyJI9Uk6ZT9Ezapw.json', 'var_call_hEev8Bv7nsgeFoPMBiTAT6Bx': 'file_storage/call_hEev8Bv7nsgeFoPMBiTAT6Bx.json'}

exec(code, env_args)
