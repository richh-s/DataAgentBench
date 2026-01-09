code = """import json
path = var_call_cBY07VVhdToJgICFJgfLQOnv
with open(path, 'r', encoding='utf-8') as f:
    repos = json.load(f)
repo_names = [r['repo_name'] for r in repos]
chunks = [repo_names[i:i+500] for i in range(0, len(repo_names), 500)]
queries = []
for ch in chunks:
    in_list = ','.join(["'" + s.replace("'","''") + "'" for s in ch])
    q = (
        "SELECT COUNT(*) AS cnt FROM commits "
        f"WHERE repo_name IN ({in_list}) "
        "AND message IS NOT NULL "
        "AND length(message) < 1000 "
        "AND NOT (lower(message) LIKE 'merge%' OR lower(message) LIKE 'update%' OR lower(message) LIKE 'test%');"
    )
    queries.append(q)
print('__RESULT__:')
print(json.dumps({'queries': queries}))"""

env_args = {'var_call_cBY07VVhdToJgICFJgfLQOnv': 'file_storage/call_cBY07VVhdToJgICFJgfLQOnv.json', 'var_call_GiBXcbU1ci2vywFpdconRX7P': [{'commit_message_count': '15016'}]}

exec(code, env_args)
