code = """import json, pandas as pd
from pathlib import Path

path = Path(var_call_Vze9xVeDncn7VRYU7xzfW3y9)
repos = pd.read_json(path)
repo_list = repos['repo_name'].tolist()

chunks = []
chunk_size = 900
for i in range(0, len(repo_list), chunk_size):
    chunk = repo_list[i:i+chunk_size]
    in_list = ",".join(["'"+r.replace("'","''")+"'" for r in chunk])
    chunks.append(f"SELECT COUNT(*) AS cnt FROM commits WHERE repo_name IN ({in_list}) AND message IS NOT NULL AND length(message) < 1000 AND lower(trim(message)) NOT LIKE 'merge%' AND lower(trim(message)) NOT LIKE 'update%' AND lower(trim(message)) NOT LIKE 'test%'")

queries = [f"({q})" for q in chunks]
union_query = " UNION ALL ".join(queries)

print("__RESULT__:")
print(json.dumps(union_query))"""

env_args = {'var_call_Vze9xVeDncn7VRYU7xzfW3y9': 'file_storage/call_Vze9xVeDncn7VRYU7xzfW3y9.json', 'var_call_j4fu3NAjWGHxAbozr67qCFVu': [{'cnt': '15016'}]}

exec(code, env_args)
