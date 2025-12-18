code = """import pandas as pd
import json

packageinfo_data_path = locals()['var_function-call-16529299900424573549']
with open(packageinfo_data_path, 'r') as f:
    packageinfo_data = json.load(f)

df_packageinfo = pd.DataFrame(packageinfo_data)

# Filter for NPM packages and parse VersionInfo
df_packageinfo = df_packageinfo[df_packageinfo['System'] == 'NPM'].copy()
df_packageinfo['VersionInfo'] = df_packageinfo['VersionInfo'].apply(json.loads)

# Filter for releases and extract Ordinal
df_packageinfo = df_packageinfo[df_packageinfo['VersionInfo'].apply(lambda x: x.get('IsRelease', False))]
df_packageinfo['Ordinal'] = df_packageinfo['VersionInfo'].apply(lambda x: x.get('Ordinal'))

# Find the latest version for each package
latest_versions = df_packageinfo.loc[df_packageinfo.groupby('Name')['Ordinal'].idxmax()]

# Select relevant columns
latest_versions = latest_versions[['Name', 'Version', 'System']]

print('__RESULT__:')
print(latest_versions.to_json(orient='records'))"""

env_args = {'var_function-call-10744039473036088012': ['packageinfo'], 'var_function-call-16529299900424573549': 'file_storage/function-call-16529299900424573549.json'}

exec(code, env_args)
