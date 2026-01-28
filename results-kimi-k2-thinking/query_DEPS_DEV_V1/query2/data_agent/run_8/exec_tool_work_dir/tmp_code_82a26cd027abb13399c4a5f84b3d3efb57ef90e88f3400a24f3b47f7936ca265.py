code = """import json
import pandas as pd

# Read the full result from the file
result_file = var_functions.query_db:8
with open(result_file, 'r') as f:
    packages = json.load(f)

# Filter for NPM packages with MIT license that are releases
mit_release_packages = []
for pkg in packages:
    try:
        # Parse licenses - it's a string that looks like JSON
        licenses_str = pkg['Licenses']
        if 'MIT' in licenses_str:
            # Parse version info
            version_info_str = pkg['VersionInfo']
            if '"IsRelease": true' in version_info_str:
                mit_release_packages.append({
                    'System': pkg['System'],
                    'Name': pkg['Name'],
                    'Version': pkg['Version']
                })
    except Exception as e:
        continue

print('__RESULT__:')
print(json.dumps({
    'count': len(mit_release_packages),
    'sample': mit_release_packages[:5]
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.query_db:2': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'Licenses': '[\n  "ISC"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_functions.list_db:6': ['project_info', 'project_packageversion'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
