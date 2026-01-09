code = """import json, pandas as pd

# load repo list from file
path = var_call_yYjIRG4qCqOhEEBqlqy92KG2
with open(path, 'r') as f:
    repos = json.load(f)
repo_names = sorted({r['repo_name'] for r in repos if r.get('repo_name')})

# build a DuckDB-safe IN list (escape single quotes)
vals = ",".join(["'" + rn.replace("'","''") + "'" for rn in repo_names])

# craft query
query = f"""
SELECT COUNT(*) AS cnt
FROM commits
WHERE repo_name IN ({vals})
  AND message IS NOT NULL
  AND length(message) < 1000
  AND lower(substr(message, 1, 5)) <> 'merge'
  AND lower(substr(message, 1, 6)) <> 'update'
  AND lower(substr(message, 1, 4)) <> 'test'
"""

import os
res = {'repo_count': len(repo_names), 'sql': query}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_yYjIRG4qCqOhEEBqlqy92KG2': 'file_storage/call_yYjIRG4qCqOhEEBqlqy92KG2.json', 'var_call_B7tk1cNsbKv9FnTWAfy1EhMD': [{'cnt': '15016'}], 'var_call_9NHC9inv8ymahY6AKD2ImXqA': [{'cnt': '17976'}]}

exec(code, env_args)
