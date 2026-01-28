code = """import json
# var_call_Ipgl9ejtelPv0Dx3Xlp22Hd5 contains the file path to the JSON result from previous query
path = var_call_Ipgl9ejtelPv0Dx3Xlp22Hd5
with open(path, 'r') as f:
    data = json.load(f)
# data is a list of records with 'repo_name'
repo_names = [r['repo_name'] for r in data]
import json as _json
output = _json.dumps(repo_names)
print("__RESULT__:")
print(output)"""

env_args = {'var_call_Ipgl9ejtelPv0Dx3Xlp22Hd5': 'file_storage/call_Ipgl9ejtelPv0Dx3Xlp22Hd5.json'}

exec(code, env_args)
