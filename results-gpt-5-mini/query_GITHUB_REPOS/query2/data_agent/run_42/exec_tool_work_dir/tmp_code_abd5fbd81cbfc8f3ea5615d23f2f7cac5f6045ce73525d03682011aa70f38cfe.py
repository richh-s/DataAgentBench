code = """import json
p = var_call_Plm8LCGbK2eCNLoex1OvFNu9
with open(p,'r') as f:
    data = json.load(f)
# find max copies
max_copies = max(d['copies'] for d in data)
max_items = [ {'id': d['id'], 'sample_repo_name': d['sample_repo_name'], 'sample_path': d['sample_path'], 'copies': d['copies']} for d in data if d['copies']==max_copies]

print("__RESULT__:")
print(json.dumps({'max_copies': max_copies, 'items': max_items}))"""

env_args = {'var_call_CgUdQ8ytJvrIQCOmv8Brmi2h': 'file_storage/call_CgUdQ8ytJvrIQCOmv8Brmi2h.json', 'var_call_Plm8LCGbK2eCNLoex1OvFNu9': 'file_storage/call_Plm8LCGbK2eCNLoex1OvFNu9.json'}

exec(code, env_args)
