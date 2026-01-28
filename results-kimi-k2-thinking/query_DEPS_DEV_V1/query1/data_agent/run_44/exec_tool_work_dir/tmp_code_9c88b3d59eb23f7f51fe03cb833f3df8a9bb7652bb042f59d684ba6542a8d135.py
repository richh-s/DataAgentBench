code = """# Load and process NPM package data
import json
import pandas as pd

# Get the filepath from storage
filepath = locals()['var_functions.query_db:14']

# Read the package data
with open(filepath, 'r') as f:
    package_data = json.load(f)

# Create DataFrame
pkg_df = pd.DataFrame(package_data)

# Parse VersionInfo JSON to extract IsRelease and Ordinal
def parse_version_info(vinfo):
    try:
        # Remove newlines and parse JSON
        vinfo_clean = vinfo.replace('\n', ' ').strip()
        return json.loads(vinfo_clean)
    except:
        return {'IsRelease': False, 'Ordinal': 0}

# Extract IsRelease and Ordinal
version_parsed = pkg_df['VersionInfo'].apply(parse_version_info)
pkg_df['IsRelease'] = version_parsed.apply(lambda x: x.get('IsRelease', False))
pkg_df['Ordinal'] = version_parsed.apply(lambda x: x.get('Ordinal', 0))

# Filter for release versions only
release_df = pkg_df[pkg_df['IsRelease'] == True]

# Group by package name and find the release with max ordinal (latest version)
latest_releases = release_df.loc[release_df.groupby('Name')['Ordinal'].idxmax()]

# Keep only relevant columns
latest_releases = latest_releases[['System', 'Name', 'Version', 'Ordinal']]

print(f"Total unique NPM packages with releases: {latest_releases.shape[0]}")
print(json.dumps(latest_releases.head(5).to_dict('records'), indent=2))

print("__RESULT__:")
print(latest_releases.to_json(orient='records'))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:2': ['project_info', 'project_packageversion'], 'var_functions.query_db:5': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:12': {'total_records': 661372, 'first_record': {'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectName': 'dataminingsupply/dms-io'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectName': 'isacvale/fc'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectName': 'laihaojie/jie'}]}

exec(code, env_args)
