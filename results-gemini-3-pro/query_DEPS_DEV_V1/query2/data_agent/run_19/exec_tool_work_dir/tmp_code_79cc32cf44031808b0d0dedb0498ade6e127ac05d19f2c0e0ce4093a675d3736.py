code = """import json

# Load package info
pkg_file = locals()['var_function-call-17831794086571236963']
with open(pkg_file, 'r') as f:
    packages_list = json.load(f)

# Index packages for fast lookup: (Name, Version) -> {Licenses, VersionInfo}
pkg_lookup = {}
for p in packages_list:
    pkg_lookup[(p['Name'], p['Version'])] = p

# Load sorted projects
projects_data = locals()['var_function-call-1806918777565722917']
valid_projects = [p for p in projects_data if p['ProjectName'] and p['ProjectName'] not in ['named', 'titled']]

# Load mappings
mapping_file = locals()['var_function-call-4022048896721310058']
with open(mapping_file, 'r') as f:
    mappings_data = json.load(f)

# Project -> [(Name, Version)]
project_to_packages = {}
for m in mappings_data:
    pname = m['ProjectName']
    if pname not in project_to_packages:
        project_to_packages[pname] = []
    project_to_packages[pname].append((m['Name'], m['Version']))

# Check candidates
winners = []
for proj in valid_projects:
    pname = proj['ProjectName']
    # Only check if we have mapping data (we only fetched names for top 10, but mapping has all)
    # But wait, query_db for packageinfo only queried the names for the top 10.
    # So if a project is not in the top 10, we likely won't have its package info unless it shares a package.
    # So we can only verify the ones we queried.
    
    if pname not in project_to_packages:
        continue
        
    pairs = project_to_packages[pname]
    found_valid_pkg = False
    
    for name, ver in pairs:
        if (name, ver) in pkg_lookup:
            p_info = pkg_lookup[(name, ver)]
            
            # Check License
            # Licenses is a JSON array string
            try:
                licenses = json.loads(p_info['Licenses'])
            except:
                licenses = []
            if isinstance(licenses, str): licenses = [licenses] # Handle potential malformed
            
            has_mit = False
            for lic in licenses:
                if 'MIT' in lic:
                    has_mit = True
                    break
            
            # Check Release
            # VersionInfo is a JSON object string
            is_release = False
            try:
                v_info = json.loads(p_info['VersionInfo'])
                if v_info.get('IsRelease') == True:
                    is_release = True
            except:
                pass
            
            if has_mit and is_release:
                found_valid_pkg = True
                break
    
    if found_valid_pkg:
        winners.append(pname)
    
    if len(winners) >= 5:
        break

print("__RESULT__:")
print(json.dumps(winners))"""

