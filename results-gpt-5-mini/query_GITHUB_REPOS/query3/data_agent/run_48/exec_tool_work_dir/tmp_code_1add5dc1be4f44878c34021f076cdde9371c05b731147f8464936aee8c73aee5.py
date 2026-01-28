code = """import json
# var_call_hBUqC2b3cuJPjKmWtlZNQDAo is the storage key from the earlier query_db call containing the JSON file path
path = var_call_hBUqC2b3cuJPjKmWtlZNQDAo
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)
repo_names = [r['repo_name'] for r in records]
# Build an IN-list for SQL. Escape single quotes by doubling them.
escaped = [name.replace("'", "''") for name in repo_names]
in_list = ','.join(["'" + e + "'" for e in escaped])
# If the list is empty, set to an impossible value
if not in_list:
    in_list = "''"
output = in_list
import json as _json
print("__RESULT__:")
print(_json.dumps(output))"""

env_args = {'var_call_hBUqC2b3cuJPjKmWtlZNQDAo': 'file_storage/call_hBUqC2b3cuJPjKmWtlZNQDAo.json'}

exec(code, env_args)
