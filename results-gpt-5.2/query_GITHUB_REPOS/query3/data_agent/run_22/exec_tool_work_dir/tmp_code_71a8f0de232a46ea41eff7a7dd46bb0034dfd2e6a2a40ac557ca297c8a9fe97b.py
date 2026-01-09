code = """import json

repos_src = var_call_JJdLhLCaS28fYsDOhaKyGVIV
if isinstance(repos_src, str):
    with open(repos_src, 'r', encoding='utf-8') as f:
        repos = json.load(f)
else:
    repos = repos_src

repo_names_set = set()
for r in repos:
    rn = r.get('repo_name')
    if rn:
        repo_names_set.add(rn)
repo_names = sorted(repo_names_set)

in_list = ','.join(["'" + rn.replace("'", "''") + "'" for rn in repo_names])

query = (
    "SELECT COUNT(*) AS commit_message_count\n"
    "FROM commits\n"
    f"WHERE repo_name IN ({in_list})\n"
    "  AND message IS NOT NULL\n"
    "  AND LENGTH(message) < 1000\n"
    "  AND LOWER(message) NOT LIKE 'merge%'\n"
    "  AND LOWER(message) NOT LIKE 'update%'\n"
    "  AND LOWER(message) NOT LIKE 'test%';"
)

print('__RESULT__:')
print(json.dumps({'duckdb_query': query, 'repo_count': len(repo_names)}))"""

env_args = {'var_call_JJdLhLCaS28fYsDOhaKyGVIV': 'file_storage/call_JJdLhLCaS28fYsDOhaKyGVIV.json', 'var_call_91MlK4dH5eiW94J8HqE1u3LG': [{'commit_message_count': '15016'}]}

exec(code, env_args)
