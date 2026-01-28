code = """import json
import re

# Step 1: Load package data and filter for MIT releases
print("Loading package data...")
package_data_key = 'var_functions.query_db:5'
package_data_path = locals().get(package_data_key)

if isinstance(package_data_path, str):
    with open(package_data_path, 'r') as f:
        package_data = json.load(f)
else:
    package_data = package_data

# Filter for NPM MIT releases
mit_packages = []
for pkg in package_data:
    if pkg.get('System') != 'NPM':
        continue
    
    licenses_str = pkg.get('Licenses', '')
    if 'MIT' not in licenses_str:
        continue
    
    version_info_str = pkg.get('VersionInfo', '')
    if not version_info_str or 'IsRelease' not in version_info_str:
        continue
    
    # Check if IsRelease is true
    if '"IsRelease": true' in version_info_str or '"IsRelease":true' in version_info_str:
        mit_packages.append({
            'System': pkg['System'],
            'Name': pkg['Name'],
            'Version': pkg['Version']
        })

print(f"Found {len(mit_packages)} MIT release packages")

# Step 2: Load project_packageversion data
print("Loading project mappings...")
ppv_path = locals().get('var_functions.query_db:20')

if isinstance(ppv_path, str):
    with open(ppv_path, 'r') as f:
        ppv_data = json.load(f)
else:
    ppv_data = ppv_path

# Filter for NPM packages only
npm_ppv = [item for item in ppv_data if item.get('System') == 'NPM']

print(f"Found {len(npm_ppv)} NPM project mappings")

# Step 3: Load project_info data
print("Loading project info...")
proj_info_path = locals().get('var_functions.query_db:22')

if isinstance(proj_info_path, str):
    with open(proj_info_path, 'r') as f:
        proj_info_data = json.load(f)
else:
    proj_info_data = proj_info_path

print(f"Found {len(proj_info_data)} project info records")

# Step 4: Create lookup dictionaries
print("Creating lookups...")

# Create project_packageversion lookup: (System, Name, Version) -> ProjectName
ppv_lookup = {}
for item in npm_ppv:
    key = (item.get('System'), item.get('Name'), item.get('Version'))
    ppv_lookup[key] = item.get('ProjectName')

# Create project_info lookup: ProjectName -> Project_Information
proj_lookup = {}
for item in proj_info_data:
    # Extract project name from Project_Information
    proj_info = item.get('Project_Information', '')
    if 'project' in proj_info and 'is hosted' in proj_info:
        # Extract project name between "project" and "is hosted"
        match = re.search(r'project\s+([^\s]+)\s+is hosted', proj_info)
        if match:
            proj_name = match.group(1)
            proj_lookup[proj_name] = proj_info

print(f"Created {len(ppv_lookup)} package-to-project mappings")
print(f"Created {len(proj_lookup)} project info mappings")

# Step 5: Match packages to projects and extract fork counts
print("Matching packages to projects...")
package_forks = []

for pkg in mit_packages:
    key = (pkg['System'], pkg['Name'], pkg['Version'])
    project_name = ppv_lookup.get(key)
    
    if project_name and project_name in proj_lookup:
        proj_info = proj_lookup[project_name]
        
        # Extract fork count
        fork_match = re.search(r'(\d+)\s+forks?', proj_info)
        if fork_match:
            fork_count = int(fork_match.group(1))
            package_forks.append({
                'package_name': pkg['Name'],
                'version': pkg['Version'],
                'project_name': project_name,
                'forks': fork_count
            })

print(f"Matched {len(package_forks)} packages with fork information")

# Step 6: Sort and get top 5
top_packages = sorted(package_forks, key=lambda x: x['forks'], reverse=True)[:5]

result = {
    'total_mit_packages': len(mit_packages),
    'matched_packages': len(package_forks),
    'top_5_packages': top_packages
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.query_db:2': [{'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'System': 'NPM', 'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'System': 'NPM', 'Name': '@eden-network/data', 'Version': '1.0.9-sev.5', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 14\n}'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:14': {'count': 176998, 'sample': [{'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0'}, {'System': 'NPM', 'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1'}, {'System': 'NPM', 'Name': '@eclipsejs/cli', 'Version': '1.0.0'}, {'System': 'NPM', 'Name': '@ebot7/edem-react', 'Version': '0.18.8'}, {'System': 'NPM', 'Name': '@e4a/irmaseal-wasm-bindings', 'Version': '0.0.1'}, {'System': 'NPM', 'Name': '@ebury/chameleon-components', 'Version': '0.1.46'}, {'System': 'NPM', 'Name': '@e-group/material-form', 'Version': '3.13.9'}, {'System': 'NPM', 'Name': '@e-group/material-layout', 'Version': '3.4.5'}, {'System': 'NPM', 'Name': '@dspworkplace/ui', 'Version': '1.0.3'}, {'System': 'NPM', 'Name': '@ditojs/router', 'Version': '0.125.0'}]}, 'var_functions.list_db:16': ['project_info', 'project_packageversion'], 'var_functions.query_db:18': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}]}

exec(code, env_args)
