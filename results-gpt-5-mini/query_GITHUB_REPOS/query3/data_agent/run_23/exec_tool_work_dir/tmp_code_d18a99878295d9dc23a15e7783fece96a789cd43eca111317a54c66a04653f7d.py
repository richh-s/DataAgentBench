code = """import json
# var_call_HDcK5iM8SUpW9eZ5veiEaqeT is the storage key from the previous query_db call
path = var_call_HDcK5iM8SUpW9eZ5veiEaqeT
with open(path, 'r') as f:
    records = json.load(f)
repo_names = sorted({r['repo_name'] for r in records if 'repo_name' in r})
import json
print("__RESULT__:")
print(json.dumps(repo_names))"""

env_args = {'var_call_HDcK5iM8SUpW9eZ5veiEaqeT': 'file_storage/call_HDcK5iM8SUpW9eZ5veiEaqeT.json'}

exec(code, env_args)
