code = """import json
import pandas as pd

file_path = locals()['var_function-call-15075189816740011234']
with open(file_path, 'r') as f:
    package_data = json.load(f)

df = pd.DataFrame(package_data)

# Parse VersionInfo column
df['VersionInfo'] = df['VersionInfo'].apply(json.loads)
df['IsRelease'] = df['VersionInfo'].apply(lambda x: x.get('IsRelease'))
df['Ordinal'] = df['VersionInfo'].apply(lambda x: x.get('Ordinal'))

# Filter for releases only
releases_df = df[df['IsRelease'] == True]

# Find the latest version for each package based on Ordinal
latest_releases = releases_df.loc[releases_df.groupby('Name')['Ordinal'].idxmax()]

# Select relevant columns
result = latest_releases[['Name', 'Version']].to_json(orient='records')
print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-15075189816740011234': 'file_storage/function-call-15075189816740011234.json'}

exec(code, env_args)
