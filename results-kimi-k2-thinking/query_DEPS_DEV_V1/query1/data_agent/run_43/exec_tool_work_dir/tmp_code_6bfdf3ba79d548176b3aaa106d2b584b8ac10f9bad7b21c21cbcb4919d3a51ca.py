code = """import json
import pandas as pd

# Read the query result from the file
with open(var_functions.query_db:4, 'r') as f:
    package_data = json.load(f)

print('__RESULT__:')
print(f"Total NPM package records: {len(package_data)}")
print(f"Sample record: {package_data[0] if package_data else 'No data'}")

# Let's see how many unique packages
unique_packages = set()
for row in package_data:
    unique_packages.add(row['Name'])
    
print(f"Unique packages: {len(unique_packages)}")

# Check VersionInfo structure
if package_data:
    try:
        vi = json.loads(package_data[0]['VersionInfo'])
        print(f"VersionInfo structure: {vi}")
    except:
        print("Failed to parse VersionInfo")
        print(f"VersionInfo raw: {package_data[0]['VersionInfo']}")"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:1': ['project_info', 'project_packageversion'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
