code = """import json
import pandas as pd

df = pd.read_json(var_call_j80c8oNb2v7d8dHebxPFmJjy)
repos = df['repo_name'].tolist()

chunks = []
chunk_size = 500
for i in range(0, len(repos), chunk_size):
    chunk = repos[i:i+chunk_size]
    in_list = ",".join(["'" + r.replace("'", "''") + "'" for r in chunk])
    query = f"SELECT count(*) as cnt FROM commits WHERE repo_name IN ({in_list}) AND message IS NOT NULL AND length(message) < 1000 AND lower(trim(message)) NOT LIKE 'merge%' AND lower(trim(message)) NOT LIKE 'update%' AND lower(trim(message)) NOT LIKE 'test%';"
    chunks.append(query)

result = " ; ".join(chunks)
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_j80c8oNb2v7d8dHebxPFmJjy': 'file_storage/call_j80c8oNb2v7d8dHebxPFmJjy.json', 'var_call_PqignCIRInUQlA8AZ0k6mJaT': [{'1': '1'}]}

exec(code, env_args)
