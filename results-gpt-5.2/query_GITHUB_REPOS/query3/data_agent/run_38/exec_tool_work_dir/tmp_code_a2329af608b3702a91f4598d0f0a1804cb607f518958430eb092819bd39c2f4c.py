code = """import json, pandas as pd

# load repo list from file path
path = var_call_ioHf39wi8QtDiRcv7ZGNUfe8
with open(path, 'r') as f:
    repos = json.load(f)
repo_names = sorted({r['repo_name'] for r in repos if r.get('repo_name')})

# create an IN clause chunked
chunks = []
chunk_size = 500
for i in range(0, len(repo_names), chunk_size):
    chunk = repo_names[i:i+chunk_size]
    in_list = ','.join(["'" + x.replace("'","''") + "'" for x in chunk])
    chunks.append(f"repo_name IN ({in_list})")
where_repos = ' OR '.join(chunks) if chunks else 'FALSE'

query = f"""
SELECT COUNT(*) AS commit_message_count
FROM commits
WHERE message IS NOT NULL
  AND length(message) < 1000
  AND lower(message) NOT LIKE 'merge%'
  AND lower(message) NOT LIKE 'update%'
  AND lower(message) NOT LIKE 'test%'
  AND ({where_repos});
""".strip()

out = json.dumps({'query': query, 'repo_count': len(repo_names)})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_ioHf39wi8QtDiRcv7ZGNUfe8': 'file_storage/call_ioHf39wi8QtDiRcv7ZGNUfe8.json'}

exec(code, env_args)
