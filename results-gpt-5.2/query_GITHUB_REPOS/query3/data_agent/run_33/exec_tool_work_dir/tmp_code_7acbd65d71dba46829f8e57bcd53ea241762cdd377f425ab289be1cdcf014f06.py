code = """import json
import pandas as pd

# var_call_5GUg84X5hO9MKHGRyKudnnJ8 contains a file path with repo list
path = var_call_5GUg84X5hO9MKHGRyKudnnJ8
with open(path, 'r', encoding='utf-8') as f:
    repos = json.load(f)
repo_names = [r['repo_name'] for r in repos]

# Build chunked IN clauses for DuckDB
chunks = []
chunk_size = 500
for i in range(0, len(repo_names), chunk_size):
    sub = repo_names[i:i+chunk_size]
    quoted = ",".join(["'" + s.replace("'","''") + "'" for s in sub])
    chunks.append(f"repo_name IN ({quoted})")
where_in = " OR ".join([f"({c})" for c in chunks]) if chunks else "FALSE"

query = (
"SELECT COUNT(*) AS commit_message_count\n"
"FROM commits\n"
"WHERE message IS NOT NULL\n"
"  AND length(message) < 1000\n"
"  AND lower(substr(message, 1, 5)) <> 'merge'\n"
"  AND lower(substr(message, 1, 6)) <> 'update'\n"
"  AND lower(substr(message, 1, 4)) <> 'test'\n"
f"  AND ({where_in});\n"
)

result = {"repo_count": len(repo_names), "duckdb_query": query}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_5GUg84X5hO9MKHGRyKudnnJ8': 'file_storage/call_5GUg84X5hO9MKHGRyKudnnJ8.json'}

exec(code, env_args)
