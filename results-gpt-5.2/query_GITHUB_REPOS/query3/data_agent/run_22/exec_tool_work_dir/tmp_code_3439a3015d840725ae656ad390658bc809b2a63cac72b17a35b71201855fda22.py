code = """import json

repos_src = var_call_JJdLhLCaS28fYsDOhaKyGVIV
if isinstance(repos_src, str):
    with open(repos_src, 'r', encoding='utf-8') as f:
        repos = json.load(f)
else:
    repos = repos_src

repo_names = []
seen = set()
for r in repos:
    rn = r.get('repo_name')
    if rn and rn not in seen:
        seen.add(rn)
        repo_names.append(rn)
repo_names.sort()

in_list = ','.join(["'" + rn.replace("'", "''") + "'" for rn in repo_names])

parts = []
parts.append('SELECT COUNT(*) AS commit_message_count')
parts.append('FROM commits')
parts.append('WHERE repo_name IN (' + in_list + ')')
parts.append('  AND message IS NOT NULL')
parts.append('  AND LENGTH(message) < 1000')
parts.append("  AND LOWER(message) NOT LIKE 'merge%'")
parts.append("  AND LOWER(message) NOT LIKE 'update%'")
parts.append("  AND LOWER(message) NOT LIKE 'test%'")
query = '\n'.join(parts) + ';'

print('__RESULT__:')
print(json.dumps({'duckdb_query': query, 'repo_count': len(repo_names)}))"""

env_args = {'var_call_JJdLhLCaS28fYsDOhaKyGVIV': 'file_storage/call_JJdLhLCaS28fYsDOhaKyGVIV.json', 'var_call_91MlK4dH5eiW94J8HqE1u3LG': [{'commit_message_count': '15016'}]}

exec(code, env_args)
