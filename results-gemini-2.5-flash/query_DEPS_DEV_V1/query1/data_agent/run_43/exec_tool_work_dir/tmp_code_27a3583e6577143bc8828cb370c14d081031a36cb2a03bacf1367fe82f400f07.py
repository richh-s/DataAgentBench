code = """import json
import pandas as pd

package_data = pd.read_json(locals()['var_function-call-14514614563328429382'])

# Filter for IsRelease = true and parse Ordinal
package_data['VersionInfo'] = package_data['VersionInfo'].apply(json.loads)
package_data_filtered = package_data[package_data['VersionInfo'].apply(lambda x: x.get('IsRelease', False))]
package_data_filtered['Ordinal'] = package_data_filtered['VersionInfo'].apply(lambda x: x.get('Ordinal'))

# Find the latest release for each package
latest_releases = package_data_filtered.loc[package_data_filtered.groupby('Name')['Ordinal'].idxmax()]

# Select relevant columns and convert to JSON
result = latest_releases[['Name', 'Version']].to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-14514614563328429382': 'file_storage/function-call-14514614563328429382.json'}

exec(code, env_args)
