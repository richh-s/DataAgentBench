code = """# Access variables using locals() dictionary
import json

packages_path = locals()['var_functions.query_db:0']
with open(packages_path, 'r') as f:
    all_packages = json.load(f)

# Count and filter packages
npm_packages = [p for p in all_packages if p.get('System') == 'NPM']

# Extract MIT license packages that are releases
mit_release_packs = []
for p in npm_packages:
    licenses = p.get('Licenses', '')
    version_info = p.get('VersionInfo', '')
    
    has_mit = 'MIT' in licenses
    is_release = False
    if 'IsRelease' in version_info:
        try:
            # Parse the JSON-like string
            import ast
            vi = ast.literal_eval(version_info)
            is_release = vi.get('IsRelease', False)
        except:
            pass
    
    if has_mit and is_release:
        mit_release_packs.append(p)

result = {
    'total_packages': len(all_packages),
    'npm_packages': len(npm_packages),
    'mit_release_packages': len(mit_release_packs),
    'sample': mit_release_packs[:3]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:7': {'packages_count': 100, 'projects_count': 100}}

exec(code, env_args)
