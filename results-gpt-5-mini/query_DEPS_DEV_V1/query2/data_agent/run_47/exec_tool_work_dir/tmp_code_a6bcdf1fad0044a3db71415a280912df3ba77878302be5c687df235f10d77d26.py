code = """import json
import pandas as pd

# Load previous large query results from storage file paths
with open(var_call_VYsnH3VHoutas1uQRAJH0NED, 'r') as f:
    pkg_records = json.load(f)
with open(var_call_XXsSx4B5pKCeNjXQ88rDo9OT, 'r') as f:
    projpkg_records = json.load(f)

pkg_df = pd.DataFrame(pkg_records)
projpkg_df = pd.DataFrame(projpkg_records)

# Ensure columns exist
needed_cols = ['System','Name','Version']
for c in needed_cols:
    if c not in pkg_df.columns:
        pkg_df[c] = None
    if c not in projpkg_df.columns:
        projpkg_df[c] = None

# Merge on System, Name, Version to get ProjectName for MIT release packages
merged = pkg_df.merge(projpkg_df[['System','Name','Version','ProjectName']], on=['System','Name','Version'], how='left')

# Extract unique, non-null ProjectName values
project_names = merged['ProjectName'].dropna().unique().tolist()

# Limit to reasonable number if extremely large to avoid huge SQL; but keep all
# Convert to plain Python list of strings
project_names = [str(x) for x in project_names]

import json
print("__RESULT__:")
print(json.dumps(project_names))"""

env_args = {'var_call_rNmnhECaaLnU0NkbPqzziZpa': 'file_storage/call_rNmnhECaaLnU0NkbPqzziZpa.json', 'var_call_VYsnH3VHoutas1uQRAJH0NED': 'file_storage/call_VYsnH3VHoutas1uQRAJH0NED.json', 'var_call_XXsSx4B5pKCeNjXQ88rDo9OT': 'file_storage/call_XXsSx4B5pKCeNjXQ88rDo9OT.json'}

exec(code, env_args)
