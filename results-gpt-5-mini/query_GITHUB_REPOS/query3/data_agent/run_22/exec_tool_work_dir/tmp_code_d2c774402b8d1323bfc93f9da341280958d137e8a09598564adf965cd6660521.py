code = """import json
# Read the stored JSON result from the previous query
with open(var_call_qQvSn6gfJ3QlgHOtf1DMXXyj, 'r') as f:
    rows = json.load(f)

# Extract repo_name values and deduplicate
repo_names = sorted({r['repo_name'] for r in rows if 'repo_name' in r})

# Escape single quotes by doubling them for SQL
escaped = [rn.replace("'", "''") for rn in repo_names]

# Build IN clause safely
# If no repos, create an empty IN clause that yields no rows
if escaped:
    in_clause = ", ".join("'{}'".format(r) for r in escaped)
else:
    in_clause = "''"

query = (
    "SELECT COUNT(*) AS cnt FROM commits "
    "WHERE message IS NOT NULL AND message != '' "
    "AND length(message) < 1000 "
    "AND lower(ltrim(message)) NOT LIKE 'merge%' "
    "AND lower(ltrim(message)) NOT LIKE 'update%' "
    "AND lower(ltrim(message)) NOT LIKE 'test%' "
    "AND repo_name IN (" + in_clause + ");"
)

import json
print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_call_qQvSn6gfJ3QlgHOtf1DMXXyj': 'file_storage/call_qQvSn6gfJ3QlgHOtf1DMXXyj.json'}

exec(code, env_args)
