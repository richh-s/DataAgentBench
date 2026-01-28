code = """import json
import re

# Load data
project_mapping_path = locals()['var_functions.query_db:9']
package_path = locals()['var_functions.query_db:0']
project_fork_info_path = locals()['var_functions.query_db:20']

with open(package_path, 'r') as f:
    packages = json.load(f)

with open(project_mapping_path, 'r') as f:
    project_mappings = json.load(f)

with open(project_fork_info_path, 'r') as f:
    all_fork_projects = json.load(f)

# Create package lookup
package_dict = {(p['System'], p['Name'], p['Version']): p for p in packages}

# Build valid project names and also map project_name -> package names
valid_project_names = set()
project_to_packages = {}

for mapping in project_mappings:
    key = (mapping['System'], mapping['Name'], mapping['Version'])
    if key in package_dict:
        project_name = mapping['ProjectName']
        valid_project_names.add(project_name)
        if project_name not in project_to_packages:
            project_to_packages[project_name] = set()
        project_to_packages[project_name].add(mapping['Name'])

# Parse fork data and filter to valid projects
valid_projects_with_forks = []
for proj in all_fork_projects:
    info = proj['Project_Information']
    
    # Extract fork count
    fork_match = re.search(r'(\d+) forks?', info)
    if not fork_match:
        continue
    
    forks = int(fork_match.group(1))
    
    # Extract project name
    name_match = re.search(r'the project\s+([^\s]+/[^\s]+)\s+on\s+GitHub', info, re.IGNORECASE)
    if not name_match:
        name_match = re.search(r'GitHub\s+(?:project|repository)\s+([^\s]+/[^\s]+)', info, re.IGNORECASE)
    if not name_match:
        name_match = re.search(r'GitHub\s+under\s+the\s+name\s+([^\s]+/[^\s]+)', info, re.IGNORECASE)
    if not name_match:
        continue
    
    project_name = name_match.group(1).rstrip(',')
    
    # Check if this is a valid project
    if project_name in valid_project_names:
        packages_for_project = list(project_to_packages.get(project_name, []))[:3]  # Get up to 3 package names
        valid_projects_with_forks.append({
            'project_name': project_name,
            'forks': forks,
            'package_names': packages_for_project
        })

# Sort and get top 5
sorted_projects = sorted(valid_projects_with_forks, key=lambda x: x['forks'], reverse=True)
top_5 = sorted_projects[:5]

# Format result for verification
verification = {
    'total_valid_projects_with_forks': len(valid_projects_with_forks),
    'top_5': top_5
}

print('__RESULT__:')
print(json.dumps(verification, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'count': 176998, 'first_3_records': [{'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'System': 'NPM', 'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'System': 'NPM', 'Name': '@eclipsejs/cli', 'Version': '1.0.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}'}]}, 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:8': {'package_count': 176998, 'project_count': 591699, 'sample_package': {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, 'sample_project': {'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectName': 'dataminingsupply/dms-io'}}, 'var_functions.query_db:10': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]'}], 'var_functions.execute_python:12': {'total_packages_with_mit_license_and_release': 176998, 'total_npm_projects': 591699, 'matched_projects': 5336, 'matched_package_versions': 162114}, 'var_functions.execute_python:14': {'project_name_count': 5336, 'sample_names': ['ljharb/has-symbols', 'ditdot-dev/vue-flow-form', 'dynamis-finance/dynamis-ui-kit', 'dogmoneyswap/dogmoneyswap', 'doc-process/ra-language-romanian', 'global-repo/global-sdk', 'donutteam/custom-api-classes', 'eden-js/eslint-config-eden', 'dtereshenko/react-gpt', 'dolittle-runtime/contracts']}, 'var_functions.query_db:16': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.'}, {'Project_Information': 'The project is hosted on GitHub under the name learnfrontend-dc/product-cart, and it currently has 2 open issues. It has garnered a total of 11 stars and has been forked 12 times.'}, {'Project_Information': 'The project leebyron/jasmine-check is hosted on GitHub and currently has 0 open issues, 11 stars, and 3 forks.'}, {'Project_Information': 'The project leebyron/testcheck-js on GitHub has an open issues count of 29, a stars count of 1185, and a forks count of 58, making it a notable repository in the community.'}, {'Project_Information': 'The project leecade/react-native-swiper is hosted on GitHub and has a total of 786 open issues, along with an impressive 10,249 stars and 2,392 forks, making it a popular choice among developers for implementing swiping functionality in React Native applications.'}, {'Project_Information': 'The project legendjaden/aftablecolumn on GitHub currently has an open issues count of 35, a stars count of 136, and a forks count of 29.'}, {'Project_Information': 'The project lekoarts/gatsby-themes on GitHub currently has 11 open issues, 1836 stars, and 568 forks, making it a popular choice among developers looking for Gatsby themes.'}, {'Project_Information': 'The project leo-ran/easy-node-reflect is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks, indicating that it may be in its early stages or not yet widely recognized within the GitHub community.'}, {'Project_Information': 'The project named leo-ran/easy-node-server is hosted on GitHub and currently has an open issues count of 0, stars count of 0, and forks count of 0.'}, {'Project_Information': 'The project named leofelix077/bunchofnothing on GitHub currently has 40 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leoilab/react-native-analytics-segment-io on GitHub currently has 26 open issues, 71 stars, and 36 forks, making it a notable repository for those interested in integrating analytics into React Native applications.'}, {'Project_Information': 'The project on GitHub, named leonardparisi/easy-express-server, currently has an open issues count of 0, a stars count of 0, and a forks count of 0.'}, {'Project_Information': 'The project leoroese/template-cli is hosted on GitHub and currently has 1 open issue, along with a total of 17 stars and 13 forks.'}, {'Project_Information': 'The project levelkdev/dxswap-sdk on GitHub currently has 27 open issues, 8 stars, and 11 forks, making it a noteworthy resource for developers interested in its functionality and contributions.'}, {'Project_Information': 'The project leviticusmb/ghostly on GitHub currently has 0 open issues, 2 stars, and 1 fork.'}, {'Project_Information': 'The project libertydsnp/activity-content on GitHub currently has 1 open issue, 1 star, and 0 forks.'}], 'var_functions.execute_python:18': {'project_count': 5336, 'first_few': ['ahmadreza-s/dotlottie-player', 'dusty-phillips/rescript-zora', 'donotjs/donot-transform-rollup', 'faye/websocket-extensions-node', 'ducdhm/dudo-adminui']}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': [{'project_name': 'leaflet/leaflet', 'forks': 5782, 'info': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'project_name': 'theia-ide/theia', 'forks': 2451, 'info': 'The project theia-ide/theia on GitHub is an open-source IDE with an open issues count of 1359, and it has garnered a significant following, evident from its 18526 stars and 2451 forks.'}, {'project_name': 'sass/node-sass', 'forks': 1326, 'info': 'The project sass/node-sass on GitHub currently has 189 open issues, 8498 stars, and 1326 forks, making it a popular choice among developers for managing stylesheets with Sass.'}, {'project_name': 'shaka-project/shaka-player', 'forks': 1319, 'info': 'The project shaka-project/shaka-player on GitHub is a well-regarded open-source initiative, currently featuring 110 open issues, 6949 stars, and 1319 forks, reflecting its popularity and active development within the community.'}, {'project_name': 'microsoft/typescript-website,', 'forks': 1308, 'info': 'The project is hosted on GitHub under the name microsoft/typescript-website, which currently has 32 open issues, 2019 stars, and 1308 forks.'}], 'var_functions.execute_python:24': {'matching_projects': 5336}, 'var_functions.execute_python:26': {'valid_project_count': 5336, 'sample_valid': ['doutorspace/isvalid', 'donutteam/eslint-config', 'ecodev/natural-search', 'dodi-smart/nuki-graphql-api', 'aeb-labs/graphql-weaver', 'segmentio/analytics-node', 'dotchev/cpu-percentage', 'doubco/logbook', 'easy-webpack/config-babel', 'danghungtb26/dvh-module']}, 'var_functions.execute_python:28': ['1. sass/node-sass - 1326 forks', '2. microsoft/typescript-website - 1308 forks', '3. ternjs/acorn - 944 forks', '4. thejameskyle/react-loadable - 857 forks', '5. tailwindcss/tailwindcss - 848 forks']}

exec(code, env_args)
