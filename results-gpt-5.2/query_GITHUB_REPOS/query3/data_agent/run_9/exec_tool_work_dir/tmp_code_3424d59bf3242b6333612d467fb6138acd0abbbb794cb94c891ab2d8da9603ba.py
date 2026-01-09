code = """import json, pandas as pd

# load repo list from prior call
path = var_call_0OjodcdmTxSeTjqnYics1DUZ
with open(path, 'r') as f:
    repos = json.load(f)
repo_names = [r['repo_name'] for r in repos]

# build an IN clause safely by escaping single quotes
escaped = [rn.replace("'", "''") for rn in repo_names]
# DuckDB has a limit on expression length; use VALUES join instead
values_rows = ",".join([f"('{rn}')" for rn in escaped])
query = f"""
SELECT COUNT(*) AS cnt
FROM commits c
JOIN (VALUES {values_rows}) v(repo_name) ON v.repo_name = c.repo_name
WHERE c.message IS NOT NULL
  AND length(c.message) < 1000
  AND lower(c.message) NOT LIKE 'merge%'
  AND lower(c.message) NOT LIKE 'update%'
  AND lower(c.message) NOT LIKE 'test%'
"""

out = {"query": query}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_0OjodcdmTxSeTjqnYics1DUZ': 'file_storage/call_0OjodcdmTxSeTjqnYics1DUZ.json'}

exec(code, env_args)
