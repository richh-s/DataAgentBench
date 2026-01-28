code = """import json
import os
import re
from collections import defaultdict

# Load all data
releases_file = './tmp/tmp_7h8j5t.json'
ppv_file = './tmp/tmp_s9j2w1.json' 
pi_file = './tmp/tmp_n7k3y9.json'

releases_raw = json.load(open(releases_file)) if os.path.exists(releases_file) else []
ppv_data = json.load(open(ppv_file)) if os.path.exists(ppv_file) else []
pi_data = json.load(open(pi_file)) if os.path.exists(pi_file) else []

print(f'Loaded {len(releases_raw)} releases, {len(ppv_data)} package-project mappings, {len(pi_data)} project infos')

# Process releases - find latest version per package
package_latest = {}
for pkg in releases_raw:
    try:
        version_info = json.loads(pkg['VersionInfo'])
        if version_info.get('IsRelease', False):
            name = pkg['Name']
            ordinal = version_info.get('Ordinal', 0)
            if name not in package_latest or ordinal > package_latest[name]['Ordinal']:
                package_latest[name] = {
                    'Version': pkg['Version'],
                    'Ordinal': ordinal
                }
    except:
        continue

print(f'Found {len(package_latest)} packages with releases')

# Build project info map
project_stars = {}
for proj in pi_data:
    try:
        info = proj.get('Project_Information', '')
        name_match = re.search(r'project\s+([\w-]+/[\w-]+)', info, re.I)
        if name_match:
            proj_name = name_match.group(1)
            stars_match = re.search(r'([\d,]+)\s+stars', info)
            if stars_match:
                stars = int(stars_match.group(1).replace(',', ''))
                project_stars[proj_name] = stars
    except:
        continue

print(f'Found {len(project_stars)} projects with stars')

# Check for overlaps
release_pkg_names = set(package_latest.keys())
ppv_pkg_names = set(p['Name'] for p in ppv_data)
ppv_proj_names = set(p['ProjectName'] for p in ppv_data)
pi_proj_names = set(project_stars.keys())

print(f'Release packages: {len(release_pkg_names)}')
print(f'PPV packages: {len(ppv_pkg_names)}')
print(f'PPV projects: {len(ppv_proj_names)}')
print(f'PI projects: {len(pi_proj_names)}')
print(f'Release ∩ PPV packages: {len(release_pkg_names.intersection(ppv_pkg_names))}')
print(f'PPV ∩ PI projects: {len(ppv_proj_names.intersection(pi_proj_names))}')

# Force direct matching to find valid combinations
scored = []
for ppv in ppv_data:
    pkg = ppv['Name']
    proj = ppv['ProjectName']
    ver = ppv['Version']
    
    if pkg in package_latest and proj in project_stars:
        if ver == package_latest[pkg]['Version']:
            scored.append({
                'package': pkg,
                'version': ver,
                'project': proj,
                'stars': project_stars[proj]
            })

print(f'Matched {len(scored)} packages with stars')
if scored:
    top5 = sorted(scored, key=lambda x: x['stars'], reverse=True)[:5]
    print(json.dumps(top5, indent=2))
else:
    print('No matches found')"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:2': ['project_info', 'project_packageversion'], 'var_functions.query_db:5': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@ecl%2Ftwig-component-carousel/3.11.1"\n  }\n]'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@douganderson444%2Fpanzoom-node/v/1.1.5"\n  }\n]'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@douganderson444%2Fpanzoom-node/v/1.1.1"\n  }\n]'}, {'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@dreamworld%2Fdw-select/3.1.2-fix-double-click-issue.1"\n  }\n]'}, {'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@discue%2Fui-components/0.13.0"\n  }\n]'}], 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_functions.query_db:10': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.'}, {'Project_Information': 'The project is hosted on GitHub under the name learnfrontend-dc/product-cart, and it currently has 2 open issues. It has garnered a total of 11 stars and has been forked 12 times.'}, {'Project_Information': 'The GitHub project ledgerproject/keypairoom currently has 3 open issues, 3 stars, and 0 forks.'}, {'Project_Information': 'The project leebyron/jasmine-check is hosted on GitHub and currently has 0 open issues, 11 stars, and 3 forks.'}, {'Project_Information': 'The project leebyron/testcheck-js on GitHub has an open issues count of 29, a stars count of 1185, and a forks count of 58, making it a notable repository in the community.'}, {'Project_Information': 'The project leecade/react-native-swiper is hosted on GitHub and has a total of 786 open issues, along with an impressive 10,249 stars and 2,392 forks, making it a popular choice among developers for implementing swiping functionality in React Native applications.'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:17': {'error': 'File not found, need to query with smaller result set'}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'tmp_files': [], 'expected_file': './tmp/tmp_0t3l9z.json', 'file_exists': False}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:24': {'tmp_dir': '/tmp', 'all_files': [], 'matching_files': [], 'current_dir': '/workspace'}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_functions.execute_python:36': {'ppv_records': 5000, 'pi_records': 1000, 'ppv_sample': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectName': 'dataminingsupply/dms-io'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectName': 'isacvale/fc'}], 'pi_sample': [{'ProjectName': 'a7650/vue3-draggable-resizable'}, {'ProjectName': 'doreamonjs/doreamon'}]}, 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.execute_python:40': {'matched_packages': 0, 'top_5_packages': []}, 'var_functions.execute_python:42': [], 'var_functions.execute_python:46': [], 'var_functions.execute_python:48': {'message': 'No matches found', 'scored_count': 0}, 'var_functions.execute_python:50': []}

exec(code, env_args)
