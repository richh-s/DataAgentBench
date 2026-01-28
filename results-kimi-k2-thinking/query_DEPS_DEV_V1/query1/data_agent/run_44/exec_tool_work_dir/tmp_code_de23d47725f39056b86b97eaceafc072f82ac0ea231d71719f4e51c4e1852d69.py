code = """# Let's take a different approach - handle all processing with simpler code
import json, sqlite3, re
from pathlib import Path

# Create in-memory database for easier processing
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Load and process package data
packages_path = locals()['var_functions.query_db:52']
with open(packages_path, 'r') as f:
    packages = json.load(f)

# Create package table
cursor.execute('CREATE TABLE packages (Name TEXT, Version TEXT, VersionInfo TEXT)')
for pkg in packages:
    cursor.execute('INSERT INTO packages VALUES (?, ?, ?)', 
                   (pkg['Name'], pkg['Version'], pkg['VersionInfo']))

# Extract release versions with parsed VersionInfo
cursor.execute('''
    SELECT Name, Version, 
           REPLACE(REPLACE(VersionInfo, X'0A', ' '), X'0D', '') as CleanInfo
    FROM packages
''')

release_packages = []
for row in cursor.fetchall():
    try:
        clean_json = row[2].strip()
        vinfo = json.loads(clean_json)
        if vinfo.get('IsRelease', False):
            release_packages.append({
                'Name': row[0],
                'Version': row[1],
                'Ordinal': vinfo.get('Ordinal', 0)
            })
    except:
        pass

print('Release packages found:', len(release_packages))

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
cursor.execute('CREATE TABLE releases (Name TEXT, Version TEXT, Ordinal INTEGER)')
for pkg in release_packages:
    cursor.execute('INSERT INTO releases VALUES (?, ?, ?)', 
                   (pkg['Name'], pkg['Version'], pkg['Ordinal']))

# Find latest release per package
cursor.execute('''
    SELECT Name, Version, MAX(Ordinal) as MaxOrdinal
    FROM releases 
    GROUP BY Name
''')

latest_packages = cursor.fetchall()
print('Latest releases:', len(latest_packages))

# Load project mappings
mappings_path = locals()['var_functions.query_db:34']
with open(mappings_path, 'r') as f:
    mappings = json.load(f)

# Filter GITHUB mappings
github_mappings = [m for m in mappings if m.get('ProjectType') == 'GITHUB']
project_map = {(m['Name'], m['Version']): m['ProjectName'] for m in github_mappings}

# Load project info
project_infos = locals()['var_functions.query_db:42']
stars_map = {}

for proj in project_infos:
    info = proj['Project_Information']
    # Extract repository name
    match = re.search(r'project\s+([^\s]+/[^\s]+)\s+', info)
    if match:
        repo = match.group(1)
        # Extract stars
        stars_match = re.search(r'(\d+)\s+stars', info)
        if stars_match:
            stars = int(stars_match.group(1).replace(',', ''))
            stars_map[repo] = stars

print('Projects with stars:', len(stars_map))

# Combine data and find top 5
combined = []
for name, version, _ in latest_packages:
    key = (name, version)
    if key in project_map:
        repo = project_map[key]
        if repo in stars_map:
            combined.append({
                'PackageName': name,
                'Version': version,
                'Repo': repo,
                'Stars': stars_map[repo]
            })

# Sort and get top 5
top5 = sorted(combined, key=lambda x: x['Stars'], reverse=True)[:5]
print('__RESULT__:', json.dumps(top5, indent=1))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:2': ['project_info', 'project_packageversion'], 'var_functions.query_db:5': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:12': {'total_records': 661372, 'first_record': {'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectName': 'dataminingsupply/dms-io'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectName': 'isacvale/fc'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectName': 'laihaojie/jie'}], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:42': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_functions.query_db:50': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'Name': '@edgedev/firebase', 'Version': '1.0.12', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}'}, {'Name': '@eden-network/data', 'Version': '1.0.9-sev.5', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 14\n}'}], 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json'}

exec(code, env_args)
