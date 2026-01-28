code = """import json
import re

# Read all release packages from file
query_result = locals()['var_functions.query_db:22']
if isinstance(query_result, str) and query_result.endswith('.json'):
    with open(query_result, 'r') as f:
        release_packages = json.load(f)
else:
    release_packages = query_result

print(f"Total release packages: {len(release_packages)}")

# Group by package name and find latest (highest ordinal) for each
from collections import defaultdict

package_versions = defaultdict(list)
for pkg in release_packages:
    name = pkg.get('Name')
    version = pkg.get('Version')
    try:
        version_info = json.loads(pkg.get('VersionInfo', '{}'))
        ordinal = version_info.get('Ordinal', 0)
        package_versions[name].append({
            'Version': version,
            'Ordinal': ordinal,
            'Original': pkg
        })
    except:
        continue

# Get latest version for each package
latest_packages = []
for name, versions in package_versions.items():
    if versions:
        latest = max(versions, key=lambda x: x['Ordinal'])
        latest_packages.append({
            'Name': name,
            'Version': latest['Version'],
            'Ordinal': latest['Ordinal']
        })

print(f"Latest releases per package: {len(latest_packages)}")
print(f"Sample latest packages:")
for i, pkg in enumerate(latest_packages[:10]):
    print(f"  {pkg['Name']}: {pkg['Version']}")

# Save results
print('__RESULT__:')
print(json.dumps(latest_packages[:100]))  # Return first 100 for next steps"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:2': ['project_info', 'project_packageversion'], 'var_functions.query_db:5': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'Name': '@edgedev/firebase', 'Version': '1.0.12', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}'}, {'Name': '@eden-network/data', 'Version': '1.0.9-sev.5', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 14\n}'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'Name': '@edgedev/firebase', 'Version': '1.0.12', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}'}, {'Name': '@eden-network/data', 'Version': '1.0.9-sev.5', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 14\n}'}, {'Name': '@dyoshikawa/mentor-php-env', 'Version': '0.0.11', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 10\n}'}, {'Name': '@eclipsejs/cli', 'Version': '1.0.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}'}, {'Name': '@dytesdk/electron-main', 'Version': '1.0.2', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 6\n}'}, {'Name': '@dxos/client', 'Version': '2.31.8-dev.dcd68d50', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1605\n}'}, {'Name': '@dxos/client', 'Version': '2.31.8-dev.dcd68d50', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1605\n}'}, {'Name': '@ebot7/edem-react', 'Version': '0.18.8', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 55\n}'}, {'Name': '@e4a/irmaseal-wasm-bindings', 'Version': '0.0.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 1\n}'}, {'Name': '@ebury/chameleon-components', 'Version': '0.1.46', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 46\n}'}, {'Name': '@dxos/console-app', 'Version': '1.0.0-beta.4', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 4\n}'}, {'Name': '@dxos/console-app', 'Version': '1.0.0-beta.4', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 4\n}'}], 'var_functions.execute_python:14': {'total_records': 661372, 'sample_records': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}]}, 'var_functions.execute_python:16': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.2.2'}, {'Name': '@discue/ui-components', 'Version': '0.38.2'}, {'Name': '@dvcol/web-extension-utils', 'Version': '2.3.4'}, {'Name': '@edgedev/firebase', 'Version': '2.0.20'}, {'Name': '@dyoshikawa/mentor-php-env', 'Version': '0.1.0'}, {'Name': '@eclipsejs/cli', 'Version': '1.1.0'}, {'Name': '@dytesdk/electron-main', 'Version': '1.1.0'}, {'Name': '@ebot7/edem-react', 'Version': '0.24.1'}, {'Name': '@e4a/irmaseal-wasm-bindings', 'Version': '0.2.3'}, {'Name': '@ebury/chameleon-components', 'Version': '2.4.1'}, {'Name': '@e-group/material-form', 'Version': '7.41.4'}, {'Name': '@e-group/material-layout', 'Version': '7.40.2'}, {'Name': '@edgeros/jsre-types', 'Version': '2.2.4'}, {'Name': '@dxos/client', 'Version': '2.33.8'}, {'Name': '@edgeandnode/components', 'Version': '27.5.2'}, {'Name': '@dkoerner/propertyui', 'Version': '0.1.70'}, {'Name': '@dspworkplace/ui', 'Version': '1.5.47'}, {'Name': '@ditojs/router', 'Version': '2.10.5'}, {'Name': '@ditojs/ui', 'Version': '2.10.5'}], 'var_functions.query_db:18': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_functions.query_db:21': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
