code = """import json
import re

packageinfo_file = var_functions.query_db:12
with open(packageinfo_file, 'r') as f:
    packages = json.load(f)

packageversion_file = var_functions.query_db:8
with open(packageversion_file, 'r') as f:
    project_versions = json.load(f)

projectinfo_file = var_functions.query_db:16
with open(projectinfo_file, 'r') as f:
    project_info = json.load(f)

package_map = {(p['System'], p['Name'], p['Version']): p for p in packages}

project_map = {}
for pv in project_versions:
    key = (pv['System'], pv['Name'], pv['Version'])
    if key in package_map:
        project_name = pv['ProjectName']
        project_map[project_name] = pv

fork_pattern = re.compile(r'(\d+) forks')
projects_with_forks = []

for info in project_info:
    project_text = info['Project_Information']
    match = fork_pattern.search(project_text)
    if match:
        forks = int(match.group(1))
        projects_with_forks.append({
            'project_info': project_text,
            'forks': forks,
            'licenses': info.get('Licenses', '[]')
        })

print('__RESULT__:')
print(json.dumps({
    'total_packages': len(packages),
    'total_projects': len(projects_with_forks),
    'sample_projects': projects_with_forks[:5]
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:2': ['project_info', 'project_packageversion'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.'}, {'Project_Information': 'The project is hosted on GitHub under the name learnfrontend-dc/product-cart, and it currently has 2 open issues. It has garnered a total of 11 stars and has been forked 12 times.'}, {'Project_Information': 'The GitHub project ledgerproject/keypairoom currently has 3 open issues, 3 stars, and 0 forks.'}, {'Project_Information': 'The project leebyron/jasmine-check is hosted on GitHub and currently has 0 open issues, 11 stars, and 3 forks.'}, {'Project_Information': 'The project leebyron/testcheck-js on GitHub has an open issues count of 29, a stars count of 1185, and a forks count of 58, making it a notable repository in the community.'}, {'Project_Information': 'The project leecade/react-native-swiper is hosted on GitHub and has a total of 786 open issues, along with an impressive 10,249 stars and 2,392 forks, making it a popular choice among developers for implementing swiping functionality in React Native applications.'}], 'var_functions.query_db:16': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]'}, {'Project_Information': 'The GitHub project ledgerproject/keypairoom currently has 3 open issues, 3 stars, and 0 forks.', 'Licenses': '[\n  "AGPL-3.0"\n]'}, {'Project_Information': 'The project leebyron/jasmine-check is hosted on GitHub and currently has 0 open issues, 11 stars, and 3 forks.', 'Licenses': '[]'}, {'Project_Information': 'The project leebyron/testcheck-js on GitHub has an open issues count of 29, a stars count of 1185, and a forks count of 58, making it a notable repository in the community.', 'Licenses': '[\n  "non-standard"\n]'}, {'Project_Information': 'The project leecade/react-native-swiper is hosted on GitHub and has a total of 786 open issues, along with an impressive 10,249 stars and 2,392 forks, making it a popular choice among developers for implementing swiping functionality in React Native applications.', 'Licenses': '[\n  "MIT"\n]'}, {'Project_Information': 'The project legendjaden/aftablecolumn on GitHub currently has an open issues count of 35, a stars count of 136, and a forks count of 29.', 'Licenses': '[]'}, {'Project_Information': 'The project lekoarts/gatsby-themes on GitHub currently has 11 open issues, 1836 stars, and 568 forks, making it a popular choice among developers looking for Gatsby themes.', 'Licenses': '[\n  "MIT"\n]'}, {'Project_Information': 'The GitHub project lenconda/dollie currently has 0 open issues, 12 stars, and 3 forks, making it a noteworthy repository in its category.', 'Licenses': '[\n  "MIT"\n]'}, {'Project_Information': 'The project leo-ran/easy-node-reflect is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks, indicating that it may be in its early stages or not yet widely recognized within the GitHub community.', 'Licenses': '[]'}, {'Project_Information': 'The project named leo-ran/easy-node-server is hosted on GitHub and currently has an open issues count of 0, stars count of 0, and forks count of 0.', 'Licenses': '[]'}, {'Project_Information': 'The project named leofelix077/bunchofnothing on GitHub currently has 40 open issues, 0 stars, and 0 forks.', 'Licenses': '[]'}, {'Project_Information': 'The project leoilab/react-native-analytics-segment-io on GitHub currently has 26 open issues, 71 stars, and 36 forks, making it a notable repository for those interested in integrating analytics into React Native applications.', 'Licenses': '[\n  "MIT"\n]'}, {'Project_Information': 'The project on GitHub, named leonardparisi/easy-express-server, currently has an open issues count of 0, a stars count of 0, and a forks count of 0.', 'Licenses': '[]'}, {'Project_Information': 'The project leoroese/template-cli is hosted on GitHub and currently has 1 open issue, along with a total of 17 stars and 13 forks.', 'Licenses': '[]'}, {'Project_Information': 'The project is a GitHub repository named letrungdo/react-ui-component-lib, which currently has 0 open issues, 4 stars, and 0 forks.', 'Licenses': '[]'}, {'Project_Information': 'The project levelkdev/dxswap-sdk on GitHub currently has 27 open issues, 8 stars, and 11 forks, making it a noteworthy resource for developers interested in its functionality and contributions.', 'Licenses': '[\n  "AGPL-3.0"\n]'}]}

exec(code, env_args)
