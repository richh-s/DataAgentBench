code = """import json
import pandas as pd

# Load the full packageinfo data from the JSON file
with open(locals()['var_function-call-10633105012564164927'], 'r') as f:
    packageinfo_data = json.load(f)

df_packageinfo = pd.DataFrame(packageinfo_data)

# Filter for NPM packages and where IsRelease is true
df_packageinfo_npm = df_packageinfo[df_packageinfo['System'] == 'NPM'].copy()
df_packageinfo_npm['VersionInfo'] = df_packageinfo_npm['VersionInfo'].apply(json.loads)
df_packageinfo_npm['IsRelease'] = df_packageinfo_npm['VersionInfo'].apply(lambda x: x.get('IsRelease'))
df_packageinfo_npm['Ordinal'] = df_packageinfo_npm['VersionInfo'].apply(lambda x: x.get('Ordinal'))

df_releases = df_packageinfo_npm[df_packageinfo_npm['IsRelease'] == True]

# Find the latest release for each package based on Ordinal
# If multiple versions have the same highest Ordinal, sort by Version string to get a consistent "latest"
df_releases['Version_tuple'] = df_releases['Version'].apply(lambda x: tuple(map(int, (x.split('.')))))
latest_releases = df_releases.loc[df_releases.groupby('Name')['Ordinal'].idxmax()]

# Sort by Version in case of same Ordinal to get a consistent "latest" (e.g. 1.0.0 vs 1.0.1)
latest_releases = latest_releases.sort_values(by=['Name', 'Ordinal', 'Version'], ascending=[True, True, True])
latest_releases = latest_releases.groupby('Name').tail(1)


result = latest_releases.to_json(orient='records')
print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-10633105012564164927': 'file_storage/function-call-10633105012564164927.json'}

exec(code, env_args)
