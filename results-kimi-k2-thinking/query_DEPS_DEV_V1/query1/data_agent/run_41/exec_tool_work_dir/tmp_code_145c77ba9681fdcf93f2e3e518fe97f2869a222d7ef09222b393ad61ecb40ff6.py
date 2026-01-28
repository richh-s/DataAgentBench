code = """import json
import re

# Load all data files
pkg_file = locals()['var_functions.query_db:58']
ppv_file = locals()['var_functions.query_db:60']
pi_file = locals()['var_functions.query_db:28']

with open(pkg_file, 'r') as f:
    packages = json.load(f)

with open(ppv_file, 'r') as f:
    project_pvs = json.load(f)

with open(pi_file, 'r') as f:
    project_infos = json.load(f)

# Step 1: Find latest release for each package
print('Finding latest release versions...')
for pkg in packages:
    version_info = pkg['VersionInfo']
    # Extract IsRelease and Ordinal
    is_release = '"IsRelease": true' in version_info
    ordinal = 0
    match = re.search(r'"Ordinal":\s*(\d+)', version_info)
    if match:
        ordinal = int(match.group(1))
    pkg['IsRelease'] = is_release
    pkg['Ordinal'] = ordinal

# Get latest release version for each package
release_packages = [pkg for pkg in packages if pkg['IsRelease']]
latest_by_package = {}
for pkg in release_packages:
    name = pkg['Name']
    if name not in latest_by_package or pkg['Ordinal'] > latest_by_package[name]['Ordinal']:
        latest_by_package[name] = {
            'Name': name,
            'Version': pkg['Version'],
            'Ordinal': pkg['Ordinal']
        }

latest_packages = list(latest_by_package.values())
print(f'Found {len(latest_packages)} latest package releases')

# Step 2: Create package-to-project mapping
print('Creating package-to-project mapping...')
package_to_project = {}
for pv in project_pvs:
    key = (pv['Name'], pv['Version'])
    package_to_project[key] = pv['ProjectName']

print(f'Mapped {len(package_to_project)} package versions to projects')

# Step 3: Extract GitHub stars from project info
print('Extracting GitHub stars...')
project_to_stars = {}
for info in project_infos:
    proj_info = info.get('Project_Information', '')
    # Extract stars using regex
    match = re.search(r'(\d+(?:,\d+)*)\s+stars?', proj_info)
    if match:
        stars_str = match.group(1).replace(',', '')
        try:
            stars = int(stars_str)
            # Extract project name
            proj_match = re.search(r'project\s+([\w\-]+/[\w\-]+)', proj_info)
            if proj_match:
                proj_name = proj_match.group(1)
                project_to_stars[proj_name] = stars
        except:
            pass

print(f'Extracted stars for {len(project_to_stars)} projects')

# Step 4: Match packages with stars
print('Matching packages with GitHub stars...')
package_stars = []
for pkg in latest_packages:
    key = (pkg['Name'], pkg['Version'])
    if key in package_to_project:
        project_name = package_to_project[key]
        if project_name in project_to_stars:
            package_stars.append({
                'Name': pkg['Name'],
                'Version': pkg['Version'],
                'Project': project_name,
                'Stars': project_to_stars[project_name]
            })

print(f'Matched {len(package_stars)} packages with stars')

# Step 5: Get top 5
if package_stars:
    top_5 = sorted(package_stars, key=lambda x: x['Stars'], reverse=True)[:5]
    result = {
        'success': True,
        'top_5': top_5,
        'total_matched': len(package_stars),
        'message': 'Top 5 NPM packages by GitHub stars'
    }
else:
    result = {
        'success': False,
        'message': 'No packages matched',
        'total_matched': 0
    }

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': [{'Name': '@discordx/music', 'Version': '4.0.0-dev.1637888858.e2b75b9', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 149\n}'}, {'Name': '@discordx/music', 'Version': '4.0.0-dev.1637888858.e2b75b9', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 149\n}'}, {'Name': '@discordx/music', 'Version': '4.0.0-dev.1638102812.c236d4d', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 150\n}'}, {'Name': '@discordx/music', 'Version': '4.0.0-dev.1638102812.c236d4d', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 150\n}'}, {'Name': '@discordx/music', 'Version': '4.0.0-dev.1638167238.d70dfa2', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 151\n}'}, {'Name': '@discordx/music', 'Version': '4.0.0-dev.1638167238.d70dfa2', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 151\n}'}, {'Name': '@discordx/music', 'Version': '4.0.0-dev.1638275366.fe8249d', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 152\n}'}, {'Name': '@discordx/music', 'Version': '4.0.0-dev.1638275366.fe8249d', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 152\n}'}, {'Name': '@discordx/music', 'Version': '4.0.0-dev.1638321186.9e03b58', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 153\n}'}, {'Name': '@discordx/music', 'Version': '4.0.0-dev.1638321186.9e03b58', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 153\n}'}, {'Name': '@discordx/music', 'Version': '4.0.0-dev.1638426439.24d2cfa', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 154\n}'}, {'Name': '@discordx/music', 'Version': '4.0.0-dev.1638426439.24d2cfa', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 154\n}'}, {'Name': '@discordx/music', 'Version': '4.0.0-dev.1638493787.0de1743', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 155\n}'}, {'Name': '@discordx/music', 'Version': '4.0.0-dev.1638493787.0de1743', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 155\n}'}, {'Name': '@discordx/music', 'Version': '4.0.0-dev.1638534904.3ffc9cd', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 156\n}'}, {'Name': '@discordx/music', 'Version': '4.0.0-dev.1638534904.3ffc9cd', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 156\n}'}, {'Name': '@discordx/music', 'Version': '4.0.0-dev.1638753077.3871cff', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 157\n}'}, {'Name': '@discordx/music', 'Version': '4.0.0-dev.1638753077.3871cff', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 157\n}'}, {'Name': '@discordx/music', 'Version': '4.0.0-dev.1638772051.effa93e', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 158\n}'}, {'Name': '@discordx/music', 'Version': '4.0.0-dev.1638772051.effa93e', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 158\n}'}], 'var_functions.query_db:2': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.10', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dlcs/ng', 'Version': '1.0.0', 'ProjectType': 'GITHUB', 'ProjectName': 'winup/dlcs-ng', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dms/cli', 'Version': '1.0.1', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-cli', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dms/cli', 'Version': '1.0.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-cli', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dms/cli', 'Version': '0.8.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-cli', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dms/cli', 'Version': '0.9.3', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-cli', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dms/cli', 'Version': '0.2.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-cli', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@domp/fp', 'Version': '0.0.1', 'ProjectType': 'GITHUB', 'ProjectName': 'dom-packages/fp', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@domp/is', 'Version': '0.2.0', 'ProjectType': 'GITHUB', 'ProjectName': 'lohfu/domp-is', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@domp/is', 'Version': '0.1.3', 'ProjectType': 'GITHUB', 'ProjectName': 'lohfu/domp-is', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dosy/ws', 'Version': '8.11.1', 'ProjectType': 'GITHUB', 'ProjectName': 'dosyago/ws', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dosy/ws', 'Version': '8.11.4', 'ProjectType': 'GITHUB', 'ProjectName': 'dosyago/ws', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dot/cdk', 'Version': '2.1.0', 'ProjectType': 'GITHUB', 'ProjectName': 'shellscape/dot', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dot/cdk', 'Version': '0.1.0', 'ProjectType': 'GITHUB', 'ProjectName': 'shellscape/dot', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'Name': '@discordx/music', 'Version': '4.0.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 200\n}'}, {'Name': '@discordx/music', 'Version': '4.0.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 200\n}'}, {'Name': '@discordx/music', 'Version': '4.0.2', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 201\n}'}, {'Name': '@discordx/music', 'Version': '4.0.2', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 201\n}'}, {'Name': '@discordx/music', 'Version': '4.1.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 202\n}'}, {'Name': '@discordx/music', 'Version': '4.1.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 202\n}'}, {'Name': '@discordx/music', 'Version': '5.0.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 207\n}'}, {'Name': '@discordx/music', 'Version': '5.0.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 207\n}'}, {'Name': '@discordx/music', 'Version': '5.0.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 208\n}'}, {'Name': '@discordx/music', 'Version': '5.0.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 208\n}'}, {'Name': '@discordx/music', 'Version': '5.0.2', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 209\n}'}, {'Name': '@discordx/music', 'Version': '5.0.2', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 209\n}'}, {'Name': '@discordx/music', 'Version': '6.0.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 211\n}'}, {'Name': '@discordx/music', 'Version': '6.0.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 211\n}'}, {'Name': '@discordx/music', 'Version': '6.0.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 212\n}'}, {'Name': '@discordx/music', 'Version': '6.0.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 212\n}'}, {'Name': '@discordx/music', 'Version': '6.0.2', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 213\n}'}, {'Name': '@discordx/music', 'Version': '6.0.2', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 213\n}'}, {'Name': '@discordx/pagination', 'Version': '1.0.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 1\n}'}, {'Name': '@discordx/pagination', 'Version': '1.0.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 1\n}'}, {'Name': '@discordx/pagination', 'Version': '2.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 10\n}'}, {'Name': '@discordx/pagination', 'Version': '2.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 10\n}'}, {'Name': '@discordx/pagination', 'Version': '2.1.2', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 11\n}'}, {'Name': '@discordx/pagination', 'Version': '2.1.2', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 11\n}'}, {'Name': '@discordx/pagination', 'Version': '2.2.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'Name': '@discordx/pagination', 'Version': '2.2.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'Name': '@discordx/pagination', 'Version': '2.2.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}'}, {'Name': '@discordx/pagination', 'Version': '2.2.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}'}, {'Name': '@discordx/pagination', 'Version': '2.2.2', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'Name': '@discordx/pagination', 'Version': '2.2.2', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'Name': '@discordx/pagination', 'Version': '1.0.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 2\n}'}, {'Name': '@discordx/pagination', 'Version': '1.0.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 2\n}'}, {'Name': '@discordx/pagination', 'Version': '1.1.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 3\n}'}, {'Name': '@discordx/pagination', 'Version': '1.1.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 3\n}'}, {'Name': '@discordx/pagination', 'Version': '3.0.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 34\n}'}, {'Name': '@discordx/pagination', 'Version': '3.0.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 34\n}'}, {'Name': '@discordx/pagination', 'Version': '3.1.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 35\n}'}, {'Name': '@discordx/pagination', 'Version': '3.1.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 35\n}'}, {'Name': '@discordx/pagination', 'Version': '3.2.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 36\n}'}, {'Name': '@discordx/pagination', 'Version': '3.2.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 36\n}'}, {'Name': '@discordx/pagination', 'Version': '3.3.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 37\n}'}, {'Name': '@discordx/pagination', 'Version': '3.3.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 37\n}'}, {'Name': '@discordx/pagination', 'Version': '3.3.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 38\n}'}, {'Name': '@discordx/pagination', 'Version': '3.3.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 38\n}'}, {'Name': '@discordx/pagination', 'Version': '3.4.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 39\n}'}, {'Name': '@discordx/pagination', 'Version': '3.4.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 39\n}'}, {'Name': '@discordx/pagination', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 4\n}'}, {'Name': '@discordx/pagination', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 4\n}'}, {'Name': '@discordx/pagination', 'Version': '3.4.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 40\n}'}, {'Name': '@discordx/pagination', 'Version': '3.4.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 40\n}'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.list_db:14': ['packageinfo'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.list_db:24': ['project_info', 'project_packageversion'], 'var_functions.query_db:26': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:40': {'total_packages': 661372, 'first_package': {'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, 'version_info_sample': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, 'var_functions.execute_python:42': {'total_packages': 661372, 'release_packages': 337844, 'latest_packages': 15811, 'sample_latest': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'IsRelease': True, 'Ordinal': 29}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.2.2', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 25\n}', 'IsRelease': True, 'Ordinal': 25}, {'Name': '@discue/ui-components', 'Version': '0.38.2', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 45\n}', 'IsRelease': True, 'Ordinal': 45}, {'Name': '@dvcol/web-extension-utils', 'Version': '2.3.4', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 27\n}', 'IsRelease': True, 'Ordinal': 27}, {'Name': '@edgedev/firebase', 'Version': '2.0.20', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 133\n}', 'IsRelease': True, 'Ordinal': 133}]}, 'var_functions.execute_python:48': {'message': 'Latest packages prepared', 'count': 15811, 'sample': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Ordinal': 29}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.2.2', 'Ordinal': 25}, {'Name': '@discue/ui-components', 'Version': '0.38.2', 'Ordinal': 45}]}, 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json', 'var_functions.execute_python:54': {'status': 'loaded', 'counts': {'packages': 661372, 'project_packageversions': 1000, 'project_infos': 770}}, 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json'}

exec(code, env_args)
