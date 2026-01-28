code = """import json
import pandas as pd
import re
from collections import defaultdict

# Access data from storage
pkg_info = locals()['var_functions.query_db:4']
proj_pkg = locals()['var_functions.query_db:26']
proj_info = locals()['var_functions.query_db:12']

print(f"Package info records: {len(pkg_info)}")
print(f"Project-package mappings: {len(proj_pkg)}")
print(f"Project info records: {len(proj_info)}")

# Step 1: Parse package info to identify release versions and find latest for each package
print("\n=== Step 1: Processing package versions ===")

pkg_versions = defaultdict(list)

for pkg in pkg_info:
    name = pkg['Name']
    version = pkg['Version']
    version_info_str = pkg.get('VersionInfo', '{}')
    
    try:
        if isinstance(version_info_str, str):
            version_info = json.loads(version_info_str)
        else:
            version_info = version_info_str
    except:
        version_info = {}
    
    if isinstance(version_info, dict):
        is_release = version_info.get('IsRelease', False)
        ordinal = version_info.get('Ordinal', 0)
    else:
        is_release = False
        ordinal = 0
    
    if is_release:
        pkg_versions[name].append({
            'version': version,
            'ordinal': ordinal,
            'pkg_data': pkg
        })

# Find latest release for each package (highest ordinal)
latest_pkgs = {}
for name, versions in pkg_versions.items():
    if versions:
        latest = max(versions, key=lambda x: x['ordinal'])
        latest_pkgs[name] = latest

print(f"Found {len(latest_pkgs)} packages with release versions")
print("Sample packages with latest versions:")
count = 0
for name, latest in list(latest_pkgs.items())[:5]:
    print(f"  {name}: v{latest['version']} (ordinal: {latest['ordinal']})")
    count += 1

print(f"\n=== Step 2: Mapping packages to projects ===")

# Create lookup for project mappings
proj_lookup = {}
for pp in proj_pkg:
    key = (pp['System'], pp['Name'], pp['Version'])
    proj_lookup[key] = pp['ProjectName']

# Map latest packages to their projects
pkg_project_map = {}
for name, latest in latest_pkgs.items():
    key = ('NPM', name, latest['version'])
    if key in proj_lookup:
        pkg_project_map[name] = {
            'version': latest['version'],
            'project_name': proj_lookup[key],
            'pkg_data': latest['pkg_data']
        }

print(f"Successfully mapped {len(pkg_project_map)} packages to projects")
print("Sample mappings:")
for name, data in list(pkg_project_map.items())[:5]:
    print(f"  {name} -> {data['project_name']}")

print(f"\n=== Step 3: Extracting stars from project info ===")

# Create project info lookup with stars
proj_stars = {}
for proj in proj_info:
    proj_text = proj['Project_Information']
    # Extract GitHub project name from the text
    if 'GitHub' in proj_text:
        # Pattern: "The project <owner/repo> is hosted on GitHub"
        match = re.search(r'The project ([\w-]+/[\w-]+) is hosted on GitHub', proj_text)
        if match:
            repo_name = match.group(1)
            # Extract stars
            stars_match = re.search(r'(\d+) stars', proj_text)
            if stars_match:
                stars = int(stars_match.group(1))
                proj_stars[repo_name] = stars

print(f"Extracted star counts for {len(proj_stars)} projects")
print("Sample star counts:")
for repo, stars in list(proj_stars.items())[:5]:
    print(f"  {repo}: {stars} stars")

print(f"\n=== Step 4: Combining data and finding top packages ===")

# Combine everything
packages_with_stars = []
for name, data in pkg_project_map.items():
    project_name = data['project_name']
    stars = proj_stars.get(project_name, 0)
    packages_with_stars.append({
        'package_name': name,
        'version': data['version'],
        'project_name': project_name,
        'stars': stars
    })

# Sort by stars
top_packages = sorted(packages_with_stars, key=lambda x: x['stars'], reverse=True)

print(f"Found {len(packages_with_stars)} packages with GitHub projects")
print(f"Top 10 packages by stars:")
for i, pkg in enumerate(top_packages[:10]):
    print(f"  {i+1}. {pkg['package_name']} - {pkg['stars']} stars (v{pkg['version']})")

# Get top 5
top_5 = top_packages[:5]

# Format result
result = []
for pkg in top_5:
    result.append({
        'package': pkg['package_name'],
        'version': pkg['version'],
        'stars': pkg['stars'],
        'github_repo': pkg['project_name']
    })

print("\n=== FINAL RESULT ===")
import json as js
print(js.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.query_db:2': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'System': 'NPM', 'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'System': 'NPM', 'Name': '@edgedev/firebase', 'Version': '1.0.12', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}'}, {'System': 'NPM', 'Name': '@eden-network/data', 'Version': '1.0.9-sev.5', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 14\n}'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.list_db:6': ['project_info', 'project_packageversion'], 'var_functions.query_db:7': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectName': 'dataminingsupply/dms-io'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectName': 'isacvale/fc'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.10', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.17', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@dlcs/ng', 'Version': '1.0.0', 'ProjectName': 'winup/dlcs-ng'}, {'System': 'NPM', 'Name': '@dms/cli', 'Version': '1.0.1', 'ProjectName': 'dataminingsupply/dms-cli'}, {'System': 'NPM', 'Name': '@dms/cli', 'Version': '1.0.0', 'ProjectName': 'dataminingsupply/dms-cli'}, {'System': 'NPM', 'Name': '@dms/cli', 'Version': '0.8.0', 'ProjectName': 'dataminingsupply/dms-cli'}, {'System': 'NPM', 'Name': '@dms/cli', 'Version': '0.9.3', 'ProjectName': 'dataminingsupply/dms-cli'}, {'System': 'NPM', 'Name': '@dms/cli', 'Version': '0.2.0', 'ProjectName': 'dataminingsupply/dms-cli'}, {'System': 'NPM', 'Name': '@domp/fp', 'Version': '0.0.1', 'ProjectName': 'dom-packages/fp'}, {'System': 'NPM', 'Name': '@domp/is', 'Version': '0.2.0', 'ProjectName': 'lohfu/domp-is'}, {'System': 'NPM', 'Name': '@domp/is', 'Version': '0.1.3', 'ProjectName': 'lohfu/domp-is'}, {'System': 'NPM', 'Name': '@dosy/ws', 'Version': '8.11.1', 'ProjectName': 'dosyago/ws'}, {'System': 'NPM', 'Name': '@dosy/ws', 'Version': '8.11.4', 'ProjectName': 'dosyago/ws'}, {'System': 'NPM', 'Name': '@dot/cdk', 'Version': '2.1.0', 'ProjectName': 'shellscape/dot'}, {'System': 'NPM', 'Name': '@dot/cdk', 'Version': '0.1.0', 'ProjectName': 'shellscape/dot'}], 'var_functions.query_db:8': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
