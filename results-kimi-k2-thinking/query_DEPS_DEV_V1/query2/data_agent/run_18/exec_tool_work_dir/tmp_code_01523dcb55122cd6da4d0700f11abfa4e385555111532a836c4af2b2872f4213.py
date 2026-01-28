code = """import json

# Load both datasets
package_path = locals()['var_functions.query_db:0']
project_path = locals()['var_functions.query_db:9']

with open(package_path, 'r') as f:
    packages = json.load(f)

with open(project_path, 'r') as f:
    projects = json.load(f)

print('__RESULT__:')
print(json.dumps({
    'package_count': len(packages),
    'project_count': len(projects),
    'sample_package': packages[0],
    'sample_project': projects[0]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'count': 176998, 'first_3_records': [{'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'System': 'NPM', 'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'System': 'NPM', 'Name': '@eclipsejs/cli', 'Version': '1.0.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}'}]}, 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json'}

exec(code, env_args)
