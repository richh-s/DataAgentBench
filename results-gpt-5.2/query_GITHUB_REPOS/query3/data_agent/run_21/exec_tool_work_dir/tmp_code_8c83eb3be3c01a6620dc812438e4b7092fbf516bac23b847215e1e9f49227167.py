code = """import json, pandas as pd

# load repo list from the json file path stored in var_call_Nwq1180vjP6iuAH2QwE3QsbT
path = var_call_Nwq1180vjP6iuAH2QwE3QsbT
with open(path, 'r', encoding='utf-8') as f:
    repos = json.load(f)
repo_names = [r['repo_name'] for r in repos]

# chunk into groups for SQL IN clauses
chunks = []
chunk = []
max_chunk = 800  # keep query size manageable
for rn in repo_names:
    chunk.append(rn)
    if len(chunk) >= max_chunk:
        chunks.append(chunk)
        chunk = []
if chunk:
    chunks.append(chunk)

queries = []
for ch in chunks:
    # escape single quotes
    items = ",".join(["'" + s.replace("'","''") + "'" for s in ch])
    q = f"SELECT COUNT(*) AS c FROM commits WHERE message IS NOT NULL AND LENGTH(message) < 1000 AND LOWER(TRIM(message)) NOT LIKE 'merge%' AND LOWER(TRIM(message)) NOT LIKE 'update%' AND LOWER(TRIM(message)) NOT LIKE 'test%' AND repo_name IN ({items});"
    queries.append(q)

out = {'num_repos': len(repo_names), 'queries': queries[:5], 'num_queries': len(queries)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Nwq1180vjP6iuAH2QwE3QsbT': 'file_storage/call_Nwq1180vjP6iuAH2QwE3QsbT.json'}

exec(code, env_args)
