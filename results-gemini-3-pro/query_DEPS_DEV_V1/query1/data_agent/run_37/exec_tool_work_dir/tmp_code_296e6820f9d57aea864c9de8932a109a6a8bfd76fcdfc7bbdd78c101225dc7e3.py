code = """# Re-run the ranking and print top 20 with project info
# Reuse variables from previous execution if possible? 
# No, must reload files. But I can just copy-paste the logic.

import json
import re

file_path_pinfo = locals()['var_function-call-3442210262496942819']
with open(file_path_pinfo, 'r') as f:
    project_info_list = json.load(f)

project_stars = {}
for item in project_info_list:
    info = item.get('Project_Information', '')
    name_match = re.search(r'project (?:is hosted on GitHub under the name |named |is a GitHub repository named )?([\w.-]+/[\w.-]+)', info, re.IGNORECASE)
    if name_match:
        p_name = name_match.group(1)
        stars_match = re.search(r'(\d+(?:,\d+)*)\s+stars', info)
        if not stars_match:
            stars_match = re.search(r'stars count of\s+(\d+(?:,\d+)*)', info)
        if stars_match:
            stars = int(stars_match.group(1).replace(',', ''))
            project_stars[p_name] = stars

file_path_pkg = locals()['var_function-call-2608383040838855877']
with open(file_path_pkg, 'r') as f:
    package_list = json.load(f)

latest_packages = {}
for pkg in package_list:
    name = pkg['Name']
    ver = pkg['Version']
    date = pkg['UpstreamPublishedAt']
    try:
        date_val = float(date)
    except:
        date_val = 0.0
    if name not in latest_packages:
        latest_packages[name] = {'Version': ver, 'Date': date_val}
    else:
        if date_val > latest_packages[name]['Date']:
            latest_packages[name] = {'Version': ver, 'Date': date_val}

file_path_ppv = locals()['var_function-call-2553915081167357847']
with open(file_path_ppv, 'r') as f:
    ppv_list = json.load(f)

package_stars = {}
package_project = {}

for item in ppv_list:
    p_name = item.get('ProjectName')
    pkg_name = item.get('Name')
    
    if p_name in project_stars and pkg_name in latest_packages:
        stars = project_stars[p_name]
        if pkg_name not in package_stars:
            package_stars[pkg_name] = stars
            package_project[pkg_name] = p_name
        else:
            if stars > package_stars[pkg_name]:
                package_stars[pkg_name] = stars
                package_project[pkg_name] = p_name

ranked_packages = []
for pkg_name, stars in package_stars.items():
    latest = latest_packages[pkg_name]
    ranked_packages.append({
        'Name': pkg_name,
        'Version': latest['Version'],
        'Stars': stars,
        'Project': package_project[pkg_name]
    })

ranked_packages.sort(key=lambda x: x['Stars'], reverse=True)

print("__RESULT__:")
print(json.dumps(ranked_packages[:15]))"""

