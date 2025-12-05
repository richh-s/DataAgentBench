code = """import json, pandas as pd

# Load full NPM packageinfo
path_pkg = var_call_pyqCblEaSD4sw63fhwujNc5n
with open(path_pkg, 'r') as f:
    pkg = json.load(f)

# Filter MIT and IsRelease true
pkg_df = pd.DataFrame(pkg)

def has_mit(lic_str):
    try:
        arr = json.loads(lic_str) if isinstance(lic_str, str) else []
    except Exception:
        return False
    return 'MIT' in arr

def is_release(vi_str):
    try:
        obj = json.loads(vi_str) if isinstance(vi_str, str) else {}
    except Exception:
        return False
    return bool(obj.get('IsRelease'))

pkg_df = pkg_df[pkg_df['Licenses'].apply(has_mit) & pkg_df['VersionInfo'].apply(is_release)]

# Load NPM project_packageversion
path_ppv = var_call_0jdSSGGuauaDMCAF71F91XvK
with open(path_ppv, 'r') as f:
    ppv = json.load(f)
ppv_df = pd.DataFrame(ppv)
ppv_df = ppv_df[ppv_df['ProjectType'] == 'GITHUB']

# Join on System, Name, Version
merged = pkg_df.merge(ppv_df, on=['System','Name','Version'], how='inner')

# From ProjectName, we need fork counts from project_info.Project_Information text
path_pinfo = var_call_vnAe8WVvo1trCEt5TkF1WcoN
with open(path_pinfo, 'r') as f:
    pinfo = json.load(f)
pi_df = pd.DataFrame(pinfo)

# Extract project name and forks via simple parsing
import re

names = []
forks = []
for txt in pi_df['Project_Information']:
    mname = re.search(r"project ([^ ]+/[^ ]+)", txt)
    if not mname:
        mname = re.search(r"named ([^ ]+/[^ ]+)", txt)
    names.append(mname.group(1) if mname else None)
    mfork = re.search(r"(\d+) forks", txt)
    forks.append(int(mfork.group(1)) if mfork else None)

pi_df['ProjectName'] = names
pi_df['Forks'] = forks

pi_df = pi_df.dropna(subset=['ProjectName','Forks'])

# Join merged with pi_df on ProjectName
merged2 = merged.merge(pi_df[['ProjectName','Forks']], on='ProjectName', how='inner')

# For each project, get max fork count (should be same per project but just in case)
proj_forks = merged2.groupby('ProjectName')['Forks'].max().reset_index()

# Top 5 by forks
top5 = proj_forks.sort_values('Forks', ascending=False).head(5)

result = top5.to_dict(orient='records')

res_json = json.dumps(result)
print("__RESULT__:")
print(res_json)"""

env_args = {'var_call_pyqCblEaSD4sw63fhwujNc5n': 'file_storage/call_pyqCblEaSD4sw63fhwujNc5n.json', 'var_call_wGYXeW1oxvPkw3a0y6ML7nz5': ['project_info', 'project_packageversion'], 'var_call_0jdSSGGuauaDMCAF71F91XvK': 'file_storage/call_0jdSSGGuauaDMCAF71F91XvK.json', 'var_call_vnAe8WVvo1trCEt5TkF1WcoN': 'file_storage/call_vnAe8WVvo1trCEt5TkF1WcoN.json'}

exec(code, env_args)
