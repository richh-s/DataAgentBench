code = """import json, re
from collections import defaultdict

# Load all data
packages_path = locals()['var_functions.query_db:52']
with open(packages_path, 'r') as f:
    packages = json.load(f)

mappings_path = locals()['var_functions.query_db:34']
with open(mappings_path, 'r') as f:
    mappings = json.load(f)

project_infos = locals()['var_functions.query_db:42']

# Step 1: Find latest release per package
print('Step 1: Processing packages...')
latest_by_package = {}

for pkg in packages:
    try:
        # Clean up the VersionInfo string
        vinfo_str = pkg['VersionInfo'].replace('\n', ' ').replace('\r', '').strip()
        vinfo = json.loads(vinfo_str)
        
        if vinfo.get('IsRelease', False):
            name = pkg['Name']
            ordinal = vinfo.get('Ordinal', 0)
            version = pkg['Version']
            
            if name not in latest_by_package or ordinal > latest_by_package[name]['ordinal']:
                latest_by_package[name] = {
                    'version': version,
                    'ordinal': ordinal
                }
    except Exception as e:
        pass

print(f'Found {len(latest_by_package)} packages with latest releases')

# Step 2: Build GITHUB project mappings
print('Step 2: Building project mappings...')
github_mappings = [m for m in mappings if m.get('ProjectType') == 'GITHUB']
print(f'Total GITHUB mappings: {len(github_mappings)}')

# Build lookup: (name, version) -> repo
project_lookup = {}
for m in github_mappings:
    key = (m['Name'], m['Version'])
    project_lookup[key] = m['ProjectName']

print(f'Project lookup keys: {len(project_lookup)}')

# Step 3: Process project info and extract stars more robustly
print('Step 3: Processing project info...')
stars_by_repo = {}

# Debug: show one example
print('Sample Project_Information:')
if project_infos:
    print(project_infos[1]['Project_Information'][:200])

for idx, proj in enumerate(project_infos):
    info = proj['Project_Information']
    
    # Try multiple patterns for repository extraction
    repo_patterns = [
        r'project\s+([^\s]+/[^\s]+)\s+is hosted',
        r'project\s+([^\s]+/[^\s]+)\s+on GitHub',
        r'project\s+([^\s]+/[^\s]+)[\s,]',
    ]
    
    repo = None
    for pattern in repo_patterns:
        match = re.search(pattern, info)
        if match:
            repo = match.group(1)
            break
    
    if not repo:
        continue
    
    # Try multiple patterns for stars extraction
    stars_patterns = [
        r'(\d+)\s+stars',
        r'stars?\s+count\s+of\s+(\d+)',
        r'stars?\s+count\s+(\d+)',
        r'([\d,]+)\s+stars',
    ]
    
    stars = None
    for pattern in stars_patterns:
        match = re.search(pattern, info, re.IGNORECASE)
        if match:
            stars_str = match.group(1).replace(',', '')
            try:
                stars = int(stars_str)
                break
            except:
                pass
    
    if stars is not None and stars > 0:
        stars_by_repo[repo] = stars

print(f'Repositories with star counts: {len(stars_by_repo)}')

# Show some examples with high stars
sorted_stars = sorted(stars_by_repo.items(), key=lambda x: x[1], reverse=True)[:10]
print('Top repositories by stars:')
for repo, stars in sorted_stars:
    print(f'  {repo}: {stars}')

# Step 4: Combine and find matches
print('Step 4: Finding matches...')
matches = []

matched_packages = 0
matched_projects = 0
matched_stars = 0

for pkg_name, pkg_data in latest_by_package.items():
    matched_packages += 1
    key = (pkg_name, pkg_data['version'])
    
    if key in project_lookup:
        matched_projects += 1
        repo = project_lookup[key]
        
        if repo in stars_by_repo:
            matched_stars += 1
            matches.append({
                'PackageName': pkg_name,
                'Version': pkg_data['version'],
                'Repo': repo,
                'Stars': stars_by_repo[repo]
            })

print(f'Packages with latest releases: {matched_packages}')
print(f'With project mappings: {matched_projects}')
print(f'With star data: {matched_stars}')

# Get top 5
top_matches = sorted(matches, key=lambda x: x['Stars'], reverse=True)[:5]

print('\nTop 5:')
for i, m in enumerate(top_matches, 1):
    print(f"{i}. {m['PackageName']} v{m['Version']} ({m['Repo']}) - {m['Stars']} stars")

print('\n__RESULT__:')
print(json.dumps(top_matches, indent=2))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:2': ['project_info', 'project_packageversion'], 'var_functions.query_db:5': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:12': {'total_records': 661372, 'first_record': {'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectName': 'dataminingsupply/dms-io'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectName': 'isacvale/fc'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectName': 'laihaojie/jie'}], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:42': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_functions.query_db:50': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'Name': '@edgedev/firebase', 'Version': '1.0.12', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}'}, {'Name': '@eden-network/data', 'Version': '1.0.9-sev.5', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 14\n}'}], 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json', 'var_functions.execute_python:54': [{'PackageName': '@ec-nordbund/leaflet', 'Version': '1.7.1', 'Repo': 'leaflet/leaflet', 'Stars': 38715}, {'PackageName': '@duchesstoffee/react-responsive-carousel', 'Version': '3.2.10', 'Repo': 'leandrowd/react-responsive-carousel', 'Stars': 534}, {'PackageName': '@dumbstuff/template', 'Version': '0.2.0', 'Repo': 'lberrocal/npm-packages-template', 'Stars': 0}]}

exec(code, env_args)
