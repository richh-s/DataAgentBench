code = """import json
import pandas as pd

path = var_call_5ZTCXCHHQ70vA2Ov71Sskkcl
with open(path, 'r') as f:
    data = json.load(f)

repos = [r['repo_name'] for r in data]

chunks = []
chunk_size = 500
for i in range(0, len(repos), chunk_size):
    chunk = repos[i:i+chunk_size]
    in_list = ",".join("'" + r.replace("'", "''") + "'" for r in chunk)
    query = f"SELECT COUNT(*) AS cnt FROM commits WHERE repo_name IN ({in_list}) AND message IS NOT NULL AND length(message) < 1000 AND lower(trim(message)) NOT LIKE 'merge%' AND lower(trim(message)) NOT LIKE 'update%' AND lower(trim(message)) NOT LIKE 'test%';"
    chunks.append({"db_name": "artifacts_database", "query": query})

result = json.dumps(chunks)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_5ZTCXCHHQ70vA2Ov71Sskkcl': 'file_storage/call_5ZTCXCHHQ70vA2Ov71Sskkcl.json', 'var_call_8UInXdcmSzFezejQFgnCcOBJ': [{'cnt': '15016'}]}

exec(code, env_args)
