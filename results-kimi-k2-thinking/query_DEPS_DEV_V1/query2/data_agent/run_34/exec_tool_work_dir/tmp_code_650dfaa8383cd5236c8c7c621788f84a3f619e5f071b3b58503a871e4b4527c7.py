code = """# Refine the logic to get unique projects with highest fork counts
import json
import re

# Load data
package_path = locals().get('var_functions.query_db:14')
project_pkg_path = locals().get('var_functions.query_db:12')
project_info_path = locals().get('var_functions.query_db:16')

with open(package_path, 'r') as f:
    packages = json.load(f)

with open(project_pkg_path, 'r') as f:
    project_mappings = json.load(f)

with open(project_info_path, 'r') as f:
    project_info = json.load(f)

# Extract fork counts from project info
project_forks = {}
for info in project_info:
    text = info['Project_Information']
    # Extract fork count
    fork_match = re.search(r'(\d+) forks?', text)
    # Extract project name
    proj_match = re.search(r'The project ([\w-]+/[\w-]+)', text)
    
    if fork_match and proj_match:
        forks = int(fork_match.group(1))
        project_name = proj_match.group(1)
        project_forks[project_name] = forks

# Create package to project mapping
package_to_project = {}
for mapping in project_mappings:
    key = (mapping['System'], mapping['Name'], mapping['Version'])
    package_to_project[key] = mapping['ProjectName']

# Match packages with projects and aggregate by project
project_packages = {}
for pkg in packages:
    key = (pkg['System'], pkg['Name'], pkg['Version'])
    if key in package_to_project:
        project_name = package_to_project[key]
        if project_name in project_forks:
            if project_name not in project_packages:
                project_packages[project_name] = {
                    'project': project_name,
                    'forks': project_forks[project_name],
                    'packages': []
                }
            project_packages[project_name]['packages'].append({
                'name': pkg['Name'],
                'version': pkg['Version']
            })

# Convert to list and sort by fork count
top_projects = sorted(project_packages.values(), key=lambda x: x['forks'], reverse=True)

# Get top 5
top5 = top_projects[:5]

# Format the result
result = []
for i, proj in enumerate(top5, 1):
    result.append({
        'rank': i,
        'project': proj['project'],
        'forks': proj['forks'],
        'packages': proj['packages'][:3]  # Show first 3 packages for brevity
    })

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['project_info', 'project_packageversion'], 'var_functions.query_db:9': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project is hosted on GitHub under the name learnfrontend-dc/product-cart, and it currently has 2 open issues. It has garnered a total of 11 stars and has been forked 12 times.', 'Licenses': '[]', 'Description': 'None', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The GitHub project ledgerproject/keypairoom currently has 3 open issues, 3 stars, and 0 forks.', 'Licenses': '[\n  "AGPL-3.0"\n]', 'Description': 'Component to generate and regenerate a keypair, in a deterministic and private way', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leebyron/jasmine-check is hosted on GitHub and currently has 0 open issues, 11 stars, and 3 forks.', 'Licenses': '[]', 'Description': 'Generative property testing for Jasmine', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leebyron/testcheck-js on GitHub has an open issues count of 29, a stars count of 1185, and a forks count of 58, making it a notable repository in the community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': 'Generative testing for JavaScript', 'Homepage': 'http://leebyron.com/testcheck-js', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leecade/react-native-swiper is hosted on GitHub and has a total of 786 open issues, along with an impressive 10,249 stars and 2,392 forks, making it a popular choice among developers for implementing swiping functionality in React Native applications.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'The best Swiper component for React Native.', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_functions.query_db:8': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.10', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dlcs/ng', 'Version': '1.0.0', 'ProjectType': 'GITHUB', 'ProjectName': 'winup/dlcs-ng', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dms/cli', 'Version': '1.0.1', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-cli', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dms/cli', 'Version': '1.0.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-cli', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:28': {'num_packages': 176998, 'num_mappings': 591699, 'num_projects': 770, 'packages_sample': [{'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@discue%2Fui-components/0.13.0"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}', 'Hashes': '[\n  {\n    "Hash": "9BaLXgrA89SmryO88KCXZg==",\n    "Type": "MD5"\n  },\n  {\n    "Hash": "1ehWf/vTvGu5BskEEAeiQL1rNcM=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "UOcNM2Ee5byWKfgJ8Q9am9B369//NKxfLA9nr20EClco8KptuYrcBXZXqOpBk3jJByBoEaek8n47WqZMiB7TDA==",\n    "Type": "SHA512"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1656518476000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'Licenses': '[\n  "MIT"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@dvcol%2Fweb-extension-utils/1.1.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}', 'Hashes': '[\n  {\n    "Hash": "DRev+9MwPdl0AFvrRsdl0w==",\n    "Type": "MD5"\n  },\n  {\n    "Hash": "ZRlEK5Y8S/lD8hQgODR86ZyR+CE=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "cdyQ28FZ8Py7FGKpvoJmDcedIx45qbbsEQAuZTXBQy05X2O7VT6ZpwJ0EjfBDf+jozqqD0H6hKuwZhA021wuPA==",\n    "Type": "SHA512"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1651424462000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}], 'mappings_sample': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectName': 'dataminingsupply/dms-io'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectName': 'isacvale/fc'}], 'projects_sample': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}]}, 'var_functions.execute_python:30': {'matched_count': 3475, 'top5': [{'name': '@dreampie/semantic-ui', 'version': '2.2.11', 'project': 'semantic-org/semantic-ui', 'forks': 4955}, {'name': '@dreampie/semantic-ui', 'version': '2.2.11', 'project': 'semantic-org/semantic-ui', 'forks': 4955}, {'name': '@dlwlrma00/react-native-webview-bypass-ssl', 'version': '11.0.3', 'project': 'react-native-community/react-native-webview', 'forks': 2962}, {'name': '@dlwlrma00/react-native-webview-bypass-ssl', 'version': '11.0.3', 'project': 'react-native-community/react-native-webview', 'forks': 2962}, {'name': '@dpoineau/react-scripts>1.0.0>node-sass', 'version': '3.10.1', 'project': 'sass/node-sass', 'forks': 1326}]}}

exec(code, env_args)
