code = """import json

# Load matched packages
with open('matched_packages.json', 'r') as f:
    matched_packages = json.load(f)

print(f'Matched packages: {len(matched_packages)}')
print('Sample:', matched_packages[:5])

# Load project stars
with open('project_stars.json', 'r') as f:
    project_stars = json.load(f)

print(f'Project stars mapped: {len(project_stars)}')
print('Sample projects:', list(project_stars.items())[:5])

# Combine: add star count to each matched package
final_list = []
matched_count = 0

for pkg in matched_packages:
    project_name = pkg['ProjectName']
    if project_name in project_stars:
        pkg['Stars'] = project_stars[project_name]
        final_list.append(pkg)
        matched_count += 1
    else:
        # Some projects might be referenced differently
        # Try common variations just in case
        alt_name = project_name.replace('https://github.com/', '')
        if alt_name in project_stars:
            pkg['Stars'] = project_stars[alt_name]
            final_list.append(pkg)
            matched_count += 1
        else:
            pkg['Stars'] = 0

print(f'Packages with star data: {matched_count}')

# Sort by stars descending
top_packages = sorted(final_list, key=lambda x: x['Stars'], reverse=True)[:20]
print('Top 20:')
for i, pkg in enumerate(top_packages, 1):
    print(f"{i}. {pkg['Name']} (v{pkg['Version']}) - {pkg['Stars']} stars - {pkg['ProjectName']}")

# Save top 5 for final answer
top_5 = top_packages[:5]
with open('top_5_packages.json', 'w') as f:
    json.dump(top_5, f)

result = f'Found top {len(top_5)} packages'
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:2': ['project_info', 'project_packageversion'], 'var_functions.query_db:4': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'Name': '@edgedev/firebase', 'Version': '1.0.12', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}'}, {'Name': '@eden-network/data', 'Version': '1.0.9-sev.5', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 14\n}'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': 'Found 15811 unique NPM packages with latest releases', 'var_functions.query_db:12': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': 'Processed 15811 latest NPM releases', 'var_functions.query_db:20': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': 'Created lookup for 15811 latest NPM releases', 'var_functions.execute_python:28': 'Matched 15811 packages to GitHub repositories', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:32': 'Mapped 569 projects'}

exec(code, env_args)
