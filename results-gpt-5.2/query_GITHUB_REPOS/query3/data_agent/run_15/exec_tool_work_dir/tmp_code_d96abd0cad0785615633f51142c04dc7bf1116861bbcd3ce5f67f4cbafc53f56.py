code = """import json, pandas as pd

# Load repo list from file path
path = var_call_sLHCuX0XKU7J8rRMQoXzSiXL
with open(path, 'r', encoding='utf-8') as f:
    repos = json.load(f)
repo_names = sorted({r['repo_name'] for r in repos if r.get('repo_name')})

# Build DuckDB VALUES list for IN clause
# Escape single quotes
vals = ",\n    ".join(["('" + rn.replace("'", "''") + "')" for rn in repo_names])
query = f"""
SELECT COUNT(*) AS commit_message_count
FROM commits
WHERE message IS NOT NULL
  AND LENGTH(message) < 1000
  AND LOWER(message) NOT LIKE 'merge%'
  AND LOWER(message) NOT LIKE 'update%'
  AND LOWER(message) NOT LIKE 'test%'
  AND repo_name IN (
    SELECT repo_name FROM (VALUES
    {vals}
    ) v(repo_name)
  );
"""

out = {
  "repo_count": len(repo_names),
  "duckdb_query": query
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_sLHCuX0XKU7J8rRMQoXzSiXL': 'file_storage/call_sLHCuX0XKU7J8rRMQoXzSiXL.json', 'var_call_PTVUCRIVmb2BwYsWqtCFjQS7': [{'commit_message_count': '0'}]}

exec(code, env_args)
