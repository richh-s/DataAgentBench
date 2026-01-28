code = """import json
path = var_call_EuLNsnopDEE1uSCRnlRrwjF5
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)
repo_names = [r.get('repo_name') for r in records if r.get('repo_name')]
repo_names = sorted(list(dict.fromkeys(repo_names)))

# Limit the IN list size to avoid huge queries; chunk into batches of 1000
chunks = [repo_names[i:i+1000] for i in range(0, len(repo_names), 1000)]
queries = []

def sql_escape(s):
    return s.replace("'", "''")

for chunk in chunks:
    in_list = ','.join("'{}'".format(sql_escape(r)) for r in chunk)
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
    queries.append(sql)

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_call_EuLNsnopDEE1uSCRnlRrwjF5': 'file_storage/call_EuLNsnopDEE1uSCRnlRrwjF5.json', 'var_call_Y4JEa5QVJ1rP12PYfnkCADvx': 'ok'}

exec(code, env_args)
