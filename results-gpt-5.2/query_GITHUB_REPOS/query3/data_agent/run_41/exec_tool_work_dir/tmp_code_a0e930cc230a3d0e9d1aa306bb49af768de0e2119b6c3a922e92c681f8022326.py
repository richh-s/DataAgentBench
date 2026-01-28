code = """import json

repos = var_call_aqTgJ5scw4sSLZp15jCw9SkE
if isinstance(repos, str):
    with open(repos, 'r') as f:
        repos = json.load(f)
repo_names = [r['repo_name'] for r in repos]

chunk_size = 500
conds = []
for i in range(0, len(repo_names), chunk_size):
    chunk = repo_names[i:i+chunk_size]
    in_list = ','.join(["'" + s.replace("'","''") + "'" for s in chunk])
    conds.append('repo_name IN (' + in_list + ')')
where_repo = '(' + ' OR '.join(conds) + ')' if conds else 'FALSE'

query = (
    "SELECT COUNT(*) AS commit_message_count "
    "FROM commits "
    "WHERE message IS NOT NULL "
    "AND length(message) < 1000 "
    "AND lower(message) NOT LIKE 'merge%' "
    "AND lower(message) NOT LIKE 'update%' "
    "AND lower(message) NOT LIKE 'test%' "
    "AND " + where_repo
)

print('__RESULT__:')
print(json.dumps(query))"""

env_args = {'var_call_aqTgJ5scw4sSLZp15jCw9SkE': 'file_storage/call_aqTgJ5scw4sSLZp15jCw9SkE.json', 'var_call_pPp4Pnei4ElYnBklsWKXywUV': [{'commit_message_count': '15016'}]}

exec(code, env_args)
