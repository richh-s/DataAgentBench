code = """import json
import pandas as pd
import re

# Load the full package data from file
package_file = locals()['var_functions.query_db:10']
with open(package_file, 'r') as f:
    package_data = json.load(f)

# Load the project info data from file
project_file = locals()['var_functions.query_db:26']
with open(project_file, 'r') as f:
    project_data = json.load(f)

# Load the mapping data
mapping_data = locals()['var_functions.query_db:18']

print(f"Total packages: {len(package_data)}")
print(f"Total project info records: {len(project_data)}")
print(f"Total mapping records: {len(mapping_data)}")

# Step 1: Filter NPM packages with MIT license and IsRelease=true
mit_release_packages = []

for pkg in package_data:
    if pkg['System'] == 'NPM':
        # Check MIT license
        has_mit = 'MIT' in pkg['Licenses']
        if not has_mit:
            try:
                licenses = json.loads(pkg['Licenses'])
                has_mit = 'MIT' in str(licenses)
            except:
                pass
        
        # Check if release version
        is_release = '"IsRelease": true' in pkg['VersionInfo']
        if not is_release:
            try:
                version_info = json.loads(pkg['VersionInfo'])
                is_release = version_info.get('IsRelease', False)
            except:
                pass
        
        if has_mit and is_release:
            mit_release_packages.append({
                'System': pkg['System'],
                'Name': pkg['Name'],
                'Version': pkg['Version']
            })

print(f"MIT release packages: {len(mit_release_packages)}")

# Step 2: Create DataFrames
packages_df = pd.DataFrame(mit_release_packages)
mapping_df = pd.DataFrame(mapping_data)

# Step 3: Merge to get GitHub project names
if not packages_df.empty and not mapping_df.empty:
    mapped_projects = pd.merge(packages_df, mapping_df, on=['System', 'Name', 'Version'], how='inner')
    print(f"Mapped to projects: {len(mapped_projects)}")
    
    # Step 4: Extract project names and fork counts from project_info
    project_records = []
    for proj in project_data:
        proj_info = proj.get('Project_Information', '')
        
        # Extract project name (owner/repo format)
        name_match = re.search(r'The project ([\w-]+/[\w-]+)', proj_info, re.IGNORECASE)
        if not name_match:
            name_match = re.search(r'named ([\w-]+/[\w-]+)', proj_info, re.IGNORECASE)
        if not name_match:
            name_match = re.search(r'([\w-]+/[\w-]+)\s', proj_info)
        
        if name_match:
            project_name = name_match.group(1)
            
            # Extract fork count
            fork_match = re.search(r'(\d+)\s+forks?', proj_info, re.IGNORECASE)
            fork_count = int(fork_match.group(1)) if fork_match else 0
            
            project_records.append({
                'ProjectName': project_name,
                'fork_count': fork_count,
                'full_info': proj_info
            })
    
    projects_df = pd.DataFrame(project_records)
    print(f"Parsed project info records: {len(projects_df)}")
    
    # Step 5: Merge everything together
    final_df = pd.merge(mapped_projects, projects_df, on='ProjectName', how='inner')
    print(f"Final combined records: {len(final_df)}")
    
    if not final_df.empty:
        # Sort by fork count and get top 5
        top_5 = final_df.sort_values('fork_count', ascending=False).head(5)
        
        result = []
        for _, row in top_5.iterrows():
            result.append({
                'ProjectName': row['ProjectName'],
                'ForkCount': int(row['fork_count']),
                'PackageName': row['Name'],
                'Version': row['Version']
            })
        
        print("__RESULT__:")
        print(json.dumps(result, indent=2))
    else:
        print("No matching records found after final merge")
        print("__RESULT__:")
        print(json.dumps([]))
else:
    print("No packages or mappings found")
    print("__RESULT__:")
    print(json.dumps([]))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:2': ['project_info', 'project_packageversion'], 'var_functions.query_db:5': [], 'var_functions.query_db:8': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'Licenses': '[\n  "ISC"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'System': 'NPM', 'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'System': 'NPM', 'Name': '@edgedev/firebase', 'Version': '1.0.12', 'Licenses': '[\n  "ISC"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}'}, {'System': 'NPM', 'Name': '@eden-network/data', 'Version': '1.0.9-sev.5', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 14\n}'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_functions.execute_python:16': {'sample_package': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}], 'sample_project': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}]}, 'var_functions.query_db:18': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.10', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dlcs/ng', 'Version': '1.0.0', 'ProjectType': 'GITHUB', 'ProjectName': 'winup/dlcs-ng', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dms/cli', 'Version': '1.0.1', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-cli', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dms/cli', 'Version': '1.0.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-cli', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_functions.execute_python:22': [], 'var_functions.query_db:24': [{'ProjectName': 'eclipse-scout/scout.rt'}, {'ProjectName': 'eco/ecomponents'}, {'ProjectName': 'edgeandnode/common'}, {'ProjectName': 'discordx-ts/discordx'}, {'ProjectName': 'dolittle/home'}, {'ProjectName': 'taidomi-sapi-de-cv/domitai-sdk'}, {'ProjectName': 'dragonaxe01/packages.ts-logger'}, {'ProjectName': 'dweomercraft/events'}, {'ProjectName': 'dword-design/config-node'}, {'ProjectName': 'dxcli/manifest-file'}, {'ProjectName': 'easy-boot/easyboot'}, {'ProjectName': 'easynm/chores'}, {'ProjectName': 'dotupnet/dotup-ts-types'}, {'ProjectName': 'etcdigital/app.doutor.etc.br'}, {'ProjectName': 'draculjs/modular-framework'}, {'ProjectName': 'duotek/duotek-backoffice-ui'}, {'ProjectName': 'duvholt/tslint-yield'}, {'ProjectName': 'dyrkow/lint'}, {'ProjectName': 'ebuilding/platform-sdk'}, {'ProjectName': 'eclass/cev-providers'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
