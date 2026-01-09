code = """import json
lang_src = var_call_FsG5iB7b6YmaIUYdsLgDfofK
if isinstance(lang_src, str):
    with open(lang_src, 'r', encoding='utf-8') as f:
        lang_records = json.load(f)
else:
    lang_records = lang_src
commits = var_call_Q7W3BYSjaLtppYSywUmphCG2
lang_set = {r['repo_name'] for r in lang_records}
filtered = []
for r in commits:
    if r.get('repo_name') in lang_set:
        filtered.append((int(r['commit_count']), r['repo_name']))
filtered.sort(key=lambda x: x[0], reverse=True)
top5 = [name for _, name in filtered[:5]]
result = "\n".join(top5)
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_FsG5iB7b6YmaIUYdsLgDfofK': 'file_storage/call_FsG5iB7b6YmaIUYdsLgDfofK.json', 'var_call_Q7W3BYSjaLtppYSywUmphCG2': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
