code = """import json
import re

# Load all data sources
packages_file = locals()['var_functions.query_db:20']
proj_versions_file = locals()['var_functions.query_db:28']
proj_forks_file = locals()['var_functions.query_db:30']

with open(packages_file, 'r') as f:
    packages = json.load(f)

with open(proj_versions_file, 'r') as f:
    proj_versions = json.load(f)

with open(proj_forks_file, 'r') as f:
    proj_forks = json.load(f)

# Create package to repo mapping
pkg_to_repo = {}
for pv in proj_versions:
    key = (pv['System'], pv['Name'], pv['Version'])
    pkg_to_repo[key] = pv['ProjectName']

# Find packages with repos
packages_with_repos = []
for pkg in packages:
    key = (pkg['System'], pkg['Name'], pkg['Version'])
    if key in pkg_to_repo:
        packages_with_repos.append({
            'pkg': pkg['Name'],
            'ver': pkg['Version'],
            'repo': pkg_to_repo[key]
        })

# Extract fork counts with better regex patterns
repo_to_forks = {}
fork_patterns = [
    re.compile(r'(\d+) forks'),
    re.compile(r'forks count of (\d+)'),
]

repo_patterns = [
    re.compile(r'project\s+([\w-]+/[\w-]+)', re.IGNORECASE),
    re.compile(r'GitHub project named\s+([\w-]+/[\w-]+)', re.IGNORECASE),
    re.compile(r'project\s+([\w-]+/[\w-]+)\s+on GitHub', re.IGNORECASE),
]

for proj in proj_forks:
    info = proj['Project_Information']
    forks = None
    for fp in fork_patterns:
        match = fp.search(info)
        if match:
            forks = int(match.group(1))
            break
    
    if forks is None:
        continue
        
    repo = None
    for rp in repo_patterns:
        match = rp.search(info)
        if match:
            repo = match.group(1)
            break
    
    if repo:
        repo_to_forks[repo.lower()] = forks

# Match and get top projects
results = []
for pkg in packages_with_repos:
    repo_lower = pkg['repo'].lower()
    if repo_lower in repo_to_forks:
        results.append({
            'package': pkg['pkg'],
            'version': pkg['ver'],
            'repo': pkg['repo'],
            'forks': repo_to_forks[repo_lower]
        })

# Sort and get unique top 5
unique_results = {}
for r in results:
    repo = r['repo']
    if repo not in unique_results or r['forks'] > unique_results[repo]['forks']:
        unique_results[repo] = r

top_5 = sorted(unique_results.values(), key=lambda x: x['forks'], reverse=True)[:5]

output = {
    'top_5': top_5,
    'summary': {
        'total_mit_packages': len(packages),
        'with_github_repo': len(packages_with_repos),
        'with_fork_info': len(results),
        'unique_repos': len(unique_results),
        'repos_scanned': len(repo_to_forks)
    }
}

print('__RESULT__:')
print(json.dumps(output, indent=2))"""

