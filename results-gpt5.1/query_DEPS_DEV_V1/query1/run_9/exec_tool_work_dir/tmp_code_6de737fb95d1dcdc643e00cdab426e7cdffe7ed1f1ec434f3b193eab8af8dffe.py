code = """import json, pandas as pd
from pathlib import Path

# Load full results from files
pkg_path = Path(var_call_FAkwhCIksf6jnMIV6xVxkSr9)
with pkg_path.open() as f:
    packageinfo = json.load(f)

ppv_path = Path(var_call_i78NZ1MzeRNVx1JnNvPHXTC7)
with ppv_path.open() as f:
    project_packageversion = json.load(f)

# Build DataFrames
pkg_df = pd.DataFrame(packageinfo)[['System','Name','Version']]
ppv_df = pd.DataFrame(project_packageversion)[['System','Name','Version','ProjectName']]

# Latest version per NPM package from packageinfo (order by Version lexicographically as proxy)
pkg_df_npm = pkg_df[pkg_df['System']=='NPM'].copy()
# sort by Name then Version and take last as latest
pkg_df_npm_sorted = pkg_df_npm.sort_values(['Name','Version'])
latest_pkg = pkg_df_npm_sorted.groupby('Name', as_index=False).tail(1)

# Join with project_packageversion on System, Name, Version
merged = latest_pkg.merge(ppv_df, on=['System','Name','Version'], how='inner')

# We don't have structured star counts, so we must parse from Project_Information in project_info.
# First, get distinct ProjectNames to query.
projects = sorted(merged['ProjectName'].dropna().unique().tolist())

result = json.dumps({'project_names_sample': projects[:10], 'count_projects': len(projects)})
print('__RESULT__:')
print(result)"""

env_args = {'var_call_FAkwhCIksf6jnMIV6xVxkSr9': 'file_storage/call_FAkwhCIksf6jnMIV6xVxkSr9.json', 'var_call_i78NZ1MzeRNVx1JnNvPHXTC7': 'file_storage/call_i78NZ1MzeRNVx1JnNvPHXTC7.json'}

exec(code, env_args)
