code = """import json, pandas as pd

# load repo list from file path in var_call_m5ldAFLHfT69bMiVmOHUwW42
path = var_call_m5ldAFLHfT69bMiVmOHUwW42
with open(path, 'r', encoding='utf-8') as f:
    repos = json.load(f)
repo_names = [r['repo_name'] for r in repos]

# Build a DuckDB IN list safely by json dumping and joining
# We'll output the count query text and run it via query_db in next step
escaped = ",".join(["'" + rn.replace("'","''") + "'" for rn in repo_names])
q = f"""
SELECT COUNT(*) AS commit_message_count
FROM commits
WHERE repo_name IN ({escaped})
  AND message IS NOT NULL
  AND LENGTH(message) < 1000
  AND LOWER(message) NOT LIKE 'merge%'
  AND LOWER(message) NOT LIKE 'update%'
  AND LOWER(message) NOT LIKE 'test%';
""".strip()

print('__RESULT__:')
print(json.dumps({'query': q, 'repo_count': len(repo_names)}))"""

env_args = {'var_call_m5ldAFLHfT69bMiVmOHUwW42': 'file_storage/call_m5ldAFLHfT69bMiVmOHUwW42.json', 'var_call_QeQqX2AX98iUfrFERXid8eVQ': [{'commit_message_count': '15016'}]}

exec(code, env_args)
