code = """import json
import re

# Load NPM package data with versioning info
package_records = var_functions_query_db_44
print(f"Loaded {len(package_records)} NPM package records")

# Group by package name and find latest release version
from collections import defaultdict

packages_by_name = defaultdict(list)
for record in package_records:
    if record.get('System') == 'NPM':
        try:
            # Parse VersionInfo JSON
            version_info = json.loads(record['VersionInfo'])
            packages_by_name[record['Name']].append({
                'Name': record['Name'],
                'Version': record['Version'],
                'Ordinal': version_info.get('Ordinal', 0),
                'IsRelease': version_info.get('IsRelease', False)
            })
        except:
            continue

# Find latest release version for each package
latest_packages = []
for name, versions in packages_by_name.items():
    # Filter for release versions only
    release_versions = [v for v in versions if v['IsRelease']]
    if release_versions:
        # Get the version with highest Ordinal
        latest = max(release_versions, key=lambda x: x['Ordinal'])
        latest_packages.append(latest)

print(f"Found {len(latest_packages)} NPM packages with latest release versions")

# Load project package mappings
project_mappings = var_functions_query_db_36
print(f"Loaded {len(project_mappings)} project-package mappings")

# Create a lookup for (Name, Version) -> ProjectName
project_lookup = {}
for mapping in project_mappings:
    key = (mapping['Name'], mapping['Version'])
    project_lookup[key] = mapping['ProjectName']

# Match packages to projects
matched_packages = []
for pkg in latest_packages:
    key = (pkg['Name'], pkg['Version'])
    if key in project_lookup:
        matched_packages.append({
            'Name': pkg['Name'],
            'Version': pkg['Version'],
            'ProjectName': project_lookup[key]
        })

print(f"Matched {len(matched_packages)} packages to GitHub projects")

# Load project info data
project_info_records = var_functions_query_db_42
print(f"Loaded {len(project_info_records)} project info records")

# Extract star counts from Project_Information field
project_stars = {}
for record in project_info_records:
    info = record['Project_Information']
    # Extract star count using regex
    match = re.search(r'(\d+(?:,\d+)*)\s+stars', info)
    if match:
        stars_str = match.group(1).replace(',', '')
        stars = int(stars_str)
        # Extract project name (owner/repo format)
        proj_match = re.search(r'project\s+([\w-]+/[\w-]+)', info)
        if proj_match:
            project_name = proj_match.group(1)
            project_stars[project_name] = stars

print(f"Extracted star counts for {len(project_stars)} projects")

# Combine packages with their star counts
packages_with_stars = []
for pkg in matched_packages:
    project_name = pkg['ProjectName']
    if project_name in project_stars:
        packages_with_stars.append({
            'Package': pkg['Name'],
            'Version': pkg['Version'],
            'Project': project_name,
            'Stars': project_stars[project_name]
        })

print(f"Found {len(packages_with_stars)} packages with star information")

# Sort by stars descending and get top 5
top_5 = sorted(packages_with_stars, key=lambda x: x['Stars'], reverse=True)[:5]

print("\n=== TOP 5 NPM PACKAGES BY GITHUB STARS ===")
for i, pkg in enumerate(top_5, 1):
    print(f"{i}. {pkg['Package']} (v{pkg['Version']})")
    print(f"   Project: {pkg['Project']}")
    print(f"   Stars: {pkg['Stars']:,}")
    print()

# Prepare result for output
result = []
for pkg in top_5:
    result.append({
        'package': pkg['Package'],
        'version': pkg['Version'],
        'github_stars': pkg['Stars'],
        'project': pkg['Project']
    })

__RESULT__:
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.query_db:2': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'System': 'NPM', 'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'System': 'NPM', 'Name': '@edgedev/firebase', 'Version': '1.0.12', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}'}, {'System': 'NPM', 'Name': '@eden-network/data', 'Version': '1.0.9-sev.5', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 14\n}'}], 'var_functions.list_db:5': ['project_info', 'project_packageversion'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.query_db:10': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectName': 'dataminingsupply/dms-io'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectName': 'isacvale/fc'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.10', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.17', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@dlcs/ng', 'Version': '1.0.0', 'ProjectName': 'winup/dlcs-ng'}, {'System': 'NPM', 'Name': '@dms/cli', 'Version': '1.0.1', 'ProjectName': 'dataminingsupply/dms-cli'}, {'System': 'NPM', 'Name': '@dms/cli', 'Version': '1.0.0', 'ProjectName': 'dataminingsupply/dms-cli'}], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:42': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.'}, {'Project_Information': 'The project is hosted on GitHub under the name learnfrontend-dc/product-cart, and it currently has 2 open issues. It has garnered a total of 11 stars and has been forked 12 times.'}, {'Project_Information': 'The GitHub project ledgerproject/keypairoom currently has 3 open issues, 3 stars, and 0 forks.'}, {'Project_Information': 'The project leebyron/jasmine-check is hosted on GitHub and currently has 0 open issues, 11 stars, and 3 forks.'}, {'Project_Information': 'The project leebyron/testcheck-js on GitHub has an open issues count of 29, a stars count of 1185, and a forks count of 58, making it a notable repository in the community.'}, {'Project_Information': 'The project leecade/react-native-swiper is hosted on GitHub and has a total of 786 open issues, along with an impressive 10,249 stars and 2,392 forks, making it a popular choice among developers for implementing swiping functionality in React Native applications.'}], 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:46': [{'total_npm_packages': '661372'}]}

exec(code, env_args)
