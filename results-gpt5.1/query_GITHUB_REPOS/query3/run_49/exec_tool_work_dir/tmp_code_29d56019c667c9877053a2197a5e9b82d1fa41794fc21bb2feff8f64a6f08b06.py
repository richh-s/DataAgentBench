code = """import json, pandas as pd
from pathlib import Path

# Load full repo_name list from the JSON file path stored in var_call_MoOY0lqBnUDT2bjDrmpU0rdt
path = Path(var_call_MoOY0lqBnUDT2bjDrmpU0rdt)
with path.open() as f:
    repos = json.load(f)
repo_names = [r['repo_name'] for r in repos]

# Build an IN clause batched to avoid overly long queries
batch_size = 500
batches = [repo_names[i:i+batch_size] for i in range(0, len(repo_names), batch_size)]

queries = []
for batch in batches:
    in_list = ",".join("'" + name.replace("'", "''") + "'" for name in batch)
    q = f"SELECT COUNT(*) AS cnt FROM commits WHERE repo_name IN ({in_list}) AND message IS NOT NULL AND LENGTH(message) < 1000 AND LOWER(TRIM(message)) NOT LIKE 'merge%' AND LOWER(TRIM(message)) NOT LIKE 'update%' AND LOWER(TRIM(message)) NOT LIKE 'test%';"
    queries.append(q)

result = json.dumps(queries)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_MoOY0lqBnUDT2bjDrmpU0rdt': 'file_storage/call_MoOY0lqBnUDT2bjDrmpU0rdt.json', 'var_call_xWSXVCnrggCfGtolnDm4n5cG': [{'cnt': '15014'}]}

exec(code, env_args)
