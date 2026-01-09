code = """import json

path = var_call_0OjodcdmTxSeTjqnYics1DUZ
with open(path, 'r') as f:
    repos = json.load(f)
repo_names = [r['repo_name'] for r in repos]
escaped = [rn.replace("'", "''") for rn in repo_names]
values_rows = ",".join(["('" + rn + "')" for rn in escaped])

query = (
    "SELECT COUNT(*) AS cnt\n"
    "FROM commits c\n"
    "JOIN (VALUES " + values_rows + ") AS v(repo_name) ON v.repo_name = c.repo_name\n"
    "WHERE c.message IS NOT NULL\n"
    "  AND length(c.message) < 1000\n"
    "  AND lower(c.message) NOT LIKE 'merge%'\n"
    "  AND lower(c.message) NOT LIKE 'update%'\n"
    "  AND lower(c.message) NOT LIKE 'test%'\n"
)

print('__RESULT__:')
print(json.dumps({'query': query, 'n_repos': len(repo_names)}))"""

env_args = {'var_call_0OjodcdmTxSeTjqnYics1DUZ': 'file_storage/call_0OjodcdmTxSeTjqnYics1DUZ.json'}

exec(code, env_args)
