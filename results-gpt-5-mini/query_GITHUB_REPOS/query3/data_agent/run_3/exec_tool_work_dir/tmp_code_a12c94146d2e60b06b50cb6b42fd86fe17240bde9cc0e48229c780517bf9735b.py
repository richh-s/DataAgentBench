code = """import json
path = var_call_Y8n4hNIVJiv8fplkYiIB1j0w
with open(path, 'r') as f:
    records = json.load(f)
repo_names = sorted({r['repo_name'] for r in records if 'repo_name' in r})
# escape single quotes
def esc(s):
    return s.replace("'", "''")
chunk_size = 500
sqls = []
for i in range(0, len(repo_names), chunk_size):
    chunk = repo_names[i:i+chunk_size]
    in_list = ",".join("'" + esc(n) + "'" for n in chunk)
    sql = (
        "SELECT count(*) AS cnt FROM commits "
        "WHERE message IS NOT NULL AND message <> '' "
        "AND length(message) < 1000 "
        "AND lower(trim(message)) NOT LIKE 'merge%' "
        "AND lower(trim(message)) NOT LIKE 'update%' "
        "AND lower(trim(message)) NOT LIKE 'test%' "
        "AND repo_name IN (" + in_list + ");"
    )
    sqls.append(sql)
print('__RESULT__:')
print(json.dumps(sqls))"""

env_args = {'var_call_Y8n4hNIVJiv8fplkYiIB1j0w': 'file_storage/call_Y8n4hNIVJiv8fplkYiIB1j0w.json', 'var_call_ZJYOAJeL0dqFnVWGdEyk0UpD': 'file_storage/call_ZJYOAJeL0dqFnVWGdEyk0UpD.json'}

exec(code, env_args)
