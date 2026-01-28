code = """import json, re

# Load package data
packages = json.load(open(locals()['var_functions.query_db:52']))

# Load project mappings
mappings = json.load(open(locals()['var_functions.query_db:34']))

# Load project info
projects = json.load(open(locals()['var_functions.query_db:66']))

print('Loaded', len(packages), 'packages,', len(mappings), 'mappings,', len(projects), 'projects')

# Step 1: Find latest release version per NPM package
latest_package = {}

for p in packages:
    if p['System'] != 'NPM':
        continue
    try:
        # Parse VersionInfo more carefully
        vinfo_str = p['VersionInfo']
        # Replace newlines with spaces
        vinfo_clean = vinfo_str.replace('\n', ' ').strip()
        # Now parse as JSON
        vinfo_obj = json.loads(vinfo_clean)
        if vinfo_obj['IsRelease']:
            name = p['Name']
            ordinal = vinfo_obj['Ordinal']
            version = p['Version']
            if name not in latest_package or ordinal > latest_package[name][1]:
                latest_package[name] = (version, ordinal)
    except Exception as e:
        pass

print('Latest releases:', len(latest_package))

# Step 2: Create GitHub project mapping
gh_map = {}
for m in mappings:
    if m['ProjectType'] == 'GITHUB':
        key = (m['Name'], m['Version'])
        gh_map[key] = m['ProjectName']

print('GitHub mappings:', len(gh_map))

# Step 3: Extract GitHub stars
stars_map = {}
for proj in projects:
    info = proj['Project_Information']
    m = re.search(r'project\s+([^\s]+/[^\s]+)', info)
    if m:
        repo = m.group(1)
        m2 = re.search(r'(\d+\,?\d*)\s+stars', info)
        if m2:
            stars = int(m2.group(1).replace(',', ''))
            stars_map[repo] = stars

print('Stars data:', len(stars_map))

# Step 4: Combine everything
candidates = []
for name in latest_package:
    version = latest_package[name][0]
    key = (name, version)
    if key in gh_map:
        repo = gh_map[key]
        if repo in stars_map:
            candidates.append({
                'PackageName': name,
                'Version': version,
                'GitHubRepo': repo,
                'Stars': stars_map[repo]
            })

print('Total candidates:', len(candidates))

# Get top 5
top5 = sorted(candidates, key=lambda x: x['Stars'], reverse=True)[:5]

for i, item in enumerate(top5, 1):
    print(f"{i}. {item['PackageName']} v{item['Version']}")
    print(f"   Repo: {item['GitHubRepo']}")
    print(f"   Stars: {item['Stars']:,}")
    print()

print('__RESULT__:')
print(json.dumps(top5, indent=2))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:2': ['project_info', 'project_packageversion'], 'var_functions.query_db:5': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:12': {'total_records': 661372, 'first_record': {'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectName': 'dataminingsupply/dms-io'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectName': 'isacvale/fc'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectName': 'laihaojie/jie'}], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:42': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_functions.query_db:50': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'Name': '@edgedev/firebase', 'Version': '1.0.12', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}'}, {'Name': '@eden-network/data', 'Version': '1.0.9-sev.5', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 14\n}'}], 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json', 'var_functions.execute_python:54': [{'PackageName': '@ec-nordbund/leaflet', 'Version': '1.7.1', 'Repo': 'leaflet/leaflet', 'Stars': 38715}, {'PackageName': '@duchesstoffee/react-responsive-carousel', 'Version': '3.2.10', 'Repo': 'leandrowd/react-responsive-carousel', 'Stars': 534}, {'PackageName': '@dumbstuff/template', 'Version': '0.2.0', 'Repo': 'lberrocal/npm-packages-template', 'Stars': 0}], 'var_functions.execute_python:62': [{'PackageName': '@ec-nordbund/leaflet', 'Version': '1.7.1', 'GitHubRepo': 'leaflet/leaflet', 'Stars': 38715}, {'PackageName': '@duchesstoffee/react-responsive-carousel', 'Version': '3.2.10', 'GitHubRepo': 'leandrowd/react-responsive-carousel', 'Stars': 2534}, {'PackageName': '@dumbstuff/template', 'Version': '0.2.0', 'GitHubRepo': 'lberrocal/npm-packages-template', 'Stars': 0}], 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json'}

exec(code, env_args)
