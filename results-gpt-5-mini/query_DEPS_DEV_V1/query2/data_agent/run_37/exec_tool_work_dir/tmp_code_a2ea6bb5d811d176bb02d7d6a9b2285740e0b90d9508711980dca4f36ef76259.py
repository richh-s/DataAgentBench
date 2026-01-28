code = """import json
# load both datasets
pkg_fp = var_call_xoiRbYVhG6oB3Nh77ykHM5fW
proj_fp = var_call_aTGIMvGhLIZaefb28WGSKnYH
with open(pkg_fp,'r') as f:
    pkgs = json.load(f)
with open(proj_fp,'r') as f:
    proj_pkg = json.load(f)
# Build mapping from (Name, Version) to list of ProjectName
map_nv_to_projects = {}
for r in proj_pkg:
    key = (r['Name'], r['Version'])
    map_nv_to_projects.setdefault(key, set()).add(r['ProjectName'])
# For each package record from pkgs that is NPM and MIT and IsRelease, find matching projects
matches = []
for r in pkgs:
    key = (r['Name'], r['Version'])
    if key in map_nv_to_projects:
        for p in map_nv_to_projects[key]:
            matches.append({'Name': r['Name'], 'Version': r['Version'], 'ProjectName': p})
# take unique ProjectName list
proj_names = sorted(list({m['ProjectName'] for m in matches}))
out = {'num_matched_projects': len(proj_names), 'sample_projects': proj_names[:200]}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_GFjoBvPPCjrqO1febE5dj3UX': ['packageinfo'], 'var_call_GEHAWCkzbkVYIGaW9lhUPqPS': ['project_info', 'project_packageversion'], 'var_call_xoiRbYVhG6oB3Nh77ykHM5fW': 'file_storage/call_xoiRbYVhG6oB3Nh77ykHM5fW.json', 'var_call_zMmer7wq6EmKDMw9EUItrB3A': 'file_storage/call_zMmer7wq6EmKDMw9EUItrB3A.json', 'var_call_aTGIMvGhLIZaefb28WGSKnYH': 'file_storage/call_aTGIMvGhLIZaefb28WGSKnYH.json'}

exec(code, env_args)
