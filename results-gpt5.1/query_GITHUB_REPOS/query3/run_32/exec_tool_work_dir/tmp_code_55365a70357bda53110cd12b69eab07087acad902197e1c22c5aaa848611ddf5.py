code = """import json, pandas as pd
from pathlib import Path

path = Path(var_call_OTUOH9JSHbr0NQa3X0rbbdsJ)
repos = pd.read_json(path).repo_name.tolist()

chunk_size = 500
queries = []
for i in range(0, len(repos), chunk_size):
    chunk = repos[i:i+chunk_size]
    in_list = ','.join(["'"+r.replace("'", "''")+"'" for r in chunk])
    q = f"SELECT COUNT(*) AS cnt FROM commits WHERE repo_name IN ({in_list}) AND message IS NOT NULL AND length(message) < 1000 AND lower(trim(message)) NOT LIKE 'merge%' AND lower(trim(message)) NOT LIKE 'update%' AND lower(trim(message)) NOT LIKE 'test%';"
    queries.append(q)

print('__RESULT__:')
print(json.dumps(queries))"""

env_args = {'var_call_OTUOH9JSHbr0NQa3X0rbbdsJ': 'file_storage/call_OTUOH9JSHbr0NQa3X0rbbdsJ.json', 'var_call_RM4YWWPYtykZfJRoZa9J1Ufm': [{'cnt': '15016'}]}

exec(code, env_args)
