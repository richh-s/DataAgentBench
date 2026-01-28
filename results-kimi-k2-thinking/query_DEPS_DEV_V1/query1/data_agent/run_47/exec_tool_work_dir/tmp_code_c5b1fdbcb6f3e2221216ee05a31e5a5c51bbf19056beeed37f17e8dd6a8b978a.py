code = """import json
import re

# Load all NPM packages
f = globals()['var_functions.query_db:46']
with open(f, 'r') as file:
    all_npm_packages = json.load(file)

# Load project mappings
f2 = globals()['var_functions.query_db:44']
with open(f2, 'r') as file:
    project_mappings = json.load(file)

# Load project info
f3 = globals()['var_functions.query_db:36']
with open(f3, 'r') as file:
    project_info_raw = json.load(file)

# Step 1: Find latest release version per package
latest_versions = {}
for pkg in all_npm_packages:
    try:
        vi = json.loads(pkg['VersionInfo'].replace('\n', ' ').strip())
        if vi.get('IsRelease', False):
            name = pkg['Name']
            version = pkg['Version']
            ordinal = vi.get('Ordinal', 0)
            if name not in latest_versions or ordinal > latest_versions[name]['Ordinal']:
                latest_versions[name] = {'Name': name, 'Version': version, 'Ordinal': ordinal}
    except:
        continue

latest_packages = list(latest_versions.values())

# Step 2: Map packages to projects
proj_lookup = {}
for m in project_mappings:
    proj_lookup[(m['Name'], m['Version'])] = m['ProjectName']

matched = []
for pkg in latest_packages:
    key = (pkg['Name'], pkg['Version'])
    if key in proj_lookup:
        matched.append({
            'Name': pkg['Name'],
            'Version': pkg['Version'],
            'Project': proj_lookup[key]
        })

# Step 3: Extract stars from project info
proj_stars = {}
for info in project_info_raw:
    text = info['Project_Information']
    stars_match = re.search(r'(\d+(?:,\d+)*)\s+stars', text)
    if stars_match:
        stars = int(stars_match.group(1).replace(',', ''))
        proj_match = re.search(r'The project\s+([\w-]+/[\w-]+)', text)
        if proj_match:
            proj_stars[proj_match.group(1)] = stars

# Step 4: Add stars to matched packages
result = []
for m in matched:
    if m['Project'] in proj_stars:
        result.append({
            'PackageName': m['Name'],
            'Version': m['Version'],
            'Project': m['Project'],
            'Stars': proj_stars[m['Project']]
        })

# Step 5: Sort by stars and get top 5
top_5 = sorted(result, key=lambda x: x['Stars'], reverse=True)[:5]

out = {
    'total_packages': len(all_npm_packages),
    'latest_release': len(latest_packages),
    'matched_projects': len(matched),
    'with_star_data': len(result),
    'top_5': top_5
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:2': ['project_info', 'project_packageversion'], 'var_functions.query_db:5': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'Name': '@edgedev/firebase', 'Version': '1.0.12', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}'}, {'Name': '@eden-network/data', 'Version': '1.0.9-sev.5', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 14\n}'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:16': 'file_storage/functions.execute_python:16.json', 'var_functions.query_db:18': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectName': 'dataminingsupply/dms-io'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectName': 'isacvale/fc'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.10', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.17', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@dlcs/ng', 'Version': '1.0.0', 'ProjectName': 'winup/dlcs-ng'}, {'System': 'NPM', 'Name': '@dms/cli', 'Version': '1.0.1', 'ProjectName': 'dataminingsupply/dms-cli'}, {'System': 'NPM', 'Name': '@dms/cli', 'Version': '1.0.0', 'ProjectName': 'dataminingsupply/dms-cli'}], 'var_functions.query_db:20': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.'}, {'Project_Information': 'The project is hosted on GitHub under the name learnfrontend-dc/product-cart, and it currently has 2 open issues. It has garnered a total of 11 stars and has been forked 12 times.'}, {'Project_Information': 'The GitHub project ledgerproject/keypairoom currently has 3 open issues, 3 stars, and 0 forks.'}, {'Project_Information': 'The project leebyron/jasmine-check is hosted on GitHub and currently has 0 open issues, 11 stars, and 3 forks.'}, {'Project_Information': 'The project leebyron/testcheck-js on GitHub has an open issues count of 29, a stars count of 1185, and a forks count of 58, making it a notable repository in the community.'}, {'Project_Information': 'The project leecade/react-native-swiper is hosted on GitHub and has a total of 786 open issues, along with an impressive 10,249 stars and 2,392 forks, making it a popular choice among developers for implementing swiping functionality in React Native applications.'}, {'Project_Information': 'The project legendjaden/aftablecolumn on GitHub currently has an open issues count of 35, a stars count of 136, and a forks count of 29.'}, {'Project_Information': 'The project lekoarts/gatsby-themes on GitHub currently has 11 open issues, 1836 stars, and 568 forks, making it a popular choice among developers looking for Gatsby themes.'}, {'Project_Information': 'The GitHub project lenconda/dollie currently has 0 open issues, 12 stars, and 3 forks, making it a noteworthy repository in its category.'}, {'Project_Information': 'The project leo-ran/easy-node-reflect is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks, indicating that it may be in its early stages or not yet widely recognized within the GitHub community.'}, {'Project_Information': 'The project named leo-ran/easy-node-server is hosted on GitHub and currently has an open issues count of 0, stars count of 0, and forks count of 0.'}, {'Project_Information': 'The project named leofelix077/bunchofnothing on GitHub currently has 40 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leoilab/react-native-analytics-segment-io on GitHub currently has 26 open issues, 71 stars, and 36 forks, making it a notable repository for those interested in integrating analytics into React Native applications.'}, {'Project_Information': 'The project on GitHub, named leonardparisi/easy-express-server, currently has an open issues count of 0, a stars count of 0, and a forks count of 0.'}, {'Project_Information': 'The project leoroese/template-cli is hosted on GitHub and currently has 1 open issue, along with a total of 17 stars and 13 forks.'}, {'Project_Information': 'The project is a GitHub repository named letrungdo/react-ui-component-lib, which currently has 0 open issues, 4 stars, and 0 forks.'}], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:30': {'npm_packages_count': 10000, 'project_mappings_count': 597602}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.execute_python:34': {'total_mappings': 597602, 'npm_mappings': 597602, 'unique_combinations': 325940}, 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:40': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.'}, {'Project_Information': 'The project is hosted on GitHub under the name learnfrontend-dc/product-cart, and it currently has 2 open issues. It has garnered a total of 11 stars and has been forked 12 times.'}, {'Project_Information': 'The GitHub project ledgerproject/keypairoom currently has 3 open issues, 3 stars, and 0 forks.'}, {'Project_Information': 'The project leebyron/jasmine-check is hosted on GitHub and currently has 0 open issues, 11 stars, and 3 forks.'}, {'Project_Information': 'The project leebyron/testcheck-js on GitHub has an open issues count of 29, a stars count of 1185, and a forks count of 58, making it a notable repository in the community.'}, {'Project_Information': 'The project leecade/react-native-swiper is hosted on GitHub and has a total of 786 open issues, along with an impressive 10,249 stars and 2,392 forks, making it a popular choice among developers for implementing swiping functionality in React Native applications.'}], 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.execute_python:48': {'total_npm_packages': 661372, 'total_project_mappings': 597602, 'project_info_records': 100}, 'var_functions.execute_python:52': {'total_packages': 661372, 'total_mappings': 325940, 'projects_with_stars': 57, 'sample_mappings': [['lberrocal/npm-packages-template', 0], ['leaflet/leaflet', 417], ['leandrowd/react-responsive-carousel', 2534], ['leebyron/jasmine-check', 11], ['leecade/react-native-swiper', 10249], ['lekoarts/gatsby-themes', 1836], ['leo-ran/easy-node-reflect', 0], ['leoilab/react-native-analytics-segment-io', 71], ['leoroese/template-cli', 17], ['levelkdev/dxswap-sdk', 8]]}, 'var_functions.execute_python:58': {'npm_packages': 661372, 'mappings': 597602, 'project_info': 100}}

exec(code, env_args)
