code = """import json
import re

# Check if the files exist and load them
packages_file = locals()['var_functions.query_db:68']
versions_file = locals()['var_functions.query_db:58']
projects_file = locals()['var_functions.query_db:26']

print('Files exist:')
print('Packages file:', packages_file is not None)
print('Versions file:', versions_file is not None)
print('Projects file:', projects_file is not None)

# Load full data
with open(packages_file, 'r') as f:
    packages = json.load(f)

with open(versions_file, 'r') as f:
    versions = json.load(f)

with open(projects_file, 'r') as f:
    projects = json.load(f)

print('\nData loaded:')
print('Packages:', len(packages))
print('Versions:', len(versions))
print('Projects:', len(projects))

# Check MIT package keys
mit_keys = [(p['System'], p['Name'], p['Version']) for p in packages[:10]]
print('\nSample MIT package keys:', mit_keys)

# Check version keys
version_keys = [(v['System'], v['Name'], v['Version'], v['ProjectName']) for v in versions[:10]]
print('\nSample version keys:', version_keys)

# Check project forks
project_data = []
for proj in projects[:10]:
    info = proj.get('Project_Information', '')
    
    repo_match = re.search(r'The project ([^ ]+) on GitHub', info)
    fork_match = re.search(r'forks count of (\d+)', info)
    
    if not fork_match:
        fork_match = re.search(r'and (\d+) forks', info)
    
    if repo_match and fork_match:
        project_data.append((repo_match.group(1), int(fork_match.group(1))))
    elif repo_match:
        project_data.append((repo_match.group(1), 0))

print('\nSample project data (repo, forks):', project_data)

# Now check for actual matches
mit_key_set = set(mit_keys)
matching_versions = [v for v in versions if (v['System'], v['Name'], v['Version']) in mit_key_set]

print('\nMatching versions found:', len(matching_versions))
if matching_versions:
    print('Sample matching versions:')
    for v in matching_versions[:5]:
        print(f"  - {v['Name']} {v['Version']} -> {v['ProjectName']}")

# Build full project forks dict
project_forks_full = {}
for proj in projects:
    info = proj.get('Project_Information', '')
    if not info:
        continue
    
    repo_match = re.search(r'The project ([^ ]+) on GitHub', info)
    if not repo_match:
        continue
    
    repo = repo_match.group(1)
    fork_match = re.search(r'forks count of (\d+)', info)
    
    if fork_match:
        forks = int(fork_match.group(1))
    else:
        fork_match = re.search(r'and (\d+) forks', info)
        forks = int(fork_match.group(1)) if fork_match else 0
    
    if forks > 0:
        project_forks_full[repo] = forks

print('\nProjects with forks > 0:', len(project_forks_full))
if project_forks_full:
    top_projects = sorted(project_forks_full.items(), key=lambda x: x[1], reverse=True)[:5]
    print('Top 5 projects by forks:')
    for repo, forks in top_projects:
        print(f"  - {repo}: {forks} forks")

# Final check - find overlaps
if matching_versions:
    version_projects = set(v['ProjectName'] for v in matching_versions)
    fork_projects = set(project_forks_full.keys())
    
    overlap = version_projects.intersection(fork_projects)
    print(f'\nOverlap between package versions and projects with forks: {len(overlap)}')
    if overlap:
        print('Sample overlaps:')
        for repo in list(overlap)[:5]:
            print(f"  - {repo}: {project_forks_full[repo]} forks")"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:2': ['project_info', 'project_packageversion'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.10', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dlcs/ng', 'Version': '1.0.0', 'ProjectType': 'GITHUB', 'ProjectName': 'winup/dlcs-ng', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dms/cli', 'Version': '1.0.1', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-cli', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dms/cli', 'Version': '1.0.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-cli', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:13': 'file_storage/functions.query_db:13.json', 'var_functions.query_db:12': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.'}, {'Project_Information': 'The project is hosted on GitHub under the name learnfrontend-dc/product-cart, and it currently has 2 open issues. It has garnered a total of 11 stars and has been forked 12 times.'}, {'Project_Information': 'The GitHub project ledgerproject/keypairoom currently has 3 open issues, 3 stars, and 0 forks.'}, {'Project_Information': 'The project leebyron/jasmine-check is hosted on GitHub and currently has 0 open issues, 11 stars, and 3 forks.'}, {'Project_Information': 'The project leebyron/testcheck-js on GitHub has an open issues count of 29, a stars count of 1185, and a forks count of 58, making it a notable repository in the community.'}, {'Project_Information': 'The project leecade/react-native-swiper is hosted on GitHub and has a total of 786 open issues, along with an impressive 10,249 stars and 2,392 forks, making it a popular choice among developers for implementing swiping functionality in React Native applications.'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:68': 'file_storage/functions.query_db:68.json', 'var_functions.execute_python:74': [], 'var_functions.execute_python:82': []}

exec(code, env_args)
