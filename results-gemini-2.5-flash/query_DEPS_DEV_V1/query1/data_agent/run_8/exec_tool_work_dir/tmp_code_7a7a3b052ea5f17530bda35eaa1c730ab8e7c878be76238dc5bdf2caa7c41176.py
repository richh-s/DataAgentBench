code = """import json
import pandas as pd

package_info_path = locals()['var_function-call-5263700515361630309']
with open(package_info_path, 'r') as f:
    package_info = json.load(f)

df_package_info = pd.DataFrame(package_info)

# Filter for IsRelease = true and parse Ordinal
df_package_info['VersionInfoParsed'] = df_package_info['VersionInfo'].apply(lambda x: json.loads(x) if pd.notnull(x) else {})
df_package_info_filtered = df_package_info[df_package_info['VersionInfoParsed'].apply(lambda x: x.get('IsRelease', False))]
df_package_info_filtered['Ordinal'] = df_package_info_filtered['VersionInfoParsed'].apply(lambda x: x.get('Ordinal'))

# Find the latest version for each package based on Ordinal
latest_versions = df_package_info_filtered.loc[df_package_info_filtered.groupby('Name')['Ordinal'].idxmax()]

print("__RESULT__:")
print(latest_versions[['Name', 'Version']].to_json(orient='records'))"""

env_args = {'var_function-call-5263700515361630309': 'file_storage/function-call-5263700515361630309.json'}

exec(code, env_args)
