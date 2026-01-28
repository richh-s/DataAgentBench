code = """import json, pandas as pd

# Load repo list from sqlite query result stored in a json file
path = var_call_GvAITfP6oyVv9ugf4515BZw9
with open(path, 'r') as f:
    repos = json.load(f)
repo_list = [r['repo_name'] for r in repos]

# Build batched IN clauses and query commits count per batch
batch_size = 500
counts = []
for i in range(0, len(repo_list), batch_size):
    batch = repo_list[i:i+batch_size]
    in_list = ','.join(["'" + s.replace("'","''") + "'" for s in batch])
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
    counts.append(q)

print('__RESULT__:')
print(json.dumps({'repo_count': len(repo_list), 'queries': counts}))"""

env_args = {'var_call_GvAITfP6oyVv9ugf4515BZw9': 'file_storage/call_GvAITfP6oyVv9ugf4515BZw9.json'}

exec(code, env_args)
