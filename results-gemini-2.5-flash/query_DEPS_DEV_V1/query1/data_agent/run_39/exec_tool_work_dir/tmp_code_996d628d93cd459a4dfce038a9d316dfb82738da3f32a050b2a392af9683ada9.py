code = """import pandas as pd
import json

package_info_data = pd.read_json(locals()['var_function-call-10417754161782902564'])

def parse_version_info(version_info_str):
    try:
        return json.loads(version_info_str)
    except json.JSONDecodeError:
        return {}

package_info_data['ParsedVersionInfo'] = package_info_data['VersionInfo'].apply(parse_version_info)

# Filter for IsRelease = true and extract Ordinal
release_packages = package_info_data[
    package_info_data['ParsedVersionInfo'].apply(lambda x: x.get('IsRelease', False))
].copy()

release_packages['Ordinal'] = release_packages['ParsedVersionInfo'].apply(lambda x: x.get('Ordinal'))

# Find the latest release version for each package
latest_release_packages = release_packages.loc[release_packages.groupby('Name')['Ordinal'].idxmax()]

result = latest_release_packages[['Name', 'Version']].to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-2542952245398537233': ['packageinfo'], 'var_function-call-10417754161782902564': 'file_storage/function-call-10417754161782902564.json'}

exec(code, env_args)
