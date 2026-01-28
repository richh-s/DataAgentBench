code = """import json
import pandas as pd

# Load the two large query results from storage file paths
path_pkg = var_call_Dt1jep51h0je3AQG3K8y5sM7
path_projver = var_call_cnnhcBTvzreBOELoPOM90KVp

with open(path_pkg, 'r') as f:
    pkg_records = json.load(f)
with open(path_projver, 'r') as f:
    projver_records = json.load(f)

df_pkg = pd.DataFrame(pkg_records)
df_proj = pd.DataFrame(projver_records)

# Ensure columns exist
for c in ['System','Name','Version']:
    if c not in df_pkg.columns:
        df_pkg[c] = None
    if c not in df_proj.columns:
        df_proj[c] = None

# Inner join on System, Name, Version
merged = pd.merge(df_pkg[['System','Name','Version']], df_proj[['System','Name','Version','ProjectName']], on=['System','Name','Version'], how='inner')

# Get unique ProjectName list
unique_projects = sorted(merged['ProjectName'].dropna().unique().tolist())

# Output as JSON string
out = json.dumps(unique_projects)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_Ynihs5S7g9dRrvzFs4lsKAop': ['packageinfo'], 'var_call_yfgJV2CWFhqmptLhP2gg9379': ['project_info', 'project_packageversion'], 'var_call_Dt1jep51h0je3AQG3K8y5sM7': 'file_storage/call_Dt1jep51h0je3AQG3K8y5sM7.json', 'var_call_cnnhcBTvzreBOELoPOM90KVp': 'file_storage/call_cnnhcBTvzreBOELoPOM90KVp.json'}

exec(code, env_args)
