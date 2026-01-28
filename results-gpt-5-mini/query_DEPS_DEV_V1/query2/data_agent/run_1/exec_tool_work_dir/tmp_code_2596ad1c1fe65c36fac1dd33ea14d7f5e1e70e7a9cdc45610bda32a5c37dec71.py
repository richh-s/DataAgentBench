code = """import json
# load the two large results using their file paths
fp_pairs = var_call_6wivde3LLZKivV7PoIz7h2oI
fp_projmap = var_call_hOu0eUEw9QMltxlq4dHpjw1h
with open(fp_pairs, 'r', encoding='utf-8') as f:
    pairs = json.load(f)
with open(fp_projmap, 'r', encoding='utf-8') as f:
    projmap = json.load(f)
# Build mapping from (Name, Version) to ProjectName from projmap
map_nv_to_proj = {}
for r in projmap:
    key = (r.get('Name'), r.get('Version'))
    # prefer first encountered
    if key not in map_nv_to_proj:
        map_nv_to_proj[key] = r.get('ProjectName')
# For each pair, find project name
results = []
for p in pairs:
    key = (p['Name'], p['Version'])
    proj = map_nv_to_proj.get(key)
    if proj:
        results.append({'Name': p['Name'], 'Version': p['Version'], 'ProjectName': proj})
# Deduplicate by ProjectName (one project may have multiple packages/versions); keep first
seen = set()
unique_projects = []
for r in results:
    pn = r['ProjectName']
    if pn not in seen:
        seen.add(pn)
        unique_projects.append(r)
# Save intermediate
out = json.dumps(unique_projects)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_OEReunzHmE74cZY4WNSIkfET': ['packageinfo'], 'var_call_o5zSgoYFYlDqAiCwnnXLwH5B': ['project_info', 'project_packageversion'], 'var_call_sYGEyX5JrMt2dOgtF3WlNf4f': 'file_storage/call_sYGEyX5JrMt2dOgtF3WlNf4f.json', 'var_call_6wivde3LLZKivV7PoIz7h2oI': 'file_storage/call_6wivde3LLZKivV7PoIz7h2oI.json', 'var_call_hOu0eUEw9QMltxlq4dHpjw1h': 'file_storage/call_hOu0eUEw9QMltxlq4dHpjw1h.json'}

exec(code, env_args)
