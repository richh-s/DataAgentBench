code = """import json
import re

# Read the full result from the file
file_path = locals()['var_functions.query_db:8']
with open(file_path, 'r') as f:
    packages_data = json.load(f)

# Parse VersionInfo to extract Ordinal and filter for IsRelease = true
latest_versions = {}

for pkg in packages_data:
    name = pkg['Name']
    version = pkg['Version']
    version_info_str = pkg['VersionInfo']
    
    # Parse VersionInfo JSON string
    try:
        # Clean up the string
        version_info_str = version_info_str.replace('\n', '').strip()
        version_info = json.loads(version_info_str)
        
        is_release = version_info.get('IsRelease', False)
        ordinal = version_info.get('Ordinal', 0)
        
        # Only consider release versions
        if is_release:
            # Track the latest version (highest ordinal) for each package
            if name not in latest_versions or ordinal > latest_versions[name]['Ordinal']:
                latest_versions[name] = {
                    'Name': name,
                    'Version': version,
                    'Ordinal': ordinal
                }
    except:
        # Skip if parsing fails
        continue

# Convert to list of latest release versions
latest_release_packages = list(latest_versions.values())

print('__RESULT__:')
print(json.dumps(latest_release_packages))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:2': ['project_info', 'project_packageversion'], 'var_functions.query_db:5': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'Name': '@edgedev/firebase', 'Version': '1.0.12', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}'}, {'Name': '@eden-network/data', 'Version': '1.0.9-sev.5', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 14\n}'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
