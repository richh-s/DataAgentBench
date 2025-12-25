code = """import json
import pandas as pd

# var_call_09zzTGBunaXfb78p5wIpLxXD contains a file path string when large; handle both cases
repos_data = var_call_09zzTGBunaXfb78p5wIpLxXD
if isinstance(repos_data, str):
    # Load full result from JSON file
    with open(repos_data, 'r') as f:
        repos = json.load(f)
else:
    repos = repos_data

repo_names = [r['repo_name'] for r in repos]

# Build SQL IN clause in chunks to avoid size limits
chunks = []
chunk_size = 500
for i in range(0, len(repo_names), chunk_size):
    chunk = repo_names[i:i+chunk_size]
    in_list = ",".join(["'" + name.replace("'", "''") + "'" for name in chunk])
    query = f"SELECT COUNT(*) AS cnt FROM commits WHERE repo_name IN ({in_list}) AND message IS NOT NULL AND length(message) < 1000 AND LOWER(message) NOT LIKE 'merge%' AND LOWER(message) NOT LIKE 'update%' AND LOWER(message) NOT LIKE 'test%';"
    chunks.append(query)

# Store all queries as a JSON list string
result = json.dumps(chunks)

print("__RESULT__:")
print(result)"""

env_args = {'var_call_09zzTGBunaXfb78p5wIpLxXD': 'file_storage/call_09zzTGBunaXfb78p5wIpLxXD.json', 'var_call_8eXnlDmaHEFr3cOoTLpSTdFC': [{'cnt': '15016'}]}

exec(code, env_args)
