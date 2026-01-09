code = """import json, pandas as pd

# Load repos list (may be stored as a JSON file path)
repos_src = var_call_JJdLhLCaS28fYsDOhaKyGVIV
if isinstance(repos_src, str):
    with open(repos_src, 'r', encoding='utf-8') as f:
        repos = json.load(f)
else:
    repos = repos_src

repo_names = sorted({r['repo_name'] for r in repos if r.get('repo_name')})

# Build an IN list safely for SQL
# DuckDB uses single quotes; escape any single quotes in names (unlikely)
in_list = ','.join(["'" + rn.replace("'", "''") + "'" for rn in repo_names])

query = f"""
SELECT COUNT(*) AS commit_message_count
FROM commits
WHERE repo_name IN ({in_list})
  AND message IS NOT NULL
  AND LENGTH(message) < 1000
  AND LOWER(message) NOT LIKE 'merge%'
  AND LOWER(message) NOT LIKE 'update%'
  AND LOWER(message) NOT LIKE 'test%'
"""

result = {'duckdb_query': query, 'repo_count': len(repo_names)}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_JJdLhLCaS28fYsDOhaKyGVIV': 'file_storage/call_JJdLhLCaS28fYsDOhaKyGVIV.json', 'var_call_91MlK4dH5eiW94J8HqE1u3LG': [{'commit_message_count': '15016'}]}

exec(code, env_args)
