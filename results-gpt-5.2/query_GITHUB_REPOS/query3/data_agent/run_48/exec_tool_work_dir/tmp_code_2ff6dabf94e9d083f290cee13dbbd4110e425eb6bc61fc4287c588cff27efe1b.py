code = """import json
path = var_call_FyCcrS1VIozaZXKX92I1XumZ
with open(path, 'r', encoding='utf-8') as f:
    repos = json.load(f)
repo_list = [r['repo_name'] for r in repos]
chunks = [repo_list[i:i+400] for i in range(0, len(repo_list), 400)]

qs = []
for ch in chunks:
    in_list = "(" + ",".join(["'" + x.replace("'","''") + "'" for x in ch]) + ")"
    q = (
        "SELECT COUNT(*) AS commit_message_count FROM commits "
        "WHERE message IS NOT NULL "
        "AND length(message) < 1000 "
        "AND lower(trim(message)) NOT LIKE 'merge%' "
        "AND lower(trim(message)) NOT LIKE 'update%' "
        "AND lower(trim(message)) NOT LIKE 'test%' "
        f"AND repo_name IN {in_list};"
    )
    qs.append(q)

print('__RESULT__:')
print(json.dumps(qs))"""

env_args = {'var_call_FyCcrS1VIozaZXKX92I1XumZ': 'file_storage/call_FyCcrS1VIozaZXKX92I1XumZ.json', 'var_call_maofEvbonAZxeQVPYiJzip4x': [{'any_owner': 'facebook'}, {'any_owner': 'tensorflow'}, {'any_owner': 'twbs'}, {'any_owner': 'Microsoft'}, {'any_owner': 'torvalds'}], 'var_call_hjIOdI5dy98CwjX5uSpTTO1v': [{'commit_message_count': '0'}], 'var_call_wyIJHAlaLE7lVoYnHBebDDuS': 'file_storage/call_wyIJHAlaLE7lVoYnHBebDDuS.json', 'var_call_56kGgLbGFdA91YLDdS44gMKl': [{'c': '0'}]}

exec(code, env_args)
