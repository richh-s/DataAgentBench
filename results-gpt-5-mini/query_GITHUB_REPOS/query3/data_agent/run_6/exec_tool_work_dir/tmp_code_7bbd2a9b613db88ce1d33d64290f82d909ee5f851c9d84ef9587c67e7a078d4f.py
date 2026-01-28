code = """import json
# Load metadata result (may be a filepath or list)
meta_var = var_call_lVNH86PrtpVHNoTtw7BoPxYe
if isinstance(meta_var, str):
    with open(meta_var, 'r') as f:
        meta = json.load(f)
else:
    meta = meta_var

meta_repos = set()
for r in meta:
    if isinstance(r, dict) and 'repo_name' in r:
        meta_repos.add(r['repo_name'])

commits = var_call_paBStlCdSp6wjxY7ZltJ05zr
total = 0
for r in commits:
    rn = r.get('repo_name')
    cnt = r.get('cnt')
    try:
        c = int(cnt)
    except Exception:
        try:
            c = int(float(cnt))
        except Exception:
            c = 0
    if rn in meta_repos:
        total += c

print("__RESULT__:")
print(json.dumps(total))"""

env_args = {'var_call_lVNH86PrtpVHNoTtw7BoPxYe': 'file_storage/call_lVNH86PrtpVHNoTtw7BoPxYe.json', 'var_call_paBStlCdSp6wjxY7ZltJ05zr': [{'repo_name': 'tensorflow/tensorflow', 'cnt': '114'}, {'repo_name': 'facebook/react', 'cnt': '104'}, {'repo_name': 'Microsoft/vscode', 'cnt': '171'}, {'repo_name': 'apple/swift', 'cnt': '963'}, {'repo_name': 'torvalds/linux', 'cnt': '13413'}, {'repo_name': 'twbs/bootstrap', 'cnt': '251'}]}

exec(code, env_args)
