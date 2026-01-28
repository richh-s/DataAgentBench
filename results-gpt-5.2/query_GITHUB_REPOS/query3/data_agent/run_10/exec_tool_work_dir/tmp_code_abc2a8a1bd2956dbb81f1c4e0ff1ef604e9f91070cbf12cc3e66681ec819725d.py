code = """import json, pandas as pd

# Load repo list from file if needed
src = var_call_hdegDIIzK5FCL1EEauw72YhW
if isinstance(src, str):
    with open(src, 'r', encoding='utf-8') as f:
        repos = json.load(f)
else:
    repos = src
repo_names = sorted({r['repo_name'] for r in repos if r.get('repo_name')})

# Build a DuckDB IN list safely
# Escape single quotes by doubling them
in_list = ','.join(["'" + rn.replace("'", "''") + "'" for rn in repo_names])

query = f"""
SELECT COUNT(*) AS cnt
FROM commits
WHERE message IS NOT NULL
  AND length(message) < 1000
  AND lower(message) NOT LIKE 'merge%'
  AND lower(message) NOT LIKE 'update%'
  AND lower(message) NOT LIKE 'test%'
  AND repo_name IN ({in_list});
"""

out = json.dumps({'query': query, 'repo_count': len(repo_names)})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_hdegDIIzK5FCL1EEauw72YhW': 'file_storage/call_hdegDIIzK5FCL1EEauw72YhW.json'}

exec(code, env_args)
