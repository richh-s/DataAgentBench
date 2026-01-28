code = """import json, pandas as pd

# Load repo list (may be file path)
repo_res = var_call_O8FLJdxKgenhe2IVl3Lurdja
if isinstance(repo_res, str):
    with open(repo_res, 'r', encoding='utf-8') as f:
        repo_res = json.load(f)
repos = [r['repo_name'] for r in repo_res]

# Build DuckDB IN list safely
# Escape single quotes by doubling
repos_escaped = [r.replace("'", "''") for r in repos]

# To avoid overly long IN clauses, chunk into groups
chunks = [repos_escaped[i:i+500] for i in range(0, len(repos_escaped), 500)]

filters = []
for ch in chunks:
    filters.append("repo_name IN (" + ",".join(["'"+x+"'" for x in ch]) + ")")
repo_filter_sql = "(" + " OR ".join(filters) + ")" if filters else "FALSE"

query = f"""
SELECT COUNT(*)::BIGINT AS commit_message_count
FROM commits
WHERE {repo_filter_sql}
  AND message IS NOT NULL
  AND length(message) < 1000
  AND lower(message) NOT LIKE 'merge%'
  AND lower(message) NOT LIKE 'update%'
  AND lower(message) NOT LIKE 'test%'
;"""

out = {'duckdb_query': query}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_O8FLJdxKgenhe2IVl3Lurdja': 'file_storage/call_O8FLJdxKgenhe2IVl3Lurdja.json', 'var_call_u6wF6PsWKGgkVhkHI8pfuCn9': [{'commit_message_count': '0'}]}

exec(code, env_args)
