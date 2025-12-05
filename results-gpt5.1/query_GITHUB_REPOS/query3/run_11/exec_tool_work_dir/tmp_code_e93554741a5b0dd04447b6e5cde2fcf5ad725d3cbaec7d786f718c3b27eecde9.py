code = """import json
import pandas as pd

# load repo list from file path
path = var_call_EM2i1rOgD7VbHoH1a8kq1shD
with open(path, 'r') as f:
    repos = json.load(f)

repo_names = [r['repo_name'] for r in repos]

# build IN clause batches to avoid too large query
batches = []
step = 500
for i in range(0, len(repo_names), step):
    batch = repo_names[i:i+step]
    in_list = ",".join("'" + r.replace("'", "''") + "'" for r in batch)
    q = f"SELECT COUNT(*) AS cnt FROM commits c WHERE c.repo_name IN ({in_list}) " \
        "AND c.message IS NOT NULL " \
        "AND LENGTH(c.message) < 1000 " \
        "AND NOT (LOWER(TRIM(c.message)) LIKE 'merge%' " \
        "OR LOWER(TRIM(c.message)) LIKE 'update%' " \
        "OR LOWER(TRIM(c.message)) LIKE 'test%');"
    batches.append(q)

print('__RESULT__:')
print(json.dumps(batches))"""

env_args = {'var_call_0476aUYCHzqDQk2nVUx99BHL': 'file_storage/call_0476aUYCHzqDQk2nVUx99BHL.json', 'var_call_EM2i1rOgD7VbHoH1a8kq1shD': 'file_storage/call_EM2i1rOgD7VbHoH1a8kq1shD.json'}

exec(code, env_args)
