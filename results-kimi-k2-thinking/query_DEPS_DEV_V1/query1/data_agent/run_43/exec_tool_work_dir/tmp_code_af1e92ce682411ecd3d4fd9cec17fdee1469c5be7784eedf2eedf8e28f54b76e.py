code = """import json
import pandas as pd

# Read the query result from the file
result_file = var_functions.query_db:12
with open(result_file, 'r') as f:
    package_data = json.load(f)

# Process the VersionInfo field to extract IsRelease and Ordinal
processed_packages = []
for row in package_data:
    try:
        version_info = json.loads(row['VersionInfo'])
        processed_packages.append({
            'Name': row['Name'],
            'Version': row['Version'],
            'IsRelease': version_info.get('IsRelease', False),
            'Ordinal': version_info.get('Ordinal', 0)
        })
    except:
        # Skip if VersionInfo can't be parsed
        continue

# Filter for release versions only and find the latest release for each package
release_packages = [p for p in processed_packages if p['IsRelease']]

# Group by package name and find the one with highest Ordinal (latest release)
latest_releases = {}
for pkg in release_packages:
    name = pkg['Name']
    if name not in latest_releases or pkg['Ordinal'] > latest_releases[name]['Ordinal']:
        latest_releases[name] = pkg

result_packages = list(latest_releases.values())
print('__RESULT__:')
print(json.dumps({
    'total_release_versions': len(release_packages),
    'unique_packages_with_releases': len(result_packages),
    'sample_latest_releases': result_packages[:5]
}))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:1': ['project_info', 'project_packageversion'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
