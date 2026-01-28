code = """import json, pandas as pd

# load repo list from the json file path stored in var_call_5N5ExCtY5IwfsujnWXeMWINp
path = var_call_5N5ExCtY5IwfsujnWXeMWINp
with open(path, 'r', encoding='utf-8') as f:
    repos = json.load(f)
repo_names = sorted({r['repo_name'] for r in repos if r.get('repo_name')})

# build VALUES list for DuckDB
vals = ",".join(["('" + rn.replace("'","''") + "')" for rn in repo_names])
query = f"""
WITH target_repos(repo_name) AS (
  VALUES {vals}
)
SELECT COUNT(*) AS commit_message_count
FROM commits c
JOIN target_repos t ON t.repo_name = c.repo_name
WHERE c.message IS NOT NULL
  AND length(c.message) < 1000
  AND lower(c.message) NOT LIKE 'merge%'
  AND lower(c.message) NOT LIKE 'update%'
  AND lower(c.message) NOT LIKE 'test%';
"""

print('__RESULT__:')
print(json.dumps({'query': query}))"""

env_args = {'var_call_5N5ExCtY5IwfsujnWXeMWINp': 'file_storage/call_5N5ExCtY5IwfsujnWXeMWINp.json'}

exec(code, env_args)
