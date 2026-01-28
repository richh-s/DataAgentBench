code = """import json, pandas as pd

# Load repo list (Shell + Apache-2.0) from the sqlite query result file
p = var_call_w084PNVwsgr7OJGySoIsAbrX
with open(p, 'r', encoding='utf-8') as f:
    repos = json.load(f)
repo_names = [r['repo_name'] for r in repos]

# Build a DuckDB IN list safely (escape single quotes)
repo_names_escaped = [rn.replace("'", "''") for rn in repo_names]
# If empty, result is 0
if not repo_names_escaped:
    out = json.dumps({"count": 0})
    print('__RESULT__:')
    print(out)
else:
    # Chunk to avoid overly long query strings
    chunks = []
    chunk_size = 500
    for i in range(0, len(repo_names_escaped), chunk_size):
        chunk = repo_names_escaped[i:i+chunk_size]
        in_list = ",".join([f"'{x}'" for x in chunk])
        chunks.append(f"repo_name IN ({in_list})")
    where_repo = " OR ".join([f"({c})" for c in chunks])

    query = f"""
    SELECT COUNT(*) AS cnt
    FROM commits
    WHERE message IS NOT NULL
      AND length(message) < 1000
      AND lower(message) NOT LIKE 'merge%'
      AND lower(message) NOT LIKE 'update%'
      AND lower(message) NOT LIKE 'test%'
      AND ({where_repo})
    """

    # run duckdb query via query_db tool is not possible inside python; so just output the query and repo_count
    out = json.dumps({"repo_count": len(repo_names_escaped), "duckdb_query": query})
    print('__RESULT__:')
    print(out)"""

env_args = {'var_call_w084PNVwsgr7OJGySoIsAbrX': 'file_storage/call_w084PNVwsgr7OJGySoIsAbrX.json'}

exec(code, env_args)
