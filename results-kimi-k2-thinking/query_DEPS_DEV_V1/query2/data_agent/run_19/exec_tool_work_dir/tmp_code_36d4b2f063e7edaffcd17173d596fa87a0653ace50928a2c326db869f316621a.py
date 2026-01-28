code = """import json
import re
from collections import defaultdict

# Load all the data
print("Loading data...")

# Package data
pkg_path = locals().get('var_functions.query_db:5')
with open(pkg_path, 'r') as f:
    package_data = json.load(f)

# Project package version data  
ppv_path = locals().get('var_functions.query_db:20')
with open(ppv_path, 'r') as f:
    ppv_data = json.load(f)

# Project info data
proj_path = locals().get('var_functions.query_db:26')
with open(proj_path, 'r') as f:
    proj_info_data = json.load(f)

print(f"Loaded {len(package_data)} packages, {len(ppv_data)} package-project mappings, {len(proj_info_data)} project info records")

# Step 1: Filter NPM MIT release packages
print("Filtering MIT release packages...")
mit_packages = []
for pkg in package_data:
    if pkg.get('System') == 'NPM':
        licenses = pkg.get('Licenses', '')
        version_info = pkg.get('VersionInfo', '')
        if 'MIT' in licenses and '"IsRelease": true' in version_info:
            mit_packages.append(pkg)

print(f"Found {len(mit_packages)} MIT release NPM packages")

# Step 2: Build package-to-project mappings (by name only, not version)
print("Building mappings...")
package_to_projects = defaultdict(set)
for mapping in ppv_data:
    if mapping.get('System') == 'NPM':
        key = (mapping.get('Name'),)
        project_name = mapping.get('ProjectName')
        if project_name:
            package_to_projects[key].add(project_name)

print(f"Built mappings for {len(package_to_projects)} unique package names")

# Step 3: Build project fork lookup
print("Building fork lookup...")
project_forks = {}
for proj in proj_info_data:
    proj_info = proj.get('Project_Information', '')
    # Extract project name
    match = re.search(r'project\s+([^\s]+)\s+is hosted', proj_info)
    if match:
        proj_name = match.group(1)
        # Extract fork count
        fork_match = re.search(r'(\d+)\s+forks?', proj_info)
        if fork_match:
            forks = int(fork_match.group(1))
            project_forks[proj_name] = forks

print(f"Found fork info for {len(project_forks)} projects")

# Step 4: Find matches and calculate max forks per package
print("Finding matches...")
package_max_forks = {}

for pkg in mit_packages:
    pkg_name = pkg.get('Name')
    key = (pkg_name,)
    
    if key in package_to_projects:
        project_names = package_to_projects[key]
        max_forks = 0
        best_project = None
        
        for proj_name in project_names:
            if proj_name in project_forks:
                forks = project_forks[proj_name]
                if forks > max_forks:
                    max_forks = forks
                    best_project = proj_name
        
        if best_project:
            if pkg_name not in package_max_forks or max_forks > package_max_forks[pkg_name]['forks']:
                package_max_forks[pkg_name] = {
                    'forks': max_forks,
                    'project': best_project,
                    'version': pkg.get('Version')
                }

print(f"Found {len(package_max_forks)} packages with fork information")

# Step 5: Get top 5
top_5 = sorted(package_max_forks.items(), key=lambda x: x[1]['forks'], reverse=True)[:5]

result = []
for pkg_name, info in top_5:
    result.append({
        'package_name': pkg_name,
        'github_project': info['project'],
        'forks': info['forks'],
        'version': info['version']
    })

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.query_db:2': [{'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'System': 'NPM', 'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'System': 'NPM', 'Name': '@eden-network/data', 'Version': '1.0.9-sev.5', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 14\n}'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:14': {'count': 176998, 'sample': [{'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0'}, {'System': 'NPM', 'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1'}, {'System': 'NPM', 'Name': '@eclipsejs/cli', 'Version': '1.0.0'}, {'System': 'NPM', 'Name': '@ebot7/edem-react', 'Version': '0.18.8'}, {'System': 'NPM', 'Name': '@e4a/irmaseal-wasm-bindings', 'Version': '0.0.1'}, {'System': 'NPM', 'Name': '@ebury/chameleon-components', 'Version': '0.1.46'}, {'System': 'NPM', 'Name': '@e-group/material-form', 'Version': '3.13.9'}, {'System': 'NPM', 'Name': '@e-group/material-layout', 'Version': '3.4.5'}, {'System': 'NPM', 'Name': '@dspworkplace/ui', 'Version': '1.0.3'}, {'System': 'NPM', 'Name': '@ditojs/router', 'Version': '0.125.0'}]}, 'var_functions.list_db:16': ['project_info', 'project_packageversion'], 'var_functions.query_db:18': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_functions.execute_python:24': {'total_mit_packages': 176998, 'matched_packages': 6, 'top_5_packages': [{'package_name': '@dumbstuff/template', 'version': '0.1.0', 'project_name': 'lberrocal/npm-packages-template', 'forks': 0}, {'package_name': '@dumbstuff/template', 'version': '0.1.0', 'project_name': 'lberrocal/npm-packages-template', 'forks': 0}, {'package_name': '@dumbstuff/template', 'version': '0.2.0', 'project_name': 'lberrocal/npm-packages-template', 'forks': 0}, {'package_name': '@dumbstuff/template', 'version': '0.2.0', 'project_name': 'lberrocal/npm-packages-template', 'forks': 0}, {'package_name': '@dumbstuff/template', 'version': '0.0.0', 'project_name': 'lberrocal/npm-packages-template', 'forks': 0}]}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
