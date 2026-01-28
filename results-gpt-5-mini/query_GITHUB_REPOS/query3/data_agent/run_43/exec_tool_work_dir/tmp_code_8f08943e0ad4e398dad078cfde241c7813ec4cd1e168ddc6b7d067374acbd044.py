code = """import json
# Read the large repo list file produced earlier
path = var_call_o07qUZM7tOOEYrrLcwATeuAg
with open(path, 'r') as f:
    rows = json.load(f)
repo_set = set(r.get('repo_name') for r in rows if r.get('repo_name'))
# var_call_3gEgj4ce15H58DZxeUZrp2Us is available as a list of dicts
commit_counts = var_call_3gEgj4ce15H58DZxeUZrp2Us
matched = []
total = 0
for r in commit_counts:
    name = r.get('repo_name')
    cnt = int(r.get('cnt')) if r.get('cnt') is not None else 0
    if name in repo_set:
        matched.append({'repo_name': name, 'cnt': cnt})
        total += cnt
# Prepare result
result = {'total_commit_messages': total, 'matched_repos': matched}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_o07qUZM7tOOEYrrLcwATeuAg': 'file_storage/call_o07qUZM7tOOEYrrLcwATeuAg.json', 'var_call_ILAcYIeQibldR8TUCpd7INQV': 'file_storage/call_ILAcYIeQibldR8TUCpd7INQV.json', 'var_call_3gEgj4ce15H58DZxeUZrp2Us': [{'repo_name': 'tensorflow/tensorflow', 'cnt': '114'}, {'repo_name': 'facebook/react', 'cnt': '104'}, {'repo_name': 'Microsoft/vscode', 'cnt': '171'}, {'repo_name': 'twbs/bootstrap', 'cnt': '251'}, {'repo_name': 'torvalds/linux', 'cnt': '13413'}, {'repo_name': 'apple/swift', 'cnt': '963'}]}

exec(code, env_args)