env_args = {'var_function-call-13190375359863328996': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}], 'var_function-call-13190375359863328867': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-13190375359863332834': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}], 'var_function-call-7540295345936586167': 'file_storage/function-call-7540295345936586167.json', 'var_function-call-1806918777565722917': [{'ProjectName': 'leaflet/leaflet', 'ForkCount': '5782'}, {'ProjectName': 'semantic-org/semantic-ui', 'ForkCount': '4955'}, {'ProjectName': 'react-native-community/react-native-webview', 'ForkCount': '2962'}, {'ProjectName': 'theia-ide/theia', 'ForkCount': '2451'}, {'ProjectName': 'react-native-device-info', 'ForkCount': '1449'}, {'ProjectName': 'sass/node-sass', 'ForkCount': '1326'}, {'ProjectName': 'shaka-project/shaka-player', 'ForkCount': '1319'}, {'ProjectName': 'is', 'ForkCount': '1308'}, {'ProjectName': 'mbrn/material-table', 'ForkCount': '1035'}, {'ProjectName': 'ternjs/acorn', 'ForkCount': '944'}, {'ProjectName': 'mjmlio/mjml', 'ForkCount': '937'}, {'ProjectName': '', 'ForkCount': '897'}, {'ProjectName': '', 'ForkCount': '866'}, {'ProjectName': 'thejameskyle/react-loadable', 'ForkCount': '857'}, {'ProjectName': 'matt-esch/virtual-dom', 'ForkCount': '851'}, {'ProjectName': 'tailwindcss/tailwindcss', 'ForkCount': '848'}, {'ProjectName': 'mono/mono', 'ForkCount': '845'}, {'ProjectName': 'n4kz/react-native-material-textfield', 'ForkCount': '841'}, {'ProjectName': 'mapbox/node-sqlite3', 'ForkCount': '805'}, {'ProjectName': 'mobxjs/mobx', 'ForkCount': '783'}, {'ProjectName': 'ljharb/qs', 'ForkCount': '746'}, {'ProjectName': 'react-icons/react-icons', 'ForkCount': '730'}, {'ProjectName': '', 'ForkCount': '700'}, {'ProjectName': 'tmpvar/jsdom', 'ForkCount': '668'}, {'ProjectName': 'leandrowd/react-responsive-carousel', 'ForkCount': '636'}, {'ProjectName': 'react-native-elements/react-native-elements', 'ForkCount': '623'}, {'ProjectName': 'supasate/connected-react-router', 'ForkCount': '605'}, {'ProjectName': 'securingsincity/react-ace', 'ForkCount': '603'}, {'ProjectName': 'malte-wessel/react-custom-scrollbars', 'ForkCount': '595'}, {'ProjectName': 'marcbachmann/node-html-pdf', 'ForkCount': '586'}, {'ProjectName': 'namespace-ee/react-calendar-timeline', 'ForkCount': '585'}, {'ProjectName': 'lekoarts/gatsby-themes', 'ForkCount': '568'}, {'ProjectName': 'signavio/react-mentions', 'ForkCount': '562'}, {'ProjectName': 'mapbox/mapbox-gl-draw', 'ForkCount': '561'}, {'ProjectName': 'mui-org/material-ui', 'ForkCount': '522'}, {'ProjectName': 'named', 'ForkCount': '514'}, {'ProjectName': 'styled-components/styled-components', 'ForkCount': '513'}, {'ProjectName': 'marmelab/gremlins.js', 'ForkCount': '507'}, {'ProjectName': 'riophae/vue-treeselect', 'ForkCount': '504'}, {'ProjectName': 'naoufal/react-native-touch-id', 'ForkCount': '484'}, {'ProjectName': 'serverless-nextjs/serverless-next.js', 'ForkCount': '450'}, {'ProjectName': 'sveltejs/sapper', 'ForkCount': '449'}, {'ProjectName': 'naoufal/react-native-payments', 'ForkCount': '420'}, {'ProjectName': '', 'ForkCount': '419'}, {'ProjectName': 'microsoft/monaco-editor', 'ForkCount': '407'}, {'ProjectName': 'named', 'ForkCount': '402'}, {'ProjectName': 'leecade/react-native-swiper', 'ForkCount': '392'}, {'ProjectName': 'salesforce/lwc', 'ForkCount': '386'}, {'ProjectName': 'spite/three.meshline', 'ForkCount': '375'}, {'ProjectName': 'mozilla/source-map', 'ForkCount': '366'}, {'ProjectName': '', 'ForkCount': '364'}, {'ProjectName': 'semantic-org/semantic-ui-css', 'ForkCount': '362'}, {'ProjectName': '', 'ForkCount': '336'}, {'ProjectName': 'terkelg/prompts', 'ForkCount': '322'}, {'ProjectName': 'then/promise', 'ForkCount': '320'}, {'ProjectName': 'quilljs/quill', 'ForkCount': '318'}, {'ProjectName': '', 'ForkCount': '303'}, {'ProjectName': '', 'ForkCount': '299'}, {'ProjectName': 'sockjs/sockjs-client', 'ForkCount': '298'}, {'ProjectName': 'request/request-promise', 'ForkCount': '297'}, {'ProjectName': 'thomasdondorf/puppeteer-cluster', 'ForkCount': '287'}, {'ProjectName': '', 'ForkCount': '273'}, {'ProjectName': 'mixu/markdown-styles', 'ForkCount': '255'}, {'ProjectName': 'react-component/tabs', 'ForkCount': '233'}, {'ProjectName': 'react-native-webrtc/react-native-webrtc', 'ForkCount': '227'}, {'ProjectName': '', 'ForkCount': '219'}, {'ProjectName': 'named', 'ForkCount': '211'}, {'ProjectName': 'thejameskyle/spectacle-code-slide', 'ForkCount': '202'}, {'ProjectName': 'tabookey-dev/tabookey-gasless', 'ForkCount': '202'}, {'ProjectName': '', 'ForkCount': '184'}, {'ProjectName': '', 'ForkCount': '178'}, {'ProjectName': 'named', 'ForkCount': '174'}, {'ProjectName': 'titled', 'ForkCount': '173'}, {'ProjectName': 'lukasz-galka/ngx-gallery', 'ForkCount': '173'}, {'ProjectName': 'rjsf-team/react-jsonschema-form', 'ForkCount': '170'}, {'ProjectName': '', 'ForkCount': '169'}, {'ProjectName': 'th3rdwave/react-native-safe-area-context', 'ForkCount': '165'}, {'ProjectName': '', 'ForkCount': '159'}, {'ProjectName': 'lucasferreira/react-native-flash-message', 'ForkCount': '154'}, {'ProjectName': 'segmentio/analytics-node', 'ForkCount': '152'}, {'ProjectName': '', 'ForkCount': '151'}, {'ProjectName': '', 'ForkCount': '146'}, {'ProjectName': 'rvagg/node-worker-farm', 'ForkCount': '145'}, {'ProjectName': 'mikeal/watch', 'ForkCount': '144'}, {'ProjectName': 'mozilla-services/react-jsonschema-form', 'ForkCount': '137'}, {'ProjectName': 'maronato/vue-toastification', 'ForkCount': '129'}, {'ProjectName': 'moox/eslint-loader', 'ForkCount': '128'}, {'ProjectName': 'sethsandaru/vue-form-builder', 'ForkCount': '128'}, {'ProjectName': '', 'ForkCount': '128'}, {'ProjectName': 'strongloop/fsevents', 'ForkCount': '127'}, {'ProjectName': 'sindresorhus/globby', 'ForkCount': '126'}, {'ProjectName': 'redpandatronicsuk/react-native-check-app-install', 'ForkCount': '125'}, {'ProjectName': 'murhafsousli/ngx-sharebuttons', 'ForkCount': '123'}, {'ProjectName': '', 'ForkCount': '119'}, {'ProjectName': 'leaflet/leaflet.fullscreen', 'ForkCount': '118'}, {'ProjectName': '', 'ForkCount': '118'}, {'ProjectName': 'menudocs/erela.js', 'ForkCount': '115'}, {'ProjectName': '', 'ForkCount': '112'}, {'ProjectName': 'mdevils/node-html-entities', 'ForkCount': '110'}, {'ProjectName': 'mikeal/tunnel-agent', 'ForkCount': '105'}], 'var_function-call-4022048896721310058': 'file_storage/function-call-4022048896721310058.json', 'var_function-call-5658230673670606629': "SELECT Name, Version, Licenses, VersionInfo FROM packageinfo WHERE System = 'NPM' AND Name IN ('@ecomailcz/mjml-head-attributes'', ''@dwarvesf/react-scripts>0.7.0>acorn-globals>acorn'', ''@ecomailcz/mjml-raw'', ''@ecomailcz/mjml-head-font'', ''@dpoineau/react-scripts>1.0.0>acorn-globals>acorn'', ''@ecomailcz/mjml-head-preview'', ''@ecomailcz/mjml-core'', ''@ecomailcz/mjml-table'', ''@dpoineau/react-scripts>1.0.0>node-sass'', ''@ecomailcz/mjml-head'', ''@ecomailcz/mjml-head-style'', ''@dwarvesf/react-scripts>0.7.0>webpack>acorn'', ''@dwarvesf/react-scripts>0.7.0>acorn-jsx>acorn'', ''@ecomailcz/mjml-head-title'', ''@ecomailcz/mjml-button'', ''@ecomailcz/mjml-body'', ''@ec-nordbund/leaflet'', ''@ecomailcz/mjml-wrapper'', ''@docusaurus/react-loadable'', ''@ecomailcz/mjml'', ''@ecomailcz/mjml-migrate'', ''@dlwlrma00/react-native-webview-bypass-ssl'', ''@dongjiang/textmate-grammars'', ''@ecomailcz/mjml-section'', ''@ecomailcz/mjml-social'', ''@dpoineau/react-scripts>1.0.0>acorn'', ''@ecomailcz/mjml-text'', ''@ecomailcz/mjml-parser-xml'', ''@dwarvesf/react-scripts>0.7.0>acorn'', ''@ecomailcz/mjml-column'', ''@ecomailcz/mjml-spacer'', ''@ecomailcz/mjml-carousel'', ''@ebarmk/material-table'', ''@dpoineau/react-scripts>1.0.0>espree>acorn'', ''@e-bar.mk/material-table'', ''@ecomailcz/mjml-hero'', ''@eataly/material-table'', ''@ecomailcz/mjml-head-breakpoint'', ''@ecomailcz/mjml-group'', ''@ecomailcz/mjml-cli'', ''@ecomailcz/mjml-accordion'', ''@discovery-dni/shaka-player'', ''@dpoineau/react-scripts>1.0.0>jsdom>acorn'', ''@ecomailcz/mjml-image'', ''@dreampie/semantic-ui'', ''@ecomailcz/mjml-validator'', ''@ecomailcz/mjml-divider'', ''@ecomailcz/mjml-navbar'', ''@dwarvesf/react-scripts>0.7.0>jsdom>acorn')", 'var_function-call-17831794086571236963': 'file_storage/function-call-17831794086571236963.json'}

exec(code, env_args)
