code = """import json, pandas as pd

path = var_call_oPLAEgRAkVCuWEWXu0b2uTMY
with open(path, 'r', encoding='utf-8') as f:
    repos = json.load(f)
repo_names = sorted({r['repo_name'] for r in repos if r.get('repo_name')})

# chunk for SQL IN list size
chunks = [repo_names[i:i+500] for i in range(0, len(repo_names), 500)]
clauses = []
for ch in chunks:
    vals = ','.join(["'" + s.replace("'","''") + "'" for s in ch])
    clauses.append(f"repo_name IN ({vals})")
where_in = ' OR '.join(clauses) if clauses else 'FALSE'

query = f"""
SELECT COUNT(*) AS cnt
FROM commits
WHERE message IS NOT NULL
  AND length(message) < 1000
  AND lower(message) NOT LIKE 'merge%'
  AND lower(message) NOT LIKE 'update%'
  AND lower(message) NOT LIKE 'test%'
  AND ({where_in});
"""

out = json.dumps({'repo_count': len(repo_names), 'sql': query})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_oPLAEgRAkVCuWEWXu0b2uTMY': 'file_storage/call_oPLAEgRAkVCuWEWXu0b2uTMY.json'}

exec(code, env_args)
