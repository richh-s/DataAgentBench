code = """import json, re, os

# Load all data from the stored file paths
packages_file = locals()['var_functions.query_db:58']
pv_mappings_file = locals()['var_functions.query_db:38']
proj_info_file = locals()['var_functions.query_db:74']

with open(packages_file, 'r') as f:
    all_packages = json.load(f)

with open(pv_mappings_file, 'r') as f:
    all_pv_mappings = json.load(f)

with open(proj_info_file, 'r') as f:
    all_proj_info = json.load(f)

# Step 1: Find latest release version for each package
print('Finding latest release versions...')
latest_packages = {}
processed = 0
for pkg in all_packages:
    processed += 1
    # Process all packages to get accurate latest versions
    name = pkg['Name']
    version = pkg['Version']
    version_info = pkg['VersionInfo']
    
    # Extract ordinal using regex
    ordinal_match = re.search(r'"Ordinal":\s*(\d+)', version_info)
    ordinal = int(ordinal_match.group(1)) if ordinal_match else 0
    
    # Check if this is a release version
    is_release = '"IsRelease": true' in version_info
    
    if is_release:
        # Keep the version with highest ordinal (latest release)
        if name not in latest_packages or ordinal > latest_packages[name]['ordinal']:
            latest_packages[name] = {
                'version': version,
                'ordinal': ordinal
            }

print(f'Found latest releases for {len(latest_packages)} packages')

# Step 2: Map package+version to GitHub repository
print('Mapping packages to GitHub repositories...')
pv_to_repo = {}
for pv in all_pv_mappings:
    if pv['System'] == 'NPM':
        pv_to_repo[(pv['Name'], pv['Version'])] = pv['ProjectName']

# Step 3: Extract GitHub star counts
print('Extracting GitHub stars...')
repo_stars = {}
for info in all_proj_info:
    txt = info.get('Project_Information', '')
    if not txt or txt == 'None':
        continue
    
    # Extract stars
    stars_match = re.search(r'(\d+[\d,]*)\s+stars?', txt)
    if stars_match:
        stars = int(stars_match.group(1).replace(',', ''))
        
        # Extract repository name
        repo_match = re.search(r'project\s+(\S+?)\s', txt)
        if repo_match:
            repo_name = repo_match.group(1)
            repo_stars[repo_name] = stars

print(f'Extracted stars for {len(repo_stars)} repositories')

# Step 4: Match packages with stars (focus on real packages, not dependency paths)
print('Matching packages with stars...')
package_stars = []
processed = 0

for pkg_name, pkg_data in latest_packages.items():
    processed += 1
    # Skip dependency paths (contain >)
    if '>' in pkg_name:
        continue
    
    # Skip TypeScript types packages (start with @types/)
    if pkg_name.startswith('@types/'):
        continue
    
    key = (pkg_name, pkg_data['version'])
    if key in pv_to_repo:
        repo = pv_to_repo[key]
        if repo in repo_stars:
            # Only include if stars > 100
            if repo_stars[repo] > 100:
                package_stars.append([
                    pkg_name,
                    pkg_data['version'],
                    repo_stars[repo],
                    repo
                ])

print(f'Matched {len(package_stars)} packages with stars')

# Step 5: Sort and get top 5
package_stars.sort(key=lambda x: x[2], reverse=True)

# Get top 20 to see what's popular
top20 = package_stars[:20]

# Group by repository to avoid duplicates (different packages from same repo)
repo_seen = set()
unique_top = []
for pkg in package_stars:
    repo = pkg[3]
    if repo not in repo_seen and len(unique_top) < 5:
        repo_seen.add(repo)
        unique_top.append(pkg)

print('Top 5 unique packages:')
for i, pkg in enumerate(unique_top, 1):
    print(f"{i}. {pkg[0]} ({pkg[3]}): {pkg[2]:,} stars")

# Build final result
output = []
for i, item in enumerate(unique_top, 1):
    output.append({
        'rank': i,
        'package': item[0],
        'version': item[1],
        'stars': item[2],
        'repository': item[3]
    })

print('__RESULT__:')
print(json.dumps(output, indent=2))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:2': ['project_info', 'project_packageversion'], 'var_functions.query_db:4': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_functions.query_db:6': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_functions.query_db:8': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'Name': '@edgedev/firebase', 'Version': '1.0.12', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}'}, {'Name': '@dyoshikawa/mentor-php-env', 'Version': '0.0.11', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 10\n}'}, {'Name': '@eclipsejs/cli', 'Version': '1.0.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}'}, {'Name': '@dytesdk/electron-main', 'Version': '1.0.2', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 6\n}'}, {'Name': '@ebot7/edem-react', 'Version': '0.18.8', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 55\n}'}, {'Name': '@e4a/irmaseal-wasm-bindings', 'Version': '0.0.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 1\n}'}, {'Name': '@ebury/chameleon-components', 'Version': '0.1.46', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 46\n}'}, {'Name': '@e-group/material-form', 'Version': '3.13.9', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'Name': '@e-group/material-layout', 'Version': '3.4.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 6\n}'}, {'Name': '@edgeros/jsre-types', 'Version': '1.8.8', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 53\n}'}, {'Name': '@edgeros/jsre-types', 'Version': '1.8.12', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 57\n}'}, {'Name': '@dxos/client', 'Version': '2.18.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 1131\n}'}, {'Name': '@dxos/client', 'Version': '2.18.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 1131\n}'}, {'Name': '@edgeandnode/components', 'Version': '1.0.135', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 146\n}'}, {'Name': '@edgeandnode/components', 'Version': '1.0.58', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 69\n}'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:26': {'packages_count': 39, 'pv_count': 5}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': [{'ProjectName': 'dataminingsupply/dms-io'}, {'ProjectName': 'isacvale/fc'}, {'ProjectName': 'laihaojie/jie'}, {'ProjectName': 'laihaojie/jie'}, {'ProjectName': 'laihaojie/jie'}, {'ProjectName': 'laihaojie/jie'}, {'ProjectName': 'laihaojie/jie'}, {'ProjectName': 'winup/dlcs-ng'}, {'ProjectName': 'dataminingsupply/dms-cli'}, {'ProjectName': 'dataminingsupply/dms-cli'}], 'var_functions.query_db:35': [{'Name': '@dms/io', 'Version': '0.9.0', 'ProjectName': 'dataminingsupply/dms-io', 'Project_Information': 'None', 'Description': 'None'}, {'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectName': 'isacvale/fc', 'Project_Information': 'None', 'Description': 'None'}, {'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectName': 'laihaojie/jie', 'Project_Information': 'None', 'Description': 'None'}, {'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectName': 'laihaojie/jie', 'Project_Information': 'None', 'Description': 'None'}, {'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectName': 'laihaojie/jie', 'Project_Information': 'None', 'Description': 'None'}, {'Name': '@djie/ws', 'Version': '1.0.10', 'ProjectName': 'laihaojie/jie', 'Project_Information': 'None', 'Description': 'None'}, {'Name': '@djie/ws', 'Version': '1.0.17', 'ProjectName': 'laihaojie/jie', 'Project_Information': 'None', 'Description': 'None'}, {'Name': '@dlcs/ng', 'Version': '1.0.0', 'ProjectName': 'winup/dlcs-ng', 'Project_Information': 'None', 'Description': 'None'}, {'Name': '@dms/cli', 'Version': '1.0.1', 'ProjectName': 'dataminingsupply/dms-cli', 'Project_Information': 'None', 'Description': 'None'}, {'Name': '@dms/cli', 'Version': '1.0.0', 'ProjectName': 'dataminingsupply/dms-cli', 'Project_Information': 'None', 'Description': 'None'}], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': [{'total_packages': '661372'}], 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.execute_python:62': {'package_count': 200000}, 'var_functions.execute_python:64': {'packages': 200000, 'pv_mappings': 597602, 'proj_info': 5}, 'var_functions.execute_python:70': [{'package': '@duchesstoffee/react-responsive-carousel', 'version': '3.2.10', 'stars': 2534, 'repo': 'leandrowd/react-responsive-carousel'}], 'var_functions.query_db:72': 'file_storage/functions.query_db:72.json', 'var_functions.query_db:74': 'file_storage/functions.query_db:74.json', 'var_functions.execute_python:100': [['@docly/web', '0.2.0', 89398, 'mui-org/material-ui'], ['@dollarshaveclub/cli>1.3.0>co', '4.6.0', 11862, 'tj/co'], ['@dollarshaveclub/cli>1.11.2>co', '4.6.0', 11862, 'tj/co'], ['@dollarshaveclub/cli>1.0.0>co', '4.6.0', 11862, 'tj/co'], ['@dwarvesf/react-eslint-config', '0.0.4', 10630, 'mono/mono']], 'var_functions.query_db:102': 'file_storage/functions.query_db:102.json', 'var_functions.query_db:104': [{'Project_Information': 'The project mui-org/material-ui on GitHub is a popular open-source library with a remarkable 89,398 stars and 30,522 forks, currently facing 1,688 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': "MUI Core: Ready-to-use foundational React components, free forever. It includes Material UI, which implements Google's Material Design.", 'Homepage': 'https://mui.com/core/', 'OSSFuzz': 'nan'}], 'var_functions.query_db:106': [{'Name': '@docly/web', 'Version': '0.0.1', 'ProjectName': 'mui-org/material-ui'}, {'Name': '@dollarshaveclub/cli>1.12.0>lodash', 'Version': '4.17.11', 'ProjectName': 'lodash/lodash'}, {'Name': '@docly/web', 'Version': '0.2.1', 'ProjectName': 'mui-org/material-ui'}, {'Name': '@docler/next', 'Version': '10.1.4-canary.15', 'ProjectName': 'vercel/next.js'}, {'Name': '@dwarvesf/react-scripts>0.7.0>lodash.pickby', 'Version': '4.6.0', 'ProjectName': 'lodash/lodash'}, {'Name': '@dpoineau/react-scripts>1.0.0>lodash._basecopy', 'Version': '3.0.1', 'ProjectName': 'lodash/lodash'}, {'Name': '@dummmy/webpack-cli>1.0.4>lodash', 'Version': '4.17.19', 'ProjectName': 'lodash/lodash'}, {'Name': '@docly/web', 'Version': '0.0.362', 'ProjectName': 'mui-org/material-ui'}, {'Name': '@dwarvesf/react-scripts>0.7.0>lodash.cond', 'Version': '4.5.2', 'ProjectName': 'lodash/lodash'}, {'Name': '@dpoineau/react-scripts>1.0.0>lodash._getnative', 'Version': '3.9.1', 'ProjectName': 'lodash/lodash'}, {'Name': '@dummmy/pack-cli>1.0.8>lodash', 'Version': '4.17.19', 'ProjectName': 'lodash/lodash'}, {'Name': '@dollarshaveclub/cli>1.5.1>lodash', 'Version': '4.17.4', 'ProjectName': 'lodash/lodash'}, {'Name': '@dollarshaveclub/cli>1.7.1>lodash', 'Version': '4.17.5', 'ProjectName': 'lodash/lodash'}, {'Name': '@dollarshaveclub/cli>1.5.7>lodash', 'Version': '4.17.4', 'ProjectName': 'lodash/lodash'}, {'Name': '@dollarshaveclub/cli>1.13.1>lodash', 'Version': '4.17.11', 'ProjectName': 'lodash/lodash'}, {'Name': '@dwarvesf/react-scripts>0.7.0>lodash._basefor', 'Version': '3.0.3', 'ProjectName': 'lodash/lodash'}, {'Name': '@dpoineau/react-scripts>1.0.0>lodash.words', 'Version': '3.2.0', 'ProjectName': 'lodash/lodash'}, {'Name': '@dpoineau/react-scripts>1.0.0>lodash._createcompounder', 'Version': '3.0.0', 'ProjectName': 'lodash/lodash'}, {'Name': '@dollarshaveclub/cli>2.0.0>lodash', 'Version': '4.17.11', 'ProjectName': 'lodash/lodash'}, {'Name': '@dpoineau/react-scripts>1.0.0>lodash.endswith', 'Version': '4.2.1', 'ProjectName': 'lodash/lodash'}], 'var_functions.query_db:108': [], 'var_functions.execute_python:112': [{'rank': 1, 'package': '@docly/web', 'version': '0.2.0', 'stars': 89398, 'repository': 'mui-org/material-ui'}, {'rank': 2, 'package': '@dollarshaveclub/cli>1.3.0>co', 'version': '4.6.0', 'stars': 11862, 'repository': 'tj/co'}, {'rank': 3, 'package': '@dollarshaveclub/cli>1.11.2>co', 'version': '4.6.0', 'stars': 11862, 'repository': 'tj/co'}, {'rank': 4, 'package': '@dollarshaveclub/cli>1.0.0>co', 'version': '4.6.0', 'stars': 11862, 'repository': 'tj/co'}, {'rank': 5, 'package': '@dwarvesf/react-eslint-config', 'version': '0.0.4', 'stars': 10630, 'repository': 'mono/mono'}], 'var_functions.execute_python:114': [{'rank': 1, 'package': '@docly/web', 'version': '0.2.0', 'stars': 89398, 'repository': 'mui-org/material-ui'}, {'rank': 2, 'package': '@dudadev/mobx-react', 'version': '6.1.7', 'stars': 26802, 'repository': 'mobxjs/mobx'}, {'rank': 3, 'package': '@dplus/themed', 'version': '0.0.2', 'stars': 24814, 'repository': 'react-native-elements/react-native-elements'}, {'rank': 4, 'package': '@dongjiang/textmate-grammars', 'version': '0.0.5', 'stars': 18526, 'repository': 'theia-ide/theia'}, {'rank': 5, 'package': '@docknetwork/rsjf-material-ui', 'version': '3.2.2', 'stars': 13923, 'repository': 'rjsf-team/react-jsonschema-form'}]}

exec(code, env_args)
