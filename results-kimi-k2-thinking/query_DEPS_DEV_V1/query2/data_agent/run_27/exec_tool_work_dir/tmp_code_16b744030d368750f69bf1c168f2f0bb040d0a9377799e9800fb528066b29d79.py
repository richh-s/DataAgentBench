code = """import json
import re

# Load all data from storage
mit_packages_file = locals()['var_functions.query_db:14']
project_pkg_file = locals()['var_functions.query_db:20']

with open(mit_packages_file, 'r') as f:
    mit_packages = json.load(f)

with open(project_pkg_file, 'r') as f:
    project_packages = json.load(f)

# Create project package version lookup
project_map = {}
for pkg in project_packages:
    key = (pkg['System'], pkg['Name'], pkg['Version'])
    if key not in project_map:  # Avoid overwriting, but shouldn't matter
        project_map[key] = pkg['ProjectName']

print(f'MIT packages: {len(mit_packages)}')
print(f'Project mappings: {len(project_map)}')

# Load project info
top_projects = []
try:
    # Query project_info table to get projects with highest forks
    # that could potentially match our packages
    from collections import Counter
    
    # Count occurrences of projects in mappings
    project_counts = Counter(project_map.values())
    top_mapped_projects = project_counts.most_common(20)
    
    print('Top 20 most common projects in mappings:')
    for proj, count in top_mapped_projects:
        print(f'  {proj}: {count} package mappings')
        
    # For brevity, let's just parse a subset of project_info manually
    # The file is small (only 770 records)
    project_info_file = locals()['var_functions.query_db:40']
    with open(project_info_file, 'r') as f:
        project_info_list = json.load(f)
    
    # Build info map with parsed fork counts
    info_map = {}
    for info in project_info_list:
        text = info['Project_Information']
        if 'GitHub' not in text and 'GITHUB' not in text:
            continue
            
        # Extract fork count
        fork_match = re.search(r'(\d+) forks?', text, re.IGNORECASE)
        if fork_match:
            fork_count = int(fork_match.group(1))
            
            # Extract project name (repo path)
            # Handle different formats
            name_match = re.search(r'The project ([\w-]+/[\w-]+)', text)
            if name_match:
                project_name = name_match.group(1)
                info_map[project_name] = {
                    'info': info,
                    'fork_count': fork_count
                }
    
    print(f'Parsed project info for {len(info_map)} projects with forks')
    
    # Match MIT packages with projects and get fork counts
    results = []
    for pkg in mit_packages:
        key = (pkg['System'], pkg['Name'], pkg['Version'])
        project_name = project_map.get(key)
        
        if project_name and project_name in info_map:
            fork_count = info_map[project_name]['fork_count']
            results.append({
                'package': pkg,
                'project_name': project_name,
                'fork_count': fork_count
            })
    
    print(f'Matched {len(results)} MIT packages with project fork info')
    
    if len(results) > 0:
        # Sort and get top 10 to have room for deduplication
        top_results = sorted(results, key=lambda x: x['fork_count'], reverse=True)[:10]
        
        print('Top 10 results (with potential duplicates):')
        for i, item in enumerate(top_results, 1):
            print(f"{i}. {item['package']['Name']} -> {item['project_name']} ({item['fork_count']} forks)")
        
        # Deduplicate by project
        seen_projects = set()
        unique_top = []
        for item in top_results:
            if item['project_name'] not in seen_projects:
                seen_projects.add(item['project_name'])
                unique_top.append(item)
        
        print(f'\nTop 5 unique results:')
        final_top_5 = unique_top[:5]
        for i, item in enumerate(final_top_5, 1):
            print(f"{i}. {item['package']['Name']} v{item['package']['Version']}")
            print(f"   {item['project_name']} - {item['fork_count']} forks\n")
        
        print('__RESULT__:')
        print(json.dumps(final_top_5))
    else:
        print('No matches found with fork info')
        print('__RESULT__:')
        print(json.dumps([]))
        
except Exception as e:
    print(f'Error: {e}')
    import traceback
    traceback.print_exc()
    print('__RESULT__:')
    print(json.dumps([]))"""

env_args = {'var_functions.query_db:0': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'Licenses': '[\n  "ISC"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_functions.query_db:2': [{'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'System': 'NPM', 'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'System': 'NPM', 'Name': '@eden-network/data', 'Version': '1.0.9-sev.5', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 14\n}'}, {'System': 'NPM', 'Name': '@eclipsejs/cli', 'Version': '1.0.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.31.8-dev.dcd68d50', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1605\n}'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.31.8-dev.dcd68d50', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1605\n}'}, {'System': 'NPM', 'Name': '@ebot7/edem-react', 'Version': '0.18.8', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 55\n}'}, {'System': 'NPM', 'Name': '@e4a/irmaseal-wasm-bindings', 'Version': '0.0.1', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 1\n}'}], 'var_functions.query_db:4': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.list_db:8': ['project_info', 'project_packageversion'], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:34': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_functions.query_db:36': [{'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0'}, {'System': 'NPM', 'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1'}, {'System': 'NPM', 'Name': '@eclipsejs/cli', 'Version': '1.0.0'}, {'System': 'NPM', 'Name': '@ebot7/edem-react', 'Version': '0.18.8'}, {'System': 'NPM', 'Name': '@e4a/irmaseal-wasm-bindings', 'Version': '0.0.1'}, {'System': 'NPM', 'Name': '@ebury/chameleon-components', 'Version': '0.1.46'}, {'System': 'NPM', 'Name': '@e-group/material-form', 'Version': '3.13.9'}, {'System': 'NPM', 'Name': '@e-group/material-layout', 'Version': '3.4.5'}, {'System': 'NPM', 'Name': '@dspworkplace/ui', 'Version': '1.0.3'}, {'System': 'NPM', 'Name': '@ditojs/router', 'Version': '0.125.0'}], 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.execute_python:44': {'mit_packages_count': 176998, 'project_packages_count': 591699, 'project_info_count': 770}, 'var_functions.execute_python:46': [{'package': {'System': 'NPM', 'Name': '@dreampie/semantic-ui', 'Version': '2.2.11'}, 'project_name': 'semantic-org/semantic-ui', 'fork_count': 4955}, {'package': {'System': 'NPM', 'Name': '@dreampie/semantic-ui', 'Version': '2.2.11'}, 'project_name': 'semantic-org/semantic-ui', 'fork_count': 4955}, {'package': {'System': 'NPM', 'Name': '@dlwlrma00/react-native-webview-bypass-ssl', 'Version': '11.0.3'}, 'project_name': 'react-native-community/react-native-webview', 'fork_count': 2962}, {'package': {'System': 'NPM', 'Name': '@dlwlrma00/react-native-webview-bypass-ssl', 'Version': '11.0.3'}, 'project_name': 'react-native-community/react-native-webview', 'fork_count': 2962}, {'package': {'System': 'NPM', 'Name': '@dpoineau/react-scripts>1.0.0>node-sass', 'Version': '3.10.1'}, 'project_name': 'sass/node-sass', 'fork_count': 1326}], 'var_functions.execute_python:50': []}

exec(code, env_args)
