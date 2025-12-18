code = """import json
import pandas as pd

package_info_data = pd.read_json(locals()['var_function-call-4732325282894234512'])
df_packageinfo = pd.DataFrame(package_info_data)

# Parse VersionInfo and filter for release versions
df_packageinfo['VersionInfoParsed'] = df_packageinfo['VersionInfo'].apply(json.loads)
df_packageinfo['IsRelease'] = df_packageinfo['VersionInfoParsed'].apply(lambda x: x.get('IsRelease', False))
df_packageinfo['Ordinal'] = df_packageinfo['VersionInfoParsed'].apply(lambda x: x.get('Ordinal', 0))

df_releases = df_packageinfo[df_packageinfo['IsRelease'] == True]

# Find the latest release version for each package
idx = df_releases.groupby('Name')['Ordinal'].idxmax()
df_latest_releases = df_releases.loc[idx][['Name', 'Version']]

print("__RESULT__:")
print(df_latest_releases.to_json(orient='records'))"""

env_args = {'var_function-call-10276716253468333046': 'file_storage/function-call-10276716253468333046.json', 'var_function-call-4732325282894234512': 'file_storage/function-call-4732325282894234512.json'}

exec(code, env_args)
