code = """import pandas as pd
import json
import re
from pathlib import Path

# Read data from files
packageinfo_path = var_functions.query_db:16
mapping_path = var_functions.query_db:26
projectinfo_path = var_functions.query_db:28

with open(packageinfo_path, 'r') as f:
    packages = json.load(f)

with open(mapping_path, 'r') as f:
    mappings = json.load(f)

with open(projectinfo_path, 'r') as f:
    projects = json.load(f)

# Create DataFrames
packages_df = pd.DataFrame(packages)
mappings_df = pd.DataFrame(mappings)
projects_df = pd.DataFrame(projects)

# Extract version info
version_info = []
for item in packages_df['VersionInfo']:
    try:
        parsed = json.loads(item)
    except:
        parsed = {}
    version_info.append(parsed)

version_df = pd.DataFrame(version_info)
packages_df = pd.concat([packages_df, version_df], axis=1)

# Filter release versions
release_packages = packages_df[packages_df['IsRelease'] == True]

# Find latest version per package (max Ordinal)
idx = release_packages.groupby('Name')['Ordinal'].idxmax()
latest_packages = release_packages.loc[idx].reset_index(drop=True)

# Merge with mappings to get ProjectName
merged = pd.merge(latest_packages, mappings_df[['Name', 'Version', 'ProjectName']], 
                 on=['Name', 'Version'], how='inner')

# Create a mapping dict from ProjectName to Project_Information for fast lookup
project_info_dict = dict(zip(projects_df['Project_Information'], projects_df['Project_Information']))

# Actually, let's re-read the projects to see all columns
print('Projects columns:', projects_df.columns.tolist())
print('Mappings columns:', mappings_df.columns.tolist())
print('Packages columns:', packages_df.columns.tolist())

print('First few projects:')
print(projects_df.head())

print('First few mappings:')
print(mappings_df.head())

print('Number of latest packages:', len(latest_packages))
print('Number of merged packages:', len(merged))
print('Sample merged:')
print(merged[['Name', 'Version', 'ProjectName']].head())"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:2': ['project_info', 'project_packageversion'], 'var_functions.query_db:5': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'UpstreamPublishedAt': '1699345351000000.0'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}', 'UpstreamPublishedAt': '1670271173000000.0'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}', 'UpstreamPublishedAt': '1654791421000000.0'}, {'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}', 'UpstreamPublishedAt': '1624260093000000.0'}, {'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}', 'UpstreamPublishedAt': '1656518476000000.0'}, {'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}', 'UpstreamPublishedAt': '1651424462000000.0'}, {'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}', 'UpstreamPublishedAt': '1649368661000000.0'}, {'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}', 'UpstreamPublishedAt': '1649368661000000.0'}, {'Name': '@edgedev/firebase', 'Version': '1.0.12', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}', 'UpstreamPublishedAt': '1666049703000000.0'}, {'Name': '@eden-network/data', 'Version': '1.0.9-sev.5', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 14\n}', 'UpstreamPublishedAt': '1637610934000000.0'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:14': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:22': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_functions.query_db:24': [{'System': 'NPM', 'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1-436430db4', 'ProjectType': 'GITHUB', 'ProjectName': 'leaflet/leaflet', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE', 'ProjectName_1': 'leaflet/leaflet'}, {'System': 'NPM', 'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1-build-81dc2489', 'ProjectType': 'GITHUB', 'ProjectName': 'leaflet/leaflet', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE', 'ProjectName_1': 'leaflet/leaflet'}, {'System': 'NPM', 'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1-build', 'ProjectType': 'GITHUB', 'ProjectName': 'leaflet/leaflet', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE', 'ProjectName_1': 'leaflet/leaflet'}, {'System': 'NPM', 'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1-build-81dc24892a3f', 'ProjectType': 'GITHUB', 'ProjectName': 'leaflet/leaflet', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE', 'ProjectName_1': 'leaflet/leaflet'}, {'System': 'NPM', 'Name': '@easyv/leaflet.markercluster', 'Version': '1.5.4', 'ProjectType': 'GITHUB', 'ProjectName': 'leaflet/leaflet.markercluster', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE', 'ProjectName_1': 'leaflet/leaflet.markercluster'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}]}

exec(code, env_args)
