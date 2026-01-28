code = """import json, re, sys

print('Starting data processing')

# Load all data files
pkg_path = locals()['var_functions.query_db:52']
mappings_path = locals()['var_functions.query_db:34']
projects_path = locals()['var_functions.query_db:66']

print('Loading packages...')
with open(pkg_path) as f:
    packages = json.load(f)

print('Loading mappings...')
with open(mappings_path) as f:
    mappings = json.load(f)

print('Loading projects...')
with open(projects_path) as f:
    projects = json.load(f)

print(f'Loaded {len(packages)} packages, {len(mappings)} mappings, {len(projects)} projects')

# Step 1: Find latest release version for each NPM package
print('Finding latest releases...')
latest_packages = {}

for pkg in packages:
    if pkg.get('System') != 'NPM':
        continue
    try:
        # VersionInfo contains JSON string
        vinfo_raw = pkg['VersionInfo']
        vinfo_str = vinfo_raw.replace('\n', ' ').strip()
        vinfo = json.loads(vinfo_str)
        if vinfo.get('IsRelease'):
            name = pkg['Name']
            ordinal = vinfo['Ordinal']
            version = pkg['Version']
            if name not in latest_packages or ordinal > latest_packages[name]['ordinal']:
                latest_packages[name] = {'version': version, 'ordinal': ordinal}
    except Exception as e:
        continue

print(f'Found {len(latest_packages)} latest releases')

# Step 2: Map package+version to GitHub repository
print('Building GitHub project map...')
github_map = {}
for mapping in mappings:
    if mapping.get('ProjectType') == 'GITHUB':
        key = (mapping['Name'], mapping['Version'])
        github_map[key] = mapping['ProjectName']

print(f'Created {len(github_map)} GitHub mappings')

# Step 3: Extract GitHub stars
print('Extracting star counts...')
stars = {}
for proj in projects:
    info = proj['Project_Information']
    m = re.search(r'project\s+([\w-]+/[\w-]+)', info)
    if m:
        repo = m.group(1)
        m2 = re.search(r'(\d+[\d,]*)\s+stars', info)
        if m2:
            stars_str = m2.group(1).replace(',', '')
            try:
                stars[repo] = int(stars_str)
            except:
                pass

print(f'Extracted {len(stars)} star counts')

# Step 4: Combine and rank
print('Combining data...')
results = []
for name, data in latest_packages.items():
    key = (name, data['version'])
    if key in github_map:
        repo = github_map[key]
        if repo in stars:
            results.append({
                'PackageName': name,
                'Version': data['version'],
                'GitHubRepository': repo,
                'Stars': stars[repo]
            })

print(f'Found {len(results)} matching packages')

# Step 5: Get top 5 packages by stars
print('Getting top 5...')
top5 = sorted(results, key=lambda x: x['Stars'], reverse=True)[:5]

print('Top 5 NPM Packages by GitHub Stars:')
for i, pkg in enumerate(top5, 1):
    print(f"{i}. {pkg['PackageName']} v{pkg['Version']}")
    print(f"   Repository: {pkg['GitHubRepository']}")
    print(f"   Stars: {pkg['Stars']:,}")
    print()

# Prepare final result
final_result = {
    'packages': top5,
    'total_processed': len(latest_packages),
    'total_matched': len(results)
}

print('__RESULT__:')
print(json.dumps(final_result))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:2': ['project_info', 'project_packageversion'], 'var_functions.query_db:5': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:12': {'total_records': 661372, 'first_record': {'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectName': 'dataminingsupply/dms-io'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectName': 'isacvale/fc'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectName': 'laihaojie/jie'}], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:42': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_functions.query_db:50': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'Name': '@edgedev/firebase', 'Version': '1.0.12', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}'}, {'Name': '@eden-network/data', 'Version': '1.0.9-sev.5', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 14\n}'}], 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json', 'var_functions.execute_python:54': [{'PackageName': '@ec-nordbund/leaflet', 'Version': '1.7.1', 'Repo': 'leaflet/leaflet', 'Stars': 38715}, {'PackageName': '@duchesstoffee/react-responsive-carousel', 'Version': '3.2.10', 'Repo': 'leandrowd/react-responsive-carousel', 'Stars': 534}, {'PackageName': '@dumbstuff/template', 'Version': '0.2.0', 'Repo': 'lberrocal/npm-packages-template', 'Stars': 0}], 'var_functions.execute_python:62': [{'PackageName': '@ec-nordbund/leaflet', 'Version': '1.7.1', 'GitHubRepo': 'leaflet/leaflet', 'Stars': 38715}, {'PackageName': '@duchesstoffee/react-responsive-carousel', 'Version': '3.2.10', 'GitHubRepo': 'leandrowd/react-responsive-carousel', 'Stars': 2534}, {'PackageName': '@dumbstuff/template', 'Version': '0.2.0', 'GitHubRepo': 'lberrocal/npm-packages-template', 'Stars': 0}], 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json'}

exec(code, env_args)
