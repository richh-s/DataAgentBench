code = """import json, os, re

# Load all data from file paths
packages_path = var_functions.query_db:58
pv_mappings_path = var_functions.query_db:38
proj_info_path = var_functions.query_db:74

# Read packages data
with open(packages_path, 'r') as f:
    packages = json.load(f)

# Read package-version mappings
with open(pv_mappings_path, 'r') as f:
    pv_mappings = json.load(f)

# Read project info
with open(proj_info_path, 'r') as f:
    proj_info = json.load(f)

# Step 1: Find latest release version for each package
latest_packages = {}
for p in packages:
    name = p['Name']
    version = p['Version']
    vi = p['VersionInfo']
    
    # Extract ordinal from VersionInfo string
    m = re.search(r'Ordinal":\s*(\d+)', vi)
    ordinal = int(m.group(1)) if m else 0
    
    # Check if it's a release version
    if 'IsRelease": true' in vi:
        if name not in latest_packages or ordinal > latest_packages[name]['ordinal']:
            latest_packages[name] = {'version': version, 'ordinal': ordinal}

# Step 2: Map package+version to GitHub repository
pv_to_repo = {}
for pv in pv_mappings:
    if pv['System'] == 'NPM':
        key = (pv['Name'], pv['Version'])
        pv_to_repo[key] = pv['ProjectName']

# Step 3: Extract GitHub star counts from project info
repo_stars = {}
for info in proj_info:
    txt = info.get('Project_Information', '')
    if not txt or txt == 'None':
        continue
    
    # Extract stars count
    m = re.search(r'(\d+[\d,]*)\s+stars?', txt)
    if m:
        stars = int(m.group(1).replace(',', ''))
        
        # Extract repository name
        m2 = re.search(r'project\s+(\S+?)\s', txt)
        if m2:
            repo_name = m2.group(1)
            repo_stars[repo_name] = stars

# Step 4: Match packages with their stars
matched_packages = []
for pkg_name, pkg_info in latest_packages.items():
    key = (pkg_name, pkg_info['version'])
    if key in pv_to_repo:
        repo = pv_to_repo[key]
        if repo in repo_stars:
            matched_packages.append([
                pkg_name,
                pkg_info['version'],
                repo_stars[repo],
                repo
            ])

# Step 5: Sort by stars and get top 5
matched_packages.sort(key=lambda x: x[2], reverse=True)
top5 = matched_packages[:5]

# Build formatted output
output_lines = []
output_lines.append('Top 5 NPM Packages by GitHub Stars (Latest Release Versions)')
output_lines.append('=' * 60)
output_lines.append('')

for i, pkg in enumerate(top5, 1):
    output_lines.append(f"{i}. {pkg[0]}")
    output_lines.append(f"   Version: {pkg[1]}")
    output_lines.append(f"   Stars: {pkg[2]:,}")
    output_lines.append(f"   Repository: {pkg[3]}")
    output_lines.append("")

result_text = "\n".join(output_lines)

print('__RESULT__:')
print(json.dumps(result_text))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:2': ['project_info', 'project_packageversion'], 'var_functions.query_db:4': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_functions.query_db:6': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_functions.query_db:8': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'Name': '@edgedev/firebase', 'Version': '1.0.12', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}'}, {'Name': '@dyoshikawa/mentor-php-env', 'Version': '0.0.11', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 10\n}'}, {'Name': '@eclipsejs/cli', 'Version': '1.0.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}'}, {'Name': '@dytesdk/electron-main', 'Version': '1.0.2', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 6\n}'}, {'Name': '@ebot7/edem-react', 'Version': '0.18.8', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 55\n}'}, {'Name': '@e4a/irmaseal-wasm-bindings', 'Version': '0.0.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 1\n}'}, {'Name': '@ebury/chameleon-components', 'Version': '0.1.46', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 46\n}'}, {'Name': '@e-group/material-form', 'Version': '3.13.9', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'Name': '@e-group/material-layout', 'Version': '3.4.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 6\n}'}, {'Name': '@edgeros/jsre-types', 'Version': '1.8.8', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 53\n}'}, {'Name': '@edgeros/jsre-types', 'Version': '1.8.12', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 57\n}'}, {'Name': '@dxos/client', 'Version': '2.18.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 1131\n}'}, {'Name': '@dxos/client', 'Version': '2.18.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 1131\n}'}, {'Name': '@edgeandnode/components', 'Version': '1.0.135', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 146\n}'}, {'Name': '@edgeandnode/components', 'Version': '1.0.58', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 69\n}'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:26': {'packages_count': 39, 'pv_count': 5}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': [{'ProjectName': 'dataminingsupply/dms-io'}, {'ProjectName': 'isacvale/fc'}, {'ProjectName': 'laihaojie/jie'}, {'ProjectName': 'laihaojie/jie'}, {'ProjectName': 'laihaojie/jie'}, {'ProjectName': 'laihaojie/jie'}, {'ProjectName': 'laihaojie/jie'}, {'ProjectName': 'winup/dlcs-ng'}, {'ProjectName': 'dataminingsupply/dms-cli'}, {'ProjectName': 'dataminingsupply/dms-cli'}], 'var_functions.query_db:35': [{'Name': '@dms/io', 'Version': '0.9.0', 'ProjectName': 'dataminingsupply/dms-io', 'Project_Information': 'None', 'Description': 'None'}, {'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectName': 'isacvale/fc', 'Project_Information': 'None', 'Description': 'None'}, {'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectName': 'laihaojie/jie', 'Project_Information': 'None', 'Description': 'None'}, {'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectName': 'laihaojie/jie', 'Project_Information': 'None', 'Description': 'None'}, {'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectName': 'laihaojie/jie', 'Project_Information': 'None', 'Description': 'None'}, {'Name': '@djie/ws', 'Version': '1.0.10', 'ProjectName': 'laihaojie/jie', 'Project_Information': 'None', 'Description': 'None'}, {'Name': '@djie/ws', 'Version': '1.0.17', 'ProjectName': 'laihaojie/jie', 'Project_Information': 'None', 'Description': 'None'}, {'Name': '@dlcs/ng', 'Version': '1.0.0', 'ProjectName': 'winup/dlcs-ng', 'Project_Information': 'None', 'Description': 'None'}, {'Name': '@dms/cli', 'Version': '1.0.1', 'ProjectName': 'dataminingsupply/dms-cli', 'Project_Information': 'None', 'Description': 'None'}, {'Name': '@dms/cli', 'Version': '1.0.0', 'ProjectName': 'dataminingsupply/dms-cli', 'Project_Information': 'None', 'Description': 'None'}], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': [{'total_packages': '661372'}], 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.execute_python:62': {'package_count': 200000}, 'var_functions.execute_python:64': {'packages': 200000, 'pv_mappings': 597602, 'proj_info': 5}, 'var_functions.execute_python:70': [{'package': '@duchesstoffee/react-responsive-carousel', 'version': '3.2.10', 'stars': 2534, 'repo': 'leandrowd/react-responsive-carousel'}], 'var_functions.query_db:72': 'file_storage/functions.query_db:72.json', 'var_functions.query_db:74': 'file_storage/functions.query_db:74.json'}

exec(code, env_args)
