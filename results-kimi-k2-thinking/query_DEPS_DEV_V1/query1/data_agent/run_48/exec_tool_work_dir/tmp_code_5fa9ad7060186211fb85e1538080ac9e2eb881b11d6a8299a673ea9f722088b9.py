code = """import json
import os
import re
from collections import defaultdict

# Load all the data files we have
releases_file = './tmp/tmp_7h8j5t.json'
ppv_file = './tmp/tmp_s9j2w1.json'
pi_file = './tmp/tmp_n7k3y9.json'

# Load with proper error handling
releases_raw = []
if os.path.exists(releases_file):
    with open(releases_file, 'r') as f:
        releases_raw = json.load(f)

ppv_data = []
if os.path.exists(ppv_file):
    with open(ppv_file, 'r') as f:
        ppv_data = json.load(f)

pi_data = []
if os.path.exists(pi_file):
    with open(pi_file, 'r') as f:
        pi_data = json.load(f)

print(f'Data loaded: {len(releases_raw)} releases, {len(ppv_data)} ppv, {len(pi_data)} project info')
print()

# Step 1: Parse all release versions and find latest for each package
print('=== STEP 1: Finding latest release versions ===')
repackage_latest = {}
valid_releases = 0

for pkg in releases_raw:
    try:
        version_info = json.loads(pkg['VersionInfo'])
        if version_info.get('IsRelease', False):
            valid_releases += 1
            name = pkg['Name']
            version = pkg['Version']
            ordinal = version_info.get('Ordinal', 0)
            
            current = repackage_latest.get(name)
            if not current or ordinal > current['ordinal']:
                repackage_latest[name] = {
                    'version': version,
                    'ordinal': ordinal
                }
    except Exception as e:
        continue

print(f'Processed {valid_releases} release records')
print(f'Found latest versions for {len(repackage_latest)} packages')
print(f'Sample: {list(repackage_latest.items())[:3]}')
print()

# Step 2: Extract star counts from project info
print('=== STEP 2: Extracting project star counts ===')
project_star_map = {}
star_extraction_count = 0

for proj in pi_data:
    try:
        info = proj.get('Project_Information', '')
        # Look for project name in owner/repo or full URL format
        name_match = re.search(r'(?:project\s+)?([\w-]+/[\w-]+)', info, re.I)
        stars_match = re.search(r'(\d[\d,]*)\s+stars', info)
        
        if name_match and stars_match:
            proj_name = name_match.group(1)
            stars = int(stars_match.group(1).replace(',', ''))
            project_star_map[proj_name] = stars
            star_extraction_count += 1
    except Exception as e:
        continue

print(f'Extracted {star_extraction_count} star counts')
print(f'Sample: {list(project_star_map.items())[:5]}')
print()

# Step 3: Organize package-project mappings by project
print('=== STEP 3: Organizing package-project mappings ===')
project_packages = defaultdict(list)
for ppv in ppv_data:
    project_packages[ppv['ProjectName']].append({
        'name': ppv['Name'],
        'version': ppv['Version']
    })

print(f'Found {len(project_packages)} unique projects in PPV data')
print(f'Sample project: {list(project_packages.keys())[0] if project_packages else "None"}')
print()

# Step 4: Find matches across all three data sources
print('=== STEP 4: Finding complete matches ===')
complete_matches = []
match_count = 0

for proj_name, stars in project_star_map.items():
    if proj_name not in project_packages:
        continue
    
    packages_for_project = project_packages[proj_name]
    
    for pkg_info in packages_for_project:
        pkg_name = pkg_info['name']
        pkg_version = pkg_info['version']
        
        # Check if this package has a latest release version
        if pkg_name not in repackage_latest:
            continue
        
        # Check if this version matches the latest release
        latest_info = repackage_latest[pkg_name]
        if pkg_version != latest_info['version']:
            continue
        
        # We have a complete match
        match_count += 1
        complete_matches.append({
            'package': pkg_name,
            'version': pkg_version,
            'project': proj_name,
            'stars': stars
        })

print(f'Found {match_count} complete matches')

# Step 5: Sort and get top 5
if complete_matches:
    print('=== STEP 5: Top 5 Most Popular NPM Packages ===')
    top_packages = sorted(complete_matches, key=lambda x: x['stars'], reverse=True)[:5]
    
    for i, pkg in enumerate(top_packages, 1):
        print(f"{i}. {pkg['package']}")
        print(f"   Version: {pkg['version']}")
        print(f"   Project: {pkg['project']}")
        print(f"   GitHub Stars: {pkg['stars']:,}")
        print()
    
    result = {'top_5': top_packages}
else:
    # Debug: Show partial matches
    print('No complete matches found. Debug analysis:')
    print()
    
    latest_pkgs = set(repackage_latest.keys())
    ppv_pkgs = set(p['Name'] for p in ppv_data)
    ppv_projs = set(p['ProjectName'] for p in ppv_data)
    star_projs = set(project_star_map.keys())
    
    print(f'Release packages: {len(latest_pkgs)}')
    print(f'PPV packages: {len(ppv_pkgs)}')
    print(f'PPV projects: {len(ppv_projs)}')
    print(f'Projects with stars: {len(star_projs)}')
    print()
    print(f'Release ∩ PPV packages: {len(latest_pkgs.intersection(ppv_pkgs))}')
    print(f'PPV projects ∩ Star projects: {len(ppv_projs.intersection(star_projs))}')
    print()
    
    # Show some specific examples to debug
    high_star_projects = sorted([(k, v) for k, v in project_star_map.items() if v > 1000], key=lambda x: x[1], reverse=True)
    print(f'Projects with >1000 stars: {len(high_star_projects)}')
    for proj, stars in high_star_projects[:10]:
        in_ppv = proj in ppv_projs
        print(f'  {proj}: {stars} stars (in PPV: {in_ppv})')
    
    result = {'error': 'No complete matches found'}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:2': ['project_info', 'project_packageversion'], 'var_functions.query_db:5': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@ecl%2Ftwig-component-carousel/3.11.1"\n  }\n]'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@douganderson444%2Fpanzoom-node/v/1.1.5"\n  }\n]'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@douganderson444%2Fpanzoom-node/v/1.1.1"\n  }\n]'}, {'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@dreamworld%2Fdw-select/3.1.2-fix-double-click-issue.1"\n  }\n]'}, {'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@discue%2Fui-components/0.13.0"\n  }\n]'}], 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_functions.query_db:10': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.'}, {'Project_Information': 'The project is hosted on GitHub under the name learnfrontend-dc/product-cart, and it currently has 2 open issues. It has garnered a total of 11 stars and has been forked 12 times.'}, {'Project_Information': 'The GitHub project ledgerproject/keypairoom currently has 3 open issues, 3 stars, and 0 forks.'}, {'Project_Information': 'The project leebyron/jasmine-check is hosted on GitHub and currently has 0 open issues, 11 stars, and 3 forks.'}, {'Project_Information': 'The project leebyron/testcheck-js on GitHub has an open issues count of 29, a stars count of 1185, and a forks count of 58, making it a notable repository in the community.'}, {'Project_Information': 'The project leecade/react-native-swiper is hosted on GitHub and has a total of 786 open issues, along with an impressive 10,249 stars and 2,392 forks, making it a popular choice among developers for implementing swiping functionality in React Native applications.'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:17': {'error': 'File not found, need to query with smaller result set'}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'tmp_files': [], 'expected_file': './tmp/tmp_0t3l9z.json', 'file_exists': False}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:24': {'tmp_dir': '/tmp', 'all_files': [], 'matching_files': [], 'current_dir': '/workspace'}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_functions.execute_python:36': {'ppv_records': 5000, 'pi_records': 1000, 'ppv_sample': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectName': 'dataminingsupply/dms-io'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectName': 'isacvale/fc'}], 'pi_sample': [{'ProjectName': 'a7650/vue3-draggable-resizable'}, {'ProjectName': 'doreamonjs/doreamon'}]}, 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.execute_python:40': {'matched_packages': 0, 'top_5_packages': []}, 'var_functions.execute_python:42': [], 'var_functions.execute_python:46': [], 'var_functions.execute_python:48': {'message': 'No matches found', 'scored_count': 0}, 'var_functions.execute_python:50': [], 'var_functions.execute_python:56': [], 'var_functions.query_db:58': [{'Name': '@discordx/music', 'Version': '5.0.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 208\n}'}, {'Name': '@discordx/music', 'Version': '5.0.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 208\n}'}, {'Name': '@discordx/music', 'Version': '4.0.0-dev.1639703569.3b1e603', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 175\n}'}, {'Name': '@discordx/music', 'Version': '4.0.0-dev.1639703569.3b1e603', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 175\n}'}, {'Name': '@discordx/music', 'Version': '4.0.0-dev.1638858523.d83f446', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 162\n}'}, {'Name': '@discordx/music', 'Version': '4.0.0-dev.1638858523.d83f446', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 162\n}'}, {'Name': '@discordx/music', 'Version': '4.0.0-dev.1640654166.a3486d5', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 189\n}'}, {'Name': '@discordx/music', 'Version': '4.0.0-dev.1640654166.a3486d5', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 189\n}'}, {'Name': '@discordx/music', 'Version': '4.0.0-dev.1639376864.f895dd8', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 171\n}'}, {'Name': '@discordx/music', 'Version': '4.0.0-dev.1639376864.f895dd8', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 171\n}'}], 'var_functions.query_db:60': [{'System': 'NPM', 'Name': '@discordx/music', 'Version': '6.0.2', 'ProjectName': 'discordx-ts/discordx'}, {'System': 'NPM', 'Name': '@discordx/music', 'Version': '6.0.0', 'ProjectName': 'discordx-ts/discordx'}, {'System': 'NPM', 'Name': '@discordx/music', 'Version': '4.0.0-dev.1638493787.0de1743', 'ProjectName': 'oceanroleplay/discord.ts'}, {'System': 'NPM', 'Name': '@discordx/music', 'Version': '4.0.0-dev.1638839595.403af6d', 'ProjectName': 'oceanroleplay/discord.ts'}, {'System': 'NPM', 'Name': '@discordx/music', 'Version': '6.0.1', 'ProjectName': 'discordx-ts/discordx'}, {'System': 'NPM', 'Name': '@discordx/music', 'Version': '4.0.0-dev.1638321186.9e03b58', 'ProjectName': 'oceanroleplay/discord.ts'}, {'System': 'NPM', 'Name': '@discordx/music', 'Version': '4.0.0-dev.1638275366.fe8249d', 'ProjectName': 'oceanroleplay/discord.ts'}, {'System': 'NPM', 'Name': '@discordx/music', 'Version': '4.0.0-dev.1640826718.fab41b1', 'ProjectName': 'oceanroleplay/discord.ts'}, {'System': 'NPM', 'Name': '@discordx/music', 'Version': '6.0.1', 'ProjectName': 'discordx-ts/discordx'}, {'System': 'NPM', 'Name': '@discordx/music', 'Version': '4.0.0-dev.1640308308.69145a0', 'ProjectName': 'oceanroleplay/discord.ts'}], 'var_functions.query_db:64': [{'ProjectName': 'twbs/bootstrap'}, {'ProjectName': 'facebook/react'}, {'ProjectName': 'vercel/next.js'}, {'ProjectName': 'vuejs/vue'}], 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.execute_python:68': {'error': 'No matches found', 'debug': 'See console'}, 'var_functions.execute_python:72': {'error': 'No matches found'}, 'var_functions.execute_python:76': {'success': False, 'debug': {'latest_packages': 0, 'ppv_packages': 0, 'ppv_projects': 0, 'star_projects': 0, 'package_overlap': 0, 'project_overlap': 0, 'sample_latest': [], 'sample_ppv_packages': [], 'sample_ppv_projects': [], 'sample_star_projects': []}}, 'var_functions.execute_python:78': {'error': 'No matches found'}, 'var_functions.query_db:80': [{'Name': '@discordx/music', 'Version': '6.0.2'}, {'Name': '@discordx/pagination', 'Version': '4.0.0-dev.1670073642.4821b1ea'}, {'Name': '@discordx/utilities', 'Version': '6.0.0-dev.1674756406.d6dc0b9d'}, {'Name': '@discoteam/vueify', 'Version': '9.4.1'}, {'Name': '@discourse/babel-plugin-debug-macros', 'Version': '0.4.0-pre1'}, {'Name': '@discourse/backburner.js', 'Version': '2.7.1-0'}, {'Name': '@discourse/itsatrap', 'Version': '2.0.8'}, {'Name': '@discourse/moment-timezone-names-translations', 'Version': '1.0.0'}, {'Name': '@discourse/virtual-dom', 'Version': '2.1.2-0'}, {'Name': '@discoursegroup/commons-js', 'Version': '0.0.9'}, {'Name': '@discoursegroup/commons-test-js', 'Version': '0.0.4'}, {'Name': '@discoursegroup/relayrabbit-addons-js', 'Version': '0.0.99'}, {'Name': '@discoursegroup/relayrabbit-commons-js', 'Version': '0.0.7'}, {'Name': '@discoursegroup/relayrabbit-js', 'Version': '0.0.9'}, {'Name': '@discoursegroup/service-api-js', 'Version': '0.0.9'}, {'Name': '@discovery-dao/schemas', 'Version': '0.0.9'}, {'Name': '@discovery-dao/ui', 'Version': '0.0.9'}, {'Name': '@discovery-dni/shaka-player', 'Version': '4.2.0-custom5'}, {'Name': '@discovery-solutions/json-connection', 'Version': '2.0.6'}, {'Name': '@discovery-solutions/json-server', 'Version': '2.0.9'}, {'Name': '@discovery-solutions/react-flatlist', 'Version': '0.0.3'}, {'Name': '@discovery-solutions/react-modal', 'Version': '0.0.2'}, {'Name': '@discovery-solutions/react-router', 'Version': '0.0.2'}, {'Name': '@discovery-solutions/react-store', 'Version': '0.0.2'}, {'Name': '@discovery-solutions/utils', 'Version': '0.0.1'}, {'Name': '@discoveryjs/cli', 'Version': '2.6.0'}, {'Name': '@discoveryjs/discovery', 'Version': '1.0.0-beta.9'}, {'Name': '@discoveryjs/json-ext', 'Version': '0.5.7'}, {'Name': '@discoveryjs/natural-compare', 'Version': '1.1.0'}, {'Name': '@discoveryjs/node-modules', 'Version': '1.0.0'}, {'Name': '@discoveryjs/scan-fs', 'Version': '4.0.0-rc.1'}, {'Name': '@discoveryjs/scan-git', 'Version': '0.1.1'}, {'Name': '@discoveryjs/view-plugin-highcharts', 'Version': '1.0.1'}, {'Name': '@discowrap/core', 'Version': '0.0.1-draft.2'}, {'Name': '@discowrap/elastic', 'Version': '0.0.1-draft.2'}, {'Name': '@discoxyz/ceramic-http-client', 'Version': '2.7.0'}, {'Name': '@discretetom/batcave', 'Version': '0.2.0'}, {'Name': '@discretetom/tcping', 'Version': '0.1.4'}, {'Name': '@discretetom/ws-server', 'Version': '0.1.2'}, {'Name': '@discretize/gw2-ui-new', 'Version': '0.1.2'}, {'Name': '@discretize/typeface-menomonia', 'Version': '0.1.3'}, {'Name': '@discue/firebase-tools', 'Version': '11.19.0-2'}, {'Name': '@discue/idempotent-firebase-functions', 'Version': '0.2.0'}, {'Name': '@discue/mongodb-resource-client', 'Version': '0.7.0'}, {'Name': '@discue/paddle-integration-firestore', 'Version': '0.9.0'}, {'Name': '@discue/paddle-integration-mongodb', 'Version': '0.25.0'}, {'Name': '@discue/paddle-webhook-validator', 'Version': '1.5.0'}, {'Name': '@discue/ui-components', 'Version': '0.9.1'}, {'Name': '@discussify/styleguide', 'Version': '1.1.0'}, {'Name': '@discut/comic_automatic_packing', 'Version': '1.2.3'}, {'Name': '@discuzq/vditor', 'Version': '1.0.26'}, {'Name': '@discuzqfe/cli', 'Version': '1.3.21'}, {'Name': '@discuzqfe/plugin-center', 'Version': '2.0.20'}, {'Name': '@discuzqfe/vditor', 'Version': '1.0.30'}, {'Name': '@discuzqsdk/vditor', 'Version': '1.3.9'}, {'Name': '@discuzz/auth-firebase', 'Version': '1.11.9'}, {'Name': '@discuzz/composer-markdown', 'Version': '1.11.9'}, {'Name': '@discuzz/composer-plaintext', 'Version': '1.11.2'}, {'Name': '@discuzz/core', 'Version': '1.11.9'}, {'Name': '@discuzz/data-firestore', 'Version': '1.11.9'}, {'Name': '@discuzz/discuzz', 'Version': '1.11.9'}, {'Name': '@discuzz/locale-en', 'Version': '1.11.9'}, {'Name': '@discuzz/locale-vi', 'Version': '1.11.9'}, {'Name': '@discuzz/viewer-markdown', 'Version': '1.11.9'}, {'Name': '@discuzz/viewer-plaintext', 'Version': '1.11.2'}, {'Name': '@disedia/website-core', 'Version': '0.0.9'}, {'Name': '@disfactory/exif-js', 'Version': '2.3.0'}, {'Name': '@disfactory/leaflet-tilefilter', 'Version': '0.0.2'}, {'Name': '@dish/esbuild-loader', 'Version': '0.0.0-semantic-release'}, {'Name': '@dish/postgrator-cli', 'Version': '4.0.0'}, {'Name': '@dish/react-ssr-prepass', 'Version': '1.3.1'}, {'Name': '@dish/rollup-plugin-flat-dts', 'Version': '1.0.1'}, {'Name': '@dishhq/cli', 'Version': '0.1.5'}, {'Name': '@dishhq/sdk', 'Version': '0.1.1'}, {'Name': '@dishost/music', 'Version': '0.0.0'}, {'Name': '@dishuostec/cordova-res', 'Version': '0.8.1'}, {'Name': '@dishuostec/hyperapp-pulltorefresh', 'Version': '0.0.7'}, {'Name': '@dishuostec/rollup-plugin-proto', 'Version': '1.0.0'}, {'Name': '@dishuostec/rollup-plugin-sass', 'Version': '1.2.3'}, {'Name': '@dishuostec/sapper', 'Version': '0.28.2-rc1'}, {'Name': '@dishuostec/snowpack', 'Version': '2.15.0-ex.3'}, {'Name': '@dishuostec/ss-message', 'Version': '1.1.4'}, {'Name': '@dishuostec/ss-parser', 'Version': '1.0.3'}, {'Name': '@dishuostec/superscript', 'Version': '1.2.0'}, {'Name': '@dishuostec/svelte-store', 'Version': '1.1.3'}, {'Name': '@disist/usepubsub', 'Version': '1.0.0'}, {'Name': '@disjs/core', 'Version': '0.1.2'}, {'Name': '@disjukr/croquis-js', 'Version': '0.0.3'}, {'Name': '@dislido/cqnode', 'Version': '3.0.9'}, {'Name': '@dismal/elo', 'Version': '1.0.0'}, {'Name': '@disnetwork/core', 'Version': '0.0.2'}, {'Name': '@disnetwork/engine', 'Version': '0.0.2'}, {'Name': '@disnetwork/example', 'Version': '0.0.1'}, {'Name': '@disorn/golfswap-testnet-sdk', 'Version': '1.0.1'}, {'Name': '@disorrder/ee', 'Version': '1.0.0'}, {'Name': '@disorrder/storm', 'Version': '0.3.1'}, {'Name': '@disoul/mp4box', 'Version': '0.3.16-fix.9'}, {'Name': '@dispatchlabs/disnode-sdk', 'Version': '2.3.0'}, {'Name': '@dispatchlabs/dispatch-js', 'Version': '2.4.3'}, {'Name': '@dispilioinc/highcharts-types', 'Version': '6.0.0-1'}], 'var_functions.query_db:82': 'file_storage/functions.query_db:82.json', 'var_functions.query_db:84': [{'ProjectName': 'facebook/react'}, {'ProjectName': 'twbs/bootstrap'}, {'ProjectName': 'eslint/eslint'}, {'ProjectName': 'lodash/lodash'}, {'ProjectName': 'webpack/webpack'}, {'ProjectName': 'vercel/next.js'}, {'ProjectName': 'vuejs/vue'}]}

exec(code, env_args)
