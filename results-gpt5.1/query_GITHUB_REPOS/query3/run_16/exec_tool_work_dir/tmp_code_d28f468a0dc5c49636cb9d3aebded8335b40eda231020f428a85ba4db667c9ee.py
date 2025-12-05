code = """import json, pandas as pd
from pathlib import Path

path = Path(var_call_V5L5MpGTU7aDdoYkW6LbXx0i)
repos = pd.read_json(path).repo_name.tolist()

chunks = []
for i in range(0, len(repos), 500):
    chunk = repos[i:i+500]
    in_list = ','.join("'" + r.replace("'", "''") + "'" for r in chunk)
    chunks.append(f"SELECT COUNT(*) AS cnt FROM commits WHERE repo_name IN ({in_list}) AND message IS NOT NULL AND LENGTH(message) < 1000 AND LOWER(TRIM(message)) NOT LIKE 'merge%' AND LOWER(TRIM(message)) NOT LIKE 'update%' AND LOWER(TRIM(message)) NOT LIKE 'test%'")

queries = ' UNION ALL '.join(chunks)

result = queries

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_SPEZoHqZYysUMowcpoCxejNL': [{'cnt': '15016'}], 'var_call_V5L5MpGTU7aDdoYkW6LbXx0i': 'file_storage/call_V5L5MpGTU7aDdoYkW6LbXx0i.json'}

exec(code, env_args)
