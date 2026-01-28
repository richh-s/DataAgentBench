code = """import json
path = var_call_oy7rkcqUhosdoleV1S5dixVk
with open(path, 'r') as f:
    data = json.load(f)
# data is list of dicts
names = set()
pairs = set()
for r in data:
    if r.get('System') == 'NPM':
        names.add(r.get('Name'))
        pairs.add((r.get('Name'), r.get('Version')))
res = {'num_rows': len(data), 'unique_names': len(names), 'unique_pairs': len(pairs)}
import json
print("__RESULT__:")
print(json.dumps(res))"""

env_args = {'var_call_DVz30QS38OPrjRQdXuHLEkI5': ['packageinfo'], 'var_call_ADQ91SZxih62Z859qz1fgKUp': ['project_info', 'project_packageversion'], 'var_call_oy7rkcqUhosdoleV1S5dixVk': 'file_storage/call_oy7rkcqUhosdoleV1S5dixVk.json'}

exec(code, env_args)
