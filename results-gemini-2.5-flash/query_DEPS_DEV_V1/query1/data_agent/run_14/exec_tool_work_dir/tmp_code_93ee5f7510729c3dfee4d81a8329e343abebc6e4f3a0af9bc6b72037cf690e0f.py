code = """import json
import pandas as pd

package_info = pd.read_json(locals()['var_function-call-18442683985073922078'])

# Filter for IsRelease = True and parse Ordinal
package_info['VersionInfo'] = package_info['VersionInfo'].apply(json.loads)
release_packages = package_info[package_info['VersionInfo'].apply(lambda x: x.get('IsRelease', False))].copy()
release_packages['Ordinal'] = release_packages['VersionInfo'].apply(lambda x: x.get('Ordinal'))

# Get the latest release for each package
latest_releases = release_packages.loc[release_packages.groupby('Name')['Ordinal'].idxmax()]

# Select relevant columns
result = latest_releases[['Name', 'Version']].to_json(orient='records')

print("__RESULT__:")
print(result)"""

env_args = {'var_function-call-18442683985073922078': 'file_storage/function-call-18442683985073922078.json'}

exec(code, env_args)
