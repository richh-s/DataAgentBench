code = """import json

# Load all data from storage
latest_packages_file = locals()['var_functions.execute_python:34']
ppv_file_path = locals()['var_functions.query_db:22']
project_stars_file = locals()['var_functions.execute_python:40']

with open(latest_packages_file, 'r') as f:
    latest_packages_data = json.load(f)

with open(ppv_file_path, 'r') as f:
    ppv_data = json.load(f)

with open(project_stars_file, 'r') as f:
    project_stars_data = json.load(f)

# Extract data
latest_packages = latest_packages_data['sample_packages']  # This is just a sample, need full data
# Actually need to recompute or access the full data

# Recompute latest_packages from the original package file
package_file_path = locals()['var_functions.query_db:18']
with open(package_file_path, 'r') as f:
    package_data = json.load(f)

import re
from collections import defaultdict

latest_packages = {}
for pkg in package_data:
    if pkg['System'] == 'NPM':
        try:
            version_info_str = pkg['VersionInfo']
            version_info_str_clean = re.sub(r'\s+', ' ', version_info_str).strip()
            version_info = json.loads(version_info_str_clean)
            
            if version_info.get('IsRelease'):
                name = pkg['Name']
                ordinal = version_info.get('Ordinal', 0)
                
                if name not in latest_packages or ordinal > latest_packages[name]['ordinal']:
                    latest_packages[name] = {
                        'name': name,
                        'version': pkg['Version'],
                        'ordinal': ordinal
                    }
        except:
            continue

# Create package to github mapping
package_to_github = {}
for item in ppv_data:
    if item['System'] == 'NPM' and item['ProjectType'] == 'GITHUB':
        pkg_name = item['Name']
        if pkg_name not in package_to_github:
            package_to_github[pkg_name] = item['ProjectName']

# Create github stars mapping
project_stars = {}
for repo_name, stars in project_stars_data['top_20_repos']:  # This is also limited
    project_stars[repo_name] = stars

# Actually need to parse all project_info, not just top 20
project_all_path = locals()['var_functions.query_db:38']
with open(project_all_path, 'r') as f:
    all_project_info = json.load(f)

project_stars = {}
for item in all_project_info:
    info_text = item['Project_Information']
    repo_match = re.search(r'(?:project\s+)?([a-zA-Z0-9_.-]+/[a-zA-Z0-9_.-]+)\s+(?:is hosted on|on)\s+GitHub', info_text, re.IGNORECASE)
    stars_match = re.search(r'(\d+)\s+stars?', info_text, re.IGNORECASE)
    
    if repo_match and stars_match:
        repo_name = repo_match.group(1)
        stars = int(stars_match.group(1))
        project_stars[repo_name] = stars

# Now join everything together
package_popularity = []
for pkg_name, pkg_info in latest_packages.items():
    if pkg_name in package_to_github:
        github_repo = package_to_github[pkg_name]
        if github_repo in project_stars:
            package_popularity.append({
                'package_name': pkg_name,
                'version': pkg_info['version'],
                'github_repo': github_repo,
                'stars': project_stars[github_repo]
            })

# Sort by stars and get top 5
top_5 = sorted(package_popularity, key=lambda x: x['stars'], reverse=True)[:5]

print("__RESULT__:")
print(json.dumps({
    "total_packages_with_stars": len(package_popularity),
    "top_5_packages": top_5
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.query_db:2': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'System': 'NPM', 'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'System': 'NPM', 'Name': '@edgedev/firebase', 'Version': '1.0.12', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}'}, {'System': 'NPM', 'Name': '@eden-network/data', 'Version': '1.0.9-sev.5', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 14\n}'}], 'var_functions.query_db:5': [{'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.0.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 1\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.0.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 1\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.0.12', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 10\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.0.13', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 11\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.0.14', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.0.15', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.2', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 15\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.3', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 16\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.4', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 17\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.6', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 19\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.0.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 2\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.7', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 20\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.8', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 21\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.8', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 21\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.9', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 22\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.9', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 22\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.2.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 23\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.2.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 23\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.2.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 24\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.2.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 24\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.2.2', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 25\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.2.2', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 25\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.0.2', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 3\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.0.6', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 4\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.0.7', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 5\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.0.8', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 6\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.0.9', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.0.10', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 8\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.0.11', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 9\n}'}], 'var_functions.list_db:6': ['project_info', 'project_packageversion'], 'var_functions.query_db:8': [{'System': 'NPM', 'Name': '@discordx/music', 'Version': '5.0.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 208\n}', 'UpstreamPublishedAt': '1676224725000000.0'}, {'System': 'NPM', 'Name': '@discordx/music', 'Version': '5.0.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 208\n}', 'UpstreamPublishedAt': '1676224725000000.0'}, {'System': 'NPM', 'Name': '@discordx/music', 'Version': '4.0.0-dev.1639703569.3b1e603', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 175\n}', 'UpstreamPublishedAt': '1639703570000000.0'}, {'System': 'NPM', 'Name': '@discordx/music', 'Version': '4.0.0-dev.1639703569.3b1e603', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 175\n}', 'UpstreamPublishedAt': '1639703570000000.0'}, {'System': 'NPM', 'Name': '@discordx/music', 'Version': '4.0.0-dev.1638858523.d83f446', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 162\n}', 'UpstreamPublishedAt': '1638858525000000.0'}], 'var_functions.query_db:10': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_functions.query_db:12': [], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.'}], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:30': {'total_packages': 661372, 'sample': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'UpstreamPublishedAt': '1699345351000000.0'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}', 'UpstreamPublishedAt': '1670271173000000.0'}]}, 'var_functions.execute_python:34': {'total_latest_packages': 15811, 'sample_packages': [{'name': '@ecl/twig-component-carousel', 'version': '3.11.1', 'ordinal': 29, 'published_at': '1699345351000000.0'}, {'name': '@douganderson444/panzoom-node', 'version': '1.2.2', 'ordinal': 25, 'published_at': '1674844413000000.0'}, {'name': '@discue/ui-components', 'version': '0.38.2', 'ordinal': 45, 'published_at': '1682020735000000.0'}, {'name': '@dvcol/web-extension-utils', 'version': '2.3.4', 'ordinal': 27, 'published_at': '1680360764000000.0'}, {'name': '@edgedev/firebase', 'version': '2.0.20', 'ordinal': 133, 'published_at': '1700211829000000.0'}]}, 'var_functions.execute_python:36': {'total_mappings': 16273, 'sample_mappings': [['@dms/io', 'dataminingsupply/dms-io'], ['@dvo/fc', 'isacvale/fc'], ['@djie/ui', 'laihaojie/jie'], ['@djie/ws', 'laihaojie/jie'], ['@dlcs/ng', 'winup/dlcs-ng']]}, 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.execute_python:40': {'total_projects_with_stars': 419, 'top_20_repos': [['leaflet/leaflet', 38715], ['theia-ide/theia', 18526], ['sass/node-sass', 8498], ['ljharb/qs', 8073], ['sveltejs/sapper', 7056], ['shaka-project/shaka-player', 6949], ['react-native-community/react-native-webview', 6345], ['mapbox/node-sqlite3', 5917], ['supasate/connected-react-router', 4737], ['securingsincity/react-ace', 4005], ['mbrn/material-table', 3464], ['then/promise', 2543], ['sindresorhus/globby', 2491], ['spite/three.meshline', 2030], ['th3rdwave/react-native-safe-area-context', 1902], ['lekoarts/gatsby-themes', 1836], ['nandorojo/expo-theme-ui', 1835], ['mixu/markdown-styles', 1809], ['salesforce/lwc', 1595], ['naoufal/react-native-payments', 1560]]}}

exec(code, env_args)
