code = """import json
# var_call_LzApJQ1XxPIihdgwrDSgmVHC is provided by storage and contains the file path to the JSON result
path = var_call_LzApJQ1XxPIihdgwrDSgmVHC
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)
# Extract unique repo names
repos = sorted({r['repo_name'] for r in records if 'repo_name' in r and r['repo_name']})
# Escape single quotes in repo names
escaped = [r.replace("'", "''") for r in repos]
# If list is empty, produce a query that returns zero
if not escaped:
    sql = "SELECT 0 AS cnt;"
else:
    # Build IN list
    in_list = ",".join("'{}'".format(r) for r in escaped)
    sql = (
        "SELECT COUNT(*) AS cnt FROM commits "
        "WHERE repo_name IN (" + in_list + ") "
        "AND message IS NOT NULL "
        "AND LENGTH(message) < 1000 "
        "AND LOWER(message) NOT LIKE 'merge%' "
        "AND LOWER(message) NOT LIKE 'update%' "
        "AND LOWER(message) NOT LIKE 'test%';"
    )
import json
print("__RESULT__:")
print(json.dumps(sql))"""

env_args = {'var_call_LzApJQ1XxPIihdgwrDSgmVHC': 'file_storage/call_LzApJQ1XxPIihdgwrDSgmVHC.json'}

exec(code, env_args)
