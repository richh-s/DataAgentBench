code = """import json, re

# Load package data
with open(locals()['var_functions.query_db:6'], 'r', encoding='utf-8') as f:
    packages = json.load(f)

# Filter packages
mit_release_packages = []
for p in packages:
    if p.get('System') == 'NPM':
        try:
            licenses = json.loads(p['Licenses'])
            version_info = json.loads(p['VersionInfo'])
            if licenses and licenses[0] == 'MIT' and version_info.get('IsRelease'):
                mit_release_packages.append({
                    'System': p['System'],
                    'Name': p['Name'],
                    'Version': p['Version']
                })
        except:
            continue

print(f"Filtered {len(mit_release_packages)} MIT release packages")

# Load project-package mappings
with open(locals()['var_functions.query_db:8'], 'r', encoding='utf-8') as f:
    ppv = json.load(f)

# Create map
pkg_to_proj = {}
for row in ppv:
    if row.get('System') == 'NPM' and row.get('ProjectName'):
        key = (row['System'], row['Name'], row['Version'])
        pkg_to_proj[key] = row['ProjectName']

print(f"Created {len(pkg_to_proj)} package-project mappings")

# Map packages
mapped = []
for p in mit_release_packages:
    key = (p['System'], p['Name'], p['Version'])
    if key in pkg_to_proj:
        mapped.append({**p, 'ProjectName': pkg_to_proj[key]})

print(f"{len(mapped)} packages have project mappings")

# Load project info
with open(locals()['var_functions.query_db:24'], 'r', encoding='utf-8') as f:
    proj_info = json.load(f)

# Extract forks
proj_to_forks = {}
for proj in proj_info:
    try:
        info = proj['Project_Information']
        m = re.search(r'forks count of (\d+)', info)
        if not m:
            m = re.search(r'(\d+) forks', info)
        if m:
            parts = info.split('project ')
            if len(parts) > 1:
                proj_name = parts[1].split()[0].rstrip(',')
                proj_to_forks[proj_name] = int(m.group(1))
    except:
        continue

print(f"Extracted fork counts for {len(proj_to_forks)} projects")

# Combine and sort
results = []
for p in mapped:
    proj = p['ProjectName']
    if proj in proj_to_forks:
        results.append({
            'PackageName': p['Name'],
            'Version': p['Version'],
            'ProjectName': proj,
            'Forks': proj_to_forks[proj]
        })

top_5 = sorted(results, key=lambda x: x['Forks'], reverse=True)[:5]

print(f"Found {len(results)} packages with fork data")
print('\nTop 5:')
for i, r in enumerate(top_5, 1):
    print(f"{i}. {r['PackageName']} ({r['ProjectName']}) - {r['Forks']} forks")

print('__RESULT__:')
print(json.dumps(top_5))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:2': ['project_info', 'project_packageversion'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}], 'var_functions.query_db:14': [{'System': 'NPM', 'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1-436430db4', 'ProjectType': 'GITHUB', 'ProjectName': 'leaflet/leaflet', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1-build-81dc2489', 'ProjectType': 'GITHUB', 'ProjectName': 'leaflet/leaflet', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1-build', 'ProjectType': 'GITHUB', 'ProjectName': 'leaflet/leaflet', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1-build-81dc24892a3f', 'ProjectType': 'GITHUB', 'ProjectName': 'leaflet/leaflet', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1', 'ProjectType': 'GITHUB', 'ProjectName': 'leaflet/leaflet', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1-build-dc24892a3f', 'ProjectType': 'GITHUB', 'ProjectName': 'leaflet/leaflet', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1-436430db4203a350601e002c8de6a41fae15a4bf-2', 'ProjectType': 'GITHUB', 'ProjectName': 'leaflet/leaflet', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1-32ea41baa', 'ProjectType': 'GITHUB', 'ProjectName': 'leaflet/leaflet', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1-436430db4203a350601e002c8de6a41fae15a4bf', 'ProjectType': 'GITHUB', 'ProjectName': 'leaflet/leaflet', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1-modules', 'ProjectType': 'GITHUB', 'ProjectName': 'leaflet/leaflet', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1-436430db4-436430db4', 'ProjectType': 'GITHUB', 'ProjectName': 'leaflet/leaflet', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1-build-81dc24892a', 'ProjectType': 'GITHUB', 'ProjectName': 'leaflet/leaflet', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1-436430db4203a350601e002c8de6a41fae15a4bf-1', 'ProjectType': 'GITHUB', 'ProjectName': 'leaflet/leaflet', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:30': 'Testing variable access', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]'}]}

exec(code, env_args)