env_args = {'var_functions.query_db:0': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@ecl%2Ftwig-component-carousel/3.11.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'Hashes': '[\n  {\n    "Hash": "vH5da6eUZ94i1AcOsrC6VjSV88cMUe5A1w+CDHAt2aYXldR9sBNRCse27cIx51GnUjnj7dSe3o5A81TjraJ0Lw==",\n    "Type": "SHA512"\n  },\n  {\n    "Hash": "WZUWPp1jVp6nrUZ0n7vmthbB4OrtnLFNDOPPBBNp15I=",\n    "Type": "SHA256"\n  },\n  {\n    "Hash": "JbFslb4AeqQVI+LCXFeZKFrWmHI=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "zBm5Qvg5p2bQwUTcg6hZYA==",\n    "Type": "MD5"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1699345351000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'Licenses': '[]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@douganderson444%2Fpanzoom-node/v/1.1.5"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}', 'Hashes': '[\n  {\n    "Hash": "bn6jsFfgQaOqxYcxQLdn+w==",\n    "Type": "MD5"\n  },\n  {\n    "Hash": "Ag2muuzRUxbKTAR/H0qjiVGqd5E=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "Z2cdZL3dyM3mmLnEKE4HDFAFnE8OTVU1Lm36fasqZuFRlfjv+M8qkZs+ZAwOsR65FfhH1St2n1YvhihaMM5UEw==",\n    "Type": "SHA512"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '1', 'UpstreamPublishedAt': '1670271173000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'Licenses': '[]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@douganderson444%2Fpanzoom-node/v/1.1.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}', 'Hashes': '[\n  {\n    "Hash": "f882urh9+DaLLfg22vF4Dw==",\n    "Type": "MD5"\n  },\n  {\n    "Hash": "UavDKi+B1bjz5yL/IEUOzG5BIX0=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "Br/d41zpasemiy1jjn91jYmLFbgFFGo5+V+v5+LRxHeTg2MajAkwczkbMUyb3k8xD0UIubDfClv9roNgLIoOEQ==",\n    "Type": "SHA512"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '1', 'UpstreamPublishedAt': '1654791421000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'Licenses': '[\n  "ISC"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@dreamworld%2Fdw-select/3.1.2-fix-double-click-issue.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}', 'Hashes': '[\n  {\n    "Hash": "1e+/qEffZeAgXRtIOUmPqw==",\n    "Type": "MD5"\n  },\n  {\n    "Hash": "C3IyUAgv9Bs96QRmMOHUrQwBnS4=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "07tFydL0pzuqYZbHESf4n0N5gbgvaPZFBfRZmC+k4dqhaKjR2xRBXBpCyxji9W0kkkCVrgtiTrI/XzhgTBq80w==",\n    "Type": "SHA512"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1624260093000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@discue%2Fui-components/0.13.0"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}', 'Hashes': '[\n  {\n    "Hash": "9BaLXgrA89SmryO88KCXZg==",\n    "Type": "MD5"\n  },\n  {\n    "Hash": "1ehWf/vTvGu5BskEEAeiQL1rNcM=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "UOcNM2Ee5byWKfgJ8Q9am9B369//NKxfLA9nr20EClco8KptuYrcBXZXqOpBk3jJByBoEaek8n47WqZMiB7TDA==",\n    "Type": "SHA512"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1656518476000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}], 'var_functions.list_db:2': ['packageinfo'], 'var_functions.query_db:12': [], 'var_functions.query_db:14': [{'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'System': 'NPM', 'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'System': 'NPM', 'Name': '@eclipsejs/cli', 'Version': '1.0.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}'}, {'System': 'NPM', 'Name': '@ebot7/edem-react', 'Version': '0.18.8', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 55\n}'}, {'System': 'NPM', 'Name': '@e4a/irmaseal-wasm-bindings', 'Version': '0.0.1', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 1\n}'}, {'System': 'NPM', 'Name': '@ebury/chameleon-components', 'Version': '0.1.46', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 46\n}'}, {'System': 'NPM', 'Name': '@e-group/material-form', 'Version': '3.13.9', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@e-group/material-layout', 'Version': '3.4.5', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 6\n}'}, {'System': 'NPM', 'Name': '@dspworkplace/ui', 'Version': '1.0.3', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 4\n}'}, {'System': 'NPM', 'Name': '@ditojs/router', 'Version': '0.125.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 87\n}'}], 'var_functions.query_db:16': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_functions.query_db:18': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:24': {'count': 176170, 'sample_packages': [{'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0'}, {'System': 'NPM', 'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1'}, {'System': 'NPM', 'Name': '@eclipsejs/cli', 'Version': '1.0.0'}]}, 'var_functions.execute_python:26': {'total_packages': 176170, 'num_batches': 177, 'batch_size': 1000}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:32': {'total_projects_with_forks': 516, 'top_projects': [{'repo': 'leaflet/leaflet', 'forks': 5782, 'info': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open i'}, {'repo': 'semantic-org/semantic-ui', 'forks': 4955, 'info': 'The project semantic-org/semantic-ui is hosted on GitHub and currently has an open issues count of 1'}, {'repo': 'react-native-community/react-native-webview', 'forks': 2962, 'info': 'The project react-native-community/react-native-webview is hosted on GitHub and currently has 87 ope'}, {'repo': 'theia-ide/theia', 'forks': 2451, 'info': 'The project theia-ide/theia on GitHub is an open-source IDE with an open issues count of 1359, and i'}, {'repo': 'unknown', 'forks': 1449, 'info': 'The project react-native-device-info hosted on GitHub, under the repository name react-native-device'}, {'repo': 'sass/node-sass', 'forks': 1326, 'info': 'The project sass/node-sass on GitHub currently has 189 open issues, 8498 stars, and 1326 forks, maki'}, {'repo': 'shaka-project/shaka-player', 'forks': 1319, 'info': 'The project shaka-project/shaka-player on GitHub is a well-regarded open-source initiative, currentl'}, {'repo': 'unknown', 'forks': 1308, 'info': 'The project is hosted on GitHub under the name microsoft/typescript-website, which currently has 32 '}, {'repo': 'mbrn/material-table', 'forks': 1035, 'info': 'The project mbrn/material-table is hosted on GitHub and currently has 23 open issues, 3464 stars, an'}, {'repo': 'ternjs/acorn', 'forks': 944, 'info': 'The project ternjs/acorn on GitHub is a popular repository with a remarkable stars count of 9841 and'}]}, 'var_functions.query_db:36': [{'package_name': '@divine/uri', 'package_version': '0.3.3', 'github_repo': 'leviticusmb/esxx-2', 'Project_Information': 'The GitHub project named leviticusmb/esxx-2 currently has 0 open issues, 0 stars, and 0 forks.'}, {'package_name': '@dnausp/core', 'package_version': '0.0.1-alpha.15', 'github_repo': 'lfujiwara/dnausp-core', 'Project_Information': 'The project lfujiwara/dnausp-core is hosted on GITHUB and currently has an open issues count of 0, a stars count of 0, and a forks count of 1.'}, {'package_name': '@dnausp/core', 'package_version': '0.0.1-alpha.8', 'github_repo': 'lfujiwara/dnausp-core', 'Project_Information': 'The project lfujiwara/dnausp-core is hosted on GITHUB and currently has an open issues count of 0, a stars count of 0, and a forks count of 1.'}, {'package_name': '@dnausp/core', 'package_version': '0.0.1-alpha.10', 'github_repo': 'lfujiwara/dnausp-core', 'Project_Information': 'The project lfujiwara/dnausp-core is hosted on GITHUB and currently has an open issues count of 0, a stars count of 0, and a forks count of 1.'}, {'package_name': '@dsnp/sdk', 'package_version': '0.0.0-e3daf4', 'github_repo': 'libertydsnp/sdk-ts', 'Project_Information': 'The project libertydsnp/sdk-ts is hosted on GitHub and currently has 3 open issues, 9 stars, and 2 forks.'}, {'package_name': '@dsnp/sdk', 'package_version': '0.0.0-3e0897', 'github_repo': 'libertydsnp/sdk-ts', 'Project_Information': 'The project libertydsnp/sdk-ts is hosted on GitHub and currently has 3 open issues, 9 stars, and 2 forks.'}, {'package_name': '@dsnp/sdk', 'package_version': '2.0.1', 'github_repo': 'libertydsnp/sdk-ts', 'Project_Information': 'The project libertydsnp/sdk-ts is hosted on GitHub and currently has 3 open issues, 9 stars, and 2 forks.'}, {'package_name': '@dsnp/sdk', 'package_version': '0.0.0-bb9793', 'github_repo': 'libertydsnp/sdk-ts', 'Project_Information': 'The project libertydsnp/sdk-ts is hosted on GitHub and currently has 3 open issues, 9 stars, and 2 forks.'}, {'package_name': '@dsnp/sdk', 'package_version': '0.0.0-75624c', 'github_repo': 'libertydsnp/sdk-ts', 'Project_Information': 'The project libertydsnp/sdk-ts is hosted on GitHub and currently has 3 open issues, 9 stars, and 2 forks.'}, {'package_name': '@dsnp/sdk', 'package_version': '0.0.0-58c147', 'github_repo': 'libertydsnp/sdk-ts', 'Project_Information': 'The project libertydsnp/sdk-ts is hosted on GitHub and currently has 3 open issues, 9 stars, and 2 forks.'}, {'package_name': '@dsnp/sdk', 'package_version': '0.0.0-b0dedf', 'github_repo': 'libertydsnp/sdk-ts', 'Project_Information': 'The project libertydsnp/sdk-ts is hosted on GitHub and currently has 3 open issues, 9 stars, and 2 forks.'}, {'package_name': '@dsnp/sdk', 'package_version': '0.0.0-97604a', 'github_repo': 'libertydsnp/sdk-ts', 'Project_Information': 'The project libertydsnp/sdk-ts is hosted on GitHub and currently has 3 open issues, 9 stars, and 2 forks.'}, {'package_name': '@dsnp/sdk', 'package_version': '0.0.0-869490', 'github_repo': 'libertydsnp/sdk-ts', 'Project_Information': 'The project libertydsnp/sdk-ts is hosted on GitHub and currently has 3 open issues, 9 stars, and 2 forks.'}, {'package_name': '@dsnp/sdk', 'package_version': '0.0.0-23cc64', 'github_repo': 'libertydsnp/sdk-ts', 'Project_Information': 'The project libertydsnp/sdk-ts is hosted on GitHub and currently has 3 open issues, 9 stars, and 2 forks.'}, {'package_name': '@dsnp/sdk', 'package_version': '0.0.0-841bd2', 'github_repo': 'libertydsnp/sdk-ts', 'Project_Information': 'The project libertydsnp/sdk-ts is hosted on GitHub and currently has 3 open issues, 9 stars, and 2 forks.'}, {'package_name': '@dsnp/sdk', 'package_version': '0.0.0-efdb66', 'github_repo': 'libertydsnp/sdk-ts', 'Project_Information': 'The project libertydsnp/sdk-ts is hosted on GitHub and currently has 3 open issues, 9 stars, and 2 forks.'}, {'package_name': '@dsnp/sdk', 'package_version': '0.0.0-875b82', 'github_repo': 'libertydsnp/sdk-ts', 'Project_Information': 'The project libertydsnp/sdk-ts is hosted on GitHub and currently has 3 open issues, 9 stars, and 2 forks.'}, {'package_name': '@dsnp/sdk', 'package_version': '0.0.0-563c71', 'github_repo': 'libertydsnp/sdk-ts', 'Project_Information': 'The project libertydsnp/sdk-ts is hosted on GitHub and currently has 3 open issues, 9 stars, and 2 forks.'}, {'package_name': '@dsnp/sdk', 'package_version': '0.0.0-b62952', 'github_repo': 'libertydsnp/sdk-ts', 'Project_Information': 'The project libertydsnp/sdk-ts is hosted on GitHub and currently has 3 open issues, 9 stars, and 2 forks.'}, {'package_name': '@dsnp/sdk', 'package_version': '0.0.0-d4cd6c', 'github_repo': 'libertydsnp/sdk-ts', 'Project_Information': 'The project libertydsnp/sdk-ts is hosted on GitHub and currently has 3 open issues, 9 stars, and 2 forks.'}], 'var_functions.execute_python:40': {'total_packages': 176170, 'repos_with_fork_counts': 385, 'top_repos': [['semantic-org/semantic-ui', 4955], ['react-native-community/react-native-webview', 2962], ['theia-ide/theia', 2451], ['sass/node-sass', 1326], ['shaka-project/shaka-player', 1319], ['mbrn/material-table', 1035], ['ternjs/acorn', 944], ['mjmlio/mjml', 937], ['thejameskyle/react-loadable', 857], ['matt-esch/virtual-dom', 851]]}, 'var_functions.execute_python:46': {'keys': ['System', 'Name', 'Version', 'ProjectName'], 'sample': {'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectName': 'dataminingsupply/dms-io'}}, 'var_functions.execute_python:48': {'top_5': [{'package_name': '@dreampie/semantic-ui', 'version': '2.2.11', 'github_repo': 'semantic-org/semantic-ui', 'forks': 4955}, {'package_name': '@dreampie/semantic-ui', 'version': '2.2.11', 'github_repo': 'semantic-org/semantic-ui', 'forks': 4955}, {'package_name': '@dlwlrma00/react-native-webview-bypass-ssl', 'version': '11.0.3', 'github_repo': 'react-native-community/react-native-webview', 'forks': 2962}, {'package_name': '@dlwlrma00/react-native-webview-bypass-ssl', 'version': '11.0.3', 'github_repo': 'react-native-community/react-native-webview', 'forks': 2962}, {'package_name': '@dpoineau/react-scripts>1.0.0>node-sass', 'version': '3.10.1', 'github_repo': 'sass/node-sass', 'forks': 1326}], 'stats': {'total_mit_packages': 176170, 'packages_with_repos': 173530, 'packages_with_fork_info': 3156, 'repos_with_fork_data': 385}}, 'var_functions.query_db:50': []}

exec(code, env_args)
