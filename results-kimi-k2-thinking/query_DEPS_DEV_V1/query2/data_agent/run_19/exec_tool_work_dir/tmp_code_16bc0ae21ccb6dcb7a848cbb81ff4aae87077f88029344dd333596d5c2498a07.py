code = """import json

# Load the package data from the previous query
package_data = locals().get('var_functions.query_db:5')

# If it's a file path, read it
if isinstance(package_data, str) and package_data.endswith('.json'):
    with open(package_data, 'r') as f:
        import json as js
        package_data = js.load(f)

# Filter for MIT license and release versions
mit_release_packages = []
for pkg in package_data:
    # Check if it's NPM (we already filtered this)
    if pkg.get('System') != 'NPM':
        continue
    
    # Check MIT license
    licenses = pkg.get('Licenses', '')
    if 'MIT' not in licenses:
        continue
    
    # Check if it's a release version
    version_info = pkg.get('VersionInfo', '')
    if not version_info:
        continue
    
    try:
        # Parse the VersionInfo JSON string
        version_info_clean = version_info.replace('\n', '').strip()
        version_info_json = json.loads(version_info_clean)
        
        if version_info_json.get('IsRelease'):
            mit_release_packages.append({
                'System': pkg['System'],
                'Name': pkg['Name'],
                'Version': pkg['Version']
            })
    except:
        continue

print('__RESULT__:')
print(json.dumps(mit_release_packages[:10]))  # Print first 10 as preview
print(f"Total MIT release packages: {len(mit_release_packages)}")"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.query_db:2': [{'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'System': 'NPM', 'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'System': 'NPM', 'Name': '@eden-network/data', 'Version': '1.0.9-sev.5', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 14\n}'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
