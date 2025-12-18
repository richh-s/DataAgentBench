code = """import pandas as pd
import json

package_info_data = pd.read_json(locals()['var_function-call-17052421974825312040'])

# Filter for release versions and convert 'Ordinal' to numeric
package_info_data['VersionInfo'] = package_info_data['VersionInfo'].apply(json.loads)
package_info_data = package_info_data[package_info_data['VersionInfo'].apply(lambda x: x.get('IsRelease', False))]
package_info_data['Ordinal'] = package_info_data['VersionInfo'].apply(lambda x: x.get('Ordinal'))

# Find the latest release version for each package
latest_releases = package_info_data.loc[package_info_data.groupby('Name')['Ordinal'].idxmax()]

# Select relevant columns
latest_releases = latest_releases[['Name', 'Version']]

print('__RESULT__:')
print(latest_releases.to_json(orient='records'))"""

env_args = {'var_function-call-17052421974825312040': 'file_storage/function-call-17052421974825312040.json'}

exec(code, env_args)
