code = """import json
import pandas as pd
import sqlite3

# Read package data from SQLite
with open('var_functions.query_db:0', 'r') as f:
    package_data = json.load(f)

# Read project package version mapping data
with open('var_functions.query_db:2', 'r') as f:
    ppv_data = json.load(f)

# Load data into DataFrames
packages_df = pd.DataFrame(package_data)
ppv_df = pd.DataFrame(ppv_data)

# Parse the Licenses and VersionInfo fields to filter
mit_release_packages = []

for idx, row in packages_df.iterrows():
    # Parse licenses
    try:
        licenses = json.loads(row['Licenses']) if row['Licenses'] else []
        if 'MIT' in licenses:
            # Parse VersionInfo
            version_info = json.loads(row['VersionInfo']) if row['VersionInfo'] else {}
            if version_info.get('IsRelease', False):
                mit_release_packages.append({
                    'System': row['System'],
                    'Name': row['Name'],
                    'Version': row['Version'],
                    'Licenses': row['Licenses']
                })
    except:
        # Skip rows with invalid JSON
        continue

print('__RESULT__:')
print(json.dumps(mit_release_packages[:10]))  # Print first 10 for preview"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
