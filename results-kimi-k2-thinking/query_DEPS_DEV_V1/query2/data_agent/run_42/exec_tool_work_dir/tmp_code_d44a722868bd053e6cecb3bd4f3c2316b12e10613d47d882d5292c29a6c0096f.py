code = """import json
import pandas as pd
import os

# Read the package data from the file
with open('var_functions.query_db:2', 'r') as f:
    package_data = json.load(f)

# Convert to DataFrame for easier processing
df_packages = pd.DataFrame(package_data)

# Filter for MIT license and release versions
# Parse VersionInfo JSON string to check IsRelease
mit_release_packages = []

for idx, row in df_packages.iterrows():
    try:
        # Parse Licenses
        licenses = json.loads(row['Licenses'])
        has_mit = 'MIT' in licenses
        
        # Parse VersionInfo
        version_info = json.loads(row['VersionInfo'])
        is_release = version_info.get('IsRelease', False)
        
        if has_mit and is_release:
            mit_release_packages.append({
                'System': row['System'],
                'Name': row['Name'],
                'Version': row['Version']
            })
    except:
        continue

result = mit_release_packages[:100]  # Return first 100 to avoid overwhelming
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
