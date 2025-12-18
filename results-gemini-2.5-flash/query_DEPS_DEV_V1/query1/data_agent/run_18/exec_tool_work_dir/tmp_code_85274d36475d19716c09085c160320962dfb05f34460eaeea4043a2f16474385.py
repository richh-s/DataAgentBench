code = """import pandas as pd
import json

# Load the full data from the JSON file
with open(locals()['var_function-call-5930656202702153224'], 'r') as f:
    package_data = json.load(f)

df_packages = pd.DataFrame(package_data)

# Filter for IsRelease = true and convert Ordinal to numeric
df_packages['VersionInfo'] = df_packages['VersionInfo'].apply(json.loads)
df_packages_releases = df_packages[df_packages['VersionInfo'].apply(lambda x: x.get('IsRelease', False))].copy()
df_packages_releases['Ordinal'] = df_packages_releases['VersionInfo'].apply(lambda x: x.get('Ordinal'))
df_packages_releases['Ordinal'] = pd.to_numeric(df_packages_releases['Ordinal'])

# Find the latest release version for each package
latest_releases = df_packages_releases.loc[df_packages_releases.groupby('Name')['Ordinal'].idxmax()]

# Select relevant columns for the next step
result = latest_releases[['Name', 'Version']].to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-5930656202702153224': 'file_storage/function-call-5930656202702153224.json'}

exec(code, env_args)
