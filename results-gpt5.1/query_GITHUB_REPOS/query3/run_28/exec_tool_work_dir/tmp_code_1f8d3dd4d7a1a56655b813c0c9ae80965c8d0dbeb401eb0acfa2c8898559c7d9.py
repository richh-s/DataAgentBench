code = """import json
import pandas as pd

# var_call_HaVvi3fk2EZGN6KtyKTJmwgU contains the file path or list; handle both
repos_data = var_call_HaVvi3fk2EZGN6KtyKTJmwgU
if isinstance(repos_data, str):
    # it's a file path
    with open(repos_data, 'r') as f:
        repos = json.load(f)
else:
    repos = repos_data

# Extract repo_name list and chunk
repo_names = [r['repo_name'] for r in repos]
chunk_size = 500
chunks = [repo_names[i:i+chunk_size] for i in range(0, len(repo_names), chunk_size)]

queries = []
for ch in chunks:
    in_list = ",".join(["'" + x.replace("'", "''") + "'" for x in ch])
    q = f"SELECT COUNT(*) AS cnt FROM commits WHERE repo_name IN ({in_list}) AND message IS NOT NULL AND length(message) < 1000 AND lower(trim(message)) NOT LIKE 'merge%' AND lower(trim(message)) NOT LIKE 'update%' AND lower(trim(message)) NOT LIKE 'test%';"
    queries.append(q)

result = json.dumps(queries)

print("__RESULT__:")
print(result)"""

env_args = {'var_call_FUOhsQkimDKc5WFfZdZX1lST': [{'cnt': '15016'}], 'var_call_HaVvi3fk2EZGN6KtyKTJmwgU': 'file_storage/call_HaVvi3fk2EZGN6KtyKTJmwgU.json'}

exec(code, env_args)
