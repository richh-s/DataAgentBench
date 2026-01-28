code = """import json
import re

# Load package data
pkg_path = locals()['var_functions.query_db:14']
with open(pkg_path, 'r', encoding='utf-8') as f:
    packages = json.load(f)

# Load project mappings
proj_pkg_path = locals()['var_functions.query_db:34']
with open(proj_pkg_path, 'r', encoding='utf-8') as f:
    project_mappings = json.load(f)

# Load project info (this is already a list)
project_infos = locals()['var_functions.query_db:42']

# Step 1: Find latest release version for each NPM package
print('Processing packages...')
latest_packages = {}

for pkg in packages:
    if pkg['System'] != 'NPM':
        continue
    
    try:
        # Parse VersionInfo carefully
        vinfo_text = pkg['VersionInfo']
        vinfo_text_clean = vinfo_text.replace('\n', ' ').replace('\r', '').strip()
        
        # The string starts with { and ends with }, so it should be JSON
        if vinfo_text_clean.startswith('{') and vinfo_text_clean.endswith('}'):
            vinfo = json.loads(vinfo_text_clean)
            
            if vinfo.get('IsRelease', False):
                name = pkg['Name']
                version = pkg['Version']
                ordinal = vinfo.get('Ordinal', 0)
                
                if name not in latest_packages or ordinal > latest_packages[name]['ordinal']:
                    latest_packages[name] = {
                        'PackageName': name,
                        'Version': version,
                        'ordinal': ordinal
                    }
    except Exception as e:
        continue

print(f'Found {len(latest_packages)} latest NPM packages')

# Step 2: Create project mapping (package+version -> GitHub repo)
project_map = {}
github_mappings = [p for p in project_mappings if isinstance(p, dict) and p.get('ProjectType') == 'GITHUB']

for mapping in github_mappings:
    key = (mapping['Name'], mapping['Version'])
    project_map[key] = mapping['ProjectName']

print(f'Found {len(project_map)} GitHub project mappings')

# Step 3: Create GitHub stars mapping (repo -> stars count)
stars_map = {}
for proj in project_infos:
    info_text = proj['Project_Information']
    
    # Extract repo name (owner/repo format)
    # Pattern: "The project <owner/repo> is hosted"
    repo_match = re.search(r'project\s+([^\s/]+/[^\s]+)\s+', info_text)
    if repo_match:
        repo = repo_match.group(1)
        
        # Extract stars - look for patterns like "X stars" or "stars count X"
        stars_patterns = [
            r'(\d+)\s+stars',
            r'stars?\s+count\s+of\s+(\d+)',
            r'stars?\s+count\s+(\d+)',
        ]
        
        stars = None
        for pattern in stars_patterns:
            stars_match = re.search(pattern, info_text, re.IGNORECASE)
            if stars_match:
                # Remove commas and convert to int
                stars_str = stars_match.group(1).replace(',', '')
                stars = int(stars_str)
                break
        
        if stars is not None:
            stars_map[repo] = {
                'stars': stars,
                'description': proj.get('Description', '')
            }

print(f'Found {len(stars_map)} projects with star counts')

# Step 4: Combine and find top 5
combined = []

for pkg in latest_packages.values():
    key = (pkg['PackageName'], pkg['Version'])
    if key in project_map:
        repo = project_map[key]
        if repo in stars_map:
            combined.append({
                'PackageName': pkg['PackageName'],
                'Version': pkg['Version'],
                'GitHubRepo': repo,
                'Stars': stars_map[repo]['stars'],
                'Description': stars_map[repo]['description']
            })

print(f'Found {len(combined)} packages with GitHub projects and star data')

# Sort by stars and get top 5
top5 = sorted(combined, key=lambda x: x['Stars'], reverse=True)[:5]

print('\nTop 5 NPM packages by GitHub stars:')
for idx, item in enumerate(top5, 1):
    print(f"{idx}. {item['PackageName']} (v{item['Version']})")
    print(f"   Repository: {item['GitHubRepo']}")
    print(f"   Stars: {item['Stars']:,}")
    print(f"   Description: {item['Description'][:100]}...")
    print()

print('__RESULT__:', json.dumps(top5, indent=2))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:2': ['project_info', 'project_packageversion'], 'var_functions.query_db:5': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:12': {'total_records': 661372, 'first_record': {'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectName': 'dataminingsupply/dms-io'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectName': 'isacvale/fc'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectName': 'laihaojie/jie'}], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:42': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}]}

exec(code, env_args)
