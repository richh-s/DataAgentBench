code = """import json
import re

# Load the package data from the file
file_path = locals()['var_functions.query_db:6']
with open(file_path, 'r') as f:
    packages = json.load(f)

print(f'Loaded {len(packages)} package records')

# Process packages: extract Ordinal and find latest for each package
processed = []
for pkg in packages:
    try:
        # Extract Ordinal from VersionInfo JSON string
        version_info = pkg['VersionInfo']
        # Find the Ordinal value using regex
        ordinal_match = re.search(r'"Ordinal":\s*(\d+)', version_info)
        if ordinal_match:
            ordinal = int(ordinal_match.group(1))
            processed.append({
                'Name': pkg['Name'],
                'Version': pkg['Version'],
                'Ordinal': ordinal
            })
    except Exception as e:
        continue

print(f'Processed {len(processed)} valid records')

# Find latest (max ordinal) for each package
dict_latest = {}
for pkg in processed:
    name = pkg['Name']
    if name not in dict_latest or pkg['Ordinal'] > dict_latest[name]['Ordinal']:
        dict_latest[name] = {
            'Version': pkg['Version'],
            'Ordinal': pkg['Ordinal']
        }

print(f'Found {len(dict_latest)} unique NPM packages with releases')

# Convert to list for easier handling
latest_packages = [{'Name': k, 'Version': v['Version'], 'Ordinal': v['Ordinal']} for k, v in dict_latest.items()]
print('Sample:', latest_packages[:3])

# Save for next step
with open('latest_packages.json', 'w') as f:
    json.dump(latest_packages, f)

result = f'Found {len(latest_packages)} unique NPM packages with latest releases'
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:2': ['project_info', 'project_packageversion'], 'var_functions.query_db:4': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'Name': '@edgedev/firebase', 'Version': '1.0.12', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}'}, {'Name': '@eden-network/data', 'Version': '1.0.9-sev.5', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 14\n}'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
