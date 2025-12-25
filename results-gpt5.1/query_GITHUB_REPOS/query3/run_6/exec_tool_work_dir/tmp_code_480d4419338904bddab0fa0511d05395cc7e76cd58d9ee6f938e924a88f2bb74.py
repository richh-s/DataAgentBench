code = """import json
import pandas as pd

# var_call_ZJ21pB2Rbpf2CfuOlj962syJ is a path to the full JSON result
with open(var_call_ZJ21pB2Rbpf2CfuOlj962syJ, 'r') as f:
    repo_list = json.load(f)

repos = [r['repo_name'] for r in repo_list]

# Build an IN clause in chunks to avoid SQL limits
chunks = []
chunk_size = 500
for i in range(0, len(repos), chunk_size):
    chunk = repos[i:i+chunk_size]
    in_list = ",".join(["'" + r.replace("'", "''") + "'" for r in chunk])
    q = f"SELECT COUNT(*) AS cnt FROM commits WHERE repo_name IN ({in_list}) AND message IS NOT NULL AND length(message) < 1000 AND lower(trim(message)) NOT LIKE 'merge%' AND lower(trim(message)) NOT LIKE 'update%' AND lower(trim(message)) NOT LIKE 'test%';"
    chunks.append(q)

# Store the generated queries
result = chunks

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ZJ21pB2Rbpf2CfuOlj962syJ': 'file_storage/call_ZJ21pB2Rbpf2CfuOlj962syJ.json', 'var_call_IuQM6X8Y1Ntstwd9EAtPYa5s': [{'cnt': '15016'}]}

exec(code, env_args)
