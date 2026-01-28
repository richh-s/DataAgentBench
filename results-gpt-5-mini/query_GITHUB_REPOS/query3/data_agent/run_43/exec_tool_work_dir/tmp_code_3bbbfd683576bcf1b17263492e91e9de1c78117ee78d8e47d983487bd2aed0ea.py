code = """import json
# var_call_o07qUZM7tOOEYrrLcwATeuAg is available in the environment as provided by the previous query_db call
path = var_call_o07qUZM7tOOEYrrLcwATeuAg
with open(path, 'r') as f:
    rows = json.load(f)
# extract repo_name values
repo_names = [r.get('repo_name') for r in rows if r.get('repo_name')]
# deduplicate while preserving order
seen = set()
uniq = []
for r in repo_names:
    if r not in seen:
        seen.add(r)
        uniq.append(r)
# escape single quotes by doubling them
escaped = [r.replace("'", "''") for r in uniq]
# build IN clause
in_clause = "(" + ",".join("'{}'".format(r) for r in escaped) + ")"
import json
print("__RESULT__:")
print(json.dumps(in_clause))"""

env_args = {'var_call_o07qUZM7tOOEYrrLcwATeuAg': 'file_storage/call_o07qUZM7tOOEYrrLcwATeuAg.json'}

exec(code, env_args)
