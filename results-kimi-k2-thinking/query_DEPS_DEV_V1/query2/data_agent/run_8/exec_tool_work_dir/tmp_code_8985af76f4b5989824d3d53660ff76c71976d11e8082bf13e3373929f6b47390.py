code = """import json
import pandas as pd

# Read the package query result
packages = var_functions.query_db:2

# Parse the JSON strings to extract MIT licenses and release status
mit_packages = []
for pkg in packages:
    try:
        # Parse licenses
        licenses = json.loads(pkg['Licenses'])
        # Parse version info
        version_info = json.loads(pkg['VersionInfo'])
        
        # Check if it's NPM, MIT license, and a release
        if (pkg['System'] == 'NPM' and 
            'MIT' in licenses and 
            version_info.get('IsRelease', False)):
            mit_packages.append({
                'System': pkg['System'],
                'Name': pkg['Name'],
                'Version': pkg['Version'],
                'Licenses': licenses
            })
    except:
        continue

print('__RESULT__:')
print(json.dumps(mit_packages, indent=2))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.query_db:2': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'Licenses': '[\n  "ISC"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}]}

exec(code, env_args)
