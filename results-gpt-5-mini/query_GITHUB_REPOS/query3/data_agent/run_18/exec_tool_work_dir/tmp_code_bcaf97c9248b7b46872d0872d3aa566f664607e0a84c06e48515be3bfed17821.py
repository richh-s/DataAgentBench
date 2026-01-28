code = """import json
path = var_call_EuLNsnopDEE1uSCRnlRrwjF5
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)
repo_names = [r.get('repo_name') for r in records if r.get('repo_name')]
repo_names = sorted(list(dict.fromkeys(repo_names)))

def sql_escape(s):
    return s.replace("'", "''")

in_list = ','.join("'{}'".format(sql_escape(r)) for r in repo_names)

parts = [
    "SELECT COUNT(*) AS cnt FROM commits",
    "WHERE repo_name IN ({in_list})",
    "AND message IS NOT NULL",
    "AND message <> ''",
    "AND length(message) < 1000",
    "AND lower(ltrim(message)) NOT LIKE 'merge%'",
    "AND lower(ltrim(message)) NOT LIKE 'update%'",
    "AND lower(ltrim(message)) NOT LIKE 'test%';"
]
sql = "\n".join(parts).format(in_list=in_list)

print("__RESULT__:")
print(json.dumps(sql))"""

env_args = {'var_call_EuLNsnopDEE1uSCRnlRrwjF5': 'file_storage/call_EuLNsnopDEE1uSCRnlRrwjF5.json'}

exec(code, env_args)
