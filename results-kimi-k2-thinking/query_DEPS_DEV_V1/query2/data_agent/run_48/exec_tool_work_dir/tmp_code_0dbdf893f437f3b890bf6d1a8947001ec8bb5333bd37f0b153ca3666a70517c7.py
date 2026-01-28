code = """import json
import re

# Load MIT release packages
packages_file = locals().get('var_functions.query_db:20')
if isinstance(packages_file, str) and packages_file.endswith('.json'):
    with open(packages_file, 'r') as f:
        all_packages = json.load(f)
else:
    all_packages = packages_file

# Deduplicate packages
unique_packages = {}
for pkg in all_packages:
    key = (pkg['Name'], pkg['Version'])
    if key not in unique_packages:
        unique_packages[key] = pkg

# Load project mappings
proj_file = locals().get('var_functions.query_db:28')
if isinstance(proj_file, str) and proj_file.endswith('.json'):
    with open(proj_file, 'r') as f:
        project_mappings = json.load(f)
else:
    project_mappings = proj_file

# Create project lookup
project_lookup = {}
for mapping in project_mappings:
    key = (mapping['Name'], mapping['Version'])
    project_lookup[key] = mapping['ProjectName']

# Find matching projects
matched_projects = {}
for pkg in unique_packages.values():
    key = (pkg['Name'], pkg['Version'])
    if key in project_lookup:
        project_name = project_lookup[key]
        if project_name not in matched_projects:
            matched_projects[project_name] = pkg['Name']

# Get project info for these projects
project_names = list(matched_projects.keys())
print('__RESULT__:')
print(json.dumps({
    'total_mit_packages': len(all_packages),
    'unique_mit_packages': len(unique_packages),
    'project_mappings_count': len(project_mappings),
    'matched_projects': len(matched_projects),
    'project_names_sample': project_names[:10]
}))"""

env_args = {'var_functions.query_db:0': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'Licenses': '[\n  "ISC"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'count': 32, 'sample': [{'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]'}, {'System': 'NPM', 'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'Licenses': '[\n  "MIT"\n]'}, {'System': 'NPM', 'Name': '@eclipsejs/cli', 'Version': '1.0.0', 'Licenses': '[\n  "MIT"\n]'}, {'System': 'NPM', 'Name': '@ebot7/edem-react', 'Version': '0.18.8', 'Licenses': '[\n  "MIT"\n]'}, {'System': 'NPM', 'Name': '@e4a/irmaseal-wasm-bindings', 'Version': '0.0.1', 'Licenses': '[\n  "MIT"\n]'}]}, 'var_functions.list_db:8': ['project_info', 'project_packageversion'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:14': {'packages_count': 100, 'project_versions_count': 5000, 'packages_sample': [{'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'System': 'NPM', 'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}], 'project_versions_sample': [{'System': 'NPM', 'Name': '@discordx/music', 'Version': '4.0.0-dev.1637888858.e2b75b9', 'ProjectName': 'oceanroleplay/discord.ts'}, {'System': 'NPM', 'Name': '@discordx/music', 'Version': '4.0.0-dev.1637888858.e2b75b9', 'ProjectName': 'oceanroleplay/discord.ts'}, {'System': 'NPM', 'Name': '@discordx/music', 'Version': '4.0.0-dev.1638102812.c236d4d', 'ProjectName': 'oceanroleplay/discord.ts'}]}, 'var_functions.execute_python:18': {'mit_release_packages': 32, 'matched_packages': 1, 'unique_projects': 1}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:26': {'packages_count': 176998, 'project_versions_count': 5000, 'sample_packages': [{'System': 'NPM', 'Name': '@discordx/utilities', 'Version': '1.0.0'}, {'System': 'NPM', 'Name': '@discordx/utilities', 'Version': '1.0.0'}], 'sample_project_versions': [{'System': 'NPM', 'Name': '@discordx/music', 'Version': '4.0.0-dev.1637888858.e2b75b9', 'ProjectName': 'oceanroleplay/discord.ts'}, {'System': 'NPM', 'Name': '@discordx/music', 'Version': '4.0.0-dev.1637888858.e2b75b9', 'ProjectName': 'oceanroleplay/discord.ts'}]}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
