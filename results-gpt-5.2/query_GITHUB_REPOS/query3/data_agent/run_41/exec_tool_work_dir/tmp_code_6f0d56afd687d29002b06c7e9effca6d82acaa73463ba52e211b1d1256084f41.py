code = """import json

repos = var_call_aqTgJ5scw4sSLZp15jCw9SkE
if isinstance(repos, str):
    with open(repos, 'r') as f:
        repos = json.load(f)
repo_names = [r['repo_name'] for r in repos]

chunk_size = 500
chunks = []
for i in range(0, len(repo_names), chunk_size):
    chunk = repo_names[i:i+chunk_size]
    in_list = ','.join(["'" + s.replace("'","''") + "'" for s in chunk])
    chunks.append('repo_name IN (' + in_list + ')')

where_repo = '(' + ' OR '.join(chunks) + ')' if chunks else 'FALSE'

query = (
"SELECT COUNT(*) AS commit_message_count\n"
"FROM commits\n"
"WHERE message IS NOT NULL\n"
"  AND length(message) < 1000\n"
"  AND lower(message) NOT LIKE 'merge%'\n"
"  AND lower(message) NOT LIKE 'update%'\n"
"  AND lower(message) NOT LIKE 'test%'\n"
"  AND " + where_repo + ";"
)

print('__RESULT__:')
print(json.dumps(query))"""

env_args = {'var_call_aqTgJ5scw4sSLZp15jCw9SkE': 'file_storage/call_aqTgJ5scw4sSLZp15jCw9SkE.json', 'var_call_pPp4Pnei4ElYnBklsWKXywUV': [{'commit_message_count': '15016'}]}

exec(code, env_args)
