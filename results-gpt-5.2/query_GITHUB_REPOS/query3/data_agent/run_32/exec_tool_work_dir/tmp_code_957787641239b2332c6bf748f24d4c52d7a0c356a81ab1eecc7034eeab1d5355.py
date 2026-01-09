code = """import json, pandas as pd

# load repo list from sqlite query result file
path = var_call_6EXlZ3yhaGPRTgnLYbXxpZIf
with open(path, 'r', encoding='utf-8') as f:
    repos = json.load(f)
repo_names = [r['repo_name'] for r in repos]

# chunk IN clause to avoid huge query strings
chunks = []
chunk_size = 500
for i in range(0, len(repo_names), chunk_size):
    chunk = repo_names[i:i+chunk_size]
    # escape single quotes
    vals = ",".join(["'" + x.replace("'","''") + "'" for x in chunk])
    chunks.append(f"repo_name IN ({vals})")
where_repo = " OR ".join([f"({c})" for c in chunks]) if chunks else "FALSE"

query = f"""
SELECT COUNT(*) AS cnt
FROM commits
WHERE ({where_repo})
  AND message IS NOT NULL
  AND LENGTH(message) < 1000
  AND LOWER(message) NOT LIKE 'merge%'
  AND LOWER(message) NOT LIKE 'update%'
  AND LOWER(message) NOT LIKE 'test%'
"""

out = {'query': query}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_6EXlZ3yhaGPRTgnLYbXxpZIf': 'file_storage/call_6EXlZ3yhaGPRTgnLYbXxpZIf.json', 'var_call_apix87Gs96Yhv3FcUZcaVsce': [{'cnt': '0'}]}

exec(code, env_args)
