code = """import json

# Load the package data
package_data_path = locals().get('var_functions.query_db:5')
package_data = []

if isinstance(package_data_path, str):
    with open(package_data_path, 'r') as f:
        package_data = json.load(f)
else:
    package_data = package_data_path

# Filter for NPM packages with MIT license and marked as release
mit_release_packages = []

for pkg in package_data:
    # Only NPM packages
    if pkg.get('System') != 'NPM':
        continue
    
    # Check for MIT license
    licenses_str = pkg.get('Licenses', '')
    if 'MIT' not in licenses_str:
        continue
    
    # Check VersionInfo for IsRelease = true
    version_info_str = pkg.get('VersionInfo', '')
    if not version_info_str:
        continue
    
    # Clean and parse VersionInfo JSON
    try:
        cleaned = version_info_str.replace('\n', '').strip()
        version_info = json.loads(cleaned)
        
        if version_info.get('IsRelease'):
            mit_release_packages.append({
                'System': pkg['System'],
                'Name': pkg['Name'],
                'Version': pkg['Version']
            })
    except:
        continue

result = {
    'count': len(mit_release_packages),
    'sample': mit_release_packages[:10]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.query_db:2': [{'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'System': 'NPM', 'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'System': 'NPM', 'Name': '@eden-network/data', 'Version': '1.0.9-sev.5', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 14\n}'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
