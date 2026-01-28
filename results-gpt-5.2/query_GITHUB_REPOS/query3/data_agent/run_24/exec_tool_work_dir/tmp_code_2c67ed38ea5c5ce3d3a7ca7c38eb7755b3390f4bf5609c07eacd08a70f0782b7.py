code = """import json

# Load repo list from file
path = var_call_je9DJvnrwJLDbyejB6BzVRWc
with open(path, 'r', encoding='utf-8') as f:
    repos = json.load(f)
repo_names = sorted({r['repo_name'] for r in repos if r.get('repo_name')})

# Build VALUES list for duckdb IN clause
vals = ','.join(["('" + rn.replace("'","''") + "')" for rn in repo_names])
query = f"""
SELECT COUNT(*)::BIGINT AS commit_message_count
FROM commits
WHERE message IS NOT NULL
  AND length(message) < 1000
  AND lower(message) NOT LIKE 'merge%'
  AND lower(message) NOT LIKE 'update%'
  AND lower(message) NOT LIKE 'test%'
  AND repo_name IN (SELECT repo_name FROM (VALUES {vals}) v(repo_name));
"""

print('__RESULT__:')
print(json.dumps({'query': query, 'repo_count': len(repo_names)}))"""

env_args = {'var_call_je9DJvnrwJLDbyejB6BzVRWc': 'file_storage/call_je9DJvnrwJLDbyejB6BzVRWc.json', 'var_call_U8ZFCgipRR8iRUxgWxz1ov2k': [{'commit_message_count': '0'}]}

exec(code, env_args)
