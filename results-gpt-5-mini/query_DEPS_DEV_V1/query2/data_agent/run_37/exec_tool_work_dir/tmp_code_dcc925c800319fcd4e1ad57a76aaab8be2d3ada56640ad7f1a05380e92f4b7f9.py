code = """import json, re
# file paths from storage
pkg_fp = var_call_xoiRbYVhG6oB3Nh77ykHM5fW
proj_pkg_fp = var_call_aTGIMvGhLIZaefb28WGSKnYH
proj_info_fp = var_call_9rvkfNsWrcs7sbKXFwKeoet6
# load data
with open(pkg_fp,'r') as f:
    pkgs = json.load(f)
with open(proj_pkg_fp,'r') as f:
    proj_pkg = json.load(f)
with open(proj_info_fp,'r') as f:
    proj_infos = json.load(f)
# build set of Name/Version from pkgs (these are NPM MIT IsRelease results)
pkg_nv = set((r['Name'], r['Version']) for r in pkgs)
# build set of project repo names that map to these package versions
matched_repos = set()
for r in proj_pkg:
    key = (r['Name'], r['Version'])
    if key in pkg_nv:
        pn = r.get('ProjectName')
        if pn:
            matched_repos.add(pn.strip())
# now parse project_info entries: keep those with Licenses including MIT and whose repo path appears in matched_repos
# extract repo path from Project_Information using regex
repo_regex = re.compile(r'([A-Za-z0-9_.\-]+/[A-Za-z0-9_.\-]+)')
num_regex = re.compile(r'([0-9][0-9,]*)\s*(?:forks|fork)')
alt_regex = re.compile(r'forks? count of\s*([0-9,]+)')
results = []
for entry in proj_infos:
    lic = entry.get('Licenses') or ''
    if 'MIT' not in lic:
        continue
    pi = entry.get('Project_Information') or ''
    # find repo path
    repo = None
    m = repo_regex.search(pi)
    if m:
        repo = m.group(1)
    # if repo not found, skip
    if not repo:
        continue
    # only consider if repo in matched_repos
    if repo not in matched_repos:
        continue
    # parse forks
    fnum = None
    m2 = alt_regex.search(pi)
    if m2:
        fnum = int(m2.group(1).replace(',',''))
    else:
        m3 = num_regex.search(pi)
        if m3:
            fnum = int(m3.group(1).replace(',',''))
    if fnum is None:
        # try other patterns like 'and X forks' or ', X forks'
        m4 = re.search(r',\s*([0-9,]+)\s*forks', pi)
        if m4:
            fnum = int(m4.group(1).replace(',',''))
    if fnum is None:
        continue
    results.append({'ProjectName': repo, 'Forks': fnum, 'Project_Information': pi})
# deduplicate by ProjectName keeping max forks (if duplicates)
best = {}
for r in results:
    name = r['ProjectName']
    if name not in best or r['Forks'] > best[name]['Forks']:
        best[name] = {'ProjectName': name, 'Forks': r['Forks'], 'Project_Information': r['Project_Information']}
# sort and take top 5
top5 = sorted(best.values(), key=lambda x: x['Forks'], reverse=True)[:5]
# prepare output: list of dicts with ProjectName and Forks
out_list = [{'ProjectName': r['ProjectName'], 'Forks': r['Forks']} for r in top5]
print('__RESULT__:')
print(json.dumps(out_list))"""

