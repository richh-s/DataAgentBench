code = """import json
import re

# Read the files directly with the stored paths
mit_packages_file = '/tmp/tmpnvj8luz8.json'  # This should be the actual path from var_functions.query_db:20
project_mappings_file = '/tmp/tmp9mvyg0f1.json'  # From var_functions.query_db:28
project_info_file = '/tmp/tmp8s2g8h3j.json'  # From var_functions.query_db:34

# Load MIT packages
with open(mit_packages_file, 'r') as f:
    all_mit_packages = json.load(f)

print(f"Loaded {len(all_mit_packages)} MIT packages")
print("Sample:", all_mit_packages[0])

# Deduplicate packages by (Name, Version)
unique_packages = {}
for pkg in all_mit_packages:
    key = (pkg['Name'], pkg['Version'])
    if key not in unique_packages:
        unique_packages[key] = pkg

print(f"Unique MIT packages: {len(unique_packages)}")"""

env_args = {'var_functions.query_db:0': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'Licenses': '[\n  "ISC"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'count': 32, 'sample': [{'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]'}, {'System': 'NPM', 'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'Licenses': '[\n  "MIT"\n]'}, {'System': 'NPM', 'Name': '@eclipsejs/cli', 'Version': '1.0.0', 'Licenses': '[\n  "MIT"\n]'}, {'System': 'NPM', 'Name': '@ebot7/edem-react', 'Version': '0.18.8', 'Licenses': '[\n  "MIT"\n]'}, {'System': 'NPM', 'Name': '@e4a/irmaseal-wasm-bindings', 'Version': '0.0.1', 'Licenses': '[\n  "MIT"\n]'}]}, 'var_functions.list_db:8': ['project_info', 'project_packageversion'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:14': {'packages_count': 100, 'project_versions_count': 5000, 'packages_sample': [{'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'System': 'NPM', 'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}], 'project_versions_sample': [{'System': 'NPM', 'Name': '@discordx/music', 'Version': '4.0.0-dev.1637888858.e2b75b9', 'ProjectName': 'oceanroleplay/discord.ts'}, {'System': 'NPM', 'Name': '@discordx/music', 'Version': '4.0.0-dev.1637888858.e2b75b9', 'ProjectName': 'oceanroleplay/discord.ts'}, {'System': 'NPM', 'Name': '@discordx/music', 'Version': '4.0.0-dev.1638102812.c236d4d', 'ProjectName': 'oceanroleplay/discord.ts'}]}, 'var_functions.execute_python:18': {'mit_release_packages': 32, 'matched_packages': 1, 'unique_projects': 1}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:26': {'packages_count': 176998, 'project_versions_count': 5000, 'sample_packages': [{'System': 'NPM', 'Name': '@discordx/utilities', 'Version': '1.0.0'}, {'System': 'NPM', 'Name': '@discordx/utilities', 'Version': '1.0.0'}], 'sample_project_versions': [{'System': 'NPM', 'Name': '@discordx/music', 'Version': '4.0.0-dev.1637888858.e2b75b9', 'ProjectName': 'oceanroleplay/discord.ts'}, {'System': 'NPM', 'Name': '@discordx/music', 'Version': '4.0.0-dev.1637888858.e2b75b9', 'ProjectName': 'oceanroleplay/discord.ts'}]}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:32': {'total_mit_packages': 176998, 'unique_mit_packages': 85158, 'project_mappings_count': 597602, 'matched_projects': 5423, 'project_names_sample': ['oceanroleplay/discord.ts', 'vuejs/vueify', 'discourse/moment-timezone-names-translations', 'moonshotcollective/scaffold-moonshot-starter', 'discovery-solutions/json-connection', 'discovery-solutions/react-flatlist', 'discovery-solutions/react-modal', 'discovery-solutions/react-router', 'discovery-solutions/react-store', 'discovery-solutions/utils']}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:36': {'message': 'Starting analysis', 'matched_projects_count': 5423, 'sample_projects': ['oceanroleplay/discord.ts', 'vuejs/vueify', 'discourse/moment-timezone-names-translations', 'moonshotcollective/scaffold-moonshot-starter', 'discovery-solutions/json-connection']}}

exec(code, env_args)
