code = """import json
import pandas as pd

# Load the full result from the file
with open(locals()['var_function-call-16890172847440563023'], 'r') as f:
    package_data = json.load(f)

df_packages = pd.DataFrame(package_data)

# Parse VersionInfo to extract IsRelease and Ordinal
df_packages['VersionInfoParsed'] = df_packages['VersionInfo'].apply(json.loads)
df_packages['IsRelease'] = df_packages['VersionInfoParsed'].apply(lambda x: x.get('IsRelease', False))
df_packages['Ordinal'] = df_packages['VersionInfoParsed'].apply(lambda x: x.get('Ordinal', 0))

# Filter for actual releases
df_releases = df_packages[df_packages['IsRelease'] == True]

# Find the latest release version for each package name
idx = df_releases.groupby('Name')['Ordinal'].idxmax()
latest_releases = df_releases.loc[idx]

result = latest_releases[['Name', 'Version']].to_json(orient='records')
print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-16890172847440563023': 'file_storage/function-call-16890172847440563023.json'}

exec(code, env_args)
