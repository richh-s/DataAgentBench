code = """import json
# load package triples from previous python output
triples_path = var_call_0WCxbMuTxQGRvEiIxdI5oYtN
with open(triples_path, 'r', encoding='utf-8') as f:
    triples = json.load(f)
# load project_packageversion records
ppv_path = var_call_j0C5oPHpfXCyprf5Yum5tvPX
with open(ppv_path, 'r', encoding='utf-8') as f:
    ppv = json.load(f)
# Build mapping from (System, Name, Version) -> list of ProjectName
mapping = {}
for r in ppv:
    key = (r.get('System'), r.get('Name'), r.get('Version'))
    mapping.setdefault(key, set()).add(r.get('ProjectName'))
# For each triple, find matching ProjectNames
results = []
for t in triples:
    key = (t['System'], t['Name'], t['Version'])
    pnames = list(mapping.get(key, []))
    for pn in pnames:
        results.append({'System': t['System'], 'Name': t['Name'], 'Version': t['Version'], 'ProjectName': pn})
# deduplicate by ProjectName
seen = set()
final = []
for r in results:
    pn = r['ProjectName']
    if pn and pn not in seen:
        seen.add(pn)
        final.append(r)
# Save output
out = json.dumps(final)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_SPpf6OTIy2suP5I0T2HqEXjg': ['packageinfo'], 'var_call_i6hRKgFEWzpOJz5Z6LugaNNc': ['project_info', 'project_packageversion'], 'var_call_4QBHnENUNKnmttDHTGhGVb3H': 'file_storage/call_4QBHnENUNKnmttDHTGhGVb3H.json', 'var_call_0WCxbMuTxQGRvEiIxdI5oYtN': 'file_storage/call_0WCxbMuTxQGRvEiIxdI5oYtN.json', 'var_call_j0C5oPHpfXCyprf5Yum5tvPX': 'file_storage/call_j0C5oPHpfXCyprf5Yum5tvPX.json'}

exec(code, env_args)
