code = """import json
import re

# Load package data
pkg_file = locals()['var_functions.query_db:0']
with open(pkg_file, 'r') as f:
    packages = json.load(f)

# Create a set of (System, Name, Version) tuples for fast lookup
pkg_keys = {(pkg['System'], pkg['Name'], pkg['Version']) for pkg in packages}

# Load project_packageversion data
proj_pkg_file = locals()['var_functions.query_db:5']
with open(proj_pkg_file, 'r') as f:
    proj_mappings = json.load(f)

# Filter to only include mappings for our packages
matched_mappings = []
for mapping in proj_mappings:
    key = (mapping['System'], mapping['Name'], mapping['Version'])
    if key in pkg_keys:
        matched_mappings.append(mapping)

print('__RESULT__:')
print(json.dumps({
    'total_packages': len(packages),
    'matched_projects': len(matched_mappings)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'Found 1000 packages with MIT license and IsRelease=true', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:7': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Homepage': 'None'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Homepage': 'https://leafletjs.com'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Homepage': 'None'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/'}, {'Project_Information': 'The project is hosted on GitHub under the name learnfrontend-dc/product-cart, and it currently has 2 open issues. It has garnered a total of 11 stars and has been forked 12 times.', 'Licenses': '[]', 'Homepage': 'None'}, {'Project_Information': 'The GitHub project ledgerproject/keypairoom currently has 3 open issues, 3 stars, and 0 forks.', 'Licenses': '[\n  "AGPL-3.0"\n]', 'Homepage': 'None'}, {'Project_Information': 'The project leebyron/jasmine-check is hosted on GitHub and currently has 0 open issues, 11 stars, and 3 forks.', 'Licenses': '[]', 'Homepage': 'None'}, {'Project_Information': 'The project leebyron/testcheck-js on GitHub has an open issues count of 29, a stars count of 1185, and a forks count of 58, making it a notable repository in the community.', 'Licenses': '[\n  "non-standard"\n]', 'Homepage': 'http://leebyron.com/testcheck-js'}, {'Project_Information': 'The project leecade/react-native-swiper is hosted on GitHub and has a total of 786 open issues, along with an impressive 10,249 stars and 2,392 forks, making it a popular choice among developers for implementing swiping functionality in React Native applications.', 'Licenses': '[\n  "MIT"\n]', 'Homepage': 'None'}]}

exec(code, env_args)
