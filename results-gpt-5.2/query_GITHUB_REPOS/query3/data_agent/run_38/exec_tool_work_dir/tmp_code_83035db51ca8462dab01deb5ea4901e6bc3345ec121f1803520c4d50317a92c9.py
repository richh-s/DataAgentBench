code = """import json, pandas as pd

# commits counts per repo
commits_counts = pd.DataFrame(var_call_zWHqaupb95OPmu4tt1K8s5Ih)
commits_counts['repo_name'] = commits_counts['repo_name'].str.lower()
commits_counts['cnt'] = commits_counts['cnt'].astype(int)

# metadata repos list from file
path = var_call_dmJfAztqB5n2y5ykbhyiUK1m
with open(path,'r') as f:
    meta = json.load(f)
meta_set = {r['repo_name'] for r in meta if isinstance(r,dict) and r.get('repo_name')}

filtered = commits_counts[commits_counts['repo_name'].isin(meta_set)]
result = int(filtered['cnt'].sum())

print('__RESULT__:')
print(json.dumps({'commit_message_count': result}))"""

env_args = {'var_call_ioHf39wi8QtDiRcv7ZGNUfe8': 'file_storage/call_ioHf39wi8QtDiRcv7ZGNUfe8.json', 'var_call_zWHqaupb95OPmu4tt1K8s5Ih': [{'repo_name': 'microsoft/vscode', 'cnt': '171'}, {'repo_name': 'facebook/react', 'cnt': '104'}, {'repo_name': 'tensorflow/tensorflow', 'cnt': '114'}, {'repo_name': 'twbs/bootstrap', 'cnt': '251'}, {'repo_name': 'apple/swift', 'cnt': '963'}, {'repo_name': 'torvalds/linux', 'cnt': '13413'}], 'var_call_dmJfAztqB5n2y5ykbhyiUK1m': 'file_storage/call_dmJfAztqB5n2y5ykbhyiUK1m.json'}

exec(code, env_args)
