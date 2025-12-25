code = """import json, pandas as pd
from pathlib import Path

path = Path(var_call_E4Urr3eh7IdYIm5Mby7JA68b)
repos = pd.read_json(path)
repo_list = repos['repo_name'].tolist()

chunks = []
for i in range(0, len(repo_list), 500):
    chunk = repo_list[i:i+500]
    in_list = ','.join(["'" + r.replace("'", "''") + "'" for r in chunk])
    query = f"SELECT COUNT(*) AS cnt FROM commits WHERE repo_name IN ({in_list}) AND message IS NOT NULL AND LENGTH(message) < 1000 AND LOWER(TRIM(message)) NOT LIKE 'merge%' AND LOWER(TRIM(message)) NOT LIKE 'update%' AND LOWER(TRIM(message)) NOT LIKE 'test%';"
    chunks.append(query)

print('__RESULT__:')
print(json.dumps(chunks))"""

env_args = {'var_call_E4Urr3eh7IdYIm5Mby7JA68b': 'file_storage/call_E4Urr3eh7IdYIm5Mby7JA68b.json', 'var_call_J8cWzj1uHdFfL7pVH9sDQygH': [{'cnt': '15016'}]}

exec(code, env_args)
