code = """import json, pandas as pd

path = var_call_6KVzmpo18ziicuuz89ZbYccf
with open(path, 'r') as f:
    data = json.load(f)
repos = [r['repo_name'] for r in data]

chunks = []
chunk_size = 500
for i in range(0, len(repos), chunk_size):
    chunk = repos[i:i+chunk_size]
    in_list = "','".join(chunk)
    query = f"SELECT COUNT(*) AS cnt FROM commits WHERE repo_name IN ('{in_list}') AND message IS NOT NULL AND LENGTH(message) < 1000 AND LOWER(TRIM(message)) NOT LIKE 'merge%' AND LOWER(TRIM(message)) NOT LIKE 'update%' AND LOWER(TRIM(message)) NOT LIKE 'test%';"
    chunks.append(query)

print("__RESULT__:")
print(json.dumps(chunks))"""

env_args = {'var_call_G867ARaQK7HhcGlpPR2cUMN4': [{'cnt': '15016'}], 'var_call_6KVzmpo18ziicuuz89ZbYccf': 'file_storage/call_6KVzmpo18ziicuuz89ZbYccf.json'}

exec(code, env_args)
