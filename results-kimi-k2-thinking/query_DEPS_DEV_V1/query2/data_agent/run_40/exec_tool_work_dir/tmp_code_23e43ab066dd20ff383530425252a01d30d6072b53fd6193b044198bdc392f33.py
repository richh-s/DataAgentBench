code = """import json
import re

# Read the query result from storage
result_key = 'var_functions.query_db:0'
result_file = locals()[result_key]

with open(result_file, 'r') as f:
    packages = json.load(f)

# Filter packages that are marked as release and have MIT license
release_packages = []
for pkg in packages:
    # Check if it's a release version
    version_info_str = pkg.get('VersionInfo', '')
    if 'IsRelease": true' in version_info_str:
        release_packages.append({
            'System': pkg['System'],
            'Name': pkg['Name'],
            'Version': pkg['Version'],
            'Licenses': pkg['Licenses']
        })

# Let's check how many release packages we have
print('__RESULT__:')
print(json.dumps({
    'total_packages': len(packages),
    'release_packages': len(release_packages),
    'sample_release_packages': release_packages[:5]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
