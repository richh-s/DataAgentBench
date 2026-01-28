code = """import json
path = var_call_EuLNsnopDEE1uSCRnlRrwjF5
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)
repo_names = [r.get('repo_name') for r in records if r.get('repo_name')]
repo_names = sorted(list(dict.fromkeys(repo_names)))

chunks = [repo_names[i:i+500] for i in range(0, len(repo_names), 500)]
queries = []
for chunk in chunks:
    in_list = ",".join("'" + r.replace("'", "''") + "'" for r in chunk)
    sql = (
        "SELECT COUNT(*) AS cnt FROM commits\n"
        "WHERE repo_name IN (" + in_list + ")\n"
        "AND message IS NOT NULL\n"
        "AND message <> ''\n"
        "AND length(message) < 1000\n"
        "AND lower(ltrim(message)) NOT LIKE 'merge%'\n"
        "AND lower(ltrim(message)) NOT LIKE 'update%'\n"
        "AND lower(ltrim(message)) NOT LIKE 'test%';"
    )
    queries.append(sql)

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_call_EuLNsnopDEE1uSCRnlRrwjF5': 'file_storage/call_EuLNsnopDEE1uSCRnlRrwjF5.json', 'var_call_Y4JEa5QVJ1rP12PYfnkCADvx': 'ok'}

exec(code, env_args)
