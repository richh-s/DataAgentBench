code = """import json
import pandas as pd

# Get the file path from storage using the key as a string
storage_key = 'var_functions.query_db:2'
file_path = locals()[storage_key]

# Read the package data from the file
with open(file_path, 'r') as f:
    package_data = json.load(f)

# Convert to DataFrame
df_packages = pd.DataFrame(package_data)

# Filter for MIT license and release versions
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

# Get unique packages (by name)
unique_packages = {}
for pkg in mit_release_packages:
    unique_packages[pkg['Name']] = pkg

unique_package_list = list(unique_packages.values())

print('__RESULT__:')
print(json.dumps({
    'total_mit_release_packages': len(mit_release_packages),
    'unique_packages': len(unique_package_list),
    'sample_packages': unique_package_list[:10]
}))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
