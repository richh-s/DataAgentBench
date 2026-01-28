code = """import json, pandas as pd

# Load repo list from stored json file
path = var_call_wlQQ57s4e1fd96riyNOnezMK
with open(path, 'r', encoding='utf-8') as f:
    repos = json.load(f)
repo_names = [r['repo_name'] for r in repos]

# Build a VALUES list for DuckDB IN clause (chunked later if needed)
# We'll query in chunks to avoid extremely long SQL.
chunk_size = 5000
clauses = []
for i in range(0, len(repo_names), chunk_size):
    chunk = repo_names[i:i+chunk_size]
    # escape single quotes
    chunk_esc = [s.replace("'", "''") for s in chunk]
    in_list = ",".join([f"'{s}'" for s in chunk_esc])
    clauses.append(f"repo_name IN ({in_list})")
where_repo = " OR ".join([f"({c})" for c in clauses]) if clauses else "FALSE"

query = f"""
SELECT COUNT(*) AS cnt
FROM commits
WHERE message IS NOT NULL
  AND length(message) < 1000
  AND lower(substr(message, 1, 5)) <> 'merge'
  AND lower(substr(message, 1, 6)) <> 'update'
  AND lower(substr(message, 1, 4)) <> 'test'
  AND ({where_repo});
"""

out = {'query': query, 'repo_count': len(repo_names)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_wlQQ57s4e1fd96riyNOnezMK': 'file_storage/call_wlQQ57s4e1fd96riyNOnezMK.json'}

exec(code, env_args)
