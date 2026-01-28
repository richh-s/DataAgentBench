code = """import json
with open(var_call_MbXaRxowvDqekvVK5bzseCV9, 'r') as f:
    data = json.load(f)
cols = list(data[0].keys())
res = {"columns": cols, "sample_row": data[0]}
import json
print("__RESULT__:")
print(json.dumps(res))"""

env_args = {'var_call_MbXaRxowvDqekvVK5bzseCV9': 'file_storage/call_MbXaRxowvDqekvVK5bzseCV9.json'}

exec(code, env_args)
