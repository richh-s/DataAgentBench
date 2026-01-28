code = """import json
import re

# Load package data
pkg_file = locals()['var_functions.query_db:0']
with open(pkg_file, 'r') as f:
    packages = json.load(f)

# Load project mappings
proj_pkg_file = locals()['var_functions.query_db:5']
with open(proj_pkg_file, 'r') as f:
    proj_mappings = json.load(f)

# Load project info
proj_info_file = locals()['var_functions.query_db:12']
with open(proj_info_file, 'r') as f:
    project_info = json.load(f)

# Step 1: Create a lookup for packages by (System, Name, Version)
package_lookup = {(pkg['System'], pkg['Name'], pkg['Version']): pkg for pkg in packages}

# Step 2: Create a lookup for project mappings by package key
project_mapping_lookup = {}
for mapping in proj_mappings:
    key = (mapping['System'], mapping['Name'], mapping['Version'])
    project_mapping_lookup[key] = mapping

# Step 3: Find matches and collect project information
project_data = []
fork_pattern = r'(\d+) forks?'
stars_pattern = r'(\d+) stars?'
project_name_pattern = r'The project ([^ ]+)'

# Create a dictionary to store the highest fork count for each project
project_fork_counts = {}

for pkg_key, pkg in package_lookup.items():
    if pkg_key in project_mapping_lookup:
        mapping = project_mapping_lookup[pkg_key]
        project_name = mapping['ProjectName']
        
        # Find the project info for this project name
        project_info_text = None
        for proj in project_info:
            if project_name in proj['Project_Information']:
                project_info_text = proj['Project_Information']
                break
        
        if project_info_text:
            # Extract fork count
            fork_match = re.search(fork_pattern, project_info_text, re.IGNORECASE)
            if fork_match:
                fork_count = int(fork_match.group(1))
                
                # Store the highest fork count for this project
                if project_name not in project_fork_counts or fork_count > project_fork_counts[project_name]['forks']:
                    stars_match = re.search(stars_pattern, project_info_text, re.IGNORECASE)
                    stars_count = int(stars_match.group(1)) if stars_match else 0
                    
                    project_fork_counts[project_name] = {
                        'project': project_name,
                        'forks': fork_count,
                        'stars': stars_count,
                        'package': pkg['Name']
                    }

# Sort projects by fork count
sorted_projects = sorted(project_fork_counts.values(), key=lambda x: x['forks'], reverse=True)

# Get top 5
top_5 = sorted_projects[:5]

print('__RESULT__:')
print(json.dumps({
    'total_packages': len(packages),
    'matching_projects': len(project_fork_counts),
    'top_5': top_5
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'Found 1000 packages with MIT license and IsRelease=true', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:7': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Homepage': 'None'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Homepage': 'https://leafletjs.com'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Homepage': 'None'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/'}, {'Project_Information': 'The project is hosted on GitHub under the name learnfrontend-dc/product-cart, and it currently has 2 open issues. It has garnered a total of 11 stars and has been forked 12 times.', 'Licenses': '[]', 'Homepage': 'None'}, {'Project_Information': 'The GitHub project ledgerproject/keypairoom currently has 3 open issues, 3 stars, and 0 forks.', 'Licenses': '[\n  "AGPL-3.0"\n]', 'Homepage': 'None'}, {'Project_Information': 'The project leebyron/jasmine-check is hosted on GitHub and currently has 0 open issues, 11 stars, and 3 forks.', 'Licenses': '[]', 'Homepage': 'None'}, {'Project_Information': 'The project leebyron/testcheck-js on GitHub has an open issues count of 29, a stars count of 1185, and a forks count of 58, making it a notable repository in the community.', 'Licenses': '[\n  "non-standard"\n]', 'Homepage': 'http://leebyron.com/testcheck-js'}, {'Project_Information': 'The project leecade/react-native-swiper is hosted on GitHub and has a total of 786 open issues, along with an impressive 10,249 stars and 2,392 forks, making it a popular choice among developers for implementing swiping functionality in React Native applications.', 'Licenses': '[\n  "MIT"\n]', 'Homepage': 'None'}], 'var_functions.execute_python:8': {'total_packages': 1000, 'matched_projects': 1000}, 'var_functions.execute_python:10': {'matched_mappings': 1000, 'unique_projects': 243}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
