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
def parse_vinfo(vinfo_str):
    try:
        # Clean up the string
        vinfo_clean = vinfo_str.replace('\n', ' ').replace('\r', '').strip()
        parsed = json.loads(vinfo_clean)
        return pd.Series([parsed.get('IsRelease', False), parsed.get('Ordinal', 0)])
    except:
        return pd.Series([False, 0])

# Apply parsing
pkg_df[['IsRelease', 'Ordinal']] = pkg_df['VersionInfo'].apply(parse_vinfo)

# Filter for release versions
release_df = pkg_df[pkg_df['IsRelease'] == True].copy()

# Get latest release for each package (highest ordinal)
latest_idx = release_df.groupby('Name')['Ordinal'].idxmax()
latest_releases = release_df.loc[latest_idx]

# Keep only needed columns
result = latest_releases[['Name', 'Version']].copy()

print("Found", len(result), "unique NPM packages with release versions")
print("__RESULT__:")
import json as js
print(js.dumps(result.to_dict('records')))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:2': ['project_info', 'project_packageversion'], 'var_functions.query_db:5': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:12': {'total_records': 661372, 'first_record': {'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectName': 'dataminingsupply/dms-io'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectName': 'isacvale/fc'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectName': 'laihaojie/jie'}]}

exec(code, env_args)
