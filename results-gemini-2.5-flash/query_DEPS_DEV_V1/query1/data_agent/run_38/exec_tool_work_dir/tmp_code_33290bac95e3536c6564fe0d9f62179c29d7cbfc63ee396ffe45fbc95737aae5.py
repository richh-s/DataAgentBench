code = """import pandas as pd
import json

package_info = pd.read_json(locals()['var_function-call-14058135258420604114'])

# Filter for IsRelease = true and parse VersionInfo
release_packages = package_info[package_info['VersionInfo'].apply(lambda x: json.loads(x).get('IsRelease', False))].copy()
release_packages['Ordinal'] = release_packages['VersionInfo'].apply(lambda x: json.loads(x).get('Ordinal'))

# Find the latest release version for each package
latest_release_packages = release_packages.loc[release_packages.groupby('Name')['Ordinal'].idxmax()]

# Select relevant columns and convert to JSON
result = latest_release_packages[['Name', 'Version']].to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-14058135258420604114': 'file_storage/function-call-14058135258420604114.json'}

exec(code, env_args)
