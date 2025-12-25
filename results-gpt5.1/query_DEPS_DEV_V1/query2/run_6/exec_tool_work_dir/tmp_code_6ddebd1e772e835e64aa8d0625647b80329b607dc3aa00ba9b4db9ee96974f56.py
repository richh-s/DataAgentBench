code = """import json, pandas as pd

# Load full NPM packageinfo data
path_pkg = var_call_yBrJJOzmAYwc6lPHpuWOQcTL
with open(path_pkg, 'r') as f:
    pkg = json.load(f)

path_projmap = var_call_CJPoeZVyGcic1uf87D2mJzHd
with open(path_projmap, 'r') as f:
    projmap = json.load(f)

pkg_df = pd.DataFrame(pkg)
proj_df = pd.DataFrame(projmap)

# Filter to MIT license and IsRelease true
import ast

def has_mit(lic_str):
    try:
        arr = ast.literal_eval(lic_str) if isinstance(lic_str, str) else []
        return any(str(x).upper() == 'MIT' for x in arr)
    except Exception:
        return False

def is_release(info_str):
    try:
        d = ast.literal_eval(info_str) if isinstance(info_str, str) else {}
        return bool(d.get('IsRelease'))
    except Exception:
        return False

pkg_df = pkg_df[pkg_df['Licenses'].apply(has_mit) & pkg_df['VersionInfo'].apply(is_release)]

# Join with project_packageversion on System, Name, Version
merged = pkg_df.merge(proj_df, on=['System','Name','Version'], how='inner')

# Keep unique projects
projects = merged['ProjectName'].dropna().unique().tolist()

# Now we need project_info with fork counts embedded in Project_Information
# Query it separately in SQL later; here we just prepare list of ProjectName
result = json.dumps(projects)

print('__RESULT__:')
print(result)"""

env_args = {'var_call_yBrJJOzmAYwc6lPHpuWOQcTL': 'file_storage/call_yBrJJOzmAYwc6lPHpuWOQcTL.json', 'var_call_5lGJ7YSeu0l3iw7cDvX74VG6': ['project_info', 'project_packageversion'], 'var_call_CJPoeZVyGcic1uf87D2mJzHd': 'file_storage/call_CJPoeZVyGcic1uf87D2mJzHd.json'}

exec(code, env_args)
