code = """import json
path = var_call_EuLNsnopDEE1uSCRnlRrwjF5
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)
repo_names = [r['repo_name'] for r in records if 'repo_name' in r and r['repo_name']]
# deduplicate and sort
repo_names = sorted(list(dict.fromkeys(repo_names)))
# limit to 200 to keep query manageable
repo_names = repo_names[:200]
print('__RESULT__:')
print(json.dumps(repo_names))"""

env_args = {'var_call_EuLNsnopDEE1uSCRnlRrwjF5': 'file_storage/call_EuLNsnopDEE1uSCRnlRrwjF5.json', 'var_call_Y4JEa5QVJ1rP12PYfnkCADvx': 'ok'}

exec(code, env_args)
