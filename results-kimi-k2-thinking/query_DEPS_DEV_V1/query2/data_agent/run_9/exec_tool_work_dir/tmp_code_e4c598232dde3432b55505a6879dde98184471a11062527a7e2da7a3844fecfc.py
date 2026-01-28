code = """import json
import pandas as pd
import re

# Load package data (all NPM packages)
with open(var_functions_query_db_32, 'r', encoding='utf-8') as f:
    packages = json.load(f)

# Filter packages:
# - System = NPM (already filtered)
# - License starts with MIT
# - IsRelease = true
mit_release_packages = []
for pkg in packages:
    try:
        licenses = json.loads(pkg['Licenses']) if isinstance(pkg['Licenses'], str) else pkg['Licenses']
        version_info = json.loads(pkg['VersionInfo']) if isinstance(pkg['VersionInfo'], str) else pkg['VersionInfo']
        
        if (len(licenses) > 0 and licenses[0] == 'MIT' and 
            version_info.get('IsRelease') == True):
            mit_release_packages.append({
                'System': pkg['System'],
                'Name': pkg['Name'],
                'Version': pkg['Version']
            })
    except:
        continue

print(f"Found {len(mit_release_packages)} MIT-licensed NPM release packages")

# Load project_packageversion data
with open(var_functions_query_db_8, 'r', encoding='utf-8') as f:
    project_pkgversions = json.load(f)

# Create mapping from packages to projects
package_to_project = {}
project_pkgversion_count = 0
for ppv in project_pkgversions:
    if ppv['System'] == 'NPM' and ppv['ProjectName'] is not None:
        key = (ppv['System'], ppv['Name'], ppv['Version'])
        package_to_project[key] = ppv['ProjectName']
        project_pkgversion_count += 1

print(f"Loaded {project_pkgversion_count} NPM project-package mappings")

# Map MIT release packages to projects
mapped_packages = []
for pkg in mit_release_packages:
    key = (pkg['System'], pkg['Name'], pkg['Version'])
    if key in package_to_project:
        mapped_packages.append({
            **pkg,
            'ProjectName': package_to_project[key]
        })

print(f"Found {len(mapped_packages)} MIT release packages with project mappings")

# Load project_info data
with open(var_functions_query_db_24, 'r', encoding='utf-8') as f:
    project_infos_full = json.load(f)

# Extract fork counts from project_info
project_to_forks = {}
for proj in project_infos_full:
    try:
        proj_info = proj['Project_Information']
        # Parse project name and fork count
        # Format: "The project leaf/leaflet.markercluster ... forks count of 988"
        match = re.search(r'The project (.+?) (?:is hosted on GitHub|on GitHub).+forks count of (\d+)', proj_info)
        if match:
            project_name = match.group(1)
            forks = int(match.group(2))
            project_to_forks[project_name] = forks
        else:
            # Try alternative pattern
            match2 = re.search(r'The project (.+?) on GitHub.+?(\d+) forks', proj_info)
            if match2:
                project_name = match2.group(1)
                forks = int(match2.group(2))
                project_to_forks[project_name] = forks
    except:
        continue

print(f"Extracted fork counts for {len(project_to_forks)} projects")

# Combine and find top 5 by fork count
results = []
for pkg in mapped_packages:
    project_name = pkg['ProjectName']
    if project_name in project_to_forks:
        forks = project_to_forks[project_name]
        results.append({
            'PackageName': pkg['Name'],
            'Version': pkg['Version'],
            'ProjectName': project_name,
            'Forks': forks
        })

# Sort by fork count (descending) and get top 5
top_5 = sorted(results, key=lambda x: x['Forks'], reverse=True)[:5]

print(f"Found {len(results)} packages with fork data")

print('\nTop 5 packages:')
for i, pkg in enumerate(top_5, 1):
    print(f"{i}. {pkg['PackageName']} ({pkg['ProjectName']}) - {pkg['Forks']} forks")

print('__RESULT__:')
print(json.dumps(top_5, indent=2))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:2': ['project_info', 'project_packageversion'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}], 'var_functions.query_db:14': [{'System': 'NPM', 'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1-436430db4', 'ProjectType': 'GITHUB', 'ProjectName': 'leaflet/leaflet', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1-build-81dc2489', 'ProjectType': 'GITHUB', 'ProjectName': 'leaflet/leaflet', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1-build', 'ProjectType': 'GITHUB', 'ProjectName': 'leaflet/leaflet', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1-build-81dc24892a3f', 'ProjectType': 'GITHUB', 'ProjectName': 'leaflet/leaflet', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1', 'ProjectType': 'GITHUB', 'ProjectName': 'leaflet/leaflet', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1-build-dc24892a3f', 'ProjectType': 'GITHUB', 'ProjectName': 'leaflet/leaflet', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1-436430db4203a350601e002c8de6a41fae15a4bf-2', 'ProjectType': 'GITHUB', 'ProjectName': 'leaflet/leaflet', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1-32ea41baa', 'ProjectType': 'GITHUB', 'ProjectName': 'leaflet/leaflet', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1-436430db4203a350601e002c8de6a41fae15a4bf', 'ProjectType': 'GITHUB', 'ProjectName': 'leaflet/leaflet', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1-modules', 'ProjectType': 'GITHUB', 'ProjectName': 'leaflet/leaflet', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1-436430db4-436430db4', 'ProjectType': 'GITHUB', 'ProjectName': 'leaflet/leaflet', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1-build-81dc24892a', 'ProjectType': 'GITHUB', 'ProjectName': 'leaflet/leaflet', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1-436430db4203a350601e002c8de6a41fae15a4bf-1', 'ProjectType': 'GITHUB', 'ProjectName': 'leaflet/leaflet', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:30': 'Testing variable access', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]'}]}

exec(code, env_args)
