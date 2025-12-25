code = """import json
import re

# Load project_info
try:
    with open(locals()['var_function-call-18100558052990097696'], 'r') as f:
        project_info_data = json.load(f)
except Exception as e:
    project_info_data = []

# Parse project_info
project_stars = {}
for row in project_info_data:
    info = row.get('Project_Information', '')
    if not info:
        continue
    
    # Extract Name
    name = None
    # Prioritize specific patterns
    patterns = [
        r'The project ([^\s]+) is hosted on GitHub',
        r'The project ([^\s]+) on GitHub',
        r'The project named ([^\s]+) on GitHub',
        r'The project is hosted on GitHub under the name ([^\s,]+)',
        r'The GitHub project named ([^\s]+) currently',
        r'The GitHub project ([^\s]+) currently',
        r'The project on GitHub, named ([^\s,]+)',
        r'The project named ([^\s]+) is hosted'
    ]
    
    for pat in patterns:
        m = re.search(pat, info)
        if m:
            name = m.group(1)
            break
            
    if name:
        name = name.rstrip('.,')
        
    # Extract Stars
    stars = 0
    m_stars = re.search(r'(\d{1,3}(?:,\d{3})*|\d+)\s+stars', info)
    if not m_stars:
         m_stars = re.search(r'stars count of (\d{1,3}(?:,\d{3})*|\d+)', info)
    
    if m_stars:
        stars = int(m_stars.group(1).replace(',', ''))
    
    if name:
        project_stars[name] = stars

# Load project_packageversion
try:
    with open(locals()['var_function-call-5096818199768988361'], 'r') as f:
        ppv_data = json.load(f)
except:
    ppv_data = []

# Map (Name, Version) -> ProjectName
pkg_proj_map = {}
valid_projects = set(project_stars.keys())
relevant_package_names = set()

for row in ppv_data:
    p_name = row.get('ProjectName')
    if p_name in valid_projects:
        key = (row['Name'], row['Version'])
        pkg_proj_map[key] = p_name
        relevant_package_names.add(row['Name'])

# Load packageinfo
try:
    with open(locals()['var_function-call-5096818199768988444'], 'r') as f:
        pkg_data = json.load(f)
except:
    pkg_data = []

# Find latest version for relevant packages
latest_versions = {} # Name -> (Version, ts)

for row in pkg_data:
    name = row['Name']
    if name not in relevant_package_names:
        continue
    
    ver = row['Version']
    try:
        ts = float(row.get('UpstreamPublishedAt', 0) or 0)
    except:
        ts = 0
        
    if name not in latest_versions:
        latest_versions[name] = (ver, ts)
    else:
        if ts > latest_versions[name][1]:
            latest_versions[name] = (ver, ts)

# Combine
results = []
for name, (ver, ts) in latest_versions.items():
    if (name, ver) in pkg_proj_map:
        p_name = pkg_proj_map[(name, ver)]
        s = project_stars.get(p_name, 0)
        results.append({'Package': name, 'Version': ver, 'Stars': s})

# Sort
results.sort(key=lambda x: x['Stars'], reverse=True)

print("__RESULT__:")
print(json.dumps(results[:5]))"""

env_args = {'var_function-call-3595456565223303209': ['packageinfo'], 'var_function-call-3595456565223303914': ['project_info', 'project_packageversion'], 'var_function-call-13184596017032728031': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'UpstreamPublishedAt': '1699345351000000.0'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}', 'UpstreamPublishedAt': '1670271173000000.0'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}', 'UpstreamPublishedAt': '1654791421000000.0'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}', 'UpstreamPublishedAt': '1624260093000000.0'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}', 'UpstreamPublishedAt': '1656518476000000.0'}], 'var_function-call-13184596017032725706': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_function-call-13184596017032727477': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-13770427510417345610': [{'COUNT(*)': '661372'}], 'var_function-call-13770427510417342585': [{'count_star()': '597602'}], 'var_function-call-13770427510417343656': [{'count_star()': '770'}], 'var_function-call-18100558052990097696': 'file_storage/function-call-18100558052990097696.json', 'var_function-call-5096818199768988361': 'file_storage/function-call-5096818199768988361.json', 'var_function-call-5096818199768988444': 'file_storage/function-call-5096818199768988444.json'}

exec(code, env_args)
