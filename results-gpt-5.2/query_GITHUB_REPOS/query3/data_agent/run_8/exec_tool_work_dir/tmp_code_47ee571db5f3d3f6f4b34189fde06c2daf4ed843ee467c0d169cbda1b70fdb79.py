code = """import json, pandas as pd

# load repo list from sqlite query (stored as json file path)
path = var_call_36Id3lYz6wUmBCcqmMy1OaLT
with open(path, 'r', encoding='utf-8') as f:
    repos = json.load(f)
repo_names = [r['repo_name'] for r in repos]

# create chunked IN-list queries for duckdb
chunks = [repo_names[i:i+5000] for i in range(0, len(repo_names), 5000)]
queries = []
for ch in chunks:
    in_list = ','.join(["'" + s.replace("'","''") + "'" for s in ch])
    q = f"""
    SELECT COUNT(*) AS c
    FROM commits
    WHERE message IS NOT NULL
      AND length(message) < 1000
      AND lower(message) NOT LIKE 'merge%'
      AND lower(message) NOT LIKE 'update%'
      AND lower(message) NOT LIKE 'test%'
      AND repo_name IN ({in_list});
    """
    queries.append(q)

out = {'repo_count': len(repo_names), 'duckdb_queries': queries}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_36Id3lYz6wUmBCcqmMy1OaLT': 'file_storage/call_36Id3lYz6wUmBCcqmMy1OaLT.json'}

exec(code, env_args)
