code = """import json

# Access the stored result
result_var = locals().get('var_functions.query_db:2')

# The result is a string file path, read it
with open(result_var, 'r') as f:
    packages = json.load(f)

# Filter for MIT license and IsRelease: true
mit_release_packages = []
for pkg in packages:
    # Check for MIT in Licenses
    if 'MIT' in pkg.get('Licenses', ''):
        # Check VersionInfo for IsRelease: true
        version_info_str = pkg.get('VersionInfo', '')
        if '"IsRelease": true' in version_info_str:
            mit_release_packages.append({
                'System': pkg['System'],
                'Name': pkg['Name'],
                'Version': pkg['Version'],
                'Licenses': pkg['Licenses']
            })

print('__RESULT__:')
print(json.dumps({
    'count': len(mit_release_packages),
    'sample': mit_release_packages[:5]
}))"""

env_args = {'var_functions.query_db:0': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'Licenses': '[\n  "ISC"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
