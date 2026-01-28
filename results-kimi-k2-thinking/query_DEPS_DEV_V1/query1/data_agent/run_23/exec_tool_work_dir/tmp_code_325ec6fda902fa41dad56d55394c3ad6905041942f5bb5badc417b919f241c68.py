code = """import json, pandas as pd, re, sys

# Load data
with open(var_functions.query_db:16, 'r') as f:
    packages = json.load(f)

with open(var_functions.query_db:26, 'r') as f:
    mappings = json.load(f)

with open(var_functions.query_db:28, 'r') as f:
    projects = json.load(f)

# Create DataFrames
pkg_df = pd.DataFrame(packages)
map_df = pd.DataFrame(mappings)
proj_df = pd.DataFrame(projects)

# Parse VersionInfo
version_info = []
for item in pkg_df['VersionInfo']:
    try:
        v = json.loads(item)
    except:
        v = {}
    version_info.append(v)

version_df = pd.DataFrame(version_info)
pkg_df = pd.concat([pkg_df, version_df], axis=1)

# Filter release versions
releases = pkg_df[pkg_df['IsRelease'] == True]

# Get latest version for each package
latest = releases.loc[releases.groupby('Name')['Ordinal'].idxmax()]

# Merge with mappings
merged = pd.merge(latest, map_df[['Name', 'Version', 'ProjectName']], 
                 on=['Name', 'Version'], how='inner')

# Extract stars from project info
proj_df['Stars'] = proj_df['Project_Information'].apply(
    lambda x: int(re.search(r'(\d+|[\d,]+)\s+stars', x).group(1).replace(',','')) 
    if pd.notna(x) and re.search(r'(\d+|[\d,]+)\s+stars', x) else 0
)

# Create mapping from ProjectName to Stars
proj_dict = {}
for _, row in proj_df.iterrows():
    if pd.notna(row['Project_Information']):
        # Extract project name from the description
        match = re.search(r'project\s+([\w-]+/[\w-]+)', row['Project_Information'])
        if match:
            proj_dict[match.group(1)] = row['Stars']

# Add stars to merged
merged['Stars'] = merged['ProjectName'].apply(lambda x: proj_dict.get(x, 0))

# Get top 5
top5 = merged.sort_values('Stars', ascending=False).head(5)

# Prepare result
result = top5[['Name', 'Version', 'Stars']].to_dict('records')

# Print result in required format
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:2': ['project_info', 'project_packageversion'], 'var_functions.query_db:5': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'UpstreamPublishedAt': '1699345351000000.0'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}', 'UpstreamPublishedAt': '1670271173000000.0'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}', 'UpstreamPublishedAt': '1654791421000000.0'}, {'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}', 'UpstreamPublishedAt': '1624260093000000.0'}, {'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}', 'UpstreamPublishedAt': '1656518476000000.0'}, {'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}', 'UpstreamPublishedAt': '1651424462000000.0'}, {'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}', 'UpstreamPublishedAt': '1649368661000000.0'}, {'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}', 'UpstreamPublishedAt': '1649368661000000.0'}, {'Name': '@edgedev/firebase', 'Version': '1.0.12', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}', 'UpstreamPublishedAt': '1666049703000000.0'}, {'Name': '@eden-network/data', 'Version': '1.0.9-sev.5', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 14\n}', 'UpstreamPublishedAt': '1637610934000000.0'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:14': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:22': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_functions.query_db:24': [{'System': 'NPM', 'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1-436430db4', 'ProjectType': 'GITHUB', 'ProjectName': 'leaflet/leaflet', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE', 'ProjectName_1': 'leaflet/leaflet'}, {'System': 'NPM', 'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1-build-81dc2489', 'ProjectType': 'GITHUB', 'ProjectName': 'leaflet/leaflet', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE', 'ProjectName_1': 'leaflet/leaflet'}, {'System': 'NPM', 'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1-build', 'ProjectType': 'GITHUB', 'ProjectName': 'leaflet/leaflet', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE', 'ProjectName_1': 'leaflet/leaflet'}, {'System': 'NPM', 'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1-build-81dc24892a3f', 'ProjectType': 'GITHUB', 'ProjectName': 'leaflet/leaflet', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE', 'ProjectName_1': 'leaflet/leaflet'}, {'System': 'NPM', 'Name': '@easyv/leaflet.markercluster', 'Version': '1.5.4', 'ProjectType': 'GITHUB', 'ProjectName': 'leaflet/leaflet.markercluster', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE', 'ProjectName_1': 'leaflet/leaflet.markercluster'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}]}

exec(code, env_args)
