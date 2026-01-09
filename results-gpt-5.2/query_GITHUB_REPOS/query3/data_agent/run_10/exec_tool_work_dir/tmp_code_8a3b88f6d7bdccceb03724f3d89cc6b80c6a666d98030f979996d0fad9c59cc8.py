code = """import json

src = var_call_hdegDIIzK5FCL1EEauw72YhW
if isinstance(src, str):
    with open(src, 'r', encoding='utf-8') as f:
        repos = json.load(f)
else:
    repos = src
repo_names = sorted(set([r.get('repo_name') for r in repos if r.get('repo_name')]))

in_list = ','.join(["'" + rn.replace("'", "''") + "'" for rn in repo_names])

query = """
SELECT COUNT(*) AS cnt
FROM commits
WHERE message IS NOT NULL
  AND length(message) < 1000
  AND lower(message) NOT LIKE 'merge%'
  AND lower(message) NOT LIKE 'update%'
  AND lower(message) NOT LIKE 'test%'
  AND repo_name IN ({in_list});
""".format(in_list=in_list)

print('__RESULT__:')
print(json.dumps({'repo_count': len(repo_names), 'query': query}))"""

env_args = {'var_call_hdegDIIzK5FCL1EEauw72YhW': 'file_storage/call_hdegDIIzK5FCL1EEauw72YhW.json'}

exec(code, env_args)
