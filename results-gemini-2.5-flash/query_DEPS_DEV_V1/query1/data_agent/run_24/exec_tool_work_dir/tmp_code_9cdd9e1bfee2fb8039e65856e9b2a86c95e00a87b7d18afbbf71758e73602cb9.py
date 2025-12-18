code = """import json
import pandas as pd

package_info_data = pd.read_json(locals()['var_function-call-7087967583845426888'])

# Filter for release versions
release_versions = package_info_data[package_info_data['VersionInfo'].apply(lambda x: json.loads(x).get('IsRelease', False))]

# Convert Ordinal to numeric and handle potential errors
release_versions['Ordinal'] = release_versions['VersionInfo'].apply(lambda x: json.loads(x).get('Ordinal', 0))

# Find the latest release version for each package
latest_release_versions = release_versions.loc[release_versions.groupby('Name')['Ordinal'].idxmax()]

# Select relevant columns
result = latest_release_versions[['Name', 'Version']].to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-7087967583845426888': 'file_storage/function-call-7087967583845426888.json'}

exec(code, env_args)
