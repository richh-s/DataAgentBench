code = """import json

path = var_call_9SesQU4KCciW3TfQwgpCVElC
with open(path, 'r', encoding='utf-8') as f:
    repos = json.load(f)
repo_names = [r['repo_name'] for r in repos]

chunks = []
chunk_size = 500
for i in range(0, len(repo_names), chunk_size):
    sub = repo_names[i:i+chunk_size]
    in_list = ','.join(["'" + s.replace("'","''") + "'" for s in sub])
    q = (
        "SELECT COUNT(*) AS c FROM commits "
        "WHERE message IS NOT NULL "
        "AND length(message) < 1000 "
        "AND NOT (lower(message) LIKE 'merge%' OR lower(message) LIKE 'update%' OR lower(message) LIKE 'test%') "
        f"AND repo_name IN ({in_list})"
    )
    chunks.append(q)

full_query = " UNION ALL ".join(chunks)

print('__RESULT__:')
print(json.dumps({'query': full_query, 'num_repos': len(repo_names), 'num_chunks': len(chunks)}))"""

env_args = {'var_call_9SesQU4KCciW3TfQwgpCVElC': 'file_storage/call_9SesQU4KCciW3TfQwgpCVElC.json', 'var_call_FkmdvbN2Qla4bGF6wUlaGxB1': [{'commit_message_count': '15016'}]}

exec(code, env_args)
