code = """import json
# var_call_J100Hcf8cXp1CDcLYJbUDxF2 is provided by previous query_db call and contains the path to the full result JSON
path = var_call_J100Hcf8cXp1CDcLYJbUDxF2
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)
repo_names = sorted({r['repo_name'] for r in records if 'repo_name' in r})
# Build SQL IN list, escaping single quotes by doubling them
in_list = ','.join("'" + rn.replace("'", "''") + "'" for rn in repo_names)
# Construct the DuckDB query for artifacts_database.commits
query = (
    'SELECT COUNT(*) AS count '
    'FROM commits '
    'WHERE repo_name IN ({in_list}) '
    "AND message IS NOT NULL "
    "AND message != '' "
    "AND length(message) < 1000 "
    "AND lower(ltrim(message)) NOT LIKE 'merge%' "
    "AND lower(ltrim(message)) NOT LIKE 'update%' "
    "AND lower(ltrim(message)) NOT LIKE 'test%';"
).format(in_list=in_list)
import json
print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_call_J100Hcf8cXp1CDcLYJbUDxF2': 'file_storage/call_J100Hcf8cXp1CDcLYJbUDxF2.json'}

exec(code, env_args)
