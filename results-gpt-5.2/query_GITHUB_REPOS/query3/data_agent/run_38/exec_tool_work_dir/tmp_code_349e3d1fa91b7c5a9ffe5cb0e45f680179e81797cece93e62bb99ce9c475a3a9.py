code = """import json

path = var_call_ioHf39wi8QtDiRcv7ZGNUfe8
with open(path, 'r') as f:
    repos = json.load(f)
repo_names = sorted({r['repo_name'] for r in repos if isinstance(r, dict) and r.get('repo_name')})

chunks = []
chunk_size = 500
for i in range(0, len(repo_names), chunk_size):
    chunk = repo_names[i:i+chunk_size]
    in_list = ','.join(["'" + x.replace("'","''") + "'" for x in chunk])
    chunks.append("repo_name IN (" + in_list + ")")
where_repos = ' OR '.join(chunks) if chunks else 'FALSE'

query = (
"SELECT COUNT(*) AS commit_message_count\n"
"FROM commits\n"
"WHERE message IS NOT NULL\n"
"  AND length(message) < 1000\n"
"  AND lower(message) NOT LIKE 'merge%'\n"
"  AND lower(message) NOT LIKE 'update%'\n"
"  AND lower(message) NOT LIKE 'test%'\n"
"  AND (" + where_repos + ");"
)

print('__RESULT__:')
print(json.dumps({'query': query, 'repo_count': len(repo_names)}))"""

env_args = {'var_call_ioHf39wi8QtDiRcv7ZGNUfe8': 'file_storage/call_ioHf39wi8QtDiRcv7ZGNUfe8.json'}

exec(code, env_args)
