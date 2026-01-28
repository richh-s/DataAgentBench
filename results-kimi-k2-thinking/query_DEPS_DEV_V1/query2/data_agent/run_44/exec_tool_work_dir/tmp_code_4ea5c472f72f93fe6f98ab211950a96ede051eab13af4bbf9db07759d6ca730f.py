code = """import json
import re

# Load all packageproject mappings
proj_pkg_file = locals()['var_functions.query_db:5']
with open(proj_pkg_file, 'r') as f:
    all_mappings = json.load(f)

# Filter only NPM mappings
npm_mappings = [m for m in all_mappings if m.get('System') == 'NPM']

# Create a dictionary to map project name to package info
project_to_package = {}
for mapping in npm_mappings:
    project_name = mapping.get('ProjectName')
    if project_name:
        project_to_package[project_name] = {
            'package_name': mapping.get('Name'),
            'package_version': mapping.get('Version')
        }

# Load all project info
proj_info_file = locals()['var_functions.query_db:12']
with open(proj_info_file, 'r') as f:
    all_project_info = json.load(f)

# Extract fork counts from all projects
project_stats = []
fork_pattern = r'(\d+) forks?'
stars_pattern = r'(\d+) stars?'
issues_pattern = r'(\d+) open issues'

for proj in all_project_info:
    info_text = proj.get('Project_Information', '')
    
    fork_match = re.search(fork_pattern, info_text, re.IGNORECASE)
    stars_match = re.search(stars_pattern, info_text, re.IGNORECASE)
    issues_match = re.search(issues_pattern, info_text, re.IGNORECASE)
    
    if fork_match:  # Only include projects that have forks
        fork_count = int(fork_match.group(1))
        stars_count = int(stars_match.group(1)) if stars_match else 0
        issues_count = int(issues_match.group(1)) if issues_match else 0
        
        # Extract project name
        proj_name = None
        if 'The project ' in info_text:
            proj_part = info_text.split('The project ')[1].split(' ')[0]
            proj_name = proj_part.rstrip(',:')
        
        if proj_name:
            project_stats.append({
                'name': proj_name,
                'forks': fork_count,
                'stars': stars_count,
                'issues': issues_count,
                'package_info': project_to_package.get(proj_name)
            })

# Sort by fork count
top_projects = sorted(project_stats, key=lambda x: x['forks'], reverse=True)[:20]

print('__RESULT__:')
print(json.dumps({
    'total_npm_packages_mapped': len(project_to_package),
    'total_projects_analyzed': len(all_project_info),
    'projects_with_forks': len(project_stats),
    'top_projects': top_projects
}, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'Found 1000 packages with MIT license and IsRelease=true', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:7': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Homepage': 'None'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Homepage': 'https://leafletjs.com'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Homepage': 'None'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/'}, {'Project_Information': 'The project is hosted on GitHub under the name learnfrontend-dc/product-cart, and it currently has 2 open issues. It has garnered a total of 11 stars and has been forked 12 times.', 'Licenses': '[]', 'Homepage': 'None'}, {'Project_Information': 'The GitHub project ledgerproject/keypairoom currently has 3 open issues, 3 stars, and 0 forks.', 'Licenses': '[\n  "AGPL-3.0"\n]', 'Homepage': 'None'}, {'Project_Information': 'The project leebyron/jasmine-check is hosted on GitHub and currently has 0 open issues, 11 stars, and 3 forks.', 'Licenses': '[]', 'Homepage': 'None'}, {'Project_Information': 'The project leebyron/testcheck-js on GitHub has an open issues count of 29, a stars count of 1185, and a forks count of 58, making it a notable repository in the community.', 'Licenses': '[\n  "non-standard"\n]', 'Homepage': 'http://leebyron.com/testcheck-js'}, {'Project_Information': 'The project leecade/react-native-swiper is hosted on GitHub and has a total of 786 open issues, along with an impressive 10,249 stars and 2,392 forks, making it a popular choice among developers for implementing swiping functionality in React Native applications.', 'Licenses': '[\n  "MIT"\n]', 'Homepage': 'None'}], 'var_functions.execute_python:8': {'total_packages': 1000, 'matched_projects': 1000}, 'var_functions.execute_python:10': {'matched_mappings': 1000, 'unique_projects': 243}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'total_packages': 1000, 'matching_projects': 7, 'top_5': [{'project': 'taixw2/dx', 'forks': 14, 'stars': 84, 'package': '@dxjs/core'}, {'project': 'n43/easyapp', 'forks': 0, 'stars': 0, 'package': '@easyapp/wechat'}, {'project': 'luzzif/ethereum-contacts-registry', 'forks': 0, 'stars': 5, 'package': '@ecr/contracts'}, {'project': 'stephenliu1944/beancommons-proxy', 'forks': 0, 'stars': 0, 'package': '@easytool/proxy-config'}, {'project': 'shanebo/balm', 'forks': 0, 'stars': 0, 'package': '@dylan/balm'}]}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
