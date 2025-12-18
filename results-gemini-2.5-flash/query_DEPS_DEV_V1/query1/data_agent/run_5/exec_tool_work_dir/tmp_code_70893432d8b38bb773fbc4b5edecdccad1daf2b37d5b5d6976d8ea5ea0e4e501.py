code = """import json
import pandas as pd

with open(locals()['var_function-call-8060708402497588293'], 'r') as f:
    packageinfo_data = json.load(f)

df_packageinfo = pd.DataFrame(packageinfo_data)

# Parse VersionInfo to extract IsRelease and Ordinal
df_packageinfo['VersionInfo_Parsed'] = df_packageinfo['VersionInfo'].apply(json.loads)
df_packageinfo['IsRelease'] = df_packageinfo['VersionInfo_Parsed'].apply(lambda x: x.get('IsRelease'))
df_packageinfo['Ordinal'] = df_packageinfo['VersionInfo_Parsed'].apply(lambda x: x.get('Ordinal'))

# Filter for release versions
df_releases = df_packageinfo[df_packageinfo['IsRelease'] == True].copy()

# Find the latest release version for each package
latest_releases = df_releases.loc[df_releases.groupby('Name')['Ordinal'].idxmax()]

# Select relevant columns
latest_releases_filtered = latest_releases[['Name', 'Version']]

print("__RESULT__:")
print(latest_releases_filtered.to_json(orient='records'))"""

env_args = {'var_function-call-8060708402497588293': 'file_storage/function-call-8060708402497588293.json'}

exec(code, env_args)
