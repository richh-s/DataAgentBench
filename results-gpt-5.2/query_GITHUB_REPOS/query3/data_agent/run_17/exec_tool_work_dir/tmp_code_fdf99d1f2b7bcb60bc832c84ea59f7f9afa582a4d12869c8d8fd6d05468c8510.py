code = """import json

path = var_call_4brY4XqD5AsLnHrMhzH7tsBX
with open(path, 'r', encoding='utf-8') as f:
    repos = json.load(f)
repo_names = [r['repo_name'] for r in repos]

chunks = [repo_names[i:i+500] for i in range(0, len(repo_names), 500)]

queries = []
for ch in chunks:
    in_list = ','.join(["'" + s.replace("'","''") + "'" for s in ch])
    q = (
        "SELECT COUNT(*) AS cnt\n"
        "FROM commits\n"
        "WHERE message IS NOT NULL\n"
        "  AND length(message) < 1000\n"
        "  AND NOT (lower(trim(message)) LIKE 'merge%' OR lower(trim(message)) LIKE 'update%' OR lower(trim(message)) LIKE 'test%')\n"
        "  AND repo_name IN (" + in_list + ");"
    )
    queries.append(q)

print('__RESULT__:')
print(json.dumps({'queries': queries, 'n_repos': len(repo_names), 'n_chunks': len(chunks)}))"""

env_args = {'var_call_4brY4XqD5AsLnHrMhzH7tsBX': 'file_storage/call_4brY4XqD5AsLnHrMhzH7tsBX.json'}

exec(code, env_args)
