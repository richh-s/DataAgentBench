code = """import json

# Load projects
path_proj = locals()['var_function-call-8037384748417867872']
with open(path_proj, 'r') as f:
    projects = json.load(f)
    # They were sorted by Forks desc

# Load mappings
path_map = locals()['var_function-call-2098349176198877097']
with open(path_map, 'r') as f:
    mappings = json.load(f)

# Create proj -> names
proj_to_names = {}
for row in mappings:
    proj = row['ProjectName']
    name = row['Name']
    if ">" not in name: # Only simple names
        if proj not in proj_to_names:
            proj_to_names[proj] = set()
        proj_to_names[proj].add(name)

# Iterate top projects
top_projects_checked = []
names_to_query = set()

# Check top 20 projects
for p in projects[:20]:
    pname = p['ProjectName']
    if pname in proj_to_names:
        names = proj_to_names[pname]
        names_to_query.update(names)
        top_projects_checked.append(pname)

print(f"Projects checking: {len(top_projects_checked)}")
print(f"Names to query: {len(names_to_query)}")
print("__RESULT__:")
print(json.dumps(list(names_to_query)))"""

env_args = {'var_function-call-2660530990158088057': ['project_info', 'project_packageversion'], 'var_function-call-18445320017639605208': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-13889704856690954866': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-5248700250808617462': [{'column_name': 'Project_Information', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Licenses', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Homepage', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OSSFuzz', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-15305008436238156375': [{'count(*)': '176998'}], 'var_function-call-11166708214773113276': [{'count_star()': '591699'}], 'var_function-call-1259760636008240709': [{'count_star()': '770'}], 'var_function-call-10720076050459861026': 'file_storage/function-call-10720076050459861026.json', 'var_function-call-8037384748417867872': 'file_storage/function-call-8037384748417867872.json', 'var_function-call-11127857364150401408': ['mui-org/material-ui', 'rails/rails', 'microsoft/typescript', 'mozilla/pdf.js', 'swagger-api/swagger-ui', 'strapi/strapi', 'moment/moment', 'lodash/lodash', 'leaflet/leaflet', 'react-navigation/react-navigation', 'semantic-org/semantic-ui', 'react-native-elements/react-native-elements', 'sveltejs/svelte', 'tailwindcss/tailwindcss', 'mono/mono', 'microsoft/monaco-editor', 'quilljs/quill', 'request/request', 'tencent/vconsole', 'react-native-community/react-native-webview', 'sortablejs/vue.draggable', 'styled-components/styled-components', 'theia-ide/theia', 'leecade/react-native-swiper', 'mapbox/mapbox-gl-js', 'rjsf-team/react-jsonschema-form', 'reactive-extensions/rxjs', 'mobxjs/mobx', 'tj/commander.js', 'medusajs/medusa', 'tmpvar/jsdom', 'svg/svgo', 'sass/node-sass', 'shaka-project/shaka-player', 'microsoft/typescript-website', 'sockjs/sockjs-client', 'sboudrias/inquirer.js', 'react-native-webrtc/react-native-webrtc', 'shopify/polaris-react', 'rebilly/redoc', 'mishoo/uglifyjs2', 'react-native-community/react-native-tab-view', 'mbrn/material-table', 'leaflet/leaflet.markercluster', 'react-toolbox/react-toolbox', 'rrag/react-stockcharts', 'snowpackjs/snowpack', 'mjmlio/mjml', 'solana-labs/wallet-adapter', 'motdotla/dotenv'], 'var_function-call-4019463048744936366': "SELECT ProjectName, Name, Version FROM project_packageversion WHERE System='NPM' AND ProjectType='GITHUB' AND ProjectName IN ('mui-org/material-ui', 'rails/rails', 'microsoft/typescript', 'mozilla/pdf.js', 'swagger-api/swagger-ui', 'strapi/strapi', 'moment/moment', 'lodash/lodash', 'leaflet/leaflet', 'react-navigation/react-navigation', 'semantic-org/semantic-ui', 'react-native-elements/react-native-elements', 'sveltejs/svelte', 'tailwindcss/tailwindcss', 'mono/mono', 'microsoft/monaco-editor', 'quilljs/quill', 'request/request', 'tencent/vconsole', 'react-native-community/react-native-webview', 'sortablejs/vue.draggable', 'styled-components/styled-components', 'theia-ide/theia', 'leecade/react-native-swiper', 'mapbox/mapbox-gl-js', 'rjsf-team/react-jsonschema-form', 'reactive-extensions/rxjs', 'mobxjs/mobx', 'tj/commander.js', 'medusajs/medusa', 'tmpvar/jsdom', 'svg/svgo', 'sass/node-sass', 'shaka-project/shaka-player', 'microsoft/typescript-website', 'sockjs/sockjs-client', 'sboudrias/inquirer.js', 'react-native-webrtc/react-native-webrtc', 'shopify/polaris-react', 'rebilly/redoc', 'mishoo/uglifyjs2', 'react-native-community/react-native-tab-view', 'mbrn/material-table', 'leaflet/leaflet.markercluster', 'react-toolbox/react-toolbox', 'rrag/react-stockcharts', 'snowpackjs/snowpack', 'mjmlio/mjml', 'solana-labs/wallet-adapter', 'motdotla/dotenv')", 'var_function-call-2098349176198877097': 'file_storage/function-call-2098349176198877097.json', 'var_function-call-17419452042060611781': ['@dssd1001/wallet-adapter-coinhub', '@dssd1001/wallet-adapter-wallets', '@dummmy/webpack-cli>1.0.3>lodash', '@dummmy/webpack-cli>1.0.5>lodash', '@dollarshaveclub/cli>1.5.1>lodash', '@dollarshaveclub/cli>1.5.2>moment', '@dollarshaveclub/cli>1.5.4>moment', '@dollarshaveclub/cli>1.7.1>moment', '@dollarshaveclub/cli>1.9.1>moment', '@dollarshaveclub/cli>2.0.1>lodash'], 'var_function-call-16086012669719736030': ['@easyv/leaflet.markercluster', '@dssd1001/wallet-adapter-base', '@dssd1001/wallet-adapter-phantom', '@dssd1001/wallet-adapter-torus', '@ecomailcz/mjml-divider', '@dssd1001/wallet-adapter-react', '@ec-nordbund/leaflet', '@dssd1001/wallet-adapter-nextjs-starter', '@dssd1001/wallet-adapter-walletconnect', '@dssd1001/wallet-adapter-slope', '@ecomailcz/mjml-core', '@ebarmk/material-table', '@dssd1001/wallet-adapter-material-ui-starter', '@dongls/pdfjs-dist', '@ecomailcz/mjml-body', '@ecomailcz/mjml-head-title', '@ecomailcz/mjml-head-attributes', '@dylanvann/svelte', '@ecomailcz/mjml-image', '@ecomailcz/mjml-spacer', '@dssd1001/wallet-adapter-coinhub', '@dnaroid/medusa', '@ecomailcz/mjml-head-preview', '@dssd1001/wallet-adapter-solflare', '@dpwolfe/react-native-tab-view', '@ecomailcz/mjml-column', '@dplus/themed', '@ecomailcz/mjml-group', '@docid/monaco-editor', '@ecomailcz/mjml-navbar', '@dssd1001/wallet-adapter-material-ui', '@dssd1001/wallet-adapter-example', '@ecomailcz/mjml-parser-xml', '@ecomailcz/mjml-head-breakpoint', '@eataly/material-table', '@dongjiang/textmate-grammars', '@dssd1001/wallet-adapter-coin98', '@ecollect/redoc-cli', '@dssd1001/wallet-adapter-react-ui-starter', '@dman777/shadow-dom-quill-temp', '@ecomailcz/mjml', '@ecomailcz/mjml-social', '@ecomailcz/mjml-carousel', '@dssd1001/wallet-adapter-ant-design', '@dwarvesf/react-hooks', '@dumc11/tailwindcss', '@dssd1001/wallet-adapter-bitkeep', '@ecomailcz/mjml-validator', '@dssd1001/wallet-adapter-sollet', '@dssd1001/wallet-adapter-blocto']}

exec(code, env_args)
