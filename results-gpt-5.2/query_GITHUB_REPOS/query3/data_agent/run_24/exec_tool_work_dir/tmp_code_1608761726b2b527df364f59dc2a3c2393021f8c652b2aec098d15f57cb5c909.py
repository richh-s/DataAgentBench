code = """import json

path = var_call_je9DJvnrwJLDbyejB6BzVRWc
with open(path, 'r', encoding='utf-8') as f:
    repos = json.load(f)
repo_names = sorted({r.get('repo_name') for r in repos if r.get('repo_name')})

vals_list = []
for rn in repo_names:
    vals_list.append("('" + rn.replace("'","''") + "')")
vals = ','.join(vals_list)

query = (
"SELECT COUNT(*)::BIGINT AS commit_message_count\n"
"FROM commits\n"
"WHERE message IS NOT NULL\n"
"  AND length(message) < 1000\n"
"  AND lower(message) NOT LIKE 'merge%'\n"
"  AND lower(message) NOT LIKE 'update%'\n"
"  AND lower(message) NOT LIKE 'test%'\n"
"  AND repo_name IN (SELECT repo_name FROM (VALUES " + vals + ") v(repo_name));"
)

print('__RESULT__:')
print(json.dumps({'query': query, 'repo_count': len(repo_names)}))"""

env_args = {'var_call_je9DJvnrwJLDbyejB6BzVRWc': 'file_storage/call_je9DJvnrwJLDbyejB6BzVRWc.json', 'var_call_U8ZFCgipRR8iRUxgWxz1ov2k': [{'commit_message_count': '0'}]}

exec(code, env_args)
