code = """import json
with open(var_call_2e1tl2asUOd6KA5haPS4xUwV, 'r') as f:
    projects = json.load(f)
# filter those that look like owner/repo (contain a slash and at least one character on both sides)
proj_slash = [p for p in projects if '/' in p and len(p.split('/')[0])>0 and len(p.split('/')[1])>0]
proj_slash = sorted(list(set(proj_slash)))
output = {'count': len(proj_slash), 'projects': proj_slash}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_MEq7coGaFeZY1uYdzEuOBVxR': 'file_storage/call_MEq7coGaFeZY1uYdzEuOBVxR.json', 'var_call_DQHCHJPoGMReDnmscL4ipZwY': 'file_storage/call_DQHCHJPoGMReDnmscL4ipZwY.json', 'var_call_2e1tl2asUOd6KA5haPS4xUwV': 'file_storage/call_2e1tl2asUOd6KA5haPS4xUwV.json', 'var_call_MykHHMcZQD5RHNY0zWZurORb': 'file_storage/call_MykHHMcZQD5RHNY0zWZurORb.json'}

exec(code, env_args)
