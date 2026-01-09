code = """import json, pandas as pd

# load repo list from file
path = var_call_0baRH7YZZsXz3pmdLd8Nns3t
with open(path, 'r') as f:
    repos = json.load(f)
repo_names = sorted({r['repo_name'] for r in repos if r.get('repo_name')})

# build VALUES list for duckdb query
vals = ", ".join(["('" + rn.replace("'","''") + "')" for rn in repo_names])
query = f"""
SELECT COUNT(*) AS commit_message_count
FROM commits
WHERE message IS NOT NULL
  AND length(message) < 1000
  AND lower(message) NOT LIKE 'merge%'
  AND lower(message) NOT LIKE 'update%'
  AND lower(message) NOT LIKE 'test%'
  AND repo_name IN (SELECT repo_name FROM (VALUES {vals}) t(repo_name));
"""

result = {"repo_count": len(repo_names), "duckdb_query": query}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_0baRH7YZZsXz3pmdLd8Nns3t': 'file_storage/call_0baRH7YZZsXz3pmdLd8Nns3t.json', 'var_call_0PuI8vpqbhfyPHaqebAmiMXY': [{'commit_message_count': '0'}]}

exec(code, env_args)
