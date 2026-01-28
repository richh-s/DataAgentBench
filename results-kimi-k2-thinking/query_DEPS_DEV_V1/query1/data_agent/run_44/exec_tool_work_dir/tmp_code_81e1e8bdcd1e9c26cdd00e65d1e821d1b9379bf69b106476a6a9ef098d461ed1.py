code = """import json, re, os

# Load package data
pkg_path = locals()['var_functions.query_db:14']
with open(pkg_path, 'r', encoding='utf-8') as f:
    packages = json.load(f)

# Load project package mappings
proj_pkg_path = locals()['var_functions.query_db:34']
with open(proj_pkg_path, 'r', encoding='utf-8') as f:
    project_mappings = json.load(f)

# Load project info
proj_info_path = locals()['var_functions.query_db:42']
with open(proj_info_path, 'r', encoding='utf-8') as f:
    # This is a list not a file path, so just use it directly
    project_infos = locals()['var_functions.query_db:42']

# Step 1: Find latest release version for each NPM package
latest_releases = {}

for pkg in packages:
    if pkg['System'] != 'NPM':
        continue
    
    try:
        # Parse VersionInfo
        vinfo_str = pkg['VersionInfo'].strip()
        vinfo_str = vinfo_str.replace('\n', ' ').replace('\r', '')
        vinfo = json.loads(vinfo_str)
        
        if vinfo.get('IsRelease', False):
            name = pkg['Name']
            version = pkg['Version']
            ordinal = vinfo.get('Ordinal', 0)
            
            if name not in latest_releases or ordinal > latest_releases[name]['ordinal']:
                latest_releases[name] = {
                    'Name': name,
                    'Version': version,
                    'ordinal': ordinal
                }
    except:
        continue

print('Found', len(latest_releases), 'latest NPM release packages')

# Step 2: Create mapping of package name + version to GitHub project
project_map = {}
for mapping in project_mappings:
    if mapping['ProjectType'] == 'GITHUB':
        key = (mapping['Name'], mapping['Version'])
        project_map[key] = mapping['ProjectName']

print('Project mappings for GITHUB:', len(project_map))

# Step 3: Extract GitHub stars from project info
stars_map = {}
for proj in project_infos:
    info_text = proj['Project_Information']
    # Extract owner/repo
    match = re.search(r'project\s+([^\s]+/[^\s]+)\s+is hosted', info_text)
    if match:
        repo = match.group(1)
        # Extract stars
        stars_match = re.search(r'(?:stars count of|stars count|stars)\s+(\d+)', info_text)
        if stars_match:
            stars = int(stars_match.group(1).replace(',', ''))
            stars_map[repo] = {
                'repo': repo,
                'stars': stars,
                'description': proj.get('Description', '')
            }

print('Project info records with stars:', len(stars_map))

# Step 4: Combine everything and get top 5
results = []

for pkg_name, pkg_info in latest_releases.items():
    key = (pkg_name, pkg_info['Version'])
    if key in project_map:
        repo = project_map[key]
        if repo in stars_map:
            results.append({
                'PackageName': pkg_name,
                'Version': pkg_info['Version'],
                'Repo': repo,
                'Stars': stars_map[repo]['stars'],
                'Description': stars_map[repo]['description']
            })

# Sort by stars
sorted_results = sorted(results, key=lambda x: x['Stars'], reverse=True)
top5 = sorted_results[:5]

print('\nTop 5 NPM packages by GitHub stars:')
for i, pkg in enumerate(top5, 1):
    print(f"{i}. {pkg['PackageName']} v{pkg['Version']} - {pkg['Repo']} - {pkg['Stars']} stars")

print('\n__RESULT__:')
print(json.dumps(top5, indent=2))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:2': ['project_info', 'project_packageversion'], 'var_functions.query_db:5': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:12': {'total_records': 661372, 'first_record': {'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectName': 'dataminingsupply/dms-io'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectName': 'isacvale/fc'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectName': 'laihaojie/jie'}], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:42': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}]}

exec(code, env_args)