env_args = {'var_call_GFjoBvPPCjrqO1febE5dj3UX': ['packageinfo'], 'var_call_GEHAWCkzbkVYIGaW9lhUPqPS': ['project_info', 'project_packageversion'], 'var_call_xoiRbYVhG6oB3Nh77ykHM5fW': 'file_storage/call_xoiRbYVhG6oB3Nh77ykHM5fW.json', 'var_call_zMmer7wq6EmKDMw9EUItrB3A': 'file_storage/call_zMmer7wq6EmKDMw9EUItrB3A.json', 'var_call_aTGIMvGhLIZaefb28WGSKnYH': 'file_storage/call_aTGIMvGhLIZaefb28WGSKnYH.json', 'var_call_ogD5Q7WG4zCP1Zyz2rlGsLfK': {'num_matched_projects': 5477, 'sample_projects': ['/crislin2046', '/robpethick', '0x1ance/soulbound', '0x1ance/wishport', '0xsalah/tete', '1394/manipula', '1728954833/project-manager', '20lives/scad-js', '286810/react-native-switch-box', '431910864/dumi-antd-components', '4catalyzer/theme', '4x-sas/create-react-app', '6km/minify-css', '776a0a/dus', '7rulnik/postcss-flexibility', 'a5hik/ng-sortable', 'a7650/vue3-draggable-resizable', 'a916856595/react-dropdown', 'aareksio/koa-history-api-fallback', 'aareksio/node-steam-client', 'aaronjwang/redux-websocket', 'abacritt/angularx-social-login', 'abrcdf1023/egroup-material', 'abrcdf1023/egroup-redux', 'abrcdf1023/egroup-utils', 'abuinitski/redux-bundler-async-resources', 'accenture/sfpowerscripts', 'actorapp/react-scroll', 'adamhalasz/uniqid', 'aduth/preact-jsx-runtime', 'adyatlov/behold', 'aeb-labs/graphql-weaver', 'aelbore/esbuild-jest', 'age-bijkaart/cbuf', 'agenciaed3/event-emitter', 'agenciaed3/helix-hooks', 'agenciaed3/helix-style', 'agenciaed3/utils', 'agenciaed3/vtex-api', 'agtenr/typescript-storagefactory', 'agustinramos/react-orgchart', 'aheckmann/mquery', 'aheissenberger/serverless-appsync-offline', 'ahmadnassri/node-har-validator', 'ahmadreza-s/dotlottie-player', 'ahmadreza-s/xmlparser', 'ahomu/grunt-data-uri', 'ahram-dolphin/cli', 'ai/audio-recorder-polyfill', 'ai/browserslist', 'airbnb/babel-plugin-dynamic-import-node', 'airdwing/node-dwing-azure-iot-device-mqtt', 'airdwing/node-dwing-common', 'airtable/blocks', 'akiran/react-slick', 'akserg/ng2-dnd', 'akvelon/react-native-sms-user-consent', 'akveo/ng2-smart-table', 'alecramsay/district-analytics', 'alex3165/react-mapbox-gl', 'alexguan/node-zookeeper-client', 'alexindigo/asynckit', 'alexn400/mui-storybook', 'alexxandergrib/yoomoney-sdk', 'algolia/docsearch', 'algolia/react-element-to-jsx-string', 'alibaba/butterfly', 'alihamza1214/nuxt-multiple-fb-pixel-module', 'alioguzhan/react-editext', 'alpox/config-pug', 'alsmill/easy3wui', 'amadormf/dr-configuration', 'amadousysada/easypay_sdk', 'amasad/sane', 'aminebenkeroum/toggle-switch-react-native', 'ampedandwired/html-webpack-plugin', 'amruthpillai/fireup-cli', 'amsul/pickadate.js', 'andidittrich/node.cli-progress', 'andrelandgraf/react-ssml-dom', 'andrewdongminyoo/react-native-step-counter', 'andrewdongminyoo/segway-ble-manager', 'andrewusher/eslint-config', 'andrewusher/stylelint-config', 'andyperlitch/jsbn', 'ankit-gupta-1511/dlib-js', 'ankit2038/math-expression-evaluator', 'ankit31894/math-expression-evaluator', 'ankitverma0810/drv', 'ant-design/ant-design', 'ant-design/ant-design-icons', 'ant-design/pro-components', 'antelle/node-stream-zip', 'anteriovieira/doit', 'antfu/drauu', 'antfu/vite-plugin-md', 'antfu/vite-ssg', 'anthonygore/vuex-undo-redo', 'anthumchris/opus-stream-decoder', 'antonybudianto/cra-universal', 'anvaka/panzoom', 'apeswapfinance/apeswap-sdk', 'apollographql/apollo-link-state', 'appsignal/appsignal-javascript', 'aqkj/douhao-px2rpx', 'aqkj/douhao-singlefile', 'archergu/doubleshot', 'ardeshireshghi/react-scroll-tab', 'ardeshireshghi/vanilla-js-sidebar', 'arekinath/node-getpass', 'arekinath/node-sshpk', 'ariaminaei/dom-converter', 'ariaminaei/pretty-error', 'ariaminaei/renderkid', 'ariaminaei/utila', 'arisenio/dwebual-peepsid', 'ark-ecosystem-desktop-plugins/theme-template', 'arladmin/n8n-nodes-directus', 'arnesson/cordova-plugin-firebase', 'artema/grunt-compc', 'asbstty/tiny', 'aseemk/json5', 'ashtuchkin/iconv-lite', 'aspnetboilerplate/abp-ng2-module', 'asteriskzuo/react-native-create-thumbnail', 'astridlyre/fp', 'astridlyre/offhand', 'astroner/indexed-db', 'ateliershen/vue-scroll-trigger', 'atian25/alfred-plugin-projj', 'atlassian/cz-lerna-changelog', 'atomicpages/docusaurus-plugin-sass', 'atomicpages/eslint-config', 'atomicpages/pika-plugin-build-node', 'atomicpages/pika-plugin-build-web', 'atomicpages/pretty-checkbox', 'atomiks/tippyjs', 'ats1999/dsajs', 'atularen/ngx-monaco-editor', 'atyantik/pawjs', 'automattic/database', 'automattic/node-canvas', 'awesomeecosystem/ecosis', 'awesomeecosystem/scale', 'awilmoth/unicli', 'aws/aws-sdk-js', 'axiscommunications/media-stream-library-js', 'azlamsalam/sfpowerscripts', 'azure/azure-sdk-for-js', 'babel-utils/babel-plugin-tester', 'babel/babel', 'babel/babel-eslint', 'babel/babel-loader', 'babel/babel-preset-env', 'babel/babylon', 'bahamas10/css-color-names', 'baidu/san-devhook', 'baidu/san-devtool', 'balderdashy/sails-mongo', 'balsecaedwin/platzom', 'baoagency/polaris_view_components', 'bbecquet/leaflet.polylineoffset', 'bcoe/yargs', 'bct-taipei/react-native-dt-sdk', 'bct-taipei/react-native-sdk-ui', 'beatgammit/base64-js', 'becoswap/becoswap-sdk', 'becoswap/becoswap-toolkit', 'ben-eb/colormin', 'ben-eb/cssnano', 'ben-eb/postcss-charset', 'ben-eb/postcss-colormin', 'ben-eb/postcss-convert-values', 'ben-eb/postcss-discard-comments', 'ben-eb/postcss-discard-duplicates', 'ben-eb/postcss-discard-empty', 'ben-eb/postcss-discard-unused', 'ben-eb/postcss-merge-idents', 'ben-eb/postcss-merge-longhand', 'ben-eb/postcss-merge-rules', 'ben-eb/postcss-minify-gradients', 'ben-eb/postcss-minify-selectors', 'ben-eb/postcss-normalize-url', 'ben-eb/postcss-ordered-values', 'ben-eb/postcss-reduce-idents', 'ben-eb/postcss-reduce-initial', 'ben-eb/postcss-reduce-transforms', 'ben-eb/postcss-svgo', 'ben-eb/postcss-unique-selectors', 'ben-eb/postcss-zindex', 'ben-girardet/ecos-design-system', 'benawad/dogehouse', 'bencoveney/barrelsby', 'bencripps/react-redux-grid', 'benjamn/private', 'benmosher/eslint-plugin-import', 'bennodev19/dynamic-styles', 'berstend/puppeteer-extra', 'bestiejs/punycode.js', 'bevry/domain-browser']}, 'var_call_9rvkfNsWrcs7sbKXFwKeoet6': 'file_storage/call_9rvkfNsWrcs7sbKXFwKeoet6.json', 'var_call_RWQceM3gVMLbEhuyVtlsdS90': {'count_with_forks': 476, 'top': [{'ProjectName': 'mui-org/material-ui', 'Forks': 30522, 'Project_Information': 'The project mui-org/material-ui on GitHub is a popular open-source library with a remarkable 89,398 stars and 30,522 forks, currently facing 1,688 open issues.'}, {'ProjectName': None, 'Forks': 21423, 'Project_Information': 'The project is hosted on GitHub under the name rails/rails, which currently has an open issues count of 1199, a stars count of 55319, and a forks count of 21423.'}, {'ProjectName': 'moment/moment', 'Forks': 7201, 'Project_Information': 'The project moment/moment on GitHub has an open issues count of 305, a stars count of 47549, and a forks count of 7201, making it a popular choice among developers for handling date and time in JavaScript.'}, {'ProjectName': 'semantic-org/semantic-ui', 'Forks': 4955, 'Project_Information': 'The project semantic-org/semantic-ui is hosted on GitHub and currently has an open issues count of 1076, along with a notable stars count of 51069 and 4955 forks.'}, {'ProjectName': 'react-native-elements/react-native-elements', 'Forks': 4623, 'Project_Information': 'The project react-native-elements/react-native-elements is a GitHub repository that currently has 116 open issues, 24,814 stars, and 4,623 forks, making it a popular choice for developers looking to enhance their React Native applications.'}, {'ProjectName': 'sveltejs/svelte', 'Forks': 4091, 'Project_Information': 'The project sveltejs/svelte on GitHub is an active repository with 907 open issues, boasting an impressive 73,499 stars and 4,091 forks.'}, {'ProjectName': 'tailwindcss/tailwindcss', 'Forks': 3848, 'Project_Information': 'The project tailwindcss/tailwindcss on GitHub is a popular framework with 73,464 stars and 3,848 forks, currently having 18 open issues.'}, {'ProjectName': 'microsoft/monaco-editor', 'Forks': 3407, 'Project_Information': 'The project microsoft/monaco-editor is hosted on GitHub and currently has 385 open issues, 36,025 stars, and 3,407 forks.'}, {'ProjectName': 'react-native-community/react-native-webview', 'Forks': 2962, 'Project_Information': 'The project react-native-community/react-native-webview is hosted on GitHub and currently has 87 open issues, 6345 stars, and 2962 forks.'}, {'ProjectName': None, 'Forks': 2890, 'Project_Information': 'The project named sortablejs/vue.draggable is hosted on GitHub, where it currently has an open issues count of 279, a stars count of 19911, and a forks count of 2890, making it a popular choice among developers for implementing draggable functionalities in Vue applications.'}, {'ProjectName': 'styled-components/styled-components', 'Forks': 2513, 'Project_Information': 'The project styled-components/styled-components on GitHub is a popular library with 39,660 stars and 2,513 forks, currently featuring an open issues count of 228.'}, {'ProjectName': 'leecade/react-native-swiper', 'Forks': 2392, 'Project_Information': 'The project leecade/react-native-swiper is hosted on GitHub and has a total of 786 open issues, along with an impressive 10,249 stars and 2,392 forks, making it a popular choice among developers for implementing swiping functionality in React Native applications.'}, {'ProjectName': 'mobxjs/mobx', 'Forks': 1783, 'Project_Information': 'The project mobxjs/mobx on GitHub is a popular repository that currently has 54 open issues, along with an impressive 26,802 stars and 1,783 forks.'}, {'ProjectName': 'tj/commander.js', 'Forks': 1739, 'Project_Information': 'The project tj/commander.js is hosted on GitHub and currently has an open issues count of 20, along with a notable stars count of 25437 and a forks count of 1739.'}, {'ProjectName': 'medusajs/medusa', 'Forks': 1699, 'Project_Information': 'The project medusajs/medusa on GitHub has an open issues count of 384, a stars count of 20285, and a forks count of 1699, making it a popular choice among developers for building e-commerce applications.'}, {'ProjectName': 'tmpvar/jsdom', 'Forks': 1668, 'Project_Information': 'The project tmpvar/jsdom is hosted on GitHub, where it currently has 479 open issues, 19,356 stars, and 1,668 forks, making it a popular choice among developers looking to work with a JavaScript environment that simulates a web browser.'}, {'ProjectName': None, 'Forks': 1449, 'Project_Information': 'The project react-native-device-info hosted on GitHub, under the repository name react-native-device-info/react-native-device-info, currently has 12 open issues, 6408 stars, and 1449 forks, making it a popular choice in the React Native community for device information management.'}, {'ProjectName': 'sass/node-sass', 'Forks': 1326, 'Project_Information': 'The project sass/node-sass on GitHub currently has 189 open issues, 8498 stars, and 1326 forks, making it a popular choice among developers for managing stylesheets with Sass.'}, {'ProjectName': 'sockjs/sockjs-client', 'Forks': 1298, 'Project_Information': 'The project sockjs/sockjs-client is hosted on GitHub and currently has 29 open issues, alongside an impressive 8,401 stars and 1,298 forks, indicating a strong interest and active engagement within the developer community.'}, {'ProjectName': 'react-native-webrtc/react-native-webrtc', 'Forks': 1227, 'Project_Information': 'The project react-native-webrtc/react-native-webrtc on GitHub is a popular repository with 4,546 stars and 1,227 forks, currently having 28 open issues.'}]}}

exec(code, env_args)
