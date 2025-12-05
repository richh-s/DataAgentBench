code = """import json, pandas as pd

# load full repo list
path = var_call_pBj12lYrK0bbKyqS74qyQwzS
with open(path, 'r') as f:
    repos = json.load(f)
repo_names = [r['repo_name'] for r in repos]

# create IN clause chunks
chunks = []
for i in range(0, len(repo_names), 500):
    chunk = repo_names[i:i+500]
    in_list = ','.join("'" + n.replace("'", "''") + "'" for n in chunk)
    chunks.append(f"repo_name IN ({in_list})")

queries = ["SELECT COUNT(*) AS cnt FROM commits WHERE " + cond + " AND message IS NOT NULL AND length(message) < 1000 AND lower(trim(message)) NOT LIKE 'merge%' AND lower(trim(message)) NOT LIKE 'update%' AND lower(trim(message)) NOT LIKE 'test%'" for cond in chunks]

result = json.dumps(queries)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_tQxf67IhQdUII3AoooYPaJFx': [{'cnt': '15016'}], 'var_call_pBj12lYrK0bbKyqS74qyQwzS': 'file_storage/call_pBj12lYrK0bbKyqS74qyQwzS.json'}

exec(code, env_args)
