code = """import json

path = var_call_wWslIqbNnYleizS3X8NGpkU2
with open(path, 'r', encoding='utf-8') as f:
    repos = json.load(f)
repo_names = [r['repo_name'] for r in repos]
chunks = [repo_names[i:i+500] for i in range(0, len(repo_names), 500)]
queries = []
for ch in chunks:
    in_list = ','.join(["'" + s.replace("'","''") + "'" for s in ch])
    q = (
        "SELECT COUNT(*) AS c FROM commits "
        "WHERE message IS NOT NULL "
        "AND LENGTH(message) < 1000 "
        "AND LOWER(TRIM(message)) NOT LIKE 'merge%' "
        "AND LOWER(TRIM(message)) NOT LIKE 'update%' "
        "AND LOWER(TRIM(message)) NOT LIKE 'test%' "
        f"AND repo_name IN ({in_list});"
    )
    queries.append(q)

print('__RESULT__:')
print(json.dumps({'repo_count': len(repo_names), 'chunk_count': len(chunks), 'queries': queries[:5]}))"""

env_args = {'var_call_wWslIqbNnYleizS3X8NGpkU2': 'file_storage/call_wWslIqbNnYleizS3X8NGpkU2.json'}

exec(code, env_args)
