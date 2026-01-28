code = """import json
# Load the metadata query result stored in var_call_X6gq46gfmNqTpA50tyG3TVTO
data = None
v = var_call_X6gq46gfmNqTpA50tyG3TVTO
if isinstance(v, str):
    # It's a file path to the JSON
    with open(v, 'r', encoding='utf-8') as f:
        data = json.load(f)
else:
    data = v

# Extract repo_name values and deduplicate
repo_names = []
for item in data:
    rn = item.get('repo_name')
    if rn:
        repo_names.append(rn)
repo_names = sorted(set(repo_names))

# Escape single quotes in repo names and build IN list
def sql_escape(s):
    return s.replace("'", "''")

in_list = ','.join("'{}'".format(sql_escape(r)) for r in repo_names)

sql = (
    "SELECT COUNT(*) AS count FROM commits "
    "WHERE repo_name IN ({in_list}) "
    "AND message IS NOT NULL AND message <> '' "
    "AND length(message) < 1000 "
    "AND lower(message) NOT LIKE 'merge%' "
    "AND lower(message) NOT LIKE 'update%' "
    "AND lower(message) NOT LIKE 'test%';"
).format(in_list=in_list)

import json
print("__RESULT__:")
print(json.dumps(sql))"""

env_args = {'var_call_X6gq46gfmNqTpA50tyG3TVTO': 'file_storage/call_X6gq46gfmNqTpA50tyG3TVTO.json'}

exec(code, env_args)
