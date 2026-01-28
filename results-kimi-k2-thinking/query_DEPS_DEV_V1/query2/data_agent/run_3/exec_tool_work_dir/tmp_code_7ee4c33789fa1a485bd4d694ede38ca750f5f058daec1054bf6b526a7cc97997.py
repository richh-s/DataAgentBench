code = """import json

# Load the MIT packages from the SQLite query
with open('file_storage/functions.query_db:34.json', 'r') as f:
    mit_packages = json.load(f)

# Load the NPM project mappings from DuckDB
with open('file_storage/functions.query_db:20.json', 'r') as f:
    project_packages = json.load(f)

# Load the project info from DuckDB
with open('file_storage/functions.query_db:18.json', 'r') as f:
    project_infos = json.load(f)

print('Loaded', len(mit_packages), 'MIT packages,', len(project_packages), 'project mappings, and', len(project_infos), 'project infos')

# Create mapping: (name, version) -> repo with forks
package_to_repo = {}
repo_forks = {}

# First, parse all project infos to get fork counts
for proj in project_infos:
    info = proj.get('Project_Information', '')
    # Extract repo name and fork count
    import re
    repo_match = re.search(r'project\s+([\w\-\.]+/[\w\-\.]+)', info)
    fork_match = re.search(r'(\d+)\s+forks', info)
    if repo_match:
        repo = repo_match.group(1)
        forks = int(fork_match.group(1)) if fork_match else 0
        repo_forks[repo] = forks

# Map NPM packages to their repos
for pkg in project_packages:
    if pkg.get('System') == 'NPM':
        key = (pkg['Name'], pkg['Version'])
        repo = pkg['ProjectName']
        if repo in repo_forks:
            package_to_repo[key] = {
                'repo': repo,
                'forks': repo_forks[repo],
                'full_name': pkg.get('Name')
            }

# Find matching MIT packages
matches = []
for pkg in mit_packages:
    key = (pkg['Name'], pkg['Version'])
    if key in package_to_repo:
        repo_data = package_to_repo[key]
        matches.append({
            'project': repo_data['repo'],
            'forks': repo_data['forks'],
            'package': repo_data['full_name'],
            'version': pkg['Version']
        })

print('Found', len(matches), 'matching packages')

# Sort by forks and get top unique projects
if matches:
    # Sort all matches
    sorted_matches = sorted(matches, key=lambda x: x['forks'], reverse=True)
    # Deduplicate by project
    seen = set()
    top_5 = []
    for item in sorted_matches:
        if item['project'] not in seen:
            seen.add(item['project'])
            top_5.append(item)
            if len(top_5) >= 5:
                break
    
    print('\nTop 5 projects:')
    for i, proj in enumerate(top_5, 1):
        print(f"{i}. {proj['project']} - {proj['forks']} forks")
        print(f"   Package: {proj['package']}@{proj['version']}")
        print()
    
    result = top_5
else:
    result = []

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.query_db:2': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@ecl%2Ftwig-component-carousel/3.11.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'Hashes': '[\n  {\n    "Hash": "vH5da6eUZ94i1AcOsrC6VjSV88cMUe5A1w+CDHAt2aYXldR9sBNRCse27cIx51GnUjnj7dSe3o5A81TjraJ0Lw==",\n    "Type": "SHA512"\n  },\n  {\n    "Hash": "WZUWPp1jVp6nrUZ0n7vmthbB4OrtnLFNDOPPBBNp15I=",\n    "Type": "SHA256"\n  },\n  {\n    "Hash": "JbFslb4AeqQVI+LCXFeZKFrWmHI=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "zBm5Qvg5p2bQwUTcg6hZYA==",\n    "Type": "MD5"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1699345351000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}], 'var_functions.list_db:5': ['project_info', 'project_packageversion'], 'var_functions.query_db:6': [{'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'System': 'NPM', 'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'System': 'NPM', 'Name': '@eclipsejs/cli', 'Version': '1.0.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}'}, {'System': 'NPM', 'Name': '@ebot7/edem-react', 'Version': '0.18.8', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 55\n}'}, {'System': 'NPM', 'Name': '@e4a/irmaseal-wasm-bindings', 'Version': '0.0.1', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 1\n}'}, {'System': 'NPM', 'Name': '@ebury/chameleon-components', 'Version': '0.1.46', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 46\n}'}, {'System': 'NPM', 'Name': '@e-group/material-form', 'Version': '3.13.9', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@e-group/material-layout', 'Version': '3.4.5', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 6\n}'}, {'System': 'NPM', 'Name': '@dspworkplace/ui', 'Version': '1.0.3', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 4\n}'}, {'System': 'NPM', 'Name': '@ditojs/router', 'Version': '0.125.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 87\n}'}], 'var_functions.query_db:8': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_functions.query_db:10': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': ['test1', 'test2', 'test3'], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:30': {'status': 'check_complete'}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:40': {'mit_var': 'var_functions.query_db:34', 'proj_pkg_var': 'var_functions.query_db:20', 'proj_info_var': 'var_functions.query_db:18', 'mit_file': 'file_storage/functions.query_db:34.json', 'proj_pkg_file': 'file_storage/functions.query_db:20.json', 'proj_info_file': 'file_storage/functions.query_db:18.json'}, 'var_functions.execute_python:44': [{'project': 'schmich/instascan', 'forks': 866, 'package': '@droids/instascan@1.0.0'}, {'project': 'schmich/instascan', 'forks': 866, 'package': '@droids/instascan@1.0.0'}, {'project': 'schmich/instascan', 'forks': 866, 'package': '@droids/instascan@1.0.1'}, {'project': 'schmich/instascan', 'forks': 866, 'package': '@droids/instascan@1.0.1'}, {'project': 'mikemcl/big.js', 'forks': 419, 'package': '@dpoineau/react-scripts>1.0.0>big.js@3.1.3'}], 'var_functions.execute_python:50': [{'project': 'mpetroff/pannellum', 'forks': 700, 'package': '@dmorgenstern-init/pannellum@2.5.0'}, {'project': 'mikemcl/big.js', 'forks': 419, 'package': '@dpoineau/react-scripts>1.0.0>big.js@3.1.3'}]}

exec(code, env_args)
