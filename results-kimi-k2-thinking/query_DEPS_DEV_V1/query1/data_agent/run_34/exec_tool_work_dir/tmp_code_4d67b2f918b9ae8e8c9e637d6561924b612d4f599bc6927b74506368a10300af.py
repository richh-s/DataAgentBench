code = """import json
import pandas as pd
import re

# Load package data from the file
with open(var_functions.query_db:6, 'r') as f:
    packages_raw = json.load(f)

print(f"Total packages: {len(packages_raw)}")

# Parse and filter packages
packages = []
for pkg in packages_raw:
    try:
        # Parse VersionInfo JSON
        version_info = json.loads(pkg['VersionInfo'])
        
        packages.append({
            'Name': pkg['Name'],
            'Version': pkg['Version'],
            'IsRelease': version_info.get('IsRelease', False),
            'Ordinal': version_info.get('Ordinal', 0)
        })
    except:
        # Skip malformed entries
        continue

print(f"Successfully parsed: {len(packages)} packages")

# Convert to DataFrame
df_packages = pd.DataFrame(packages)
print(f"NPM packages: {len(df_packages)}")

# Group by Name and find latest release version for each package
latest_releases = []
for name, group in df_packages.groupby('Name'):
    # Filter for release versions only
    release_versions = group[group['IsRelease'] == True]
    if not release_versions.empty:
        # Get the version with highest ordinal (latest release)
        latest = release_versions.loc[release_versions['Ordinal'].idxmax()]
        latest_releases.append({
            'Name': latest['Name'],
            'LatestVersion': latest['Version'],
            'Ordinal': latest['Ordinal']
        })

print(f"Latest release versions found: {len(latest_releases)}")

# Convert to DataFrame for further processing
df_latest = pd.DataFrame(latest_releases)
print(f"Sample of latest releases:")
print(df_latest.head())

result = df_latest.to_json(orient='records')
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:2': ['project_info', 'project_packageversion'], 'var_functions.query_db:5': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'Name': '@edgedev/firebase', 'Version': '1.0.12', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}'}, {'Name': '@eden-network/data', 'Version': '1.0.9-sev.5', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 14\n}'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
