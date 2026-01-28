code = """import json, pandas as pd
repo_path = var_call_hquhOKZXlGStPJSQHWcmbX2D
with open(repo_path, 'r') as f:
    repos = json.load(f)
repo_list = sorted({r['repo_name'] for r in repos if r.get('repo_name')})
# chunk for IN clause safety
chunks = [repo_list[i:i+500] for i in range(0, len(repo_list), 500)]
queries = []
for ch in chunks:
    in_list = ','.join(["'"+x.replace("'","''")+"'" for x in ch])
    q = f"SELECT COUNT(*) AS c FROM commits WHERE message IS NOT NULL AND LENGTH(message) < 1000 AND LOWER(TRIM(message)) NOT LIKE 'merge%' AND LOWER(TRIM(message)) NOT LIKE 'update%' AND LOWER(TRIM(message)) NOT LIKE 'test%' AND repo_name IN ({in_list});"
    queries.append(q)
print('__RESULT__:')
print(json.dumps({'queries': queries}))"""

env_args = {'var_call_hquhOKZXlGStPJSQHWcmbX2D': 'file_storage/call_hquhOKZXlGStPJSQHWcmbX2D.json'}

exec(code, env_args)
