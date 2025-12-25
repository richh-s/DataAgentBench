code = """import pandas as pd
import json

package_data = pd.read_json(locals()['var_function-call-4961496144865610435'])

# Filter for release versions and parse VersionInfo
release_packages = package_data[package_data['VersionInfo'].notna()].copy()
release_packages['VersionInfo'] = release_packages['VersionInfo'].apply(json.loads)
release_packages = release_packages[release_packages['VersionInfo'].apply(lambda x: x.get('IsRelease', False))]

# Extract Ordinal for sorting
release_packages['Ordinal'] = release_packages['VersionInfo'].apply(lambda x: x.get('Ordinal'))

# Sort by Ordinal and get the latest version for each package
latest_release_packages = release_packages.loc[release_packages.groupby('Name')['Ordinal'].idxmax()]

# Select relevant columns
result = latest_release_packages[['Name', 'Version']].to_json(orient='records')
print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-4961496144865610435': 'file_storage/function-call-4961496144865610435.json'}

exec(code, env_args)
