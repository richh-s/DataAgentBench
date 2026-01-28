code = """import json
import re
import pandas as pd
import sys

# Load MIT packages (from query_db:36)
with open(var_functions.query_db_36, 'r') as f:
    mit_packages = json.load(f)

# Load package-version mappings (from query_db:48)
with open(var_functions.query_db_48, 'r') as f:
    pkg_versions = json.load(f)

# Load project info (from query_db:26)
with open(var_functions.query_db_26, 'r') as f:
    project_info = json.load(f)

print(f"MIT packages: {len(mit_packages)}")
print(f"Package versions: {len(pkg_versions)}")
print(f"Project info records: {len(project_info)}")

# Create key set for MIT packages
mit_keys = set((p['System'], p['Name'], p['Version']) for p in mit_packages)

# Filter package versions to only include MIT release packages
filtered_versions = [
    v for v in pkg_versions
    if (v['System'], v['Name'], v['Version']) in mit_keys
]

print(f"Filtered package versions: {len(filtered_versions)}")

# Extract fork counts from project info
project_forks = {}
for proj in project_info:
    info = proj.get('Project_Information', '')
    if not info:
        continue
    
    # Get repo name
    repo_match = re.search(r'The project ([^ ]+) on GitHub', info)
    if not repo_match:
        continue
    repo = repo_match.group(1)
    
    # Get fork count
    fork_match = re.search(r'forks count of (\d+)', info)
    if fork_match:
        forks = int(fork_match.group(1))
    else:
        fork_match = re.search(r'and (\d+) forks', info)
        forks = int(fork_match.group(1)) if fork_match else 0
    
    project_forks[repo] = forks

print(f"Projects with fork data: {len(project_forks)}")
print(f"Max forks: {max(project_forks.values() if project_forks else [0])}")

# Merge and get top packages
results = []
for v in filtered_versions:
    proj_name = v.get('ProjectName')
    if proj_name in project_forks and project_forks[proj_name] > 0:
        results.append({
            'project_name': proj_name,
            'package_name': v['Name'],
            'package_version': v['Version'],
            'forks': project_forks[proj_name]
        })

# Sort by fork count and get top 5
results.sort(key=lambda x: x['forks'], reverse=True)
top_5 = results[:5]

print(f"\nTop 5 packages by GitHub fork count:")
for i, pkg in enumerate(top_5, 1):
    print(f"{i}. {pkg['project_name']} - {pkg['forks']} forks")

print('__RESULT__:')
print(json.dumps(top_5, indent=2))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:2': ['project_info', 'project_packageversion'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.10', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dlcs/ng', 'Version': '1.0.0', 'ProjectType': 'GITHUB', 'ProjectName': 'winup/dlcs-ng', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dms/cli', 'Version': '1.0.1', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-cli', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dms/cli', 'Version': '1.0.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-cli', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:13': 'file_storage/functions.query_db:13.json', 'var_functions.query_db:12': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.'}, {'Project_Information': 'The project is hosted on GitHub under the name learnfrontend-dc/product-cart, and it currently has 2 open issues. It has garnered a total of 11 stars and has been forked 12 times.'}, {'Project_Information': 'The GitHub project ledgerproject/keypairoom currently has 3 open issues, 3 stars, and 0 forks.'}, {'Project_Information': 'The project leebyron/jasmine-check is hosted on GitHub and currently has 0 open issues, 11 stars, and 3 forks.'}, {'Project_Information': 'The project leebyron/testcheck-js on GitHub has an open issues count of 29, a stars count of 1185, and a forks count of 58, making it a notable repository in the community.'}, {'Project_Information': 'The project leecade/react-native-swiper is hosted on GitHub and has a total of 786 open issues, along with an impressive 10,249 stars and 2,392 forks, making it a popular choice among developers for implementing swiping functionality in React Native applications.'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json'}

exec(code, env_args)
