code = """import json, pandas as pd, os

# Load full results from JSON files
with open(var_call_oUWXneDPOkZEzhheLkOxCyAT, 'r') as f:
    npm_packages = json.load(f)
with open(var_call_OgMKps48EQoU0fgAxa6eM1H7, 'r') as f:
    proj_pkg_versions = json.load(f)

pkg_df = pd.DataFrame(npm_packages)[['System','Name','Version']]
ppv_df = pd.DataFrame(proj_pkg_versions)[['System','Name','Version','ProjectName']]

# Determine latest version per (System, Name) in packageinfo using lexical max of Version
latest_pkg = pkg_df.sort_values('Version').groupby(['System','Name'], as_index=False).tail(1)

# Join with project_packageversion on System, Name, Version
merged = latest_pkg.merge(ppv_df, on=['System','Name','Version'], how='inner')

# For each NPM package Name, we just need distinct (Name, Version, ProjectName)
merged = merged.drop_duplicates(subset=['Name','Version','ProjectName'])

result = merged.to_json(orient='records')

print("__RESULT__:")
print(result)"""

env_args = {'var_call_oUWXneDPOkZEzhheLkOxCyAT': 'file_storage/call_oUWXneDPOkZEzhheLkOxCyAT.json', 'var_call_OgMKps48EQoU0fgAxa6eM1H7': 'file_storage/call_OgMKps48EQoU0fgAxa6eM1H7.json'}

exec(code, env_args)
