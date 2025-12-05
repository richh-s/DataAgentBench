code = """import json, pandas as pd, os

# Load large query results from files
with open(var_call_jNPi455iwHeYaYsZeY57uqs1, 'r') as f:
    pkginfo = json.load(f)
with open(var_call_uJDcnvkWsqG4krz2tKwObVwE, 'r') as f:
    proj_pkg = json.load(f)

pkg_df = pd.DataFrame(pkginfo)[['System','Name','Version']]
proj_pkg_df = pd.DataFrame(proj_pkg)[['System','Name','Version','ProjectName']]

# Only NPM already filtered, ensure again
pkg_df = pkg_df[pkg_df['System']=='NPM']
proj_pkg_df = proj_pkg_df[proj_pkg_df['System']=='NPM']

# Determine latest version per package name in NPM using lexical max as proxy
latest_versions = pkg_df.groupby('Name')['Version'].max().reset_index().rename(columns={'Version':'LatestVersion'})

# Join back to get (Name, LatestVersion) pairs that actually exist
latest_pkg = pd.merge(latest_versions, pkg_df, left_on=['Name','LatestVersion'], right_on=['Name','Version'], how='inner')

# Join with project_packageversion to get ProjectName for those latest versions
latest_with_proj = pd.merge(latest_pkg[['Name','Version']], proj_pkg_df, on=['Name','Version'], how='inner')

# Need project_info with stars; Project_Information text includes stars, but we only have that column plus Homepage,Licenses,Description
# Fetch project_info now separately using SQL-compatible columns

result = latest_with_proj.head(10).to_json(orient='records')

print("__RESULT__:")
print(result)"""

env_args = {'var_call_jNPi455iwHeYaYsZeY57uqs1': 'file_storage/call_jNPi455iwHeYaYsZeY57uqs1.json', 'var_call_uJDcnvkWsqG4krz2tKwObVwE': 'file_storage/call_uJDcnvkWsqG4krz2tKwObVwE.json'}

exec(code, env_args)
