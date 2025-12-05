code = """import json
import pandas as pd

# Load full repo list from file
path = var_call_cIMrUkDYffwVUoCMNnxVH1o2
with open(path, 'r') as f:
    repos = json.load(f)

repo_names = [r['repo_name'] for r in repos]

# Build an IN clause chunked to avoid overly large queries
chunks = []
chunk_size = 900
for i in range(0, len(repo_names), chunk_size):
    chunk = repo_names[i:i+chunk_size]
    in_list = ",".join("'" + r.replace("'", "''") + "'" for r in chunk)
    where = f"repo_name IN ({in_list})"
    chunks.append(where)

# Build the final WHERE clause joined with OR
where_clauses = " OR ".join(f"({w})" for w in chunks)

query = "SELECT COUNT(*) AS cnt FROM commits WHERE " + where_clauses + " AND message IS NOT NULL AND LENGTH(message) < 1000 AND LOWER(message) NOT LIKE 'merge%' AND LOWER(message) NOT LIKE 'update%' AND LOWER(message) NOT LIKE 'test%';"

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_call_JT0tI5yvoOQmXXviljeJiPVp': ['commits', 'contents', 'files'], 'var_call_cIMrUkDYffwVUoCMNnxVH1o2': 'file_storage/call_cIMrUkDYffwVUoCMNnxVH1o2.json'}

exec(code, env_args)
