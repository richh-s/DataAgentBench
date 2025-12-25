code = """import json
import pandas as pd

# Load the full JSON data from the file
with open(locals()['var_function-call-7931738845791159468'], 'r') as f:
    package_data = json.load(f)

df = pd.DataFrame(package_data)

# Convert VersionInfo string to dictionary and extract IsRelease and Ordinal
df['VersionInfo'] = df['VersionInfo'].apply(json.loads)
df['IsRelease'] = df['VersionInfo'].apply(lambda x: x.get('IsRelease'))
df['Ordinal'] = df['VersionInfo'].apply(lambda x: x.get('Ordinal'))

# Filter for IsRelease = true and sort by UpstreamPublishedAt and Ordinal to get the latest release
latest_releases = df[df['IsRelease'] == True]
latest_releases['UpstreamPublishedAt'] = pd.to_numeric(latest_releases['UpstreamPublishedAt'])
latest_releases = latest_releases.sort_values(by=['Name', 'UpstreamPublishedAt', 'Ordinal'], ascending=[True, False, False])
latest_releases = latest_releases.drop_duplicates(subset=['Name'], keep='first')

# Select relevant columns for the next step
result = latest_releases[['System', 'Name', 'Version']].to_json(orient='records')

print("__RESULT__:")
print(result)"""

env_args = {'var_function-call-7931738845791159468': 'file_storage/function-call-7931738845791159468.json'}

exec(code, env_args)
