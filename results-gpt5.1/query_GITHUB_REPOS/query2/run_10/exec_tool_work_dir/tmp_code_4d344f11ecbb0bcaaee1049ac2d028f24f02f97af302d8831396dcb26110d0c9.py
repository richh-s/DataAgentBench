code = """import json, pandas as pd, os
path = var_call_yRXuhJ7KaAEfGPbkIJnO6wQi
with open(path, 'r') as f:
    data = json.load(f)
# count occurrences of each id
counts = {}
repos = {}
for row in data:
    fid = row['id']
    repo = row['sample_repo_name']
    counts[fid] = counts.get(fid, 0) + 1
    # track one repo per id (arbitrary if multiple)
    repos.setdefault(fid, repo)
# find max frequency
max_count = max(counts.values()) if counts else 0
# get ids with max_count
top_ids = [fid for fid, c in counts.items() if c == max_count]
# map to repos
top_repos = sorted({repos[fid] for fid in top_ids})
result = {"max_count": max_count, "top_ids": top_ids, "top_repos": top_repos}
result_str = json.dumps(result)
print("__RESULT__:")
print(result_str)"""

env_args = {'var_call_pddqNrrwb0815PRc8mYKARnE': [], 'var_call_9UI7T8AlauMNAKgp257pypKF': [], 'var_call_yRXuhJ7KaAEfGPbkIJnO6wQi': 'file_storage/call_yRXuhJ7KaAEfGPbkIJnO6wQi.json'}

exec(code, env_args)
