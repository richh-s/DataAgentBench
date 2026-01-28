code = """import json, re

# Load all data files
pkg_file = locals()['var_functions.query_db:52']
mappings_file = locals()['var_functions.query_db:34']
proj_info_file = locals()['var_functions.query_db:66']

with open(pkg_file, 'r') as f1:
    all_packages = json.load(f1)

with open(mappings_file, 'r') as f2:
    all_mappings = json.load(f2)

with open(proj_info_file, 'r') as f3:
    all_projects = json.load(f3)

print('Loaded', len(all_packages), 'packages,', len(all_mappings), 'mappings,', len(all_projects), 'projects')

# Step 1: Find latest release versions for NPM packages
latest_releases = {}

for pkg in all_packages:
    if pkg['System'] != 'NPM':
        continue
    
    # Parse VersionInfo - it's a JSON string
    try:
        vinfo_str = pkg['VersionInfo']
        # The JSON may have newlines, but json.load should handle it since it's already a string
        # Actually VersionInfo is a string that contains JSON, so we need to parse it
        vinfo_obj = json.loads(vinfo_str)
        
        if vinfo_obj.get('IsRelease', False):
            name = pkg['Name']
            version = pkg['Version']
            ordinal = vinfo_obj.get('Ordinal', 0)
            
            if name not in latest_releases or ordinal > latest_releases[name]['ordinal']:
                latest_releases[name] = {
                    'version': version,
                    'ordinal': ordinal
                }
    except Exception as e:
        continue

print('Found', len(latest_releases), 'latest package releases')

# Step 2: Build GitHub project mapping
github_project_map = {}
for mapping in all_mappings:
    if mapping.get('ProjectType') == 'GITHUB':
        key = (mapping['Name'], mapping['Version'])
        github_project_map[key] = mapping['ProjectName']

print('GitHub project mappings:', len(github_project_map))

# Step 3: Extract GitHub star counts from project info
stars_by_repository = {}

for proj in all_projects:
    info = proj['Project_Information']
    
    # Extract repository name (owner/repo format)
    match = re.search(r'project\s+([^\s]+/[^\s]+)', info)
    if match:
        repo = match.group(1)
        
        # Extract star count
        stars_match = re.search(r'(\d[\d,]*)\s+stars', info)
        if stars_match:
            stars_str = stars_match.group(1).replace(',', '')
            try:
                stars = int(stars_str)
                stars_by_repository[repo] = stars
            except:
                pass

print('Repositories with star data:', len(stars_by_repository))

# Step 4: Find top 5 packages by stars
final_results = []

for name, data in latest_releases.items():
    key = (name, data['version'])
    if key in github_project_map:
        repo = github_project_map[key]
        if repo in stars_by_repository:
            final_results.append({
                'PackageName': name,
                'Version': data['version'],
                'GitHubRepository': repo,
                'GitHubStars': stars_by_repository[repo]
            })

print('Total matched packages:', len(final_results))

# Sort by stars and get top 5
top5_packages = sorted(final_results, key=lambda x: x['GitHubStars'], reverse=True)[:5]

print('\nTop 5 NPM Packages by GitHub Stars:')
for idx, pkg in enumerate(top5_packages, 1):
    print(f"{idx}. {pkg['PackageName']} (v{pkg['Version']})")
    print(f"   Repository: {pkg['GitHubRepository']}")
    print(f"   Stars: {pkg['GitHubStars']:,}")
    print()

result = {'top_packages': top5_packages}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:2': ['project_info', 'project_packageversion'], 'var_functions.query_db:5': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:12': {'total_records': 661372, 'first_record': {'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectName': 'dataminingsupply/dms-io'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectName': 'isacvale/fc'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectName': 'laihaojie/jie'}], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:42': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_functions.query_db:50': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'Name': '@edgedev/firebase', 'Version': '1.0.12', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}'}, {'Name': '@eden-network/data', 'Version': '1.0.9-sev.5', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 14\n}'}], 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json', 'var_functions.execute_python:54': [{'PackageName': '@ec-nordbund/leaflet', 'Version': '1.7.1', 'Repo': 'leaflet/leaflet', 'Stars': 38715}, {'PackageName': '@duchesstoffee/react-responsive-carousel', 'Version': '3.2.10', 'Repo': 'leandrowd/react-responsive-carousel', 'Stars': 534}, {'PackageName': '@dumbstuff/template', 'Version': '0.2.0', 'Repo': 'lberrocal/npm-packages-template', 'Stars': 0}], 'var_functions.execute_python:62': [{'PackageName': '@ec-nordbund/leaflet', 'Version': '1.7.1', 'GitHubRepo': 'leaflet/leaflet', 'Stars': 38715}, {'PackageName': '@duchesstoffee/react-responsive-carousel', 'Version': '3.2.10', 'GitHubRepo': 'leandrowd/react-responsive-carousel', 'Stars': 2534}, {'PackageName': '@dumbstuff/template', 'Version': '0.2.0', 'GitHubRepo': 'lberrocal/npm-packages-template', 'Stars': 0}], 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json'}

exec(code, env_args)
