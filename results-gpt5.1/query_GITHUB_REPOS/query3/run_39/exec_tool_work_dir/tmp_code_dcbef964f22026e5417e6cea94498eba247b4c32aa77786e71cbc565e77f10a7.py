code = """import json, pandas as pd
from pathlib import Path

path = Path(var_call_pT4Rq8N4omLfCpVvYKT7f5YH)
repos = pd.read_json(path).repo_name.tolist()

# Build an IN clause in chunks to avoid parameter limits
chunks = [repos[i:i+500] for i in range(0, len(repos), 500)]
queries = []
for ch in chunks:
    in_list = ','.join("'" + r.replace("'", "''") + "'" for r in ch)
    q = f"SELECT COUNT(*) AS cnt FROM commits WHERE repo_name IN ({in_list}) AND message IS NOT NULL AND LENGTH(message) < 1000 AND LOWER(TRIM(message)) NOT LIKE 'merge%' AND LOWER(TRIM(message)) NOT LIKE 'update%' AND LOWER(TRIM(message)) NOT LIKE 'test%';"
    queries.append(q)

result = '\n'.join(queries)

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_pT4Rq8N4omLfCpVvYKT7f5YH': 'file_storage/call_pT4Rq8N4omLfCpVvYKT7f5YH.json', 'var_call_JGeFsfy1Z5Yc4yqNhYqzniJW': [{'cnt': '15016'}]}

exec(code, env_args)
