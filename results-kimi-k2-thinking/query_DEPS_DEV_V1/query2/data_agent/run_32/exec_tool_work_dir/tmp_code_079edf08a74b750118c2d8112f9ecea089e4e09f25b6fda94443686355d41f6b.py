code = """import json
import re

# Load the three datasets
mit_packages_file = locals()['var_functions.query_db:44']
projectversions_file = locals()['var_functions.query_db:40']
projectinfo_file = locals()['var_functions.query_db:46']

with open(mit_packages_file, 'r') as f:
    mit_packages = json.load(f)

with open(projectversions_file, 'r') as f:
    project_versions = json.load(f)

with open(projectinfo_file, 'r') as f:
    project_info = json.load(f)

print(f'Loaded {len(mit_packages)} MIT packages')
print(f'Loaded {len(project_versions)} project versions')
print(f'Loaded {len(project_info)} project info records')

# Create set for fast lookup of MIT packages
mit_package_set = set()
for pkg in mit_packages:
    key = (pkg.get('Name', '').lower(), pkg.get('Version', ''))
    mit_package_set.add(key)

print(f'MIT package set size: {len(mit_package_set)}')

# Build project fork count dictionary
project_forks = {}
for proj in project_info:
    info = proj.get('Project_Information', '')
    # Extract fork count
    fork_match = re.search(r'forks[^\d]*(\d+)', info, re.IGNORECASE)
    if fork_match:
        fork_count = int(fork_match.group(1))
        # Extract project name
        proj_match = re.search(r'(?:project|repository)\s+([\w\-]+/[\w\-]+)', info, re.IGNORECASE)
        if proj_match:
            project_name = proj_match.group(1)
            project_forks[project_name.lower()] = fork_count

print(f'Project forks extracted: {len(project_forks)}')

# Map projects to their MIT packages and count forks
project_stats = {}
for pv in project_versions:
    # Check if this package version is MIT
    pv_key = (pv.get('Name', '').lower(), pv.get('Version', ''))
    if pv_key in mit_package_set:
        project_name = pv.get('ProjectName', '')
        if project_name:
            project_key = project_name.lower()
            # Initialize if new
            if project_key not in project_stats:
                project_stats[project_key] = {
                    'name': project_name,
                    'package_count': 0,
                    'forks': project_forks.get(project_key, 0)
                }
            project_stats[project_key]['package_count'] += 1

print(f'Projects with MIT packages: {len(project_stats)}')

# Convert to list and sort by fork count
projects_list = list(project_stats.values())
projects_list.sort(key=lambda x: x['forks'], reverse=True)

top_5 = projects_list[:5]

result = {
    'total_projects': len(projects_list),
    'top_5_projects': top_5
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:5': 'file_storage/functions.execute_python:5.json', 'var_functions.list_db:6': ['project_info', 'project_packageversion'], 'var_functions.query_db:8': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.10', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dlcs/ng', 'Version': '1.0.0', 'ProjectType': 'GITHUB', 'ProjectName': 'winup/dlcs-ng', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dms/cli', 'Version': '1.0.1', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-cli', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dms/cli', 'Version': '1.0.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-cli', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_functions.execute_python:10': {'count': 100, 'sample': [['@discue/ui-components', '0.13.0'], ['@dvcol/web-extension-utils', '1.1.1'], ['@eclipsejs/cli', '1.0.0'], ['@ebot7/edem-react', '0.18.8'], ['@e4a/irmaseal-wasm-bindings', '0.0.1'], ['@ebury/chameleon-components', '0.1.46'], ['@e-group/material-form', '3.13.9'], ['@e-group/material-layout', '3.4.5'], ['@dspworkplace/ui', '1.0.3'], ['@ditojs/router', '0.125.0']]}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/'}, {'Project_Information': 'The project is hosted on GitHub under the name learnfrontend-dc/product-cart, and it currently has 2 open issues. It has garnered a total of 11 stars and has been forked 12 times.', 'Licenses': '[]', 'Description': 'None', 'Homepage': 'None'}, {'Project_Information': 'The GitHub project ledgerproject/keypairoom currently has 3 open issues, 3 stars, and 0 forks.', 'Licenses': '[\n  "AGPL-3.0"\n]', 'Description': 'Component to generate and regenerate a keypair, in a deterministic and private way', 'Homepage': 'None'}, {'Project_Information': 'The project leebyron/jasmine-check is hosted on GitHub and currently has 0 open issues, 11 stars, and 3 forks.', 'Licenses': '[]', 'Description': 'Generative property testing for Jasmine', 'Homepage': 'None'}, {'Project_Information': 'The project leebyron/testcheck-js on GitHub has an open issues count of 29, a stars count of 1185, and a forks count of 58, making it a notable repository in the community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': 'Generative testing for JavaScript', 'Homepage': 'http://leebyron.com/testcheck-js'}, {'Project_Information': 'The project leecade/react-native-swiper is hosted on GitHub and has a total of 786 open issues, along with an impressive 10,249 stars and 2,392 forks, making it a popular choice among developers for implementing swiping functionality in React Native applications.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'The best Swiper component for React Native.', 'Homepage': 'None'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.execute_python:34': {'count': 2000, 'unique_count': 702, 'sample': [['@discue/ui-components', '0.13.0'], ['@dvcol/web-extension-utils', '1.1.1'], ['@eclipsejs/cli', '1.0.0'], ['@ebot7/edem-react', '0.18.8'], ['@e4a/irmaseal-wasm-bindings', '0.0.1'], ['@ebury/chameleon-components', '0.1.46'], ['@e-group/material-form', '3.13.9'], ['@e-group/material-layout', '3.4.5'], ['@dspworkplace/ui', '1.0.3'], ['@ditojs/router', '0.125.0']]}, 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:52': [{'Name': '@discue/ui-components', 'Version': '0.13.0'}, {'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1'}, {'Name': '@eclipsejs/cli', 'Version': '1.0.0'}, {'Name': '@ebot7/edem-react', 'Version': '0.18.8'}, {'Name': '@e4a/irmaseal-wasm-bindings', 'Version': '0.0.1'}, {'Name': '@ebury/chameleon-components', 'Version': '0.1.46'}, {'Name': '@e-group/material-form', 'Version': '3.13.9'}, {'Name': '@e-group/material-layout', 'Version': '3.4.5'}, {'Name': '@dspworkplace/ui', 'Version': '1.0.3'}, {'Name': '@ditojs/router', 'Version': '0.125.0'}]}

exec(code, env_args)
