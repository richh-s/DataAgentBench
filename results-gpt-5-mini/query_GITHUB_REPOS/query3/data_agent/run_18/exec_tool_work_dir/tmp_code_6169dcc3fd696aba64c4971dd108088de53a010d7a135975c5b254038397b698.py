code = """import json
path = var_call_EuLNsnopDEE1uSCRnlRrwjF5
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)
repo_names = [r.get('repo_name') for r in records if r.get('repo_name')]
repo_names = sorted(list(dict.fromkeys(repo_names)))

def sql_escape(s):
    return s.replace("'", "''")

in_list = ','.join("'{0}'".format(sql_escape(r)) for r in repo_names)

sql = (
    'SELECT COUNT(*) AS cnt FROM commits\n'
    'WHERE repo_name IN ({in_list})\n'
    "  AND message IS NOT NULL\n"
    "  AND message <> ''\n"
    "  AND length(message) < 1000\n"
    "  AND lower(ltrim(message)) NOT LIKE 'merge%'\n"
    "  AND lower(ltrim(message)) NOT LIKE 'update%'\n"
    "  AND lower(ltrim(message)) NOT LIKE 'test%';"
).format(in_list=in_list)

print('__RESULT__:')
print(json.dumps(sql))"""

env_args = {'var_call_EuLNsnopDEE1uSCRnlRrwjF5': 'file_storage/call_EuLNsnopDEE1uSCRnlRrwjF5.json'}

exec(code, env_args)
