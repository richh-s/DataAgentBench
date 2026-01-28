code = """import json
# var_call_Y8n4hNIVJiv8fplkYiIB1j0w is the storage key from the previous query_db call
path = var_call_Y8n4hNIVJiv8fplkYiIB1j0w
with open(path, 'r') as f:
    records = json.load(f)
# extract unique repo_names
repo_names = sorted({r['repo_name'] for r in records if 'repo_name' in r})
# Build SQL IN list, escaping single quotes
def esc(s):
    return s.replace("'", "''")
chunks = []
for name in repo_names:
    chunks.append("'" + esc(name) + "'")
in_list = ",".join(chunks)
# Construct SQL for DuckDB (artifacts_database)
sql = (
    "SELECT count(*) AS cnt FROM commits "
    "WHERE message IS NOT NULL AND message <> '' "
    "AND length(message) < 1000 "
    "AND lower(trim(message)) NOT LIKE 'merge%' "
    "AND lower(trim(message)) NOT LIKE 'update%' "
    "AND lower(trim(message)) NOT LIKE 'test%' "
    "AND repo_name IN (" + in_list + ");"
)
import json
print('__RESULT__:')
print(json.dumps(sql))"""

env_args = {'var_call_Y8n4hNIVJiv8fplkYiIB1j0w': 'file_storage/call_Y8n4hNIVJiv8fplkYiIB1j0w.json'}

exec(code, env_args)
