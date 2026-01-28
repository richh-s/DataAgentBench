code = """# Load and analyze NPM package data to find latest releases for each npm package
import json
import pandas as pd

# Read the file path from storage
filepath = locals()['var_functions.query_db:14']

# Load the data
with open(filepath, 'r') as file:
    package_data = json.load(file)

# Convert to DataFrame
df_packages = pd.DataFrame(package_data)

# Function to parse VersionInfo
import json as json_module

def parse_version_info_string(vinfo):
    try:
        cleaned = vinfo.replace('\n', ' ').replace('\r', '').strip()
        parsed = json_module.loads(cleaned)
        return [parsed.get('IsRelease', False), parsed.get('Ordinal', 0)]
    except:
        return [False, 0]

# Extract IsRelease and Ordinal
temp_result = df_packages['VersionInfo'].apply(parse_version_info_string)
df_packages = df_packages.copy()
df_packages['IsRelease'] = [x[0] for x in temp_result]
df_packages['Ordinal'] = [x[1] for x in temp_result]

# Filter for release versions
release_versions = df_packages[df_packages['IsRelease'] == True]

# For each package (Name), get the version with highest Ordinal (latest release)
grouped = release_versions.groupby('Name')
latest_version_indices = grouped['Ordinal'].idxmax()
latest_releases = release_versions.loc[latest_version_indices]

# Prepare result with Name and Version
result_df = latest_releases[['Name', 'Version']].copy()

# Output results
print('__RESULT__:')
print(result_df.to_json(orient='records'))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:2': ['project_info', 'project_packageversion'], 'var_functions.query_db:5': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:12': {'total_records': 661372, 'first_record': {'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectName': 'dataminingsupply/dms-io'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectName': 'isacvale/fc'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectName': 'laihaojie/jie'}]}

exec(code, env_args)
