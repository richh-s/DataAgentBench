code = """import json
import re

# Load data from file paths stored in variables
package_data_path = locals().get('var_functions.query_db:5')
project_package_data_path = locals().get('var_functions.query_db:6')
project_info_data_path = locals().get('var_functions.query_db:18')

# Read the JSON files
with open(package_data_path, 'r') as f:
    package_data = json.load(f)

with open(project_package_data_path, 'r') as f:
    project_package_data = json.load(f)

with open(project_info_data_path, 'r') as f:
    project_info_data = json.load(f)

# Filter for NPM packages with MIT license and release version
npm_mit_release_packages = []
for pkg in package_data:
    if pkg.get('System') == 'NPM' and 'MIT' in pkg.get('Licenses', ''):
        try:
            version_info_str = pkg.get('VersionInfo', '{}')
            version_info = json.loads(version_info_str)
            if version_info.get('IsRelease'):
                npm_mit_release_packages.append(pkg)
        except:
            pass

# Build lookup by (System, Name, Version)
package_lookup = {}
for pkg in npm_mit_release_packages:
    key = (pkg['System'], pkg['Name'], pkg['Version'])
    package_lookup[key] = pkg

# Process project_info to extract project name and fork count
project_info_lookup = {}
for proj in project_info_data:
    proj_info_text = proj['Project_Information']
    
    # Extract project name (owner/repo format)
    project_name = None
    
    # Common pattern: "owner/repo" in the text
    patterns = [
        r'(?:^|\s|/)([a-zA-Z0-9_-]+/[a-zA-Z0-9_-]+)(?:\s|,|\.|"|\')',
        r'project\s+([a-zA-Z0-9_-]+/[a-zA-Z0-9_-]+)',
        r'"([a-zA-Z0-9_-]+/[a-zA-Z0-9_-]+)"'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, proj_info_text)
        if match:
            project_name = match.group(1).strip().lower()
            break
    
    if not project_name:
        continue
    
    # Extract fork count
    fork_pattern = r'(\d+)\s+forks?'
    fork_match = re.search(fork_pattern, proj_info_text, re.IGNORECASE)
    if fork_match:
        fork_count = int(fork_match.group(1))
    else:
        fork_count = 0
    
    # Store project info
    project_info_lookup[project_name] = {
        'project_name': project_name,
        'forks': fork_count,
        'raw_info': proj
    }

# Match packages with GitHub projects via project_packageversion
matched = []
for pp in project_package_data:
    if pp.get('System') == 'NPM' and pp.get('ProjectType') == 'GITHUB':
        key = (pp['System'], pp['Name'], pp['Version'])
        if key in package_lookup:
            gh_project = pp.get('ProjectName', '').lower()
            if gh_project in project_info_lookup:
                proj_data = project_info_lookup[gh_project]
                matched.append({
                    'project': gh_project,
                    'forks': proj_data['forks'],
                    'package_name': pp['Name'],
                    'version': pp['Version']
                })

# Sort by fork count and get top 5
top_5 = sorted(matched, key=lambda x: x['forks'], reverse=True)[:5]

print('__RESULT__:')
print(json.dumps(top_5, indent=2))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:2': ['project_info', 'project_packageversion'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [], 'var_functions.query_db:10': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project is hosted on GitHub under the name learnfrontend-dc/product-cart, and it currently has 2 open issues. It has garnered a total of 11 stars and has been forked 12 times.', 'Licenses': '[]', 'Description': 'None', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The GitHub project ledgerproject/keypairoom currently has 3 open issues, 3 stars, and 0 forks.', 'Licenses': '[\n  "AGPL-3.0"\n]', 'Description': 'Component to generate and regenerate a keypair, in a deterministic and private way', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leebyron/jasmine-check is hosted on GitHub and currently has 0 open issues, 11 stars, and 3 forks.', 'Licenses': '[]', 'Description': 'Generative property testing for Jasmine', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leebyron/testcheck-js on GitHub has an open issues count of 29, a stars count of 1185, and a forks count of 58, making it a notable repository in the community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': 'Generative testing for JavaScript', 'Homepage': 'http://leebyron.com/testcheck-js', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leecade/react-native-swiper is hosted on GitHub and has a total of 786 open issues, along with an impressive 10,249 stars and 2,392 forks, making it a popular choice among developers for implementing swiping functionality in React Native applications.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'The best Swiper component for React Native.', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_functions.execute_python:16': {'package_count': 176998, 'project_package_count': 591699, 'project_info_count': 10}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:22': {'package_str_type': "<class 'str'>", 'project_package_str_type': "<class 'str'>", 'project_info_str_type': "<class 'str'>", 'package_is_str': True, 'project_package_is_str': True, 'project_info_is_str': True}, 'var_functions.execute_python:24': {'package_count': 176998, 'project_package_count': 591699, 'project_info_count': 770}}

exec(code, env_args)
