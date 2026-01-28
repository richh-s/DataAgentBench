code = """import json
# var_call_UDa2dvW0mwt1Fy7YaZNXYgJi is a file path containing the metadata query result
with open(var_call_UDa2dvW0mwt1Fy7YaZNXYgJi, 'r') as f:
    data = json.load(f)
repo_names = [rec['repo_name'] for rec in data]
# Output must be a JSON-serializable string
out = json.dumps(repo_names)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_UDa2dvW0mwt1Fy7YaZNXYgJi': 'file_storage/call_UDa2dvW0mwt1Fy7YaZNXYgJi.json'}

exec(code, env_args)
