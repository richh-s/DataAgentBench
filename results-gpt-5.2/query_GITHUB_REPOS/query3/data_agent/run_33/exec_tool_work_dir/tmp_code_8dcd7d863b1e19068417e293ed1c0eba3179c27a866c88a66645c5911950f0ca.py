code = """import json

path = var_call_5GUg84X5hO9MKHGRyKudnnJ8
with open(path, 'r', encoding='utf-8') as f:
    repos = json.load(f)
repo_names = [r['repo_name'] for r in repos]

chunk_size = 500
chunks = []
for i in range(0, len(repo_names), chunk_size):
    sub = repo_names[i:i+chunk_size]
    quoted = ",".join(["'" + s.replace("'","''") + "'" for s in sub])
    chunks.append("repo_name IN (" + quoted + ")")
where_in = " OR ".join(["(" + c + ")" for c in chunks]) if chunks else "FALSE"

query = (
    "SELECT COUNT(*) AS commit_message_count "
    "FROM commits "
    "WHERE message IS NOT NULL "
    "AND length(message) < 1000 "
    "AND lower(substr(message, 1, 5)) <> 'merge' "
    "AND lower(substr(message, 1, 6)) <> 'update' "
    "AND lower(substr(message, 1, 4)) <> 'test' "
    "AND (" + where_in + ");"
)

print('__RESULT__:')
print(json.dumps({"repo_count": len(repo_names), "query": query}))"""

env_args = {'var_call_5GUg84X5hO9MKHGRyKudnnJ8': 'file_storage/call_5GUg84X5hO9MKHGRyKudnnJ8.json'}

exec(code, env_args)
