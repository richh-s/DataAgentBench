code = """import json

path = var_call_yYjIRG4qCqOhEEBqlqy92KG2
with open(path, 'r') as f:
    repos = json.load(f)
repo_names = sorted({r['repo_name'] for r in repos if r.get('repo_name')})

vals = ",".join(["'" + rn.replace("'","''") + "'" for rn in repo_names])

query = (
    "SELECT COUNT(*) AS cnt\n"
    "FROM commits\n"
    + "WHERE repo_name IN (" + vals + ")\n"
    "  AND message IS NOT NULL\n"
    "  AND length(message) < 1000\n"
    "  AND lower(substr(message, 1, 5)) <> 'merge'\n"
    "  AND lower(substr(message, 1, 6)) <> 'update'\n"
    "  AND lower(substr(message, 1, 4)) <> 'test'\n"
    ";"
)

print('__RESULT__:')
print(json.dumps({'repo_count': len(repo_names), 'query': query[:1000], 'query_len': len(query)}))"""

env_args = {'var_call_yYjIRG4qCqOhEEBqlqy92KG2': 'file_storage/call_yYjIRG4qCqOhEEBqlqy92KG2.json', 'var_call_B7tk1cNsbKv9FnTWAfy1EhMD': [{'cnt': '15016'}], 'var_call_9NHC9inv8ymahY6AKD2ImXqA': [{'cnt': '17976'}]}

exec(code, env_args)