env_args = {'var_function-call-11650093122282390699': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'UpstreamPublishedAt': '1699345351000000.0'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'UpstreamPublishedAt': '1670271173000000.0'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'UpstreamPublishedAt': '1654791421000000.0'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'UpstreamPublishedAt': '1624260093000000.0'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'UpstreamPublishedAt': '1656518476000000.0'}], 'var_function-call-11650093122282393026': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-11650093122282391257': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_function-call-3788952536165277218': [{'count(*)': '661372'}], 'var_function-call-3788952536165274197': [{'count_star()': '597602'}], 'var_function-call-3788952536165275272': [{'count_star()': '770'}], 'var_function-call-3442210262496942819': 'file_storage/function-call-3442210262496942819.json', 'var_function-call-13725768385790861377': 'file_storage/function-call-13725768385790861377.json', 'var_function-call-13467170018869718604': "'microsoft/typescript', 'mui-org/material-ui', 'sveltejs/svelte', 'tailwindcss/tailwindcss', 'lodash/lodash', 'strapi/strapi', 'rails/rails', 'semantic-org/semantic-ui', 'moment/moment', 'mozilla/pdf.js', 'quilljs/quill', 'styled-components/styled-components', 'leaflet/leaflet', 'microsoft/monaco-editor', 'mobxjs/mobx', 'request/request', 'tj/commander.js', 'react-native-elements/react-native-elements', 'swagger-api/swagger-ui', 'react-navigation/react-navigation', 'medusajs/medusa', 'sortablejs/vue.draggable', 'svg/svgo', 'snowpackjs/snowpack', 'reactive-extensions/rxjs', 'tmpvar/jsdom', 'theia-ide/theia', 'motdotla/dotenv', 'thejameskyle/react-loadable', 'tencent/vconsole', 'mjmlio/mjml', 'shelljs/shelljs', 'rjsf-team/react-jsonschema-form', 'mozilla-services/react-jsonschema-form', 'tj/co', 'matt-esch/virtual-dom', 'react-icons/react-icons', 'mishoo/uglifyjs2', 'mono/mono', 'mapbox/mapbox-gl-js', 'leecade/react-native-swiper', 'rebilly/redoc', 'ternjs/acorn', 'marmelab/gremlins.js', 'react-toolbox/react-toolbox', 'sass/node-sass', 'sockjs/sockjs-client', 'terkelg/prompts', 'ljharb/qs', 'redux-observable/redux-observable'", 'var_function-call-14286935128823628584': 'file_storage/function-call-14286935128823628584.json', 'var_function-call-12390246086987565635': 'file_storage/function-call-12390246086987565635.json', 'var_function-call-15667419505007391971': [], 'var_function-call-790809230045306760': [], 'var_function-call-192439544571704981': [{'Name': '@dwarvesf/react-scripts>0.7.0>lodash._baseclone'}, {'Name': '@dwarvesf/react-scripts>0.7.0>lodash._baseclone'}, {'Name': '@dummmy/webpack-cli>1.0.2>lodash'}, {'Name': '@dummmy/webpack-cli>1.0.2>lodash'}, {'Name': '@dollarshaveclub/cli>1.10.0>lodash'}, {'Name': '@dollarshaveclub/cli>1.10.0>lodash'}, {'Name': '@dpoineau/react-scripts>1.0.0>lodash.camelcase'}, {'Name': '@dpoineau/react-scripts>1.0.0>lodash.camelcase'}, {'Name': '@dpoineau/react-scripts>1.0.0>http-proxy-middleware>lodash'}, {'Name': '@dpoineau/react-scripts>1.0.0>http-proxy-middleware>lodash'}], 'var_function-call-192439544571704122': [{'Name': '@dummmy/pack-cli>1.0.8>lodash'}, {'Name': '@dummmy/pack-cli>1.0.9>lodash'}, {'Name': '@dummmy/webpack-cli>1.0.3>lodash'}, {'Name': '@dollarshaveclub/cli>1.0.0>lodash'}, {'Name': '@dollarshaveclub/cli>1.5.1>lodash'}, {'Name': '@dollarshaveclub/cli>1.7.1>lodash'}, {'Name': '@dollarshaveclub/cli>1.8.0>lodash'}, {'Name': '@dollarshaveclub/cli>2.2.1>lodash'}, {'Name': '@dollarshaveclub/cli>1.11.5-rc.1>lodash'}, {'Name': '@dpoineau/react-scripts>1.0.0>lodash._root'}], 'var_function-call-16003983455278985409': [], 'var_function-call-16003983455278986076': [{'Name': '@dpoineau/react-scripts>1.0.0>lodash.camelcase'}, {'Name': '@dummmy/webpack-cli>1.0.4>lodash'}, {'Name': '@dollarshaveclub/cli>1.9.1>lodash'}, {'Name': '@dollarshaveclub/cli>1.8.0>lodash'}, {'Name': '@dollarshaveclub/cli>1.5.4>lodash'}, {'Name': '@dwarvesf/react-scripts>0.7.0>lodash.keys'}, {'Name': '@dollarshaveclub/cli>1.13.0>lodash'}, {'Name': '@dwarvesf/react-scripts>0.7.0>lodash.words'}, {'Name': '@dummmy/webpack-cli>1.0.3>lodash'}, {'Name': '@dwarvesf/react-scripts>0.7.0>lodash._arrayeach'}, {'Name': '@dummmy/webpack-cli>1.0.6>lodash'}, {'Name': '@dollarshaveclub/cli>2.2.0>lodash'}, {'Name': '@dollarshaveclub/cli>2.0.0>lodash'}, {'Name': '@dwarvesf/react-scripts>0.7.0>lodash._createcompounder'}, {'Name': '@dollarshaveclub/cli>2.1.0>lodash'}, {'Name': '@dollarshaveclub/cli>1.11.5-rc.1>lodash'}, {'Name': '@dollarshaveclub/cli>1.5.7>lodash'}, {'Name': '@dollarshaveclub/cli>1.10.1>lodash'}, {'Name': '@dollarshaveclub/cli>1.11.4>lodash'}, {'Name': '@dpoineau/react-scripts>1.0.0>node-notifier>lodash.clonedeep'}, {'Name': '@dwarvesf/react-scripts>0.7.0>lodash'}, {'Name': '@dpoineau/react-scripts>1.0.0>lodash.indexof'}, {'Name': '@dpoineau/react-scripts>1.0.0>lodash.pickby'}, {'Name': '@dpoineau/react-scripts>1.0.0>lodash.findindex'}, {'Name': '@dollarshaveclub/cli>1.10.0>lodash'}, {'Name': '@dpoineau/react-scripts>1.0.0>lodash._bindcallback'}, {'Name': '@dollarshaveclub/cli>1.11.2>lodash'}, {'Name': '@dpoineau/react-scripts>1.0.0>lodash.clonedeep'}, {'Name': '@dwarvesf/react-scripts>0.7.0>lodash._getnative'}, {'Name': '@dwarvesf/react-scripts>0.7.0>lodash.pickby'}, {'Name': '@dwarvesf/react-scripts>0.7.0>lodash.indexof'}, {'Name': '@dollarshaveclub/cli>1.5.0>lodash'}, {'Name': '@dpoineau/react-scripts>1.0.0>lodash._arraycopy'}, {'Name': '@dollarshaveclub/cli>1.2.0>lodash'}, {'Name': '@dollarshaveclub/cli>1.6.0>lodash'}, {'Name': '@dpoineau/react-scripts>1.0.0>lodash._root'}, {'Name': '@dpoineau/react-scripts>1.0.0>lodash._baseassign'}, {'Name': '@dollarshaveclub/cli>1.5.3>lodash'}, {'Name': '@dwarvesf/react-scripts>0.7.0>lodash.assign'}, {'Name': '@dollarshaveclub/cli>1.11.5>lodash'}, {'Name': '@dpoineau/react-scripts>1.0.0>lodash.isarray'}, {'Name': '@dpoineau/react-scripts>1.0.0>lodash.keys'}, {'Name': '@dwarvesf/react-scripts>0.7.0>lodash._basefor'}, {'Name': '@dummmy/pack-cli>1.0.9>lodash'}, {'Name': '@dwarvesf/react-scripts>0.7.0>lodash._root'}, {'Name': '@dwarvesf/react-scripts>0.7.0>lodash._baseclone'}, {'Name': '@dollarshaveclub/cli>1.9.0>lodash'}, {'Name': '@dpoineau/react-scripts>1.0.0>lodash.cond'}, {'Name': '@dummmy/pack-cli>1.0.8>lodash'}, {'Name': '@dollarshaveclub/cli>1.1.0>lodash'}, {'Name': '@dwarvesf/react-scripts>0.7.0>lodash.camelcase'}, {'Name': '@dollarshaveclub/cli>1.3.0>lodash'}, {'Name': '@dollarshaveclub/cli>1.5.5>lodash'}, {'Name': '@dpoineau/react-scripts>1.0.0>lodash.assign'}, {'Name': '@dpoineau/react-scripts>1.0.0>lodash._basecopy'}, {'Name': '@dwarvesf/react-scripts>0.7.0>lodash._bindcallback'}, {'Name': '@dollarshaveclub/cli>1.5.6>lodash'}, {'Name': '@dollarshaveclub/cli>1.5.1>lodash'}, {'Name': '@dpoineau/react-scripts>1.0.0>lodash.find'}, {'Name': '@dpoineau/react-scripts>1.0.0>http-proxy-middleware>lodash'}, {'Name': '@dollarshaveclub/cli>2.2.2>lodash'}, {'Name': '@dpoineau/react-scripts>1.0.0>eslint-plugin-flowtype>lodash'}, {'Name': '@dpoineau/react-scripts>1.0.0>lodash'}, {'Name': '@dpoineau/react-scripts>1.0.0>lodash._basefor'}, {'Name': '@dummmy/webpack-cli>1.0.7>lodash'}, {'Name': '@dummmy/webpack-cli>1.0.2>lodash'}, {'Name': '@dwarvesf/react-scripts>0.7.0>lodash._arraycopy'}, {'Name': '@dwarvesf/react-scripts>0.7.0>lodash.isarguments'}, {'Name': '@dollarshaveclub/cli>1.12.0>lodash'}, {'Name': '@dollarshaveclub/cli>2.0.1>lodash'}, {'Name': '@dpoineau/react-scripts>1.0.0>lodash.isarguments'}, {'Name': '@dollarshaveclub/cli>1.11.3>lodash'}, {'Name': '@dwarvesf/react-scripts>0.7.0>lodash._basecopy'}, {'Name': '@dummmy/webpack-cli>1.0.5>lodash'}, {'Name': '@dollarshaveclub/cli>1.13.1>lodash'}, {'Name': '@dpoineau/react-scripts>1.0.0>lodash._arrayeach'}, {'Name': '@dpoineau/react-scripts>1.0.0>lodash.endswith'}, {'Name': '@dwarvesf/react-scripts>0.7.0>lodash.cond'}, {'Name': '@dollarshaveclub/cli>2.2.1>lodash'}, {'Name': '@dollarshaveclub/cli>2.1.1>lodash'}, {'Name': '@dollarshaveclub/cli>1.7.1>lodash'}, {'Name': '@dwarvesf/react-scripts>0.7.0>lodash.isarray'}, {'Name': '@dpoineau/react-scripts>1.0.0>lodash._getnative'}, {'Name': '@dpoineau/react-scripts>1.0.0>lodash.words'}, {'Name': '@dpoineau/react-scripts>1.0.0>lodash.deburr'}, {'Name': '@dollarshaveclub/cli>1.0.0>lodash'}, {'Name': '@dwarvesf/react-scripts>0.7.0>lodash.clonedeep'}, {'Name': '@dwarvesf/react-scripts>0.7.0>lodash.deburr'}, {'Name': '@dpoineau/react-scripts>1.0.0>html-webpack-plugin>lodash'}, {'Name': '@dpoineau/react-scripts>1.0.0>lodash._baseclone'}, {'Name': '@dollarshaveclub/cli>1.11.1>lodash'}, {'Name': '@dollarshaveclub/cli>1.11.0>lodash'}, {'Name': '@dwarvesf/react-scripts>0.7.0>lodash._baseassign'}, {'Name': '@dpoineau/react-scripts>1.0.0>lodash._createcompounder'}, {'Name': '@dollarshaveclub/cli>1.5.2>lodash'}], 'var_function-call-7901416487311222443': [], 'var_function-call-2553915081167357847': 'file_storage/function-call-2553915081167357847.json', 'var_function-call-2608383040838855877': 'file_storage/function-call-2608383040838855877.json', 'var_function-call-10301149942670686404': [{'Name': '@dmrvos/infrajs>0.0.5>typescript', 'Version': '2.6.2', 'Stars': 94931}, {'Name': '@dmrvos/infrajs>0.0.6>typescript', 'Version': '2.6.2', 'Stars': 94931}, {'Name': '@docly/web', 'Version': '0.2.3', 'Stars': 89398}, {'Name': '@dylanvann/svelte', 'Version': '3.25.4', 'Stars': 73499}, {'Name': '@dumc11/tailwindcss', 'Version': '0.4.0', 'Stars': 73464}]}

exec(code, env_args)
