code = """import json
import re

# Load MIT release packages
package_file = locals()['var_functions.query_db:18']
if isinstance(package_file, str):
    with open(package_file, 'r') as f:
        package_data = json.load(f)

# Filter for MIT licensed release packages
mit_release_set = set()
for pkg in package_data:
    if "MIT" in pkg["Licenses"] and '"IsRelease": true' in pkg["VersionInfo"]:
        key = f"{pkg['System']}:{pkg['Name']}:{pkg['Version']}"
        mit_release_set.add(key)

# Clean up package data to free memory
del package_data

# Load project package versions and match
project_file = locals()['var_functions.query_db:22']
if isinstance(project_file, str):
    with open(project_file, 'r') as f:
        project_data = json.load(f)

# Get unique project names that match our MIT release packages
matched_projects = set()
for proj in project_data:
    if proj['System'] == 'NPM':
        key = f"{proj['System']}:{proj['Name']}:{proj['Version']}"
        if key in mit_release_set:
            matched_projects.add(proj['ProjectName'])

# Clean up project data
del project_data

# Now load project info and extract fork counts
project_info_file = locals()['var_functions.query_db:26']
if isinstance(project_info_file, str):
    with open(project_info_file, 'r') as f:
        project_info_data = json.load(f)

# Extract fork counts from Project_Information field
project_forks = {}
fork_pattern = r'(\d+) forks'

for info in project_info_data:
    text = info['Project_Information']
    # Extract project name from the text
    # Usually starts with "The project" or "The GitHub project named"
    # Format is typically "owner/repo"
    
    # First try to find fork count
    fork_match = re.search(fork_pattern, text, re.IGNORECASE)
    if fork_match:
        forks = int(fork_match.group(1))
        
        # Extract project name - look for "owner/repo" pattern
        # This appears after "project" or "named" 
        proj_name_match = re.search(r'(?:project|named)\s+([a-zA-Z0-9_.-]+/[a-zA-Z0-9_.-]+)', text)
        if proj_name_match:
            proj_name = proj_name_match.group(1)
            if proj_name in matched_projects:
                project_forks[proj_name] = forks

# Sort by fork count and get top 5
top_projects = sorted(project_forks.items(), key=lambda x: x[1], reverse=True)[:5]

print("__RESULT__:")
print(json.dumps([{"project": name, "forks": forks} for name, forks in top_projects]))"""

