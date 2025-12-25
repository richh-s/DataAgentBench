code = """import json
import pandas as pd

package_data = pd.read_json(locals()['var_function-call-2495042024869739884'])

# Parse VersionInfo and filter for releases
package_data['VersionInfoParsed'] = package_data['VersionInfo'].apply(json.loads)
release_packages = package_data[package_data['VersionInfoParsed'].apply(lambda x: x.get('IsRelease', False))]

# Find the latest version for each package
latest_releases = release_packages.loc[release_packages.groupby('Name')['VersionInfoParsed'].apply(lambda x: x.apply(lambda y: y.get('Ordinal', 0)).idxmax())]

# Select relevant columns for the next step
result = latest_releases[['Name', 'Version']].to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-2495042024869739884': 'file_storage/function-call-2495042024869739884.json'}

exec(code, env_args)
