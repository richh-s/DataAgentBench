code = """import json
# Load metadata repo list
if isinstance(var_call_Ua8aa5dVexPmI3pV3CqrjEyN, str):
    with open(var_call_Ua8aa5dVexPmI3pV3CqrjEyN, 'r', encoding='utf-8') as f:
        meta = json.load(f)
else:
    meta = var_call_Ua8aa5dVexPmI3pV3CqrjEyN
meta_repos = {item['repo_name'] for item in meta if item.get('repo_name')}

# Load artifacts commit counts
if isinstance(var_call_rQAVyx18Nrvzs4jjKhW9zwpn, str):
    with open(var_call_rQAVyx18Nrvzs4jjKhW9zwpn, 'r', encoding='utf-8') as f:
        commits = json.load(f)
else:
    commits = var_call_rQAVyx18Nrvzs4jjKhW9zwpn

commit_counts = {}
for item in commits:
    rn = item.get('repo_name')
    cnt = item.get('cnt')
    try:
        cnt_int = int(cnt)
    except:
        try:
            cnt_int = int(float(cnt))
        except:
            cnt_int = 0
    commit_counts[rn] = cnt_int

# Sum counts for repos present in meta_repos
matches = []
total = 0
for rn, cnt in commit_counts.items():
    if rn in meta_repos:
        matches.append({'repo_name': rn, 'cnt': cnt})
        total += cnt

result = {'total_count': total, 'matches': matches, 'num_meta_repos': len(meta_repos)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_Ua8aa5dVexPmI3pV3CqrjEyN': 'file_storage/call_Ua8aa5dVexPmI3pV3CqrjEyN.json', 'var_call_586WphIg6o35sQY5YHRPZbMM': 'file_storage/call_586WphIg6o35sQY5YHRPZbMM.json', 'var_call_rQAVyx18Nrvzs4jjKhW9zwpn': [{'repo_name': 'tensorflow/tensorflow', 'cnt': '114'}, {'repo_name': 'facebook/react', 'cnt': '104'}, {'repo_name': 'twbs/bootstrap', 'cnt': '251'}, {'repo_name': 'apple/swift', 'cnt': '963'}, {'repo_name': 'Microsoft/vscode', 'cnt': '171'}, {'repo_name': 'torvalds/linux', 'cnt': '13413'}]}

exec(code, env_args)
