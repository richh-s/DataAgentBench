code = """import json
import pandas as pd
# load results from previous query_db calls (stored as file paths)
with open(var_call_MEq7coGaFeZY1uYdzEuOBVxR, 'r') as f:
    pkg_rows = json.load(f)
with open(var_call_DQHCHJPoGMReDnmscL4ipZwY, 'r') as f:
    projpkg_rows = json.load(f)

df_pkg = pd.DataFrame(pkg_rows)
df_projpkg = pd.DataFrame(projpkg_rows)

# Normalize types and join on System, Name, Version
common = ['System', 'Name', 'Version']
# Some Name or Version may have leading/trailing spaces; strip
for c in common:
    if c in df_pkg.columns:
        df_pkg[c] = df_pkg[c].astype(str).str.strip()
    if c in df_projpkg.columns:
        df_projpkg[c] = df_projpkg[c].astype(str).str.strip()

merged = pd.merge(df_pkg[common], df_projpkg[['System','Name','Version','ProjectName']], on=common, how='inner')
unique_projects = sorted(merged['ProjectName'].dropna().unique().tolist())

import json
result = json.dumps(unique_projects)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_MEq7coGaFeZY1uYdzEuOBVxR': 'file_storage/call_MEq7coGaFeZY1uYdzEuOBVxR.json', 'var_call_DQHCHJPoGMReDnmscL4ipZwY': 'file_storage/call_DQHCHJPoGMReDnmscL4ipZwY.json'}

exec(code, env_args)
