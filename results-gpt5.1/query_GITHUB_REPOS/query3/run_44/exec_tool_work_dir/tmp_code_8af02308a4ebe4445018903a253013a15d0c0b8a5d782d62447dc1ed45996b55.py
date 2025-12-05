code = """import json
import pandas as pd

path = var_call_Py0C996CLMzagoAXrbPkVGaP
with open(path, 'r') as f:
    repos = json.load(f)
repo_names = [r['repo_name'] for r in repos]

# Build an IN clause chunked to avoid overly long queries
chunks = []
chunk_size = 900
for i in range(0, len(repo_names), chunk_size):
    chunk = repo_names[i:i+chunk_size]
    in_list = ",".join("'" + r.replace("'", "''") + "'" for r in chunk)
    chunks.append(f"repo_name IN ({in_list})")

conditions = " OR ".join(chunks) if chunks else "1=0"
query = "SELECT COUNT(*) AS cnt FROM commits WHERE (" + conditions + ") AND message IS NOT NULL AND length(message) < 1000 AND lower(trim(message)) NOT LIKE 'merge%' AND lower(trim(message)) NOT LIKE 'update%' AND lower(trim(message)) NOT LIKE 'test%';"

result = json.dumps({'query': query})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_Py0C996CLMzagoAXrbPkVGaP': 'file_storage/call_Py0C996CLMzagoAXrbPkVGaP.json', 'var_call_KyJd2EkyNJ30yrJKTyJII5FI': [{'cnt': '15016'}]}

exec(code, env_args)
