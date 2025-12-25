code = """import json, pandas as pd
path = var_call_GNAJcP1uJiBlz0TLqrfiiXLE
with open(path) as f:
    data = json.load(f)
repos = [r['repo_name'] for r in data]
# Build an IN clause, chunked to avoid huge query limits
chunks = []
for i in range(0, len(repos), 500):
    chunk = repos[i:i+500]
    in_list = ",".join("'" + r.replace("'", "''") + "'" for r in chunk)
    q = f"SELECT COUNT(*) AS cnt FROM commits WHERE repo_name IN ({in_list}) AND message IS NOT NULL AND LENGTH(message) < 1000 AND LOWER(TRIM(message)) NOT LIKE 'merge%' AND LOWER(TRIM(message)) NOT LIKE 'update%' AND LOWER(TRIM(message)) NOT LIKE 'test%';"
    chunks.append(q)
result = json.dumps(chunks)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_0iB4LDFbhllpsIO6RbzVp1tq': [{'cnt': '15016'}], 'var_call_GNAJcP1uJiBlz0TLqrfiiXLE': 'file_storage/call_GNAJcP1uJiBlz0TLqrfiiXLE.json'}

exec(code, env_args)
