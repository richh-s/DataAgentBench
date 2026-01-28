code = """import json
import re

# Load all required data
pkg_file = locals()['var_functions.query_db:28']
with open(pkg_file, 'r') as f:
    packages = json.load(f)

proj_pkg_file = locals()['var_functions.query_db:5']
with open(proj_pkg_file, 'r') as f:
    proj_mappings = json.load(f)

proj_info_file = locals()['var_functions.query_db:12']
with open(proj_info_file, 'r') as f:
    project_info = json.load(f)

# Build lookups
package_lookup = {(pkg['System'], pkg['Name'], pkg['Version']): pkg for pkg in packages}

# Build npm package to project mapping
package_to_project = {}
for mapping in proj_mappings:
    if mapping.get('System') == 'NPM':
        package_key = (mapping.get('System'), mapping.get('Name'), mapping.get('Version'))
        if package_key in package_lookup:
            package_to_project[package_key] = mapping.get('ProjectName')

# Build project info lookup with stats extraction
fork_pattern = r'(\d+) forks?'
stars_pattern = r'(\d+) stars?'

project_stats = {}
for proj in project_info:
    info_text = proj.get('Project_Information', '')
    # Extract project name
    name_match = re.search(r'The project ([^\s]+)', info_text)
    if name_match:
        project_name = name_match.group(1)
        
        # Extract fork count
        fork_match = re.search(fork_pattern, info_text, re.IGNORECASE)
        if fork_match:
            fork_count = int(fork_match.group(1))
            
            # Extract stars
            stars_match = re.search(stars_pattern, info_text, re.IGNORECASE)
            stars_count = int(stars_match.group(1)) if stars_match else 0
            
            project_stats[project_name] = {
                'forks': fork_count,
                'stars': stars_count,
                'info': info_text
            }

# Match packages with project stats
matched_projects = []
for package_key, project_name in package_to_project.items():
    if project_name in project_stats:
        stats = project_stats[project_name]
        pkg = package_lookup[package_key]
        matched_projects.append({
            'project': project_name,
            'package_name': pkg['Name'],
            'package_version': pkg['Version'],
            'forks': stats['forks'],
            'stars': stats['stars']
        })

# Sort by forks descending
top_5 = sorted(matched_projects, key=lambda x: x['forks'], reverse=True)[:5]

print('__RESULT__:')
print(json.dumps({
    'total_mit_packages': len(packages),
    'matched_with_projects': len(matched_projects),
    'top_5_projects': top_5
}, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'Found 1000 packages with MIT license and IsRelease=true', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:7': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Homepage': 'None'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Homepage': 'https://leafletjs.com'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Homepage': 'None'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/'}, {'Project_Information': 'The project is hosted on GitHub under the name learnfrontend-dc/product-cart, and it currently has 2 open issues. It has garnered a total of 11 stars and has been forked 12 times.', 'Licenses': '[]', 'Homepage': 'None'}, {'Project_Information': 'The GitHub project ledgerproject/keypairoom currently has 3 open issues, 3 stars, and 0 forks.', 'Licenses': '[\n  "AGPL-3.0"\n]', 'Homepage': 'None'}, {'Project_Information': 'The project leebyron/jasmine-check is hosted on GitHub and currently has 0 open issues, 11 stars, and 3 forks.', 'Licenses': '[]', 'Homepage': 'None'}, {'Project_Information': 'The project leebyron/testcheck-js on GitHub has an open issues count of 29, a stars count of 1185, and a forks count of 58, making it a notable repository in the community.', 'Licenses': '[\n  "non-standard"\n]', 'Homepage': 'http://leebyron.com/testcheck-js'}, {'Project_Information': 'The project leecade/react-native-swiper is hosted on GitHub and has a total of 786 open issues, along with an impressive 10,249 stars and 2,392 forks, making it a popular choice among developers for implementing swiping functionality in React Native applications.', 'Licenses': '[\n  "MIT"\n]', 'Homepage': 'None'}], 'var_functions.execute_python:8': {'total_packages': 1000, 'matched_projects': 1000}, 'var_functions.execute_python:10': {'matched_mappings': 1000, 'unique_projects': 243}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'total_packages': 1000, 'matching_projects': 7, 'top_5': [{'project': 'taixw2/dx', 'forks': 14, 'stars': 84, 'package': '@dxjs/core'}, {'project': 'n43/easyapp', 'forks': 0, 'stars': 0, 'package': '@easyapp/wechat'}, {'project': 'luzzif/ethereum-contacts-registry', 'forks': 0, 'stars': 5, 'package': '@ecr/contracts'}, {'project': 'stephenliu1944/beancommons-proxy', 'forks': 0, 'stars': 0, 'package': '@easytool/proxy-config'}, {'project': 'shanebo/balm', 'forks': 0, 'stars': 0, 'package': '@dylan/balm'}]}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'total_npm_packages_mapped': 8381, 'total_projects_analyzed': 770, 'projects_with_forks': 473, 'top_projects': [{'name': 'leaflet/leaflet', 'forks': 5782, 'stars': 38715, 'issues': 521, 'package_info': {'package_name': '@ec-nordbund/leaflet', 'package_version': '1.7.1-436430db4203a350601e002c8de6a41fae15a4bf-1'}}, {'name': 'semantic-org/semantic-ui', 'forks': 4955, 'stars': 0, 'issues': 0, 'package_info': {'package_name': '@dreampie/semantic-ui', 'package_version': '2.2.11'}}, {'name': 'react-native-community/react-native-webview', 'forks': 2962, 'stars': 6345, 'issues': 87, 'package_info': {'package_name': '@dlwlrma00/react-native-webview-bypass-ssl', 'package_version': '11.0.3'}}, {'name': 'theia-ide/theia', 'forks': 2451, 'stars': 18526, 'issues': 0, 'package_info': {'package_name': '@dongjiang/textmate-grammars', 'package_version': '0.0.5'}}, {'name': 'react-native-device-info', 'forks': 1449, 'stars': 6408, 'issues': 12, 'package_info': None}, {'name': 'sass/node-sass', 'forks': 1326, 'stars': 8498, 'issues': 189, 'package_info': {'package_name': '@dpoineau/react-scripts>1.0.0>node-sass', 'package_version': '3.10.1'}}, {'name': 'shaka-project/shaka-player', 'forks': 1319, 'stars': 6949, 'issues': 110, 'package_info': {'package_name': '@discovery-dni/shaka-player', 'package_version': '4.1.1-custom27'}}, {'name': 'is', 'forks': 1308, 'stars': 2019, 'issues': 32, 'package_info': None}, {'name': 'mbrn/material-table', 'forks': 1035, 'stars': 3464, 'issues': 23, 'package_info': {'package_name': '@e-bar.mk/material-table', 'package_version': '1.69.2'}}, {'name': 'ternjs/acorn', 'forks': 944, 'stars': 0, 'issues': 0, 'package_info': {'package_name': '@dpoineau/react-scripts>1.0.0>acorn-globals>acorn', 'package_version': '2.7.0'}}, {'name': 'mjmlio/mjml', 'forks': 937, 'stars': 829, 'issues': 75, 'package_info': {'package_name': '@ecomailcz/mjml-head-preview', 'package_version': '4.4.0-ecm-25'}}, {'name': 'thejameskyle/react-loadable', 'forks': 857, 'stars': 576, 'issues': 36, 'package_info': {'package_name': '@docusaurus/react-loadable', 'package_version': '5.5.1'}}, {'name': 'matt-esch/virtual-dom', 'forks': 851, 'stars': 564, 'issues': 153, 'package_info': {'package_name': '@discourse/virtual-dom', 'package_version': '2.1.2-0'}}, {'name': 'tailwindcss/tailwindcss', 'forks': 848, 'stars': 464, 'issues': 18, 'package_info': {'package_name': '@dumc11/tailwindcss', 'package_version': '0.4.0'}}, {'name': 'mono/mono', 'forks': 845, 'stars': 630, 'issues': 256, 'package_info': {'package_name': '@dwarvesf/react-eslint-config', 'package_version': '0.0.3'}}, {'name': 'n4kz/react-native-material-textfield', 'forks': 841, 'stars': 890, 'issues': 120, 'package_info': {'package_name': '@dylanvann/react-native-material-textfield', 'package_version': '0.12.1'}}, {'name': 'mapbox/node-sqlite3', 'forks': 805, 'stars': 5917, 'issues': 139, 'package_info': {'package_name': '@dnonis/sqlite3', 'package_version': '6.0.1'}}, {'name': 'mobxjs/mobx', 'forks': 783, 'stars': 802, 'issues': 54, 'package_info': {'package_name': '@dudadev/mobx-react', 'package_version': '6.1.12'}}, {'name': 'ljharb/qs', 'forks': 746, 'stars': 8073, 'issues': 71, 'package_info': {'package_name': '@dpoineau/react-scripts>1.0.0>qs', 'package_version': '6.2.1'}}, {'name': 'react-icons/react-icons', 'forks': 730, 'stars': 295, 'issues': 198, 'package_info': {'package_name': '@dsch/react-icons', 'package_version': '3.12.0'}}]}, 'var_functions.execute_python:20': 'file_storage/functions.execute_python:20.json', 'var_functions.execute_python:22': {'npm_package_mappings': 597602, 'total_projects_info': 770}, 'var_functions.query_db:24': [{'System': 'NPM', 'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1-436430db4', 'ProjectName': 'leaflet/leaflet'}, {'System': 'NPM', 'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1-build-81dc2489', 'ProjectName': 'leaflet/leaflet'}, {'System': 'NPM', 'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1-build', 'ProjectName': 'leaflet/leaflet'}, {'System': 'NPM', 'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1-build-81dc24892a3f', 'ProjectName': 'leaflet/leaflet'}, {'System': 'NPM', 'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1', 'ProjectName': 'leaflet/leaflet'}, {'System': 'NPM', 'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1-build-dc24892a3f', 'ProjectName': 'leaflet/leaflet'}, {'System': 'NPM', 'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1-436430db4203a350601e002c8de6a41fae15a4bf-2', 'ProjectName': 'leaflet/leaflet'}, {'System': 'NPM', 'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1-32ea41baa', 'ProjectName': 'leaflet/leaflet'}, {'System': 'NPM', 'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1-436430db4203a350601e002c8de6a41fae15a4bf', 'ProjectName': 'leaflet/leaflet'}, {'System': 'NPM', 'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1-modules', 'ProjectName': 'leaflet/leaflet'}, {'System': 'NPM', 'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1-436430db4-436430db4', 'ProjectName': 'leaflet/leaflet'}, {'System': 'NPM', 'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1-build-81dc24892a', 'ProjectName': 'leaflet/leaflet'}, {'System': 'NPM', 'Name': '@ec-nordbund/leaflet', 'Version': '1.7.1-436430db4203a350601e002c8de6a41fae15a4bf-1', 'ProjectName': 'leaflet/leaflet'}], 'var_functions.execute_python:26': {'top_projects_count': 15, 'matched_npm_packages': 252, 'sample_matches': [{'package': '@ecomailcz/mjml', 'version': '4.4.0-ecm-26', 'project': 'mjmlio/mjml'}, {'package': '@dudadev/mobx-react', 'version': '6.1.10', 'project': 'mobxjs/mobx'}, {'package': '@dudadev/mobx-react', 'version': '6.1.7', 'project': 'mobxjs/mobx'}, {'package': '@ec-nordbund/leaflet', 'version': '1.7.1-436430db4', 'project': 'leaflet/leaflet'}, {'package': '@ec-nordbund/leaflet', 'version': '1.7.1-build-81dc2489', 'project': 'leaflet/leaflet'}, {'package': '@ecomailcz/mjml-core', 'version': '4.4.0-ecm-25', 'project': 'mjmlio/mjml'}, {'package': '@ecomailcz/mjml-head', 'version': '4.4.0-ecm-26', 'project': 'mjmlio/mjml'}, {'package': '@ecomailcz/mjml-hero', 'version': '4.4.0-ecm-23', 'project': 'mjmlio/mjml'}, {'package': '@ecomailcz/mjml-hero', 'version': '4.4.0-ecm-24', 'project': 'mjmlio/mjml'}, {'package': '@ecomailcz/mjml-text', 'version': '4.4.0-ecm-24', 'project': 'mjmlio/mjml'}, {'package': '@ecomailcz/mjml-text', 'version': '4.4.0-ecm-25', 'project': 'mjmlio/mjml'}, {'package': '@ecomailcz/mjml-group', 'version': '4.4.0-ecm-27', 'project': 'mjmlio/mjml'}, {'package': '@ecomailcz/mjml-table', 'version': '4.4.0-ecm-24', 'project': 'mjmlio/mjml'}, {'package': '@ecomailcz/mjml-navbar', 'version': '4.4.0-ecm-27', 'project': 'mjmlio/mjml'}, {'package': '@ecomailcz/mjml-section', 'version': '4.4.0-ecm-26', 'project': 'mjmlio/mjml'}, {'package': '@ecomailcz/mjml-section', 'version': '4.4.0-ecm-24', 'project': 'mjmlio/mjml'}, {'package': '@ecomailcz/mjml-wrapper', 'version': '4.4.0-ecm-27', 'project': 'mjmlio/mjml'}, {'package': '@ecomailcz/mjml-wrapper', 'version': '4.4.0-ecm-23', 'project': 'mjmlio/mjml'}, {'package': '@e-bar.mk/material-table', 'version': '1.69.2', 'project': 'mbrn/material-table'}, {'package': '@ecomailcz/mjml-carousel', 'version': '4.4.0-ecm-25', 'project': 'mjmlio/mjml'}]}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
