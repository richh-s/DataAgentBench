code = """import json
from pathlib import Path

path = Path(var_call_hQ1GrzL60bhWiN8dGm2E9KcN)
with path.open('r', encoding='utf-8') as f:
    repos = json.load(f)
repo_list = sorted({r.get('repo_name') for r in repos if r.get('repo_name')})

chunks = [repo_list[i:i+800] for i in range(0, len(repo_list), 800)]
queries = []
for ch in chunks:
    in_list = ','.join(["'" + s.replace("'","''") + "'" for s in ch])
    q = (
        "SELECT COUNT(*) AS cnt FROM commits "
        f"WHERE repo_name IN ({in_list}) "
        "AND message IS NOT NULL "
        "AND length(message) < 1000 "
        "AND lower(message) NOT LIKE 'merge%' "
        "AND lower(message) NOT LIKE 'update%' "
        "AND lower(message) NOT LIKE 'test%';"
    )
    queries.append(q)

out = json.dumps({'repo_count': len(repo_list), 'query_count': len(queries), 'queries': queries})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_hQ1GrzL60bhWiN8dGm2E9KcN': 'file_storage/call_hQ1GrzL60bhWiN8dGm2E9KcN.json', 'var_call_pw15O05SVGSYE0UzlHuDRgcp': [{'cnt': '15016'}]}

exec(code, env_args)
