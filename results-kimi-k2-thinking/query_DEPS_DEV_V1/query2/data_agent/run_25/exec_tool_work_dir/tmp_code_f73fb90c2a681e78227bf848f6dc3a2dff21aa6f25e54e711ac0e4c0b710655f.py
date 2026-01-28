code = """import json
import re

# Load data from files
with open('var_functions.query_db:5', 'r') as f:
    package_data = json.load(f)

with open('var_functions.query_db:6', 'r') as f:
    project_package_data = json.load(f)

with open('var_functions.query_db:18', 'r') as f:
    project_info_data = json.load(f)

# Filter packages that are NPM with MIT license and release versions
release_packages = []
for pkg in package_data:
    if pkg['System'] == 'NPM' and 'MIT' in pkg['Licenses']:
        try:
            version_info = json.loads(pkg['VersionInfo'])
            if version_info.get('IsRelease'):
                release_packages.append(pkg)
        except:
            pass

# Create lookup for release packages by System, Name, Version
package_lookup = {}
for pkg in release_packages:
    key = (pkg['System'], pkg['Name'], pkg['Version'])
    package_lookup[key] = pkg

# Process project info to extract project name and fork count
project_info_lookup = {}
for proj in project_info_data:
    proj_info = proj['Project_Information']
    
    # Extract project name (owner/repo format)
    project_name = None
    
    # Look for patterns like "owner/repo" or "project owner/repo"
    patterns = [
        r'\s([a-zA-Z0-9_-]+/[a-zA-Z0-9_-]+)\s',
        r'project\s+([a-zA-Z0-9_-]+/[a-zA-Z0-9_-]+)',
        r'"([a-zA-Z0-9_-]+/[a-zA-Z0-9_-]+)"'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, proj_info)
        if match:
            project_name = match.group(1).lower()
            break
    
    if not project_name:
        continue
    
    # Extract fork count (handle variations like "forks", "fork")
    fork_match = re.search(r'(\d+)\s+forks?', proj_info, re.IGNORECASE)
    if fork_match:
        fork_count = int(fork_match.group(1))
    else:
        fork_count = 0
    
    project_info_lookup[project_name] = {
        'ProjectName': project_name,
        'forks': fork_count,
        'ProjectInfo': proj
    }

# Match NPM packages with GitHub projects
matched_projects = {}

for pp in project_package_data:
    if pp['System'] == 'NPM' and pp['ProjectType'] == 'GITHUB':
        key = (pp['System'], pp['Name'], pp['Version'])
        if key in package_lookup:
            project_name = pp['ProjectName'].lower()
            if project_name in project_info_lookup:
                proj_data = project_info_lookup[project_name]
                # Include package info
                proj_data = proj_data.copy()
                proj_data['Package'] = pp
                matched_projects[project_name] = proj_data

# Sort by fork count and get top 5
top_projects = sorted(matched_projects.values(), key=lambda x: x['forks'], reverse=True)[:5]

# Format results
result = []
for proj in top_projects:
    result.append({
        'project': proj['ProjectName'],
        'forks': proj['forks'],
        'package_name': proj['Package']['Name'] if 'Package' in proj else 'Unknown',
        'version': proj['Package']['Version'] if 'Package' in proj else 'Unknown'
    })

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:2': ['project_info', 'project_packageversion'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [], 'var_functions.query_db:10': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project is hosted on GitHub under the name learnfrontend-dc/product-cart, and it currently has 2 open issues. It has garnered a total of 11 stars and has been forked 12 times.', 'Licenses': '[]', 'Description': 'None', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The GitHub project ledgerproject/keypairoom currently has 3 open issues, 3 stars, and 0 forks.', 'Licenses': '[\n  "AGPL-3.0"\n]', 'Description': 'Component to generate and regenerate a keypair, in a deterministic and private way', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leebyron/jasmine-check is hosted on GitHub and currently has 0 open issues, 11 stars, and 3 forks.', 'Licenses': '[]', 'Description': 'Generative property testing for Jasmine', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leebyron/testcheck-js on GitHub has an open issues count of 29, a stars count of 1185, and a forks count of 58, making it a notable repository in the community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': 'Generative testing for JavaScript', 'Homepage': 'http://leebyron.com/testcheck-js', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leecade/react-native-swiper is hosted on GitHub and has a total of 786 open issues, along with an impressive 10,249 stars and 2,392 forks, making it a popular choice among developers for implementing swiping functionality in React Native applications.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'The best Swiper component for React Native.', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_functions.execute_python:16': {'package_count': 176998, 'project_package_count': 591699, 'project_info_count': 10}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:22': {'package_str_type': "<class 'str'>", 'project_package_str_type': "<class 'str'>", 'project_info_str_type': "<class 'str'>", 'package_is_str': True, 'project_package_is_str': True, 'project_info_is_str': True}, 'var_functions.execute_python:24': {'package_count': 176998, 'project_package_count': 591699, 'project_info_count': 770}}

exec(code, env_args)
