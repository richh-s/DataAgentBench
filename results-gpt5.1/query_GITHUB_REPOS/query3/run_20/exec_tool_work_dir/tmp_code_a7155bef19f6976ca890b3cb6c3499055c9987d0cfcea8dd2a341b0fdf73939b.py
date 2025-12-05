code = """import json, pandas as pd
from pathlib import Path

path = Path(var_call_Ok6LdbxLXsiVm8N94WDLDxGU)
repos = pd.read_json(path)
repo_list = repos['repo_name'].tolist()

# Build an IN clause batch query to avoid too many parameters at once
batches = []
step = 500
for i in range(0, len(repo_list), step):
    batch = repo_list[i:i+step]
    in_list = ",".join("'" + r.replace("'", "''") + "'" for r in batch)
    q = f"SELECT COUNT(*) AS cnt FROM commits WHERE repo_name IN ({in_list}) AND message IS NOT NULL AND LENGTH(message) < 1000 AND LOWER(TRIM(message)) NOT LIKE 'merge%' AND LOWER(TRIM(message)) NOT LIKE 'update%' AND LOWER(TRIM(message)) NOT LIKE 'test%';"
    batches.append(q)

print('__RESULT__:')
print(json.dumps(batches))"""

env_args = {'var_call_Ok6LdbxLXsiVm8N94WDLDxGU': 'file_storage/call_Ok6LdbxLXsiVm8N94WDLDxGU.json', 'var_call_zQ3fBbETpU0logpfC0ZtcXtO': [{'cnt': '15014'}]}

exec(code, env_args)
