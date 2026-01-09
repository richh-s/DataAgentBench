code = """import json

path = var_call_oPLAEgRAkVCuWEWXu0b2uTMY
with open(path, 'r', encoding='utf-8') as f:
    repos = json.load(f)
repo_names = sorted({r.get('repo_name') for r in repos if r.get('repo_name')})

chunks = [repo_names[i:i+500] for i in range(0, len(repo_names), 500)]
clauses = []
for ch in chunks:
    vals = ','.join(["'" + s.replace("'","''") + "'" for s in ch])
    clauses.append('repo_name IN (' + vals + ')')
where_in = ' OR '.join(clauses) if clauses else 'FALSE'

query = (
    "SELECT COUNT(*) AS cnt\n"
    "FROM commits\n"
    "WHERE message IS NOT NULL\n"
    "  AND length(message) < 1000\n"
    "  AND lower(message) NOT LIKE 'merge%'\n"
    "  AND lower(message) NOT LIKE 'update%'\n"
    "  AND lower(message) NOT LIKE 'test%'\n"
    "  AND (" + where_in + ")"
)

print('__RESULT__:')
print(json.dumps({'repo_count': len(repo_names), 'query': query}))"""

env_args = {'var_call_oPLAEgRAkVCuWEWXu0b2uTMY': 'file_storage/call_oPLAEgRAkVCuWEWXu0b2uTMY.json'}

exec(code, env_args)
