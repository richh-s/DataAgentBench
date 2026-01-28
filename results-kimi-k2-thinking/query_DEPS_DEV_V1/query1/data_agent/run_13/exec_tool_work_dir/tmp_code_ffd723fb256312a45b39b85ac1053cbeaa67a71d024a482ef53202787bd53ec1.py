code = """import json

# Load release packages from package_database
file_path = locals()['var_functions.query_db:26']
if isinstance(file_path, str) and file_path.endswith('.json'):
    with open(file_path, 'r') as f:
        release_packages = json.load(f)
else:
    release_packages = locals()['var_functions.query_db:26']

# Load project mappings from project_database
mapping_file_path = locals()['var_functions.query_db:20']
if isinstance(mapping_file_path, str) and mapping_file_path.endswith('.json'):
    with open(mapping_file_path, 'r') as f:
        project_mappings = json.load(f)
else:
    project_mappings = locals()['var_functions.query_db:20']

print(f"Release packages: {len(release_packages)}")
print(f"Project mappings: {len(project_mappings)}")

# Group packages by name and find latest version
from collections import defaultdict
packages_by_name = defaultdict(list)
for pkg in release_packages:
    try:
        version_info = json.loads(pkg['VersionInfo'])
        if version_info.get('IsRelease', False):
            packages_by_name[pkg['Name']].append({
                'System': pkg['System'],
                'Name': pkg['Name'],
                'Version': pkg['Version'],
                'Ordinal': version_info.get('Ordinal', 0)
            })
    except:
        continue

# Find latest version for each package
latest_packages = {}
for name, versions in packages_by_name.items():
    if versions:
        latest = max(versions, key=lambda x: x['Ordinal'])
        latest_packages[name] = latest

print(f"Latest packages: {len(latest_packages)}")

# Build lookup for project mappings
# Package identifier -> ProjectName
package_to_project = {}
for mapping in project_mappings:
    if mapping['System'] == 'NPM':
        key = f"{mapping['Name']}@{mapping['Version']}"
        package_to_project[key] = mapping['ProjectName']

# Match latest packages with projects
matched_packages = []
for name, pkg in latest_packages.items():
    key = f"{pkg['Name']}@{pkg['Version']}"
    if key in package_to_project:
        matched_packages.append({
            'Name': pkg['Name'],
            'Version': pkg['Version'],
            'ProjectName': package_to_project[key]
        })

print(f"Matched packages: {len(matched_packages)}")
print("Sample matched packages:")
for pkg in matched_packages[:10]:
    print(f"  {pkg['Name']}@{pkg['Version']} -> {pkg['ProjectName']}")

result = {
    'matched_packages': matched_packages[:100]  # Send subset for next step
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.query_db:2': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'System': 'NPM', 'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'System': 'NPM', 'Name': '@edgedev/firebase', 'Version': '1.0.12', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}'}, {'System': 'NPM', 'Name': '@eden-network/data', 'Version': '1.0.9-sev.5', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 14\n}'}], 'var_functions.list_db:5': ['project_info', 'project_packageversion'], 'var_functions.execute_python:8': [{'Package': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo_raw': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'VersionInfo_parsed': {'IsRelease': True, 'Ordinal': 29}}, {'Package': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo_raw': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}', 'VersionInfo_parsed': {'IsRelease': True, 'Ordinal': 18}}, {'Package': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo_raw': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}', 'VersionInfo_parsed': {'IsRelease': True, 'Ordinal': 14}}, {'Package': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo_raw': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}', 'VersionInfo_parsed': {'IsRelease': False, 'Ordinal': 129}}, {'Package': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo_raw': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}', 'VersionInfo_parsed': {'IsRelease': True, 'Ordinal': 12}}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'System': 'NPM', 'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'System': 'NPM', 'Name': '@edgedev/firebase', 'Version': '1.0.12', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}'}, {'System': 'NPM', 'Name': '@eden-network/data', 'Version': '1.0.9-sev.5', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 14\n}'}, {'System': 'NPM', 'Name': '@dyoshikawa/mentor-php-env', 'Version': '0.0.11', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 10\n}'}, {'System': 'NPM', 'Name': '@eclipsejs/cli', 'Version': '1.0.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}'}, {'System': 'NPM', 'Name': '@dytesdk/electron-main', 'Version': '1.0.2', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 6\n}'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.31.8-dev.dcd68d50', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1605\n}'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.31.8-dev.dcd68d50', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1605\n}'}, {'System': 'NPM', 'Name': '@ebot7/edem-react', 'Version': '0.18.8', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 55\n}'}, {'System': 'NPM', 'Name': '@e4a/irmaseal-wasm-bindings', 'Version': '0.0.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 1\n}'}, {'System': 'NPM', 'Name': '@ebury/chameleon-components', 'Version': '0.1.46', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 46\n}'}, {'System': 'NPM', 'Name': '@dxos/console-app', 'Version': '1.0.0-beta.4', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 4\n}'}, {'System': 'NPM', 'Name': '@dxos/console-app', 'Version': '1.0.0-beta.4', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 4\n}'}, {'System': 'NPM', 'Name': '@eddeee888/gcg-typescript-resolver-files', 'Version': '0.0.0-pr9-run20-1-20221027114308', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 60\n}'}, {'System': 'NPM', 'Name': '@dxos/broadcast', 'Version': '2.19.4-dev.54bbea97', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 147\n}'}, {'System': 'NPM', 'Name': '@dxos/broadcast', 'Version': '2.19.4-dev.54bbea97', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 147\n}'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.1.2-beta.0', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 974\n}'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.1.2-beta.0', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 974\n}'}, {'System': 'NPM', 'Name': '@e-group/material-form', 'Version': '3.13.9', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@e-group/material-layout', 'Version': '3.4.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 6\n}'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.7.17-alpha.0', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1011\n}'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.7.17-alpha.0', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1011\n}'}, {'System': 'NPM', 'Name': '@dxos/broadcast', 'Version': '2.22.1-dev.e16cf8db', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 239\n}'}, {'System': 'NPM', 'Name': '@dxos/broadcast', 'Version': '2.22.1-dev.e16cf8db', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 239\n}'}, {'System': 'NPM', 'Name': '@edgeros/jsre-types', 'Version': '1.8.8', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 53\n}'}, {'System': 'NPM', 'Name': '@dxos/cli-chess', 'Version': '1.0.0-beta.84', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 25\n}'}, {'System': 'NPM', 'Name': '@dxos/cli-chess', 'Version': '1.0.0-beta.84', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 25\n}'}, {'System': 'NPM', 'Name': '@edgeros/jsre-types', 'Version': '1.8.12', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 57\n}'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.18.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 1131\n}'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.18.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 1131\n}'}, {'System': 'NPM', 'Name': '@edgeandnode/gds', 'Version': '3.0.0-global-header-1692827365828-fc1e4a1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 287\n}'}, {'System': 'NPM', 'Name': '@edgeandnode/gds', 'Version': '3.0.0-global-header-1699370867138-33c8884', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 304\n}'}, {'System': 'NPM', 'Name': '@edgeandnode/components', 'Version': '1.0.135', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 146\n}'}, {'System': 'NPM', 'Name': '@edgeandnode/components', 'Version': '1.0.58', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 69\n}'}, {'System': 'NPM', 'Name': '@dkoerner/propertyui', 'Version': '0.0.18', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@dspworkplace/ui', 'Version': '1.0.3', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 4\n}'}, {'System': 'NPM', 'Name': '@dollarshaveclub/js-utils', 'Version': '7.6.0-rc.5', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 63\n}'}, {'System': 'NPM', 'Name': '@ditojs/router', 'Version': '0.125.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 87\n}'}, {'System': 'NPM', 'Name': '@ditojs/ui', 'Version': '0.113.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 107\n}'}, {'System': 'NPM', 'Name': '@ditojs/admin', 'Version': '0.155.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 164\n}'}, {'System': 'NPM', 'Name': '@dsrv/kms', 'Version': '0.2.2', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@domojs/rfx-parsers', 'Version': '1.5.9', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 23\n}'}, {'System': 'NPM', 'Name': '@dnvgl/playwright-live-recorder', 'Version': '2.0.14', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 15\n}'}], 'var_functions.execute_python:16': {'total_packages': 661372, 'latest_release_count': 15811, 'latest_packages': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Ordinal': 29}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.2.2', 'Ordinal': 25}, {'Name': '@discue/ui-components', 'Version': '0.38.2', 'Ordinal': 45}, {'Name': '@dvcol/web-extension-utils', 'Version': '2.3.4', 'Ordinal': 27}, {'Name': '@edgedev/firebase', 'Version': '2.0.20', 'Ordinal': 133}, {'Name': '@dyoshikawa/mentor-php-env', 'Version': '0.1.0', 'Ordinal': 15}, {'Name': '@eclipsejs/cli', 'Version': '1.1.0', 'Ordinal': 14}, {'Name': '@dytesdk/electron-main', 'Version': '1.1.0', 'Ordinal': 13}, {'Name': '@ebot7/edem-react', 'Version': '0.24.1', 'Ordinal': 89}, {'Name': '@e4a/irmaseal-wasm-bindings', 'Version': '0.2.3', 'Ordinal': 19}, {'Name': '@ebury/chameleon-components', 'Version': '2.4.1', 'Ordinal': 343}, {'Name': '@e-group/material-form', 'Version': '7.41.4', 'Ordinal': 355}, {'Name': '@e-group/material-layout', 'Version': '7.40.2', 'Ordinal': 201}, {'Name': '@edgeros/jsre-types', 'Version': '2.2.4', 'Ordinal': 113}, {'Name': '@dxos/client', 'Version': '2.33.8', 'Ordinal': 1716}, {'Name': '@edgeandnode/components', 'Version': '27.5.2', 'Ordinal': 613}, {'Name': '@dkoerner/propertyui', 'Version': '0.1.70', 'Ordinal': 108}, {'Name': '@dspworkplace/ui', 'Version': '1.5.47', 'Ordinal': 180}, {'Name': '@ditojs/router', 'Version': '2.10.5', 'Ordinal': 291}, {'Name': '@ditojs/ui', 'Version': '2.10.5', 'Ordinal': 344}]}, 'var_functions.query_db:18': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectName': 'dataminingsupply/dms-io'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectName': 'isacvale/fc'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.10', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.17', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@dlcs/ng', 'Version': '1.0.0', 'ProjectName': 'winup/dlcs-ng'}, {'System': 'NPM', 'Name': '@dms/cli', 'Version': '1.0.1', 'ProjectName': 'dataminingsupply/dms-cli'}, {'System': 'NPM', 'Name': '@dms/cli', 'Version': '1.0.0', 'ProjectName': 'dataminingsupply/dms-cli'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
