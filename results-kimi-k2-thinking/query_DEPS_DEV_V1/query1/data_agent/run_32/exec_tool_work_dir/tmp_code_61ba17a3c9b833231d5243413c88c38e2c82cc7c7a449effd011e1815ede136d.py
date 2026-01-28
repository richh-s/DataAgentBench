code = """import json
import re

# Load data from the variables stored in locals
package_data = var_functions.query_db:28  # All NPM packages with IsRelease: true
pv_data = var_functions.query_db:6      # Package-Version mappings
info_data = var_functions.query_db:20   # Project info records

print('== Step 1: Process packages to get latest release versions ==')
# Get latest release versions by tracking max ordinal per package
latest_packages = {}
for pkg in package_data:
    name = pkg['Name']
    version = pkg['Version']
    # Extract ordinal from VersionInfo string
    ordinal_match = re.search(r'"Ordinal":\s*(\d+)', pkg['VersionInfo'])
    ordinal = int(ordinal_match.group(1)) if ordinal_match else 0
    
    if name not in latest_packages or ordinal > latest_packages[name]['ordinal']:
        latest_packages[name] = {
            'version': version,
            'ordinal': ordinal
        }

print(f'Found {len(latest_packages)} unique packages with releases')
print('Sample latest packages:', list(latest_packages.items())[:5])

print('\n== Step 2: Map packages to GitHub repositories ==')
# Map package+version to GitHub ProjectName
package_to_repo = {}
for pv in pv_data:
    if pv['System'] == 'NPM':
        pkg_key = (pv['Name'], pv['Version'])
        package_to_repo[pkg_key] = pv['ProjectName']

print(f'Mapped {len(package_to_repo)} package-version pairs to repos')

print('\n== Step 3: Extract stars from project_info ==')
repo_stars = {}
for record in info_data:
    proj_info = record['Project_Information']
    # Use regex to extract stars count
    stars_match = re.search(r'(\d+[\d,]*)\s+stars?', proj_info)
    if stars_match:
        # Parse stars number (remove commas and convert to int)
        stars_str = stars_match.group(1).replace(',', '')
        stars = int(stars_str)
        # Extract repo name from the text
        repo_match = re.search(r'project\s+(\S+)\s+is', proj_info) or \
                    re.search(r'project\s+(\S+)\s+on\s+GitHub', proj_info)
        if repo_match:
            repo_name = repo_match.group(1)
            repo_stars[repo_name] = stars

print(f'Found {len(repo_stars)} repos with star counts')
print('Sample repos and stars:', list(repo_stars.items())[:5])

print('\n== Step 4: Find matches between packages and projects ==')
package_stars = {}
for pkg_name, pkg_info in list(latest_packages.items())[:100]:  # Test with first 100
    pkg_key = (pkg_name, pkg_info['version'])
    if pkg_key in package_to_repo:
        repo = package_to_repo[pkg_key]
        if repo in repo_stars:
            stars = repo_stars[repo]
            package_stars[pkg_name] = {
                'version': pkg_info['version'],
                'stars': stars,
                'repo': repo
            }

print(f'Found stars for {len(package_stars)} packages')

print('\n== Step 5: Get top 5 packages by stars ==')
top_packages = sorted(package_stars.items(), key=lambda x: x[1]['stars'], reverse=True)[:5]

for pkg in top_packages:
    print(f"Package: {pkg[0]} | Version: {pkg[1]['version']} | Stars: {pkg[1]['stars']} | Repo: {pkg[1]['repo']}")

print('__RESULT__:')
print(json.dumps({'top_packages': top_packages}, default=str))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:2': ['project_info', 'project_packageversion'], 'var_functions.query_db:4': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_functions.query_db:6': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_functions.query_db:8': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'Name': '@edgedev/firebase', 'Version': '1.0.12', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}'}, {'Name': '@dyoshikawa/mentor-php-env', 'Version': '0.0.11', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 10\n}'}, {'Name': '@eclipsejs/cli', 'Version': '1.0.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}'}, {'Name': '@dytesdk/electron-main', 'Version': '1.0.2', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 6\n}'}, {'Name': '@ebot7/edem-react', 'Version': '0.18.8', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 55\n}'}, {'Name': '@e4a/irmaseal-wasm-bindings', 'Version': '0.0.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 1\n}'}, {'Name': '@ebury/chameleon-components', 'Version': '0.1.46', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 46\n}'}, {'Name': '@e-group/material-form', 'Version': '3.13.9', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'Name': '@e-group/material-layout', 'Version': '3.4.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 6\n}'}, {'Name': '@edgeros/jsre-types', 'Version': '1.8.8', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 53\n}'}, {'Name': '@edgeros/jsre-types', 'Version': '1.8.12', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 57\n}'}, {'Name': '@dxos/client', 'Version': '2.18.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 1131\n}'}, {'Name': '@dxos/client', 'Version': '2.18.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 1131\n}'}, {'Name': '@edgeandnode/components', 'Version': '1.0.135', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 146\n}'}, {'Name': '@edgeandnode/components', 'Version': '1.0.58', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 69\n}'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:26': {'packages_count': 39, 'pv_count': 5}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
