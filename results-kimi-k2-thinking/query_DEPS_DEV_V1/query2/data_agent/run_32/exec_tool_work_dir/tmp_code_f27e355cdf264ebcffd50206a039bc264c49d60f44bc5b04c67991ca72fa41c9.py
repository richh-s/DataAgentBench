code = """import json
import pandas as pd

# Load the package data from the file
package_data_file = locals()['var_functions.query_db:2']
with open(package_data_file, 'r') as f:
    package_data = json.load(f)

# Filter for release versions
def is_release(version_info_str):
    try:
        version_info = json.loads(version_info_str)
        return version_info.get('IsRelease', False)
    except:
        return False

release_packages = [
    pkg for pkg in package_data 
    if is_release(pkg['VersionInfo'])
]

print('__RESULT__:')
print(json.dumps(release_packages[:100]))  # Just preview first 100 to check"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
