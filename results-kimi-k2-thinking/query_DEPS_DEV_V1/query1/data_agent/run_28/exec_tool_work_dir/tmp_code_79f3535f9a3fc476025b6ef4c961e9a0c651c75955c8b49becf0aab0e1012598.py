code = """import json
import re
import os

# Load the three datasets
with open('var_functions.query_db_144', 'r') as f:
    packages = json.load(f)

with open('var_functions.query_db_78', 'r') as f:
    mappings = json.load(f)

with open('var_functions.query_db_106', 'r') as f:
    project_info = json.load(f)

print('Data loaded successfully')
print('Packages count:', len(packages))
print('Mappings count:', len(mappings))
print('Project info count:', len(project_info))

# Step 1: Find latest version per package (max ordinal)
latest = {}
for p in packages:
    name = p['Name']
    vi = json.loads(p['VersionInfo'])
    ordinal = vi['Ordinal']
    version = p['Version']
    
    if name not in latest or ordinal > latest[name][0]:
        latest[name] = (ordinal, version)

print('Latest versions found:', len(latest))

# Step 2: Create project lookup table
lookup = {}
for m in mappings:
    key = (m['Name'], m['Version'])
    lookup[key] = m['ProjectName']

print('Lookup table size:', len(lookup))

# Step 3: Match packages to GitHub projects
matched = []
for name, (ord_val, version) in latest.items():
    key = (name, version)
    if key in lookup:
        matched.append((name, version, lookup[key]))

print('Matched packages:', len(matched))

# Step 4: Extract star counts
stars = {}
for rec in project_info:
    txt = rec['Project_Information']
    star_match = re.search(r'([0-9,]+) stars', txt)
    proj_match = re.search(r'project ([\w-]+/[\w-]+)', txt)
    if star_match and proj_match:
        stars[proj_match.group(1)] = int(star_match.group(1).replace(',', ''))

print('Star counts extracted:', len(stars))

# Step 5: Combine and get top 5 packages by stars
results = []
for name, version, project in matched:
    if project in stars:
        results.append({
            'package': name,
            'version': version,
            'project': project,
            'stars': stars[project]
        })

print('Packages with star data:', len(results))

# Sort by stars and take top 5
top5 = sorted(results, key=lambda x: x['stars'], reverse=True)[:5]

print('\n' + '='*50)
print('TOP 5 NPM PACKAGES BY GITHUB STARS')
print('='*50)

for rank, pkg in enumerate(top5, 1):
    print(str(rank) + '. ' + pkg['project'])
    print('   Package: ' + pkg['package'] + ' (v' + pkg['version'] + ')')
    print('   Stars: ' + str(pkg['stars']))
    print()

# Return the result
result_json = json.dumps(top5, indent=2)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.query_db:2': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'System': 'NPM', 'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'System': 'NPM', 'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'System': 'NPM', 'Name': '@edgedev/firebase', 'Version': '1.0.12', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}'}, {'System': 'NPM', 'Name': '@eden-network/data', 'Version': '1.0.9-sev.5', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 14\n}'}], 'var_functions.list_db:5': ['project_info', 'project_packageversion'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.query_db:10': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectName': 'dataminingsupply/dms-io'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectName': 'isacvale/fc'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.10', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.17', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@dlcs/ng', 'Version': '1.0.0', 'ProjectName': 'winup/dlcs-ng'}, {'System': 'NPM', 'Name': '@dms/cli', 'Version': '1.0.1', 'ProjectName': 'dataminingsupply/dms-cli'}, {'System': 'NPM', 'Name': '@dms/cli', 'Version': '1.0.0', 'ProjectName': 'dataminingsupply/dms-cli'}], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:42': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.'}, {'Project_Information': 'The project is hosted on GitHub under the name learnfrontend-dc/product-cart, and it currently has 2 open issues. It has garnered a total of 11 stars and has been forked 12 times.'}, {'Project_Information': 'The GitHub project ledgerproject/keypairoom currently has 3 open issues, 3 stars, and 0 forks.'}, {'Project_Information': 'The project leebyron/jasmine-check is hosted on GitHub and currently has 0 open issues, 11 stars, and 3 forks.'}, {'Project_Information': 'The project leebyron/testcheck-js on GitHub has an open issues count of 29, a stars count of 1185, and a forks count of 58, making it a notable repository in the community.'}, {'Project_Information': 'The project leecade/react-native-swiper is hosted on GitHub and has a total of 786 open issues, along with an impressive 10,249 stars and 2,392 forks, making it a popular choice among developers for implementing swiping functionality in React Native applications.'}], 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:46': [{'total_npm_packages': '661372'}], 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json', 'var_functions.query_db:54': [{'count': '661372'}], 'var_functions.query_db:58': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'Name': '@edgedev/firebase', 'Version': '1.0.12', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}'}, {'Name': '@eden-network/data', 'Version': '1.0.9-sev.5', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 14\n}'}], 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:74': 'file_storage/functions.query_db:74.json', 'var_functions.query_db:78': 'file_storage/functions.query_db:78.json', 'var_functions.query_db:86': [{'cnt': '337844'}], 'var_functions.query_db:88': [{'ProjectName': 'dosyago/ws'}, {'ProjectName': 'eboosolutions/eboo-kit'}, {'ProjectName': 'dmsi-phoenix/dmsi-core'}, {'ProjectName': 'ionic-team/stencil-component-starter'}, {'ProjectName': 'dotenv-org/cli'}, {'ProjectName': 'drpiou/yum'}, {'ProjectName': 'drumtj/v3d'}, {'ProjectName': 'zhouzuchuan/dseven-vue'}, {'ProjectName': 'dwlib-js/enum'}, {'ProjectName': 'cryptonative-ch/aqua-js'}, {'ProjectName': 'ant-design/ant-design'}, {'ProjectName': 'eden-js/cms'}, {'ProjectName': 'fedwiki/wiki'}, {'ProjectName': 'docusgen/module-starter'}, {'ProjectName': 'domojs/chat'}, {'ProjectName': 'domojs/domojs-pioneer'}, {'ProjectName': 'lohfu/domp'}, {'ProjectName': 'dotindustries/ogre'}, {'ProjectName': 'inlife/duckdoc-cli'}, {'ProjectName': 'dupkey/typescript/mail'}, {'ProjectName': 'dragomir-ivanov/cxsd'}, {'ProjectName': 'dnslink-std/test'}, {'ProjectName': 'docusgen/github-module'}, {'ProjectName': 'dojo/streams'}, {'ProjectName': 'greg-doneup/walletconnect-monorepo'}, {'ProjectName': 'doodadjs/doodad-js-io'}, {'ProjectName': 'dvhbru/webpack'}, {'ProjectName': 'airdwing/node-dwing-common'}, {'ProjectName': 'kerwizzy/dynein'}, {'ProjectName': 'xuyizhe/easydapp'}, {'ProjectName': 'eden-js/alert'}, {'ProjectName': 'ditojs/dito-server'}, {'ProjectName': 'divvit/logger'}, {'ProjectName': 'algolia/autocomplete.js'}, {'ProjectName': 'francoischalifour/autocomplete.js'}, {'ProjectName': 'doridian/jsip'}, {'ProjectName': 'dot-event/aws'}, {'ProjectName': 'etcdigital/app.doutor.etc.br'}, {'ProjectName': 'chorney/lib'}, {'ProjectName': 'eden-js/locale'}, {'ProjectName': 'neplextech/edge-ui'}, {'ProjectName': 'discordx-ts/discordx'}, {'ProjectName': 'discowrap/core'}, {'ProjectName': 'dojo/framework'}, {'ProjectName': 'doodadjs/doodad-js'}, {'ProjectName': 'dot-event/wait'}, {'ProjectName': 'dpwanjala-npm-packages/auth'}, {'ProjectName': 'dra2020/lambda'}, {'ProjectName': 'drfte/react-ui'}, {'ProjectName': 'davidroyer/nuxtcms'}, {'ProjectName': 'eartharoid/dtf'}, {'ProjectName': 'mccoughskii/easybot'}, {'ProjectName': 'eaze/css-reset'}, {'ProjectName': 'dna-js/dna-form'}, {'ProjectName': 'danger/danger-js'}, {'ProjectName': 'doublepi/vector'}, {'ProjectName': 'timpaulaskasds/sfparty'}, {'ProjectName': 'dscout/particle'}, {'ProjectName': 'matejlauko/duotone'}, {'ProjectName': 'easyapiio/easyapi-node-sdk'}, {'ProjectName': 'easynm/chores'}, {'ProjectName': 'eda/xero-facade'}, {'ProjectName': 'edgejs/type-is'}, {'ProjectName': 'diy-iot-lock/app'}, {'ProjectName': 'djgrant/pg-taskq'}, {'ProjectName': 'dlenroc/node-roku'}, {'ProjectName': 'distributedlab-solidity-library/dev-modules'}, {'ProjectName': 'dot-build/logger'}, {'ProjectName': 'doublepi/chat-ui'}, {'ProjectName': 'duda-co/duda-svg'}, {'ProjectName': 'dmijatovic/nuxt-next-lerna'}, {'ProjectName': 'jarvis-network/core/market/ui'}, {'ProjectName': 'e-line-websolutions/woonplan-types'}, {'ProjectName': 'ebay/ebayui-core'}, {'ProjectName': 'eckhardt-d/dow-sdk'}, {'ProjectName': 'cris691/browsergap.js'}, {'ProjectName': 'dov118/eso-status'}, {'ProjectName': 'ant-design/pro-components'}, {'ProjectName': 'dra2020/dra-types'}, {'ProjectName': 'dropzone-ui/dropzone-ui-react'}, {'ProjectName': 'dscribers/surf-me'}, {'ProjectName': 'designsystemsengineer/designsystem'}, {'ProjectName': 'dynatrace-esa/authorizer'}, {'ProjectName': 'e-goi/css-inliner'}, {'ProjectName': 'earnkeeper/ekp-ui'}, {'ProjectName': 'easy-webpack/core'}, {'ProjectName': 'eclipse-scout/scout.rt'}, {'ProjectName': 'distubejs/soundcloud'}, {'ProjectName': 'dizmo/types-bundle'}, {'ProjectName': 'dmnchzl/datepicker'}, {'ProjectName': 'dojo/cli-build-app'}, {'ProjectName': 'donksolana/donk-contracts'}, {'ProjectName': 'momsfriendlydevco/doop-service-morph'}, {'ProjectName': 'drovp/save-as-path'}, {'ProjectName': 'dscribers/autosurf'}, {'ProjectName': 'dsinjs/binary-tree'}, {'ProjectName': 'stacktical/stacktical-dsla-contracts'}, {'ProjectName': 'earth-association/assets'}, {'ProjectName': 'eastdesire/jscolor'}, {'ProjectName': 'easyfeedback/rcl'}], 'var_functions.query_db:96': [{'count': '661372'}], 'var_functions.query_db:98': 'file_storage/functions.query_db:98.json', 'var_functions.query_db:100': 'file_storage/functions.query_db:100.json', 'var_functions.query_db:106': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_functions.query_db:132': 'file_storage/functions.query_db:132.json', 'var_functions.query_db:140': [{'Name': '@discordx/music', 'Version': '6.0.2', 'max_ordinal': '213'}, {'Name': '@discordx/pagination', 'Version': '3.4.1', 'max_ordinal': '40'}, {'Name': '@discordx/utilities', 'Version': '5.2.1', 'max_ordinal': '262'}, {'Name': '@discoteam/vueify', 'Version': '9.4.1', 'max_ordinal': '2'}, {'Name': '@discourse/itsatrap', 'Version': '2.0.10', 'max_ordinal': '10'}, {'Name': '@discourse/moment-timezone-names-translations', 'Version': '1.0.0', 'max_ordinal': '1'}, {'Name': '@discoursegroup/commons-js', 'Version': '0.0.11', 'max_ordinal': '10'}, {'Name': '@discoursegroup/commons-test-js', 'Version': '0.0.4', 'max_ordinal': '3'}, {'Name': '@discoursegroup/relayrabbit-addons-js', 'Version': '0.0.384', 'max_ordinal': '383'}, {'Name': '@discoursegroup/relayrabbit-commons-js', 'Version': '0.0.7', 'max_ordinal': '3'}], 'var_functions.query_db:144': 'file_storage/functions.query_db:144.json'}

exec(code, env_args)
