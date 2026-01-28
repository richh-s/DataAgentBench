code = """import json
import re

# Load the data files
packages_file = locals()['var_functions.query_db:18']
versions_file = locals()['var_functions.query_db:20']
info_file = locals()['var_functions.query_db:30']

with open(packages_file, 'r') as f:
    packages = json.load(f)

with open(versions_file, 'r') as f:
    versions = json.load(f)

with open(info_file, 'r') as f:
    project_infos = json.load(f)

# Step 1: Parse all project_info entries to extract repo names and fork counts
all_project_forks = {}
repo_patterns = [
    r'The project ([a-zA-Z0-9_-]+/[a-zA-Z0-9_-]+) (?:is hosted|on GitHub)',
    r'The project (?:named )?([a-zA-Z0-9_-]+/[a-zA-Z0-9_-]+)',
    r'The GitHub project (?:named )?([a-zA-Z0-9_-]+/[a-zA-Z0-9_-]+)',
    r'GitHub project ([a-zA-Z0-9_-]+/[a-zA-Z0-9_-]+)'
]

fork_patterns = [
    r'and (\d+) forks[,\.]',
    r'forked (\d+) times',
    r'forks count of (\d+)',
    r'(\d+) forks and',
    r'forks count of (\d+),'  # Added this pattern
]

for info in project_infos:
    info_text = info['Project_Information']
    repo_name = None
    fork_count = None
    
    for pattern in repo_patterns:
        match = re.search(pattern, info_text)
        if match:
            repo_name = match.group(1)
            break
    
    for pattern in fork_patterns:
        match = re.search(pattern, info_text)
        if match:
            try:
                fork_count = int(match.group(1))
                break
            except:
                continue
    
    if repo_name and fork_count is not None:
        all_project_forks[repo_name] = fork_count

# Step 2: Create mapping from package to project name for ALL NPM packages
# This will help us find packages even if they weren't in our MIT sample
all_package_to_project = {}
for v in versions:
    key = (v['System'], v['Name'], v['Version'])
    all_package_to_project[key] = v['ProjectName']

# Step 3: Check which of the top forked projects exist in our MIT/npm package dataset
# and have at least one release version
mit_packages = {(p['System'], p['Name'], p['Version']): p for p in packages}

# Get all unique project names from the MIT packages dataset
mit_projects = {}
for key, project_name in all_package_to_project.items():
    if key in mit_packages:
        if project_name not in mit_projects:
            mit_projects[project_name] = []
        mit_projects[project_name].append(key)

# Step 4: Find which of the top forked projects are in our MIT/npm dataset
top_forked_projects = sorted(all_project_forks.items(), key=lambda x: x[1], reverse=True)

# Get top 5 that are in our MIT/npm dataset
mit_projects_with_forks = []
for project_name, fork_count in top_forked_projects:
    if project_name in mit_projects:
        mit_projects_with_forks.append({
            'project_name': project_name,
            'fork_count': fork_count,
            'package_count': len(mit_projects[project_name])
        })
        if len(mit_projects_with_forks) >= 5:
            break

print('__RESULT__:')
print(json.dumps({
    'total_projects_in_dataset': len(mit_projects),
    'top_mit_projects_by_forks': mit_projects_with_forks,
    'all_top_10_forks': dict(top_forked_projects[:10])
}))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:2': ['project_info', 'project_packageversion'], 'var_functions.query_db:5': [{'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@discue%2Fui-components/0.13.0"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}', 'Hashes': '[\n  {\n    "Hash": "9BaLXgrA89SmryO88KCXZg==",\n    "Type": "MD5"\n  },\n  {\n    "Hash": "1ehWf/vTvGu5BskEEAeiQL1rNcM=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "UOcNM2Ee5byWKfgJ8Q9am9B369//NKxfLA9nr20EClco8KptuYrcBXZXqOpBk3jJByBoEaek8n47WqZMiB7TDA==",\n    "Type": "SHA512"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1656518476000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'Licenses': '[\n  "MIT"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@dvcol%2Fweb-extension-utils/1.1.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}', 'Hashes': '[\n  {\n    "Hash": "DRev+9MwPdl0AFvrRsdl0w==",\n    "Type": "MD5"\n  },\n  {\n    "Hash": "ZRlEK5Y8S/lD8hQgODR86ZyR+CE=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "cdyQ28FZ8Py7FGKpvoJmDcedIx45qbbsEQAuZTXBQy05X2O7VT6ZpwJ0EjfBDf+jozqqD0H6hKuwZhA021wuPA==",\n    "Type": "SHA512"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1651424462000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'Licenses': '[\n  "MIT"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@dxos%2Fclient/2.28.20-dev.a2e143d3"\n  },\n  {\n    "Label": "SOURCE_REPO",\n    "URL": "git+https://github.com/dxos/dxos.git"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}', 'Hashes': '[\n  {\n    "Hash": "X/Bx/RjabmP3jyetK5mjNIGR44HHYuOUx/8LPpVbJsavy1OqCBH5PQiQN0uhvRglOk0V62/1bqPktEhLBlaMyA==",\n    "Type": "SHA512"\n  },\n  {\n    "Hash": "Ov9ZAnHQEh6vGfmv7NQIluu/96u4rJaKkv9rvN8b8VU=",\n    "Type": "SHA256"\n  },\n  {\n    "Hash": "fCEAXMlSY/LIF6sq/Vwof4WzJjA=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "w3KWAWLUw228bMP3F84S4Q==",\n    "Type": "MD5"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '1', 'UpstreamPublishedAt': '1649368661000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'Licenses': '[\n  "MIT"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@dxos%2Fclient/2.28.20-dev.a2e143d3"\n  },\n  {\n    "Label": "SOURCE_REPO",\n    "URL": "git+https://github.com/dxos/dxos.git"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}', 'Hashes': '[\n  {\n    "Hash": "X/Bx/RjabmP3jyetK5mjNIGR44HHYuOUx/8LPpVbJsavy1OqCBH5PQiQN0uhvRglOk0V62/1bqPktEhLBlaMyA==",\n    "Type": "SHA512"\n  },\n  {\n    "Hash": "Ov9ZAnHQEh6vGfmv7NQIluu/96u4rJaKkv9rvN8b8VU=",\n    "Type": "SHA256"\n  },\n  {\n    "Hash": "fCEAXMlSY/LIF6sq/Vwof4WzJjA=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "w3KWAWLUw228bMP3F84S4Q==",\n    "Type": "MD5"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '1', 'UpstreamPublishedAt': '1649368661000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@eden-network/data', 'Version': '1.0.9-sev.5', 'Licenses': '[\n  "MIT"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@eden-network%2Fdata/1.0.9-sev.5"\n  },\n  {\n    "Label": "SOURCE_REPO",\n    "URL": "https://github.com/eden-network/eden-data.git"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 14\n}', 'Hashes': '[\n  {\n    "Hash": "UjYjBgXwDB0M65qguvWajR+TC5sXyFJgxocCr9mY6e8gsaPUqV+MZouwYFrWKl+qO+Lkz7OaIwIsU/AdTfIp7w==",\n    "Type": "SHA512"\n  },\n  {\n    "Hash": "5VX416ZCYJR+cf+GqsKsN0qi1nbdxseVSRic1Pmq3jE=",\n    "Type": "SHA256"\n  },\n  {\n    "Hash": "yA92J7wrXMzo3JomNmMRE2bPDO0=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "FF4cfQYd3SX1//lIQ8pakA==",\n    "Type": "MD5"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '1', 'UpstreamPublishedAt': '1637610934000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}], 'var_functions.query_db:6': [{'count': '176998'}], 'var_functions.query_db:8': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:16': {'count': 5000, 'sample': [{'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'System': 'NPM', 'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'System': 'NPM', 'Name': '@eclipsejs/cli', 'Version': '1.0.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}'}]}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'mit_packages_count': 50000, 'project_versions_count': 50000, 'mit_sample': [{'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'System': 'NPM', 'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}], 'project_sample': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectName': 'dataminingsupply/dms-io'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectName': 'isacvale/fc'}]}, 'var_functions.execute_python:24': {'total_mit_packages': 50000, 'total_project_versions': 50000, 'matches_found': 4060, 'sample_matches': [['NPM', '@eclass/semantic-release-ecs-deploy', '3.0.17'], ['NPM', '@dolittle/sdk.events.filtering', '13.0.0'], ['NPM', '@dword-design/postcss-link-area', '2.0.2'], ['NPM', '@dra2020/baseclient', '1.0.58'], ['NPM', '@doreamonjs/application', '1.1.26']]}, 'var_functions.query_db:28': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:32': {'packages': 50000, 'versions': 50000, 'infos': 770, 'packages_sample': {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, 'versions_sample': {'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectName': 'dataminingsupply/dms-io'}, 'infos_sample': {'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}}, 'var_functions.execute_python:34': {'total_common_packages': 4060, 'unique_projects': 1408, 'sample_projects': [['dwtechs/checkhard.js', [['NPM', '@dwtechs/checkhard', '2.19.1']]], ['drovp/utils', [['NPM', '@drovp/utils', '2.1.0'], ['NPM', '@drovp/utils', '2.1.2']]], ['dword-design/base-config-component-library', [['NPM', '@dword-design/base-config-component-library', '1.2.27'], ['NPM', '@dword-design/base-config-component-library', '1.2.29'], ['NPM', '@dword-design/base-config-component-library', '1.2.30'], ['NPM', '@dword-design/base-config-component-library', '1.2.33'], ['NPM', '@dword-design/base-config-component-library', '1.2.45'], ['NPM', '@dword-design/base-config-component-library', '1.2.58']]], ['dolittle/javascript.sdk', [['NPM', '@dolittle/sdk.events', '15.0.0'], ['NPM', '@dolittle/sdk.events.filtering', '17.0.0'], ['NPM', '@dolittle/sdk.events.processing', '14.3.2'], ['NPM', '@dolittle/sdk.events.processing', '14.3.1'], ['NPM', '@dolittle/sdk.events.handling', '22.2.0'], ['NPM', '@dolittle/sdk.resilience', '23.2.1'], ['NPM', '@dolittle/sdk.embeddings', '18.1.0'], ['NPM', '@dolittle/sdk.execution', '18.1.0'], ['NPM', '@dolittle/sdk.artifacts', '10.0.0'], ['NPM', '@dolittle/sdk.protobuf', '13.0.0'], ['NPM', '@dolittle/sdk.resilience', '3.1.1'], ['NPM', '@dolittle/sdk.events.processing', '5.0.0'], ['NPM', '@dolittle/sdk.events.filtering', '4.1.0'], ['NPM', '@dolittle/sdk.protobuf', '2.1.2'], ['NPM', '@dolittle/sdk.common', '13.0.1'], ['NPM', '@dolittle/sdk.eventhorizon', '18.1.0'], ['NPM', '@dolittle/sdk.protobuf', '18.0.0'], ['NPM', '@dolittle/sdk.services', '1.3.0'], ['NPM', '@dolittle/sdk', '1.5.2'], ['NPM', '@dolittle/sdk.execution', '22.1.0'], ['NPM', '@dolittle/sdk.events', '2.1.3'], ['NPM', '@dolittle/sdk.aggregates', '14.3.0'], ['NPM', '@dolittle/sdk.protobuf', '9.0.0'], ['NPM', '@dolittle/sdk.events', '4.0.0'], ['NPM', '@dolittle/sdk.execution', '7.0.1'], ['NPM', '@dolittle/sdk.resilience', '23.0.0'], ['NPM', '@dolittle/sdk.artifacts', '20.0.0'], ['NPM', '@dolittle/sdk.resilience', '14.3.2'], ['NPM', '@dolittle/sdk.eventhorizon', '2.2.0'], ['NPM', '@dolittle/sdk.tenancy', '23.1.0'], ['NPM', '@dolittle/sdk.events.filtering', '13.0.0'], ['NPM', '@dolittle/sdk.events.handling', '13.0.0']]], ['jeakey/docsmarker', [['NPM', '@dopro/docsmaker', '0.1.6'], ['NPM', '@dopro/docsmaker', '0.1.12']]]]}, 'var_functions.execute_python:36': {'projects_with_forks': 41, 'sample_projects': {'moox/eslint-loader': 128, 'libertyequalitydata/dynamic-data': 11, 'stephenliu1944/mock-server': 0, 'n43/easyapp': 0, 'mathiasbynens/jsesc': 51, 'quartzjer/ecc-jsbn': 11, 'lohfu/domp': 0, 'momsfriendlydevco/doop-service-files': 0, 'sindresorhus/escape-string-regexp': 55, 'megafetis/vue3-treeselect': 96}}, 'var_functions.execute_python:38': {'parsed_projects': 639, 'max_forks': 12282, 'top_10_forks': {'microsoft/typescript': 12282, 'mozilla/pdf': 9617, 'swagger-api/swagger-ui': 8824, 'moment/moment': 7201, 'lodash/lodash': 7109, 'react-navigation/react-navigation': 4989, 'semantic-org/semantic-ui': 4955, 'request/request': 3145, 'tencent/vconsole': 2982, 'react-native-community/react-native-webview': 2962}}, 'var_functions.execute_python:40': {'matched_projects': 1408, 'projects_with_forks': 93, 'top_5_projects': [['moment/moment', 7201], ['lodash/lodash', 7109], ['tj/co', 860], ['react-materialize/react-materialize', 307], ['substack/minimist', 306]]}}

exec(code, env_args)
