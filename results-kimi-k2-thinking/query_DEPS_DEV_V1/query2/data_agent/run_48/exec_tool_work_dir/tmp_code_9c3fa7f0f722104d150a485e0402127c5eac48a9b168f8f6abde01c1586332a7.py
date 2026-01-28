code = """import json
import re

# Load MIT packages (all of them)
mit_file_path = locals().get('var_functions.query_db:20')
with open(mit_file_path, 'r') as f:
    mit_packages = json.load(f)

print(f"Total MIT packages: {len(mit_packages)}")

# Load project mappings (all of them)
proj_file_path = locals().get('var_functions.query_db:28')
with open(proj_file_path, 'r') as f:
    project_mappings = json.load(f)

print(f"Total project mappings: {len(project_mappings)}")

# Load all project info
info_file_path = locals().get('var_functions.query_db:34')
with open(info_file_path, 'r') as f:
    project_infos = json.load(f)

print(f"Total project infos: {len(project_infos)}")

# Deduplicate MIT packages
unique_mit_packages = {}
for pkg in mit_packages:
    key = (pkg['Name'], pkg['Version'])
    if key not in unique_mit_packages:
        unique_mit_packages[key] = pkg

print(f"Unique MIT packages: {len(unique_mit_packages)}")

# Create project lookup
project_lookup = {}
for mapping in project_mappings:
    key = (mapping['Name'], mapping['Version'])
    project_lookup[key] = mapping['ProjectName']

# Create project info lookup
info_lookup = {}
for info in project_infos:
    # Extract project name from Project_Information
    proj_info = info['Project_Information']
    # Pattern: "The project owner/repo on GitHub..." or "The project owner/repo ..."
    if ' on GitHub' in proj_info or ' is hosted on GitHub' in proj_info:
        # Extract owner/repo
        match = re.search(r'project\s+([\w\-\.]+/[\w\-\.]+)', proj_info)
        if match:
            project_name = match.group(1)
            # Extract fork count
            fork_match = re.search(r'(\d+)\s+forks?', proj_info)
            stars_match = re.search(r'(\d+)\s+stars?', proj_info)
            
            fork_count = int(fork_match.group(1)) if fork_match else 0
            stars_count = int(stars_match.group(1)) if stars_match else 0
            
            info_lookup[project_name] = {
                'project_name': project_name,
                'forks': fork_count,
                'stars': stars_count,
                'info': proj_info[:100]  # Just for debugging
            }

print(f"Projects with fork info: {len(info_lookup)}")

# Match everything together
results = []
processed_projects = {}

for pkg_key, pkg in unique_mit_packages.items():
    if pkg_key in project_lookup:
        project_name = project_lookup[pkg_key]
        if project_name in info_lookup and project_name not in processed_projects:
            processed_projects[project_name] = True
            project_data = info_lookup[project_name]
            results.append({
                'project_name': project_name,
                'package_name': pkg['Name'],
                'forks': project_data['forks'],
                'stars': project_data['stars']
            })

print(f"Total matched projects: {len(results)}")
print("Sample results:", results[:3])

# Sort by forks and get top 5
top_5 = sorted(results, key=lambda x: x['forks'], reverse=True)[:5]

print("Top 5 projects by forks:")
for i, proj in enumerate(top_5, 1):
    print(f"{i}. {proj['project_name']} - {proj['forks']} forks")

print('__RESULT__:')
print(json.dumps(top_5))"""

env_args = {'var_functions.query_db:0': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'Licenses': '[\n  "ISC"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'count': 32, 'sample': [{'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]'}, {'System': 'NPM', 'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'Licenses': '[\n  "MIT"\n]'}, {'System': 'NPM', 'Name': '@eclipsejs/cli', 'Version': '1.0.0', 'Licenses': '[\n  "MIT"\n]'}, {'System': 'NPM', 'Name': '@ebot7/edem-react', 'Version': '0.18.8', 'Licenses': '[\n  "MIT"\n]'}, {'System': 'NPM', 'Name': '@e4a/irmaseal-wasm-bindings', 'Version': '0.0.1', 'Licenses': '[\n  "MIT"\n]'}]}, 'var_functions.list_db:8': ['project_info', 'project_packageversion'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:14': {'packages_count': 100, 'project_versions_count': 5000, 'packages_sample': [{'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'System': 'NPM', 'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}], 'project_versions_sample': [{'System': 'NPM', 'Name': '@discordx/music', 'Version': '4.0.0-dev.1637888858.e2b75b9', 'ProjectName': 'oceanroleplay/discord.ts'}, {'System': 'NPM', 'Name': '@discordx/music', 'Version': '4.0.0-dev.1637888858.e2b75b9', 'ProjectName': 'oceanroleplay/discord.ts'}, {'System': 'NPM', 'Name': '@discordx/music', 'Version': '4.0.0-dev.1638102812.c236d4d', 'ProjectName': 'oceanroleplay/discord.ts'}]}, 'var_functions.execute_python:18': {'mit_release_packages': 32, 'matched_packages': 1, 'unique_projects': 1}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:26': {'packages_count': 176998, 'project_versions_count': 5000, 'sample_packages': [{'System': 'NPM', 'Name': '@discordx/utilities', 'Version': '1.0.0'}, {'System': 'NPM', 'Name': '@discordx/utilities', 'Version': '1.0.0'}], 'sample_project_versions': [{'System': 'NPM', 'Name': '@discordx/music', 'Version': '4.0.0-dev.1637888858.e2b75b9', 'ProjectName': 'oceanroleplay/discord.ts'}, {'System': 'NPM', 'Name': '@discordx/music', 'Version': '4.0.0-dev.1637888858.e2b75b9', 'ProjectName': 'oceanroleplay/discord.ts'}]}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:32': {'total_mit_packages': 176998, 'unique_mit_packages': 85158, 'project_mappings_count': 597602, 'matched_projects': 5423, 'project_names_sample': ['oceanroleplay/discord.ts', 'vuejs/vueify', 'discourse/moment-timezone-names-translations', 'moonshotcollective/scaffold-moonshot-starter', 'discovery-solutions/json-connection', 'discovery-solutions/react-flatlist', 'discovery-solutions/react-modal', 'discovery-solutions/react-router', 'discovery-solutions/react-store', 'discovery-solutions/utils']}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:36': {'message': 'Starting analysis', 'matched_projects_count': 5423, 'sample_projects': ['oceanroleplay/discord.ts', 'vuejs/vueify', 'discourse/moment-timezone-names-translations', 'moonshotcollective/scaffold-moonshot-starter', 'discovery-solutions/json-connection']}}

exec(code, env_args)
