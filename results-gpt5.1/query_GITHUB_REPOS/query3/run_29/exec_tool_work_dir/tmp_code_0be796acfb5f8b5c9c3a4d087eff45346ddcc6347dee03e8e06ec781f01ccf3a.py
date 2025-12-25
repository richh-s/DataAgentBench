code = """import json, pandas as pd
from pathlib import Path

path = Path(var_call_bkdNXF7jaWHseyIYm1dB8MBf)
repos = pd.read_json(path)
repo_list = repos['repo_name'].tolist()
chunks = []
chunk_size = 500
for i in range(0, len(repo_list), chunk_size):
    chunk = repo_list[i:i+chunk_size]
    in_list = ",".join("'" + r.replace("'", "''") + "'" for r in chunk)
    query = f"SELECT COUNT(*) AS cnt FROM commits WHERE repo_name IN ({in_list}) AND message IS NOT NULL AND length(message) < 1000 AND lower(trim(message)) NOT LIKE 'merge%' AND lower(trim(message)) NOT LIKE 'update%' AND lower(trim(message)) NOT LIKE 'test%';"
    chunks.append(query)

full_query = " UNION ALL ".join(chunks)

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_call_bkdNXF7jaWHseyIYm1dB8MBf': 'file_storage/call_bkdNXF7jaWHseyIYm1dB8MBf.json', 'var_call_9rsuXKyLnihiAUEqOV6By447': [{'1': '1'}]}

exec(code, env_args)
