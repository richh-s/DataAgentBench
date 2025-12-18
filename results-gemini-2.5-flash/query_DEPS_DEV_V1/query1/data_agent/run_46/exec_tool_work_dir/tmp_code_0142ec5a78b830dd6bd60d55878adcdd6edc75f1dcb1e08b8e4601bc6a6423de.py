code = """import pandas as pd
import json

package_info_raw = pd.read_json(locals()['var_function-call-6475892482026271473'])
project_packageversion_raw = pd.read_json(locals()['var_function-call-9258655881987030810'])

# Process package_info to find the latest release version
package_info_df = package_info_raw.copy()
package_info_df['VersionInfoParsed'] = package_info_df['VersionInfo'].apply(json.loads)
package_info_df['IsRelease'] = package_info_df['VersionInfoParsed'].apply(lambda x: x.get('IsRelease', False))
package_info_df['Ordinal'] = package_info_df['VersionInfoParsed'].apply(lambda x: x.get('Ordinal', 0))

# Filter for releases and find the latest version based on Ordinal
latest_releases = package_info_df[package_info_df['IsRelease']].sort_values(by=['Name', 'Ordinal'], ascending=[True, False]).drop_duplicates(subset=['Name'], keep='first')

# Merge with project_packageversion
merged_df = pd.merge(latest_releases, project_packageversion_raw, on=['Name', 'Version'], how='inner')

# Select relevant columns for the next step
result = merged_df[['Name', 'Version', 'ProjectName']].to_json(orient='records')
print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-11444979742191410607': ['packageinfo'], 'var_function-call-6475892482026271473': 'file_storage/function-call-6475892482026271473.json', 'var_function-call-1011998616401049187': ['project_info', 'project_packageversion'], 'var_function-call-9258655881987030810': 'file_storage/function-call-9258655881987030810.json'}

exec(code, env_args)
