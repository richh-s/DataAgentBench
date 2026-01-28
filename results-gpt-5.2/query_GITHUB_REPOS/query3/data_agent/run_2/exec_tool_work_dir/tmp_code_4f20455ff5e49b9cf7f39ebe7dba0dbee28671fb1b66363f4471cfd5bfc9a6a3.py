code = """import json, pandas as pd

# Load repo list from file path if needed
repo_res = var_call_mAoSYumjkMfXBdUqfAhX4ASC
if isinstance(repo_res, str):
    with open(repo_res, 'r', encoding='utf-8') as f:
        repo_res = json.load(f)
repos = sorted({r['repo_name'] for r in repo_res if r.get('repo_name')})

# Build a DuckDB IN list safely
# Escape single quotes by doubling
in_list = ','.join(["'" + r.replace("'","''") + "'" for r in repos])

query = f"""
SELECT COUNT(*) AS commit_message_count
FROM commits
WHERE message IS NOT NULL
  AND length(message) < 1000
  AND NOT (lower(message) LIKE 'merge%'
           OR lower(message) LIKE 'update%'
           OR lower(message) LIKE 'test%')
  AND repo_name IN ({in_list});
"""

out = json.dumps({'query': query, 'repo_count': len(repos)})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_mAoSYumjkMfXBdUqfAhX4ASC': 'file_storage/call_mAoSYumjkMfXBdUqfAhX4ASC.json'}

exec(code, env_args)
