code = """import json
import os
import re
from collections import defaultdict, Counter

# Load data from temp files
releases_file = './tmp/tmp_7h8j5t.json'
ppv_file = './tmp/tmp_s9j2w1.json'
pi_file = './tmp/tmp_n7k3y9.json'

releases_raw = json.load(open(releases_file)) if os.path.exists(releases_file) else []
ppv_data = json.load(open(ppv_file)) if os.path.exists(ppv_file) else []
pi_data = json.load(open(pi_file)) if os.path.exists(pi_file) else []

print('=== DATA OVERVIEW ===')
print(f'Releases: {len(releases_raw)} packages')
print(f'PPV mappings: {len(ppv_data)} mappings')
print(f'Project info: {len(pi_data)} projects')
print()

# Check if data is actually there
print('=== DATA SAMPLING ===')
print('Sample release records:')
for i, pkg in enumerate(releases_raw[:5]):
    print(f"  {i+1}. {pkg.get('Name', 'N/A')}")

print('\nSample PPV mappings:')
for i, ppv in enumerate(ppv_data[:5]):
    print(f"  {i+1}. {ppv.get('Name', 'N/A')} -> {ppv.get('ProjectName', 'N/A')}")

print('\nSample project info:')
for i, proj in enumerate(pi_data[:5]):
    info = proj.get('Project_Information', '')[:100]
    print(f"  {i+1}. {info}...")

# Parse releases
package_latest = {}
valid_releases = 0
for pkg in releases_raw:
    try:
        vi = json.loads(pkg['VersionInfo'])
        if vi.get('IsRelease', False):
            valid_releases += 1
            name = pkg['Name']
            ord_ = vi.get('Ordinal', 0)
            if name not in package_latest or ord_ > package_latest[name]['ordinal']:
                package_latest[name] = {
                    'version': pkg['Version'],
                    'ordinal': ord_
                }
    except:
        continue

print(f'\n=== RELEASES ANALYSIS ===')
print(f'Valid release records: {valid_releases}')
print(f'Unique packages with releases: {len(package_latest)}')
print('Sample:')
for pkg in list(package_latest.items())[:5]:
    print(f"  {pkg[0]}: v{pkg[1]['version']} (ord {pkg[1]['ordinal']})")

# Extract project stars
project_stars = {}
for proj in pi_data:
    try:
        info = proj.get('Project_Information', '')
        name_match = re.search(r'project\s+([\w-]+/[\w-]+)', info, re.I)
        stars_match = re.search(r'(\d[\d,]*)\s+stars', info)
        if name_match and stars_match:
            proj_name = name_match.group(1)
            stars = int(stars_match.group(1).replace(',', ''))
            project_stars[proj_name] = stars
    except:
        continue

print(f'\n=== PROJECT STARS ===')
print(f'Projects with star data: {len(project_stars)}')
sorted_stars = sorted(project_stars.items(), key=lambda x: x[1], reverse=True)
print('Top projects:')
for proj, stars in sorted_stars[:10]:
    print(f"  {proj}: {stars:,} stars")

# Analyze PPV structure
print(f'\n=== PPV ANALYSIS ===')
ppv_packages = set(p['Name'] for p in ppv_data)
ppv_projects = set(p['ProjectName'] for p in ppv_data)
print(f'Unique packages in PPV: {len(ppv_packages)}')
print(f'Unique projects in PPV: {len(ppv_projects)}')

# Check overlaps
latest_packages = set(package_latest.keys())
star_projects = set(project_stars.keys())

print(f'\n=== OVERLAP ANALYSIS ===')
print(f'Release packages that match PPV packages: {len(latest_packages.intersection(ppv_packages))}')
print(f'PPV projects that match star projects: {len(ppv_projects.intersection(star_projects))}')

# Show specific examples
print('\nRelease packages in PPV (sample):')
matches = list(latest_packages.intersection(ppv_packages))
for pkg in matches[:10]:
    print(f"  {pkg}: {package_latest[pkg]['version']}")

print('\nPPV projects with stars (sample):')
proj_matches = list(ppv_projects.intersection(star_projects))
for proj in proj_matches[:10]:
    print(f"  {proj}: {project_stars[proj]} stars")

# Now try to find complete matches
print('\n=== COMPLETE MATCH ATTEMPT ===')
matches = []
for ppv in ppv_data:
    pkg_name = ppv['Name']
    proj_name = ppv['ProjectName']
    version = ppv['Version']
    
    if pkg_name in package_latest and proj_name in project_stars:
        if version == package_latest[pkg_name]['version']:
            matches.append({
                'package': pkg_name,
                'version': version,
                'project': proj_name,
                'stars': project_stars[proj_name]
            })

print(f'Found {len(matches)} complete matches!')

if matches:
    # Get top 5
    top_5 = sorted(matches, key=lambda x: x['stars'], reverse=True)[:5]
    print('\nTOP 5:')
    for i, pkg in enumerate(top_5, 1):
        print(f"{i}. {pkg['package']} v{pkg['version']} ({pkg['project']}) - {pkg['stars']:,} stars")
else:
    # Show near-misses
    print('\nNo complete matches found. Near-misses:')
    print('Checking for version mismatches...')
    
    near_misses = []
    for ppv in ppv_data:
        pkg_name = ppv['Name']
        proj_name = ppv['ProjectName']
        
        if pkg_name in package_latest and proj_name in project_stars:
            # Package and project exist but version doesn't match
            latest_ver = package_latest[pkg_name]['version']
            if ppv['Version'] != latest_ver:
                near_misses.append(f"{pkg_name}: PPV has {ppv['Version']}, latest is {latest_ver}")
    
    print(f'Found {len(near_misses)} version mismatches (sample):')
    for nm in near_misses[:5]:
        print(f"  {nm}")

def result = {'matches': len(matches), 'near_misses': len(near_misses) if not matches else 0}"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:2': ['project_info', 'project_packageversion'], 'var_functions.query_db:5': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@ecl%2Ftwig-component-carousel/3.11.1"\n  }\n]'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@douganderson444%2Fpanzoom-node/v/1.1.5"\n  }\n]'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@douganderson444%2Fpanzoom-node/v/1.1.1"\n  }\n]'}, {'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@dreamworld%2Fdw-select/3.1.2-fix-double-click-issue.1"\n  }\n]'}, {'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@discue%2Fui-components/0.13.0"\n  }\n]'}], 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_functions.query_db:10': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.'}, {'Project_Information': 'The project is hosted on GitHub under the name learnfrontend-dc/product-cart, and it currently has 2 open issues. It has garnered a total of 11 stars and has been forked 12 times.'}, {'Project_Information': 'The GitHub project ledgerproject/keypairoom currently has 3 open issues, 3 stars, and 0 forks.'}, {'Project_Information': 'The project leebyron/jasmine-check is hosted on GitHub and currently has 0 open issues, 11 stars, and 3 forks.'}, {'Project_Information': 'The project leebyron/testcheck-js on GitHub has an open issues count of 29, a stars count of 1185, and a forks count of 58, making it a notable repository in the community.'}, {'Project_Information': 'The project leecade/react-native-swiper is hosted on GitHub and has a total of 786 open issues, along with an impressive 10,249 stars and 2,392 forks, making it a popular choice among developers for implementing swiping functionality in React Native applications.'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:17': {'error': 'File not found, need to query with smaller result set'}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'tmp_files': [], 'expected_file': './tmp/tmp_0t3l9z.json', 'file_exists': False}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:24': {'tmp_dir': '/tmp', 'all_files': [], 'matching_files': [], 'current_dir': '/workspace'}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_functions.execute_python:36': {'ppv_records': 5000, 'pi_records': 1000, 'ppv_sample': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectName': 'dataminingsupply/dms-io'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectName': 'isacvale/fc'}], 'pi_sample': [{'ProjectName': 'a7650/vue3-draggable-resizable'}, {'ProjectName': 'doreamonjs/doreamon'}]}, 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.execute_python:40': {'matched_packages': 0, 'top_5_packages': []}, 'var_functions.execute_python:42': [], 'var_functions.execute_python:46': [], 'var_functions.execute_python:48': {'message': 'No matches found', 'scored_count': 0}, 'var_functions.execute_python:50': [], 'var_functions.execute_python:56': [], 'var_functions.query_db:58': [{'Name': '@discordx/music', 'Version': '5.0.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 208\n}'}, {'Name': '@discordx/music', 'Version': '5.0.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 208\n}'}, {'Name': '@discordx/music', 'Version': '4.0.0-dev.1639703569.3b1e603', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 175\n}'}, {'Name': '@discordx/music', 'Version': '4.0.0-dev.1639703569.3b1e603', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 175\n}'}, {'Name': '@discordx/music', 'Version': '4.0.0-dev.1638858523.d83f446', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 162\n}'}, {'Name': '@discordx/music', 'Version': '4.0.0-dev.1638858523.d83f446', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 162\n}'}, {'Name': '@discordx/music', 'Version': '4.0.0-dev.1640654166.a3486d5', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 189\n}'}, {'Name': '@discordx/music', 'Version': '4.0.0-dev.1640654166.a3486d5', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 189\n}'}, {'Name': '@discordx/music', 'Version': '4.0.0-dev.1639376864.f895dd8', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 171\n}'}, {'Name': '@discordx/music', 'Version': '4.0.0-dev.1639376864.f895dd8', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 171\n}'}], 'var_functions.query_db:60': [{'System': 'NPM', 'Name': '@discordx/music', 'Version': '6.0.2', 'ProjectName': 'discordx-ts/discordx'}, {'System': 'NPM', 'Name': '@discordx/music', 'Version': '6.0.0', 'ProjectName': 'discordx-ts/discordx'}, {'System': 'NPM', 'Name': '@discordx/music', 'Version': '4.0.0-dev.1638493787.0de1743', 'ProjectName': 'oceanroleplay/discord.ts'}, {'System': 'NPM', 'Name': '@discordx/music', 'Version': '4.0.0-dev.1638839595.403af6d', 'ProjectName': 'oceanroleplay/discord.ts'}, {'System': 'NPM', 'Name': '@discordx/music', 'Version': '6.0.1', 'ProjectName': 'discordx-ts/discordx'}, {'System': 'NPM', 'Name': '@discordx/music', 'Version': '4.0.0-dev.1638321186.9e03b58', 'ProjectName': 'oceanroleplay/discord.ts'}, {'System': 'NPM', 'Name': '@discordx/music', 'Version': '4.0.0-dev.1638275366.fe8249d', 'ProjectName': 'oceanroleplay/discord.ts'}, {'System': 'NPM', 'Name': '@discordx/music', 'Version': '4.0.0-dev.1640826718.fab41b1', 'ProjectName': 'oceanroleplay/discord.ts'}, {'System': 'NPM', 'Name': '@discordx/music', 'Version': '6.0.1', 'ProjectName': 'discordx-ts/discordx'}, {'System': 'NPM', 'Name': '@discordx/music', 'Version': '4.0.0-dev.1640308308.69145a0', 'ProjectName': 'oceanroleplay/discord.ts'}], 'var_functions.query_db:64': [{'ProjectName': 'twbs/bootstrap'}, {'ProjectName': 'facebook/react'}, {'ProjectName': 'vercel/next.js'}, {'ProjectName': 'vuejs/vue'}], 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.execute_python:68': {'error': 'No matches found', 'debug': 'See console'}, 'var_functions.execute_python:72': {'error': 'No matches found'}, 'var_functions.execute_python:76': {'success': False, 'debug': {'latest_packages': 0, 'ppv_packages': 0, 'ppv_projects': 0, 'star_projects': 0, 'package_overlap': 0, 'project_overlap': 0, 'sample_latest': [], 'sample_ppv_packages': [], 'sample_ppv_projects': [], 'sample_star_projects': []}}, 'var_functions.execute_python:78': {'error': 'No matches found'}, 'var_functions.query_db:80': [{'Name': '@discordx/music', 'Version': '6.0.2'}, {'Name': '@discordx/pagination', 'Version': '4.0.0-dev.1670073642.4821b1ea'}, {'Name': '@discordx/utilities', 'Version': '6.0.0-dev.1674756406.d6dc0b9d'}, {'Name': '@discoteam/vueify', 'Version': '9.4.1'}, {'Name': '@discourse/babel-plugin-debug-macros', 'Version': '0.4.0-pre1'}, {'Name': '@discourse/backburner.js', 'Version': '2.7.1-0'}, {'Name': '@discourse/itsatrap', 'Version': '2.0.8'}, {'Name': '@discourse/moment-timezone-names-translations', 'Version': '1.0.0'}, {'Name': '@discourse/virtual-dom', 'Version': '2.1.2-0'}, {'Name': '@discoursegroup/commons-js', 'Version': '0.0.9'}, {'Name': '@discoursegroup/commons-test-js', 'Version': '0.0.4'}, {'Name': '@discoursegroup/relayrabbit-addons-js', 'Version': '0.0.99'}, {'Name': '@discoursegroup/relayrabbit-commons-js', 'Version': '0.0.7'}, {'Name': '@discoursegroup/relayrabbit-js', 'Version': '0.0.9'}, {'Name': '@discoursegroup/service-api-js', 'Version': '0.0.9'}, {'Name': '@discovery-dao/schemas', 'Version': '0.0.9'}, {'Name': '@discovery-dao/ui', 'Version': '0.0.9'}, {'Name': '@discovery-dni/shaka-player', 'Version': '4.2.0-custom5'}, {'Name': '@discovery-solutions/json-connection', 'Version': '2.0.6'}, {'Name': '@discovery-solutions/json-server', 'Version': '2.0.9'}, {'Name': '@discovery-solutions/react-flatlist', 'Version': '0.0.3'}, {'Name': '@discovery-solutions/react-modal', 'Version': '0.0.2'}, {'Name': '@discovery-solutions/react-router', 'Version': '0.0.2'}, {'Name': '@discovery-solutions/react-store', 'Version': '0.0.2'}, {'Name': '@discovery-solutions/utils', 'Version': '0.0.1'}, {'Name': '@discoveryjs/cli', 'Version': '2.6.0'}, {'Name': '@discoveryjs/discovery', 'Version': '1.0.0-beta.9'}, {'Name': '@discoveryjs/json-ext', 'Version': '0.5.7'}, {'Name': '@discoveryjs/natural-compare', 'Version': '1.1.0'}, {'Name': '@discoveryjs/node-modules', 'Version': '1.0.0'}, {'Name': '@discoveryjs/scan-fs', 'Version': '4.0.0-rc.1'}, {'Name': '@discoveryjs/scan-git', 'Version': '0.1.1'}, {'Name': '@discoveryjs/view-plugin-highcharts', 'Version': '1.0.1'}, {'Name': '@discowrap/core', 'Version': '0.0.1-draft.2'}, {'Name': '@discowrap/elastic', 'Version': '0.0.1-draft.2'}, {'Name': '@discoxyz/ceramic-http-client', 'Version': '2.7.0'}, {'Name': '@discretetom/batcave', 'Version': '0.2.0'}, {'Name': '@discretetom/tcping', 'Version': '0.1.4'}, {'Name': '@discretetom/ws-server', 'Version': '0.1.2'}, {'Name': '@discretize/gw2-ui-new', 'Version': '0.1.2'}, {'Name': '@discretize/typeface-menomonia', 'Version': '0.1.3'}, {'Name': '@discue/firebase-tools', 'Version': '11.19.0-2'}, {'Name': '@discue/idempotent-firebase-functions', 'Version': '0.2.0'}, {'Name': '@discue/mongodb-resource-client', 'Version': '0.7.0'}, {'Name': '@discue/paddle-integration-firestore', 'Version': '0.9.0'}, {'Name': '@discue/paddle-integration-mongodb', 'Version': '0.25.0'}, {'Name': '@discue/paddle-webhook-validator', 'Version': '1.5.0'}, {'Name': '@discue/ui-components', 'Version': '0.9.1'}, {'Name': '@discussify/styleguide', 'Version': '1.1.0'}, {'Name': '@discut/comic_automatic_packing', 'Version': '1.2.3'}, {'Name': '@discuzq/vditor', 'Version': '1.0.26'}, {'Name': '@discuzqfe/cli', 'Version': '1.3.21'}, {'Name': '@discuzqfe/plugin-center', 'Version': '2.0.20'}, {'Name': '@discuzqfe/vditor', 'Version': '1.0.30'}, {'Name': '@discuzqsdk/vditor', 'Version': '1.3.9'}, {'Name': '@discuzz/auth-firebase', 'Version': '1.11.9'}, {'Name': '@discuzz/composer-markdown', 'Version': '1.11.9'}, {'Name': '@discuzz/composer-plaintext', 'Version': '1.11.2'}, {'Name': '@discuzz/core', 'Version': '1.11.9'}, {'Name': '@discuzz/data-firestore', 'Version': '1.11.9'}, {'Name': '@discuzz/discuzz', 'Version': '1.11.9'}, {'Name': '@discuzz/locale-en', 'Version': '1.11.9'}, {'Name': '@discuzz/locale-vi', 'Version': '1.11.9'}, {'Name': '@discuzz/viewer-markdown', 'Version': '1.11.9'}, {'Name': '@discuzz/viewer-plaintext', 'Version': '1.11.2'}, {'Name': '@disedia/website-core', 'Version': '0.0.9'}, {'Name': '@disfactory/exif-js', 'Version': '2.3.0'}, {'Name': '@disfactory/leaflet-tilefilter', 'Version': '0.0.2'}, {'Name': '@dish/esbuild-loader', 'Version': '0.0.0-semantic-release'}, {'Name': '@dish/postgrator-cli', 'Version': '4.0.0'}, {'Name': '@dish/react-ssr-prepass', 'Version': '1.3.1'}, {'Name': '@dish/rollup-plugin-flat-dts', 'Version': '1.0.1'}, {'Name': '@dishhq/cli', 'Version': '0.1.5'}, {'Name': '@dishhq/sdk', 'Version': '0.1.1'}, {'Name': '@dishost/music', 'Version': '0.0.0'}, {'Name': '@dishuostec/cordova-res', 'Version': '0.8.1'}, {'Name': '@dishuostec/hyperapp-pulltorefresh', 'Version': '0.0.7'}, {'Name': '@dishuostec/rollup-plugin-proto', 'Version': '1.0.0'}, {'Name': '@dishuostec/rollup-plugin-sass', 'Version': '1.2.3'}, {'Name': '@dishuostec/sapper', 'Version': '0.28.2-rc1'}, {'Name': '@dishuostec/snowpack', 'Version': '2.15.0-ex.3'}, {'Name': '@dishuostec/ss-message', 'Version': '1.1.4'}, {'Name': '@dishuostec/ss-parser', 'Version': '1.0.3'}, {'Name': '@dishuostec/superscript', 'Version': '1.2.0'}, {'Name': '@dishuostec/svelte-store', 'Version': '1.1.3'}, {'Name': '@disist/usepubsub', 'Version': '1.0.0'}, {'Name': '@disjs/core', 'Version': '0.1.2'}, {'Name': '@disjukr/croquis-js', 'Version': '0.0.3'}, {'Name': '@dislido/cqnode', 'Version': '3.0.9'}, {'Name': '@dismal/elo', 'Version': '1.0.0'}, {'Name': '@disnetwork/core', 'Version': '0.0.2'}, {'Name': '@disnetwork/engine', 'Version': '0.0.2'}, {'Name': '@disnetwork/example', 'Version': '0.0.1'}, {'Name': '@disorn/golfswap-testnet-sdk', 'Version': '1.0.1'}, {'Name': '@disorrder/ee', 'Version': '1.0.0'}, {'Name': '@disorrder/storm', 'Version': '0.3.1'}, {'Name': '@disoul/mp4box', 'Version': '0.3.16-fix.9'}, {'Name': '@dispatchlabs/disnode-sdk', 'Version': '2.3.0'}, {'Name': '@dispatchlabs/dispatch-js', 'Version': '2.4.3'}, {'Name': '@dispilioinc/highcharts-types', 'Version': '6.0.0-1'}], 'var_functions.query_db:82': 'file_storage/functions.query_db:82.json', 'var_functions.query_db:84': [{'ProjectName': 'facebook/react'}, {'ProjectName': 'twbs/bootstrap'}, {'ProjectName': 'eslint/eslint'}, {'ProjectName': 'lodash/lodash'}, {'ProjectName': 'webpack/webpack'}, {'ProjectName': 'vercel/next.js'}, {'ProjectName': 'vuejs/vue'}], 'var_functions.execute_python:88': {'error': 'No complete matches found'}, 'var_functions.query_db:90': [{'Name': '@ebot7/edem-react', 'Version': '0.18.8', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 55\n}'}, {'Name': '@dso-toolkit/react', 'Version': '19.0.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 5\n}'}, {'Name': '@doodl/ss-react-forms', 'Version': '2.8.3', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 23\n}'}, {'Name': '@dxos/react-appkit', 'Version': '0.1.10', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 8\n}'}, {'Name': '@dxos/react-uikit', 'Version': '0.1.12', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}'}, {'Name': '@dxos/react-list', 'Version': '0.1.50', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 52\n}'}, {'Name': '@dytesdk/react-native-core', 'Version': '0.5.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 31\n}'}, {'Name': '@dxos/react-uikit', 'Version': '0.1.14', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 15\n}'}, {'Name': '@ed-ui/react', 'Version': '0.1.22', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 15\n}'}, {'Name': '@ed-ui/react', 'Version': '0.1.22', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 15\n}'}, {'Name': '@dyb881/create-react-app', 'Version': '1.0.8', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 52\n}'}, {'Name': '@dyb881/create-react-app', 'Version': '1.0.8', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 52\n}'}, {'Name': '@easm/react', 'Version': '0.3.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 15\n}'}, {'Name': '@easm/react', 'Version': '0.3.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 15\n}'}, {'Name': '@e.react/hooks', 'Version': '0.0.2', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 2\n}'}, {'Name': '@e.react/hooks', 'Version': '0.0.2', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 2\n}'}, {'Name': '@dyb881/create-react-app', 'Version': '0.6.4', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 27\n}'}, {'Name': '@dyb881/create-react-app', 'Version': '0.6.4', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 27\n}'}, {'Name': '@ebay/ui-core-react', 'Version': '1.0.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 1\n}'}, {'Name': '@ebay/ui-core-react', 'Version': '1.0.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 1\n}'}], 'var_functions.query_db:92': [{'Name': '@doubledotlabs/dot.css>0.1.4>bootstrap', 'Version': '4.5.0', 'ProjectName': 'twbs/bootstrap'}, {'Name': '@docler/next', 'Version': '10.1.4-canary.2.1', 'ProjectName': 'vercel/next.js'}, {'Name': '@dothq/react', 'Version': '18.0.0-rc.1-next-5d08a24c2-20220225-dothq', 'ProjectName': 'facebook/react'}, {'Name': '@dothq/react-dom', 'Version': '17.0.0', 'ProjectName': 'facebook/react'}, {'Name': '@diyhub/bootstrap', 'Version': '4.0.0-beta.3', 'ProjectName': 'twbs/bootstrap'}, {'Name': '@duying/bootcss-plus', 'Version': '5.3.0-alpha1', 'ProjectName': 'twbs/bootstrap'}, {'Name': '@dszymon/vue-server-renderer', 'Version': '2.6.12-custom-render.3', 'ProjectName': 'vuejs/vue'}, {'Name': '@dszymon/vue-server-renderer', 'Version': '2.6.12-custom-render.1', 'ProjectName': 'vuejs/vue'}, {'Name': '@doubledotlabs/dot.css>0.1.2>bootstrap', 'Version': '4.5.0', 'ProjectName': 'twbs/bootstrap'}, {'Name': '@dothq/react', 'Version': '18.0.0-rc.1-next-5d08a24c2-20220225-dothq-2', 'ProjectName': 'facebook/react'}, {'Name': '@divmain/next', 'Version': '10.0.10-canary.8-experimental-1', 'ProjectName': 'vercel/next.js'}, {'Name': '@diyhub/bootstrap', 'Version': '4.0.0-beta.3', 'ProjectName': 'twbs/bootstrap'}, {'Name': '@dulcetjs/webpack', 'Version': '2.2.1', 'ProjectName': 'webpack/webpack'}, {'Name': '@duying/bootcss-plus', 'Version': '5.3.0-alpha1-2', 'ProjectName': 'twbs/bootstrap'}, {'Name': '@dpoineau/react-scripts>1.0.0>webpack', 'Version': '1.13.2', 'ProjectName': 'webpack/webpack'}, {'Name': '@doubledotlabs/dot.css>0.1.0>bootstrap', 'Version': '4.5.0', 'ProjectName': 'twbs/bootstrap'}, {'Name': '@doubledotlabs/dot.css>0.2.1>bootstrap', 'Version': '5.1.3', 'ProjectName': 'twbs/bootstrap'}, {'Name': '@dwarvesf/react-scripts>0.7.0>webpack', 'Version': '1.13.2', 'ProjectName': 'webpack/webpack'}, {'Name': '@doubledotlabs/dot.css>0.1.0>bootstrap', 'Version': '4.5.0', 'ProjectName': 'twbs/bootstrap'}, {'Name': '@doubledotlabs/dot.css>0.1.4>bootstrap', 'Version': '4.5.0', 'ProjectName': 'twbs/bootstrap'}, {'Name': '@doubledotlabs/dot.css>0.1.7>bootstrap', 'Version': '5.0.1', 'ProjectName': 'twbs/bootstrap'}, {'Name': '@doubledotlabs/dot.css>0.1.8>bootstrap', 'Version': '5.0.1', 'ProjectName': 'twbs/bootstrap'}, {'Name': '@doubledotlabs/dot.css>0.1.9>bootstrap', 'Version': '5.0.1', 'ProjectName': 'twbs/bootstrap'}, {'Name': '@doubledotlabs/dot.css>0.2.0>bootstrap', 'Version': '5.1.3', 'ProjectName': 'twbs/bootstrap'}, {'Name': '@docler/next', 'Version': '10.1.4-canary.15', 'ProjectName': 'vercel/next.js'}, {'Name': '@ecapp/webpack', 'Version': '0.1.2', 'ProjectName': 'webpack/webpack'}, {'Name': '@doubledotlabs/dot.css>0.1.1>bootstrap', 'Version': '4.5.0', 'ProjectName': 'twbs/bootstrap'}, {'Name': '@doubledotlabs/dot.css>0.1.5>bootstrap', 'Version': '4.5.0', 'ProjectName': 'twbs/bootstrap'}, {'Name': '@doubledotlabs/dot.css>0.1.6>bootstrap', 'Version': '5.0.1', 'ProjectName': 'twbs/bootstrap'}, {'Name': '@doubledotlabs/dot.css>0.1.9>bootstrap', 'Version': '5.0.1', 'ProjectName': 'twbs/bootstrap'}, {'Name': '@divmain/next', 'Version': '10.0.10-canary.8-experimental-2', 'ProjectName': 'vercel/next.js'}, {'Name': '@divmain/next', 'Version': '10.0.10-canary.8-experimental-1', 'ProjectName': 'vercel/next.js'}, {'Name': '@ecapp/webpack', 'Version': '0.1.0', 'ProjectName': 'webpack/webpack'}, {'Name': '@dothq/react-dom', 'Version': '17.0.0-xul', 'ProjectName': 'facebook/react'}, {'Name': '@dulcetjs/webpack', 'Version': '3.5.1', 'ProjectName': 'webpack/webpack'}, {'Name': '@dulcetjs/webpack', 'Version': '2.2.2', 'ProjectName': 'webpack/webpack'}, {'Name': '@duying/bootcss-plus', 'Version': '5.3.0-alpha1-1', 'ProjectName': 'twbs/bootstrap'}, {'Name': '@duying/bootcss-plus', 'Version': '5.3.0-alpha1-2', 'ProjectName': 'twbs/bootstrap'}, {'Name': '@doubledotlabs/dot.css>0.1.6>bootstrap', 'Version': '5.0.1', 'ProjectName': 'twbs/bootstrap'}, {'Name': '@doubledotlabs/dot.css>0.2.1>bootstrap', 'Version': '5.1.3', 'ProjectName': 'twbs/bootstrap'}, {'Name': '@docler/next', 'Version': '10.1.4-canary.2', 'ProjectName': 'vercel/next.js'}, {'Name': '@docler/next', 'Version': '10.1.4-canary.2.1', 'ProjectName': 'vercel/next.js'}, {'Name': '@dulcetjs/webpack', 'Version': '3.5.2', 'ProjectName': 'webpack/webpack'}, {'Name': '@dulcetjs/webpack', 'Version': '2.2.2', 'ProjectName': 'webpack/webpack'}, {'Name': '@duplotech/webpack', 'Version': '5.0.0', 'ProjectName': 'webpack/webpack'}, {'Name': '@duying/bootcss-plus', 'Version': '5.3.0-alpha1', 'ProjectName': 'twbs/bootstrap'}, {'Name': '@doubledotlabs/dot.css>0.1.3>bootstrap', 'Version': '4.5.0', 'ProjectName': 'twbs/bootstrap'}, {'Name': '@dothq/react', 'Version': '18.0.0-rc.1-next-5d08a24c2-20220225-dothq-2', 'ProjectName': 'facebook/react'}, {'Name': '@ecapp/webpack', 'Version': '0.1.1', 'ProjectName': 'webpack/webpack'}, {'Name': '@dylanvann/react-cache', 'Version': '2.0.0-alpha.0', 'ProjectName': 'facebook/react'}], 'var_functions.query_db:94': [], 'var_functions.query_db:96': [{'Name': '@dwarvesf/react-scripts>0.7.0>webpack'}, {'Name': '@doubledotlabs/dot.css>0.1.1>bootstrap'}, {'Name': '@dylanvann/react-cache'}, {'Name': '@divmain/next'}, {'Name': '@doubledotlabs/dot.css>0.2.1>bootstrap'}, {'Name': '@doubledotlabs/dot.css>0.1.7>bootstrap'}, {'Name': '@doubledotlabs/dot.css>0.1.6>bootstrap'}, {'Name': '@diyhub/bootstrap'}, {'Name': '@docler/next'}, {'Name': '@doubledotlabs/dot.css>0.1.2>bootstrap'}, {'Name': '@doubledotlabs/dot.css>0.1.9>bootstrap'}, {'Name': '@dulcetjs/webpack'}, {'Name': '@doubledotlabs/dot.css>0.2.0>bootstrap'}, {'Name': '@dszymon/vue-server-renderer'}, {'Name': '@doubledotlabs/dot.css>0.1.3>bootstrap'}, {'Name': '@doubledotlabs/dot.css>0.1.0>bootstrap'}, {'Name': '@doubledotlabs/dot.css>0.1.4>bootstrap'}, {'Name': '@dothq/react-dom'}, {'Name': '@dothq/react'}, {'Name': '@doubledotlabs/dot.css>0.1.8>bootstrap'}, {'Name': '@ecapp/webpack'}, {'Name': '@doubledotlabs/dot.css>0.1.5>bootstrap'}, {'Name': '@duying/bootcss-plus'}, {'Name': '@duplotech/webpack'}, {'Name': '@dpoineau/react-scripts>1.0.0>webpack'}], 'var_functions.execute_python:100': {'error': 'No complete matches found in the dataset'}}

exec(code, env_args)
