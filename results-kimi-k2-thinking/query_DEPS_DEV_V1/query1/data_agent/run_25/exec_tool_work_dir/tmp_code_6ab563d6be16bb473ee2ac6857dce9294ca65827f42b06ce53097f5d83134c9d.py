code = """import json
import re

# Load all NPM package data
package_file = locals()['var_functions.query_db:18']
with open(package_file, 'r') as f:
    all_packages = json.load(f)

# Load project package version mappings
project_package_file = locals()['var_functions.query_db:16']
with open(project_package_file, 'r') as f:
    project_packages = json.load(f)

# Load project info data
project_info_file = locals()['var_functions.query_db:26']
with open(project_info_file, 'r') as f:
    project_info_list = json.load(f)

# Find latest release version for each NPM package
latest_packages = {}
for pkg in all_packages:
    if pkg['System'] != 'NPM':
        continue
    
    try:
        # Parse VersionInfo - normalize the JSON string
        version_info_str = pkg['VersionInfo'].strip()
        if not version_info_str:
            continue
        version_info = json.loads(version_info_str)
        
        if version_info.get('IsRelease', False):
            name = pkg['Name']
            version = pkg['Version']
            ordinal = version_info.get('Ordinal', 0)
            
            # Track latest release (highest ordinal) for each package
            if name not in latest_packages or ordinal > latest_packages[name]['ordinal']:
                latest_packages[name] = {'version': version, 'ordinal': ordinal}
    except Exception as e:
        continue

print('Found ' + str(len(latest_packages)) + ' NPM packages with release versions')

# Create mapping from package to project name
package_to_project = {}
for pp in project_packages:
    if pp['ProjectName']:
        package_to_project[(pp['Name'], pp['Version'])] = pp['ProjectName']

# Map latest packages to GitHub projects
packages_with_projects = []
for name, info in latest_packages.items():
    key = (name, info['version'])
    if key in package_to_project:
        packages_with_projects.append({
            'package_name': name,
            'version': info['version'],
            'project_name': package_to_project[key]
        })

print(str(len(packages_with_projects)) + ' packages mapped to GitHub projects')

# Extract GitHub star counts from project info
project_stars = {}
for item in project_info_list:
    text = item['Project_Information']
    star_match = re.search(r'(\d+)\s+stars', text)
    if star_match:
        stars = int(star_match.group(1))
        name_match = re.search(r'The project\s+([\w\-]+/[\.\w\-]+)', text)
        if name_match:
            project_name = name_match.group(1)
            project_stars[project_name] = stars

print('Extracted star counts for ' + str(len(project_stars)) + ' projects')

# Find star counts for packages
packages_with_stars = []
for pkg in packages_with_projects:
    project_name = pkg['project_name']
    if project_name in project_stars:
        packages_with_stars.append({
            'package_name': pkg['package_name'],
            'version': pkg['version'],
            'project_name': project_name,
            'stars': project_stars[project_name]
        })

print(str(len(packages_with_stars)) + ' packages have star information')

# Sort and get top 5
top_5 = sorted(packages_with_stars, key=lambda x: x['stars'], reverse=True)[:5]

result = {
    'top_5_packages': top_5,
    'stats': {
        'total_npm_packages_with_releases': len(latest_packages),
        'packages_with_github_projects': len(packages_with_projects),
        'packages_with_star_info': len(packages_with_stars)
    }
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.query_db:2': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'System': 'NPM', 'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'System': 'NPM', 'Name': '@edgedev/firebase', 'Version': '1.0.12', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}'}, {'System': 'NPM', 'Name': '@eden-network/data', 'Version': '1.0.9-sev.5', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 14\n}'}], 'var_functions.query_db:4': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_functions.query_db:6': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_functions.execute_python:12': {'package_info_sample_count': 10, 'project_package_sample_count': 5, 'project_info_sample_count': 5, 'versioninfo_examples': ['{\n  "IsRelease": true,\n  "Ordinal": 29\n}', '{\n  "IsRelease": true,\n  "Ordinal": 18\n}', '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'], 'project_info_examples': ['The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.']}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:24': {'packages_loaded': 661372, 'project_packages_loaded': 597602}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': [['leaflet/leaflet', 38715], ['theia-ide/theia', 18526], ['sass/node-sass', 8498], ['ljharb/qs', 8073], ['sveltejs/sapper', 7056], ['shaka-project/shaka-player', 6949], ['react-native-community/react-native-webview', 6345], ['mapbox/node-sqlite3', 5917], ['supasate/connected-react-router', 4737], ['securingsincity/react-ace', 4005]], 'var_functions.execute_python:34': {'mappings_created': 325940, 'sample_mappings': ['@dms/io:0.9.0 -> dataminingsupply/io', '@dvo/fc:0.0.4 -> isacvale/fc', '@djie/ui:1.0.17 -> laihaojie/jie']}, 'var_functions.execute_python:38': {'message': 'Loaded 661372 package records', 'status': 'ready'}}

exec(code, env_args)
