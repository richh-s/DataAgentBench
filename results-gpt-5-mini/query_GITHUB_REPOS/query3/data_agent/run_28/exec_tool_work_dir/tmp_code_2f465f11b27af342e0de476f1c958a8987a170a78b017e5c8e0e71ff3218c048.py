code = """import json

# var_call_zRCGYBgf5jGFWwrWw7lo2QJS is a file path to the large JSON result
metadata_path = var_call_zRCGYBgf5jGFWwrWw7lo2QJS
with open(metadata_path, 'r') as f:
    metadata_rows = json.load(f)

# var_call_LEVEBntj9eKBNV8FOlubiSJb is the commits aggregation result (list of dicts)
commits_rows = var_call_LEVEBntj9eKBNV8FOlubiSJb

# Build set of repo_names from metadata
metadata_repos = set(r['repo_name'] for r in metadata_rows)

# Sum counts for repos that are in metadata_repos
total = 0
for r in commits_rows:
    repo = r.get('repo_name')
    cnt = r.get('cnt')
    try:
        cnt_int = int(cnt)
    except:
        try:
            cnt_int = int(float(cnt))
        except:
            cnt_int = 0
    if repo in metadata_repos:
        total += cnt_int

import json
print("__RESULT__:")
print(json.dumps(total))"""

env_args = {'var_call_zRCGYBgf5jGFWwrWw7lo2QJS': 'file_storage/call_zRCGYBgf5jGFWwrWw7lo2QJS.json', 'var_call_LEVEBntj9eKBNV8FOlubiSJb': [{'repo_name': 'tensorflow/tensorflow', 'cnt': '114'}, {'repo_name': 'facebook/react', 'cnt': '104'}, {'repo_name': 'Microsoft/vscode', 'cnt': '171'}, {'repo_name': 'apple/swift', 'cnt': '963'}, {'repo_name': 'torvalds/linux', 'cnt': '13413'}, {'repo_name': 'twbs/bootstrap', 'cnt': '251'}]}

exec(code, env_args)
