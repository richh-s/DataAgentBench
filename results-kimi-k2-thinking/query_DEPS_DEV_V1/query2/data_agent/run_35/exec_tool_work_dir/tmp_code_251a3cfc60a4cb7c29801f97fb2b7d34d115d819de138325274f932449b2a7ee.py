code = """import json

# Load full package data
packages_file = var_functions.query_db:0
with open(packages_file, 'r') as f:
    packages = json.load(f)

# Filter for NPM packages with MIT license and marked as release
mit_release_packages = []

for pkg in packages:
    # Check if it's NPM
    if pkg.get('System') != 'NPM':
        continue
    
    # Check MIT license
    licenses_str = pkg.get('Licenses', '[]')
    has_mit = 'MIT' in licenses_str
    
    # Check if it's a release
    version_info_str = pkg.get('VersionInfo', '{}')
    try:
        # Parse JSON-like string
        import ast
        version_info = ast.literal_eval(version_info_str)
        is_release = version_info.get('IsRelease', False) if isinstance(version_info, dict) else False
    except:
        is_release = False
    
    if has_mit and is_release:
        mit_release_packages.append({
            'System': pkg['System'],
            'Name': pkg['Name'],
            'Version': pkg['Version']
        })

print('__RESULT__:')
print(json.dumps({
    "total_packages": len(packages),
    "mit_release_packages": len(mit_release_packages),
    "sample_packages": mit_release_packages[:5]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:7': {'packages_count': 100, 'projects_count': 100}}

exec(code, env_args)
