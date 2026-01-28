code = """import json
src = var_call_hdegDIIzK5FCL1EEauw72YhW
if isinstance(src, str):
    with open(src, 'r', encoding='utf-8') as f:
        repos = json.load(f)
else:
    repos = src
repo_names = sorted(set([r.get('repo_name') for r in repos if r.get('repo_name')]))

# Build VALUES list for DuckDB
vals = ',\n'.join(["('" + rn.replace("'","''") + "')" for rn in repo_names])
query = (
"SELECT COUNT(*) AS cnt\n"
"FROM commits\n"
"WHERE message IS NOT NULL\n"
"  AND length(message) < 1000\n"
"  AND lower(message) NOT LIKE 'merge%'\n"
"  AND lower(message) NOT LIKE 'update%'\n"
"  AND lower(message) NOT LIKE 'test%'\n"
"  AND repo_name IN (SELECT repo_name FROM (VALUES\n" + vals + "\n) v(repo_name));"
)

print('__RESULT__:')
print(json.dumps({'query': query, 'repo_count': len(repo_names)}))"""

env_args = {'var_call_hdegDIIzK5FCL1EEauw72YhW': 'file_storage/call_hdegDIIzK5FCL1EEauw72YhW.json', 'var_call_hU5NmRJZafxBGOMTldPjoeuO': [{'cnt': '0'}]}

exec(code, env_args)