env_args = {'var_functions.query_db:0': [{'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@discue%2Fui-components/0.13.0"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}', 'Hashes': '[\n  {\n    "Hash": "9BaLXgrA89SmryO88KCXZg==",\n    "Type": "MD5"\n  },\n  {\n    "Hash": "1ehWf/vTvGu5BskEEAeiQL1rNcM=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "UOcNM2Ee5byWKfgJ8Q9am9B369//NKxfLA9nr20EClco8KptuYrcBXZXqOpBk3jJByBoEaek8n47WqZMiB7TDA==",\n    "Type": "SHA512"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1656518476000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'Licenses': '[\n  "MIT"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@dvcol%2Fweb-extension-utils/1.1.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}', 'Hashes': '[\n  {\n    "Hash": "DRev+9MwPdl0AFvrRsdl0w==",\n    "Type": "MD5"\n  },\n  {\n    "Hash": "ZRlEK5Y8S/lD8hQgODR86ZyR+CE=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "cdyQ28FZ8Py7FGKpvoJmDcedIx45qbbsEQAuZTXBQy05X2O7VT6ZpwJ0EjfBDf+jozqqD0H6hKuwZhA021wuPA==",\n    "Type": "SHA512"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1651424462000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'Licenses': '[\n  "MIT"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@dxos%2Fclient/2.28.20-dev.a2e143d3"\n  },\n  {\n    "Label": "SOURCE_REPO",\n    "URL": "git+https://github.com/dxos/dxos.git"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}', 'Hashes': '[\n  {\n    "Hash": "X/Bx/RjabmP3jyetK5mjNIGR44HHYuOUx/8LPpVbJsavy1OqCBH5PQiQN0uhvRglOk0V62/1bqPktEhLBlaMyA==",\n    "Type": "SHA512"\n  },\n  {\n    "Hash": "Ov9ZAnHQEh6vGfmv7NQIluu/96u4rJaKkv9rvN8b8VU=",\n    "Type": "SHA256"\n  },\n  {\n    "Hash": "fCEAXMlSY/LIF6sq/Vwof4WzJjA=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "w3KWAWLUw228bMP3F84S4Q==",\n    "Type": "MD5"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '1', 'UpstreamPublishedAt': '1649368661000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'Licenses': '[\n  "MIT"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@dxos%2Fclient/2.28.20-dev.a2e143d3"\n  },\n  {\n    "Label": "SOURCE_REPO",\n    "URL": "git+https://github.com/dxos/dxos.git"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}', 'Hashes': '[\n  {\n    "Hash": "X/Bx/RjabmP3jyetK5mjNIGR44HHYuOUx/8LPpVbJsavy1OqCBH5PQiQN0uhvRglOk0V62/1bqPktEhLBlaMyA==",\n    "Type": "SHA512"\n  },\n  {\n    "Hash": "Ov9ZAnHQEh6vGfmv7NQIluu/96u4rJaKkv9rvN8b8VU=",\n    "Type": "SHA256"\n  },\n  {\n    "Hash": "fCEAXMlSY/LIF6sq/Vwof4WzJjA=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "w3KWAWLUw228bMP3F84S4Q==",\n    "Type": "MD5"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '1', 'UpstreamPublishedAt': '1649368661000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@eden-network/data', 'Version': '1.0.9-sev.5', 'Licenses': '[\n  "MIT"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@eden-network%2Fdata/1.0.9-sev.5"\n  },\n  {\n    "Label": "SOURCE_REPO",\n    "URL": "https://github.com/eden-network/eden-data.git"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 14\n}', 'Hashes': '[\n  {\n    "Hash": "UjYjBgXwDB0M65qguvWajR+TC5sXyFJgxocCr9mY6e8gsaPUqV+MZouwYFrWKl+qO+Lkz7OaIwIsU/AdTfIp7w==",\n    "Type": "SHA512"\n  },\n  {\n    "Hash": "5VX416ZCYJR+cf+GqsKsN0qi1nbdxseVSRic1Pmq3jE=",\n    "Type": "SHA256"\n  },\n  {\n    "Hash": "yA92J7wrXMzo3JomNmMRE2bPDO0=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "FF4cfQYd3SX1//lIQ8pakA==",\n    "Type": "MD5"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '1', 'UpstreamPublishedAt': '1637610934000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'count': 176998, 'sample': [{'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0'}, {'System': 'NPM', 'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1'}, {'System': 'NPM', 'Name': '@eclipsejs/cli', 'Version': '1.0.0'}, {'System': 'NPM', 'Name': '@ebot7/edem-react', 'Version': '0.18.8'}, {'System': 'NPM', 'Name': '@e4a/irmaseal-wasm-bindings', 'Version': '0.0.1'}]}, 'var_functions.list_db:12': ['project_info', 'project_packageversion'], 'var_functions.query_db:14': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.10', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dlcs/ng', 'Version': '1.0.0', 'ProjectType': 'GITHUB', 'ProjectName': 'winup/dlcs-ng', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dms/cli', 'Version': '1.0.1', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-cli', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dms/cli', 'Version': '1.0.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-cli', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_functions.query_db:16': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'count': 176998, 'sample_keys': ['NPM:@dot-event/watchman:0.6.19', 'NPM:@dorai-ui/tabs:1.2.0', 'NPM:@eclass/semantic-release-ecs-deploy:3.0.35', 'NPM:@dockbite/ngx-gallery:1.0.0', 'NPM:@drovp/ffmpeg:0.0.0']}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:24': {'project_count': 5477, 'sample_projects': ['thoughtsunificator/domodel-popup', 'dongcode/react-native-image-viewing', 'dvlden/slope', 'earthtojake/alchemy', 'ecrypty/florijncoincore-lib', 'divedylan/sardine', 'momsfriendlydevco/doop-table', 'divriots/dockit-stencil', 'dnncommunity/dnn-elements', 'doky-fr/minify-css']}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
