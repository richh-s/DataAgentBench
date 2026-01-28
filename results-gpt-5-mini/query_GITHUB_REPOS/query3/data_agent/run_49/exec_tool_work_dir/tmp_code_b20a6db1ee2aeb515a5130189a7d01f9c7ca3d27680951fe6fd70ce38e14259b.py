code = """import json
# var_call_dCSSnFL84Ahem6tUMklT8zt9 is provided by the previous query_db call and contains the path to the JSON file
path = var_call_dCSSnFL84Ahem6tUMklT8zt9
with open(path, 'r') as f:
    data = json.load(f)
repo_names = sorted({rec.get('repo_name') for rec in data if rec.get('repo_name')})
# Build SQL IN list, escaping single quotes
escaped = ",".join("'" + rn.replace("'", "''") + "'" for rn in repo_names)
in_list = "(" + escaped + ")"
print("__RESULT__:")
print(json.dumps(in_list))"""

env_args = {'var_call_dCSSnFL84Ahem6tUMklT8zt9': 'file_storage/call_dCSSnFL84Ahem6tUMklT8zt9.json'}

exec(code, env_args)
