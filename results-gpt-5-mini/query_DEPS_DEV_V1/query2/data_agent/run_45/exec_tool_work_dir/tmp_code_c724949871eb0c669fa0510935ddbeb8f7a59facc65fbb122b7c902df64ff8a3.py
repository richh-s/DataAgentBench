code = """import json
# var_call_9WXql6CNrMRLYiHsQOH17uQs is the storage key containing the file path
path = var_call_9WXql6CNrMRLYiHsQOH17uQs
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)
# extract unique names and pairs
names = sorted(list({rec['Name'] for rec in data}))
pairs = [{'Name': rec['Name'], 'Version': rec['Version']} for rec in data]
out = {'names': names, 'pairs': pairs}
import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_9WXql6CNrMRLYiHsQOH17uQs': 'file_storage/call_9WXql6CNrMRLYiHsQOH17uQs.json'}

exec(code, env_args)
