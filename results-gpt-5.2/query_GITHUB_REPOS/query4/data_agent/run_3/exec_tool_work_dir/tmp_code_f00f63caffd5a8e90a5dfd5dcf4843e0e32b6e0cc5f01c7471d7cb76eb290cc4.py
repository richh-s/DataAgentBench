code = """import json, pandas as pd

# load languages not containing python
lang_src = var_call_FsG5iB7b6YmaIUYdsLgDfofK
if isinstance(lang_src, str):
    with open(lang_src, 'r', encoding='utf-8') as f:
        lang_records = json.load(f)
else:
    lang_records = lang_src

commits = var_call_Q7W3BYSjaLtppYSywUmphCG2

lang_set = {r['repo_name'] for r in lang_records}

# filter commit leaderboard to repos whose language_description does not include python
filtered = [r for r in commits if r['repo_name'] in lang_set]

# sort by commit_count numeric desc and take top 5
for r in filtered:
    r['commit_count_num'] = int(r['commit_count'])
filtered_sorted = sorted(filtered, key=lambda x: x['commit_count_num'], reverse=True)[:5]

answer_lines = [r['repo_name'] for r in filtered_sorted]
result = "\n".join(answer_lines)

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_FsG5iB7b6YmaIUYdsLgDfofK': 'file_storage/call_FsG5iB7b6YmaIUYdsLgDfofK.json', 'var_call_Q7W3BYSjaLtppYSywUmphCG2': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
