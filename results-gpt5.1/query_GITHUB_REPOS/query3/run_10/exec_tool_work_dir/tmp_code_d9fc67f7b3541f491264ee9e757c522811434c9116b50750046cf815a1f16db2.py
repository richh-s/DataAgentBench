code = """import json, pandas as pd
repos_file = var_call_7eh1FRNG0fGAJSguCEZeGofS
with open(repos_file, 'r') as f:
    repos = json.load(f)
repo_list = [r['repo_name'] for r in repos]
chunks = []
chunk_size = 500
for i in range(0, len(repo_list), chunk_size):
    chunk = repo_list[i:i+chunk_size]
    in_list = "','".join(name.replace("'", "''") for name in chunk)
    query = f"SELECT COUNT(*) AS cnt FROM commits WHERE repo_name IN ('{in_list}') AND message IS NOT NULL AND LENGTH(message) < 1000 AND LOWER(TRIM(message)) NOT LIKE 'merge%' AND LOWER(TRIM(message)) NOT LIKE 'update%' AND LOWER(TRIM(message)) NOT LIKE 'test%';"
    chunks.append(query)
result = json.dumps(chunks)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_7eh1FRNG0fGAJSguCEZeGofS': 'file_storage/call_7eh1FRNG0fGAJSguCEZeGofS.json', 'var_call_KKjxEDkV67g1dsL1vXh89Qgs': [{'1': '1'}]}

exec(code, env_args)
