code = """# Load data using a simpler approach to avoid string issues
import json, os, pandas as pd
import sqlite3

# Read file paths
pkg_file = locals()['var_functions.query_db:14']
proj_file = locals()['var_functions.query_db:34']

# Load both datasets
with open(pkg_file, 'r') as f:
    packages = json.load(f)

with open(proj_file, 'r') as f:
    projects = json.load(f)

# Parse packages to get latest releases
latest_release = {}
for pkg in packages:
    try:
        # Parse VersionInfo manually
        vinfo = pkg['VersionInfo'].strip()
        # Handle the JSON format with newlines
        if '\n' in vinfo:
            vinfo = vinfo.replace('\n', ' ')
        parsed = json.loads(vinfo)
        
        if parsed.get('IsRelease', False):
            name = pkg['Name']
            ordinal = parsed.get('Ordinal', 0)
            if name not in latest_release or ordinal > latest_release[name]['ordinal']:
                latest_release[name] = {
                    'Name': name,
                    'Version': pkg['Version'],
                    'ordinal': ordinal
                }
    except:
        continue

# Convert to list
latest_packages = list(latest_release.values())
print("Found", len(latest_packages), "latest release packages")

# Analyze project mappings to see structure
proj_df = pd.DataFrame(projects)
print("Project mappings columns:", proj_df.columns.tolist())
print("Sample project mappings:")
print(proj_df.head(3).to_string())

# Check for GitHub projects
print("Unique project types:", proj_df['ProjectType'].unique() if 'ProjectType' in proj_df.columns else "No ProjectType")
print("GitHub projects count:", len(proj_df[proj_df['ProjectType'] == 'GITHUB']) if 'ProjectType' in proj_df.columns else 0)

result = {
    "unique_latest_packages": len(latest_packages),
    "project_mappings_shape": proj_df.shape
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:2': ['project_info', 'project_packageversion'], 'var_functions.query_db:5': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:12': {'total_records': 661372, 'first_record': {'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectName': 'dataminingsupply/dms-io'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectName': 'isacvale/fc'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectName': 'laihaojie/jie'}], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json'}

exec(code, env_args)
