code = """import json

path = var_call_QfQxpc2tjojYfjxcEtAzXEu1
with open(path, 'r', encoding='utf-8') as f:
    repos = json.load(f)
repo_names = [r['repo_name'] for r in repos]
chunks = [repo_names[i:i+500] for i in range(0, len(repo_names), 500)]
queries = []
for ch in chunks:
    in_list = ','.join(["'" + s.replace("'","''") + "'" for s in ch])
    q = (
        "SELECT COUNT(*) AS c FROM commits "
        "WHERE message IS NOT NULL "
        "AND length(message) < 1000 "
        "AND lower(message) NOT LIKE 'merge%' "
        "AND lower(message) NOT LIKE 'update%' "
        "AND lower(message) NOT LIKE 'test%' "
        f"AND repo_name IN ({in_list});"
    )
    queries.append(q)

print('__RESULT__:')
print(json.dumps({'repo_count': len(repo_names), 'chunk_count': len(chunks), 'queries': queries}))"""

env_args = {'var_call_QfQxpc2tjojYfjxcEtAzXEu1': 'file_storage/call_QfQxpc2tjojYfjxcEtAzXEu1.json'}

exec(code, env_args)
