code = """import json, pandas as pd
import os

path = var_call_ZeR2ZIiOSC2jRtY2OiRjNuK3
with open(path, 'r') as f:
    data = json.load(f)
repos = [r['repo_name'] for r in data]
# Build an IN clause chunked to avoid too-long queries
chunks = []
chunk_size = 500
for i in range(0, len(repos), chunk_size):
    subset = repos[i:i+chunk_size]
    in_list = ",".join(["'" + r.replace("'", "''") + "'" for r in subset])
    chunks.append(f"repo_name IN ({in_list})")

queries = [f"SELECT COUNT(*) as cnt FROM commits WHERE {cond} AND message IS NOT NULL AND length(message) < 1000 AND lower(message) NOT LIKE 'merge%' AND lower(message) NOT LIKE 'update%' AND lower(message) NOT LIKE 'test%';" for cond in chunks]

result = json.dumps(queries)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_s5XpVkz7GX1ztX4tZ1k5XAd7': [{'1': '1'}], 'var_call_ZeR2ZIiOSC2jRtY2OiRjNuK3': 'file_storage/call_ZeR2ZIiOSC2jRtY2OiRjNuK3.json'}

exec(code, env_args)
