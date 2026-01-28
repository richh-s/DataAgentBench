code = """import json

path = var_call_GvAITfP6oyVv9ugf4515BZw9
with open(path, 'r') as f:
    repos = json.load(f)
repo_list = [r['repo_name'] for r in repos]

batch_size = 500
queries = []
for i in range(0, len(repo_list), batch_size):
    batch = repo_list[i:i+batch_size]
    in_list = ','.join(["'" + s.replace("'","''") + "'" for s in batch])
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
print(json.dumps({'repo_count': len(repo_list), 'batch_query_count': len(queries), 'queries': queries[:3]}))"""

env_args = {'var_call_GvAITfP6oyVv9ugf4515BZw9': 'file_storage/call_GvAITfP6oyVv9ugf4515BZw9.json'}

exec(code, env_args)
