code = """import json
import pandas as pd
import re

# Load MIT release packages from the file path stored in query_db:24
with open(var_functions.query_db_24, 'r') as f:
    mit_packages = json.load(f)

# Load project_packageversion mappings from the file path stored in query_db:20
with open(var_functions.query_db_20, 'r') as f:
    pkg_versions = json.load(f)

# Load project_info from the file path stored in query_db:26
with open(var_functions.query_db_26, 'r') as f:
    project_info = json.load(f)

print(f"Loaded {len(mit_packages)} MIT release packages")
print(f"Loaded {len(pkg_versions)} package-version mappings")
print(f"Loaded {len(project_info)} project info records")

# Preview data
print("\nSample MIT package:")
print(mit_packages[0] if mit_packages else "No packages")

print("\nSample project_packageversion:")
print(pkg_versions[0] if pkg_versions else "No mappings")

print("\nSample project_info:")
print(project_info[0] if project_info else "No project info")

# Create DataFrames
df_packages = pd.DataFrame(mit_packages)
df_pkg_versions = pd.DataFrame(pkg_versions)
df_projects = pd.DataFrame(project_info)

print(f"\nDataFrame shapes:")
print(f"Packages: {df_packages.shape}")
print(f"Package versions: {df_pkg_versions.shape}")
print(f"Projects: {df_projects.shape}")

# Extract repository name from Project_Information

def extract_repo_name(proj_info):
    if not proj_info or pd.isna(proj_info):
        return None
    match = re.search(r'The project ([^ ]+) on GitHub', proj_info)
    return match.group(1) if match else None

def extract_forks(proj_info):
    if not proj_info or pd.isna(proj_info):
        return None
    match = re.search(r'forks count of (\d+)', proj_info)
    if match:
        return int(match.group(1))
    match = re.search(r'and (\d+) forks', proj_info)
    if match:
        return int(match.group(1))
    return 0

df_projects['repo_name'] = df_projects['Project_Information'].apply(extract_repo_name)
df_projects['forks'] = df_projects['Project_Information'].apply(extract_forks)

print(f"\nProjects with extracted data: {df_projects['repo_name'].notna().sum()}")
print(f"Max forks found: {df_projects['forks'].max()}")

# Now join packages with their GitHub projects
print(f"\nJoining packages with projects...")
print("Available package columns:", df_packages.columns.tolist())
print("Available pkg_versions columns:", df_pkg_versions.columns.tolist())
print("Available projects columns:", df_projects.columns.tolist())"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:2': ['project_info', 'project_packageversion'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.10', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dlcs/ng', 'Version': '1.0.0', 'ProjectType': 'GITHUB', 'ProjectName': 'winup/dlcs-ng', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dms/cli', 'Version': '1.0.1', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-cli', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dms/cli', 'Version': '1.0.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-cli', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:13': 'file_storage/functions.query_db:13.json', 'var_functions.query_db:12': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.'}, {'Project_Information': 'The project is hosted on GitHub under the name learnfrontend-dc/product-cart, and it currently has 2 open issues. It has garnered a total of 11 stars and has been forked 12 times.'}, {'Project_Information': 'The GitHub project ledgerproject/keypairoom currently has 3 open issues, 3 stars, and 0 forks.'}, {'Project_Information': 'The project leebyron/jasmine-check is hosted on GitHub and currently has 0 open issues, 11 stars, and 3 forks.'}, {'Project_Information': 'The project leebyron/testcheck-js on GitHub has an open issues count of 29, a stars count of 1185, and a forks count of 58, making it a notable repository in the community.'}, {'Project_Information': 'The project leecade/react-native-swiper is hosted on GitHub and has a total of 786 open issues, along with an impressive 10,249 stars and 2,392 forks, making it a popular choice among developers for implementing swiping functionality in React Native applications.'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
