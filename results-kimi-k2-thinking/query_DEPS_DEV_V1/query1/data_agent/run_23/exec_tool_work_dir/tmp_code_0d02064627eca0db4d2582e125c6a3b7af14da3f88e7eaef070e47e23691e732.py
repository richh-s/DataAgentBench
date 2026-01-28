code = """import json
import pandas as pd
import re

# Load packageinfo data (NPM packages)
packageinfo_path = var_functions.query_db:16
with open(packageinfo_path, 'r') as f:
    packageinfo_raw = json.load(f)

# Load project_packageversion mapping
mapping_path = var_functions.query_db:10
with open(mapping_path, 'r') as f:
    mapping_raw = json.load(f)

# Load project_info data
projectinfo_path = var_functions.query_db:14
with open(projectinfo_path, 'r') as f:
    projectinfo_raw = json.load(f)

# Convert to DataFrames
package_df = pd.DataFrame(packageinfo_raw)
mapping_df = pd.DataFrame(mapping_raw)
project_df = pd.DataFrame(projectinfo_raw)

# Debug: examine columns
print('package_df columns:', package_df.columns.tolist())
print('mapping_df columns:', mapping_df.columns.tolist())
print('project_df columns:', project_df.columns.tolist())

# Parse VersionInfo JSON strings in package_df
version_info = []
for val in package_df['VersionInfo']:
    try:
        parsed = json.loads(val)
    except Exception as e:
        # If parsing fails, set default
        parsed = {}
    version_info.append(parsed)
version_info_df = pd.DataFrame(version_info)
package_df = pd.concat([package_df, version_info_df], axis=1)

# Filter only release versions
release_df = package_df[package_df['IsRelease'] == True]

# Determine latest release per package (max Ordinal)
latest_df = release_df.loc[release_df.groupby('Name')['Ordinal'].idxmax()].reset_index(drop=True)

# Merge with mapping on Name and Version
merged = pd.merge(latest_df, mapping_df, on=['Name', 'Version'], how='inner')

# Merge with project info on ProjectName
merged = pd.merge(merged, project_df, on=['ProjectName'], how='left')

# Extract star count from Project_Information field using regex

def extract_stars(proj_info):
    if pd.isnull(proj_info):
        return 0
    match = re.search(r'(\d+|[\d,]+)\s+stars?', proj_info)
    if match:
        star_str = match.group(1).replace(',', '')
        try:
            return int(star_str)
        except:
            return 0
    return 0

merged['Stars'] = merged['Project_Information'].apply(extract_stars)

# Sort by Stars descending
top5 = merged.sort_values(by='Stars', ascending=False).head(5)

# Prepare output: Package Name, Version, Stars
result = top5[['Name', 'Version', 'Stars']].copy()
result['Stars'] = result['Stars'].astype(int)

# Convert to JSON string
result_json = result.to_json(orient='records')
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:2': ['project_info', 'project_packageversion'], 'var_functions.query_db:5': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'UpstreamPublishedAt': '1699345351000000.0'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}', 'UpstreamPublishedAt': '1670271173000000.0'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}', 'UpstreamPublishedAt': '1654791421000000.0'}, {'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}', 'UpstreamPublishedAt': '1624260093000000.0'}, {'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}', 'UpstreamPublishedAt': '1656518476000000.0'}, {'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}', 'UpstreamPublishedAt': '1651424462000000.0'}, {'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}', 'UpstreamPublishedAt': '1649368661000000.0'}, {'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}', 'UpstreamPublishedAt': '1649368661000000.0'}, {'Name': '@edgedev/firebase', 'Version': '1.0.12', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}', 'UpstreamPublishedAt': '1666049703000000.0'}, {'Name': '@eden-network/data', 'Version': '1.0.9-sev.5', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 14\n}', 'UpstreamPublishedAt': '1637610934000000.0'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:14': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
