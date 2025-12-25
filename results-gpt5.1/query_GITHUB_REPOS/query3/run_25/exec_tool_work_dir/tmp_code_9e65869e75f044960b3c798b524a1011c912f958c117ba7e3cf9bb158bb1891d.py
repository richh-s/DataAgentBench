code = """import json, pandas as pd
from pathlib import Path

path = Path(var_call_go05Wk3xvJMfmFUt9HSgvM1G)
repos = pd.read_json(path).repo_name.unique().tolist()

# Split repos into chunks to avoid SQL size/quoting issues
chunks = []
chunk_size = 300
for i in range(0, len(repos), chunk_size):
    sub = repos[i:i+chunk_size]
    values = ",".join([f"('{r.replace("'","''")}')" for r in sub])
    q = f"SELECT COUNT(*) AS cnt FROM commits WHERE repo_name IN (SELECT column1 AS repo_name FROM (VALUES {values})) AND message IS NOT NULL AND length(message) < 1000 AND lower(message) NOT LIKE 'merge%' AND lower(message) NOT LIKE 'update%' AND lower(message) NOT LIKE 'test%';"
    chunks.append(q)

result = json.dumps(chunks)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_go05Wk3xvJMfmFUt9HSgvM1G': 'file_storage/call_go05Wk3xvJMfmFUt9HSgvM1G.json', 'var_call_2SCwTMduH3ZG6RNpC5jXIFF8': 'file_storage/call_2SCwTMduH3ZG6RNpC5jXIFF8.json'}

exec(code, env_args)
