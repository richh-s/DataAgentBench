code = """import json
import pandas as pd
import re

# File paths from previous queries
package_file_path = locals()['var_functions.query_db:24']
project_pv_file_path = locals()['var_functions.query_db:12']
project_info_file_path = locals()['var_functions.query_db:22']

# Load data
print("Loading package data...")
with open(package_file_path, 'r') as f:
    package_data = json.load(f)

print("Loading project package version data...")
with open(project_pv_file_path, 'r') as f:
    project_pv_data = json.load(f)

print("Loading project info data...")
with open(project_info_file_path, 'r') as f:
    project_info_data = json.load(f)

print(f"Total packages: {len(package_data)}")
print(f"Total project package versions: {len(project_pv_data)}")
print(f"Total project info records: {len(project_info_data)}")

# Process package data to get latest release version for each package
latest_packages = {}
for pkg in package_data:
    try:
        version_info = json.loads(pkg['VersionInfo'])
        if version_info.get('IsRelease', False):
            name = pkg['Name']
            ordinal = version_info.get('Ordinal', 0)
            if name not in latest_packages or ordinal > latest_packages[name]['Ordinal']:
                latest_packages[name] = {
                    'Name': name,
                    'Version': pkg['Version'],
                    'Ordinal': ordinal
                }
    except:
        continue

latest_package_list = list(latest_packages.values())
print(f"Latest release packages: {len(latest_package_list)}")

# Create DataFrames
package_df = pd.DataFrame(latest_package_list)
project_pv_df = pd.DataFrame(project_pv_data)

# Filter project_pv for NPM packages and join with packages
project_pv_npm_df = project_pv_df[project_pv_df['System'] == 'NPM']
print(f"NPM project package versions: {len(project_pv_npm_df)}")

# Join packages with project_packageversion
joined_df = pd.merge(
    package_df, 
    project_pv_npm_df, 
    on=['Name', 'Version'], 
    how='inner'
)

print(f"Joined records: {len(joined_df)}")

# Extract stars from Project_Information
def extract_stars(project_info_text):
    if not project_info_text:
        return 0
    # Look for patterns like "X stars" or "X,XXX stars"
    match = re.search(r'(\d+,?\d*)\s+stars?', str(project_info_text))
    if match:
        stars_str = match.group(1).replace(',', '')
        try:
            return int(stars_str)
        except:
            return 0
    return 0

# Create project info mapping
project_info_df = pd.DataFrame(project_info_data)
project_info_df['ProjectName'] = project_info_df['Project_Information'].apply(
    lambda x: re.search(r'project\s+([^\s]+)', str(x), re.IGNORECASE).group(1) if re.search(r'project\s+([^\s]+)', str(x), re.IGNORECASE) else None
)
project_info_df['Stars'] = project_info_df['Project_Information'].apply(extract_stars)

print(f"Project info records with stars: {len(project_info_df)}")

# Join with project info
final_df = pd.merge(
    joined_df,
    project_info_df[['ProjectName', 'Stars']],
    on='ProjectName',
    how='inner'
)

print(f"Final joined records: {len(final_df)}")

# Sort by stars and get top 5
top_5 = final_df.nlargest(5, 'Stars')[['Name', 'Version', 'ProjectName', 'Stars']]

result = top_5.to_dict('records')
print("__RESULT__:")
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.query_db:2': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'Name': '@edgedev/firebase', 'Version': '1.0.12', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}'}, {'Name': '@eden-network/data', 'Version': '1.0.9-sev.5', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 14\n}'}], 'var_functions.list_db:5': ['project_info', 'project_packageversion'], 'var_functions.query_db:6': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}], 'var_functions.query_db:8': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectName': 'dataminingsupply/dms-io'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectName': 'isacvale/fc'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.10', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.17', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@dlcs/ng', 'Version': '1.0.0', 'ProjectName': 'winup/dlcs-ng'}, {'System': 'NPM', 'Name': '@dms/cli', 'Version': '1.0.1', 'ProjectName': 'dataminingsupply/dms-cli'}, {'System': 'NPM', 'Name': '@dms/cli', 'Version': '1.0.0', 'ProjectName': 'dataminingsupply/dms-cli'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:18': {'total_packages': 661372, 'release_packages': 337844, 'project_pv_count': 597602}, 'var_functions.execute_python:20': {'total_latest_release_packages': 15811, 'sample': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Ordinal': 29}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.2.2', 'Ordinal': 25}, {'Name': '@discue/ui-components', 'Version': '0.38.2', 'Ordinal': 45}, {'Name': '@dvcol/web-extension-utils', 'Version': '2.3.4', 'Ordinal': 27}, {'Name': '@edgedev/firebase', 'Version': '2.0.20', 'Ordinal': 133}]}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
