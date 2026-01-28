code = """import json
path = var_call_fNDvHPSqxhTTLn5V45C4wwjs
with open(path, 'r') as f:
    data = json.load(f)
repo_names = [r['repo_name'] for r in data if 'repo_name' in r and r['repo_name']]
# deduplicate and sort
repo_names = sorted(set(repo_names))
# escape single quotes for SQL
escaped = [rn.replace("'", "''") for rn in repo_names]
# build SQL IN list
if escaped:
    sql_list = "('" + "','".join(escaped) + "')"
else:
    sql_list = "()"
import json
result = {'sql_in_list': sql_list, 'count_repos': len(escaped)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_fNDvHPSqxhTTLn5V45C4wwjs': 'file_storage/call_fNDvHPSqxhTTLn5V45C4wwjs.json'}

exec(code, env_args)
