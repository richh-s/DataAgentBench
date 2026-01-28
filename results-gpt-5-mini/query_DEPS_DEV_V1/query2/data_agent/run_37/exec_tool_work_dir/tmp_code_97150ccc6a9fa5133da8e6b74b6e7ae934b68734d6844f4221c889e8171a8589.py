code = """import json
# load matched project names from earlier step
matched_fp = var_call_ogD5Q7WG4zCP1Zyz2rlGsLfK
with open(matched_fp,'r') as f:
    matched = json.load(f)
proj_names = matched['sample_projects']
# load project_info results
proj_info_fp = var_call_9rvkfNsWrcs7sbKXFwKeoet6
with open(proj_info_fp,'r') as f:
    proj_infos = json.load(f)
# Function to parse forks count from Project_Information text
import re
def parse_forks(s):
    if not s: return None
    m = re.search(r'forks? count of ([0-9,]+)', s)
    if not m:
        m = re.search(r'forks count of ([0-9,]+)', s)
    if not m:
        m = re.search(r'([0-9,]+) forks', s)
    if not m:
        m = re.search(r'([0-9,]+) fork', s)
    if not m:
        return None
    num = int(m.group(1).replace(',',''))
    return num
# try parsing for each proj_info
results = []
for r in proj_infos:
    pi = r.get('Project_Information')
    forks = parse_forks(pi)
    if forks is not None:
        # try to extract project name from text
        m = re.search(r'project ([\w\-\./]+)', pi)
        pname = None
        if m:
            pname = m.group(1)
        # fallback to Description or None
        results.append({'Project_Information': pi, 'Forks': forks, 'ProjectName_extracted': pname, 'Description': r.get('Description')})
# sort by forks descending and take top 20
results_sorted = sorted(results, key=lambda x: x['Forks'], reverse=True)[:20]
print('__RESULT__:')
print(json.dumps({'top_parsed': results_sorted}))"""

env_args = {'var_call_GFjoBvPPCjrqO1febE5dj3UX': ['packageinfo'], 'var_call_GEHAWCkzbkVYIGaW9lhUPqPS': ['project_info', 'project_packageversion'], 'var_call_xoiRbYVhG6oB3Nh77ykHM5fW': 'file_storage/call_xoiRbYVhG6oB3Nh77ykHM5fW.json', 'var_call_zMmer7wq6EmKDMw9EUItrB3A': 'file_storage/call_zMmer7wq6EmKDMw9EUItrB3A.json', 'var_call_aTGIMvGhLIZaefb28WGSKnYH': 'file_storage/call_aTGIMvGhLIZaefb28WGSKnYH.json', 'var_call_ogD5Q7WG4zCP1Zyz2rlGsLfK': {'num_matched_projects': 5477, 'sample_projects': ['/crislin2046', '/robpethick', '0x1ance/soulbound', '0x1ance/wishport', '0xsalah/tete', '1394/manipula', '1728954833/project-manager', '20lives/scad-js', '286810/react-native-switch-box', '431910864/dumi-antd-components', '4catalyzer/theme', '4x-sas/create-react-app', '6km/minify-css', '776a0a/dus', '7rulnik/postcss-flexibility', 'a5hik/ng-sortable', 'a7650/vue3-draggable-resizable', 'a916856595/react-dropdown', 'aareksio/koa-history-api-fallback', 'aareksio/node-steam-client', 'aaronjwang/redux-websocket', 'abacritt/angularx-social-login', 'abrcdf1023/egroup-material', 'abrcdf1023/egroup-redux', 'abrcdf1023/egroup-utils', 'abuinitski/redux-bundler-async-resources', 'accenture/sfpowerscripts', 'actorapp/react-scroll', 'adamhalasz/uniqid', 'aduth/preact-jsx-runtime', 'adyatlov/behold', 'aeb-labs/graphql-weaver', 'aelbore/esbuild-jest', 'age-bijkaart/cbuf', 'agenciaed3/event-emitter', 'agenciaed3/helix-hooks', 'agenciaed3/helix-style', 'agenciaed3/utils', 'agenciaed3/vtex-api', 'agtenr/typescript-storagefactory', 'agustinramos/react-orgchart', 'aheckmann/mquery', 'aheissenberger/serverless-appsync-offline', 'ahmadnassri/node-har-validator', 'ahmadreza-s/dotlottie-player', 'ahmadreza-s/xmlparser', 'ahomu/grunt-data-uri', 'ahram-dolphin/cli', 'ai/audio-recorder-polyfill', 'ai/browserslist', 'airbnb/babel-plugin-dynamic-import-node', 'airdwing/node-dwing-azure-iot-device-mqtt', 'airdwing/node-dwing-common', 'airtable/blocks', 'akiran/react-slick', 'akserg/ng2-dnd', 'akvelon/react-native-sms-user-consent', 'akveo/ng2-smart-table', 'alecramsay/district-analytics', 'alex3165/react-mapbox-gl', 'alexguan/node-zookeeper-client', 'alexindigo/asynckit', 'alexn400/mui-storybook', 'alexxandergrib/yoomoney-sdk', 'algolia/docsearch', 'algolia/react-element-to-jsx-string', 'alibaba/butterfly', 'alihamza1214/nuxt-multiple-fb-pixel-module', 'alioguzhan/react-editext', 'alpox/config-pug', 'alsmill/easy3wui', 'amadormf/dr-configuration', 'amadousysada/easypay_sdk', 'amasad/sane', 'aminebenkeroum/toggle-switch-react-native', 'ampedandwired/html-webpack-plugin', 'amruthpillai/fireup-cli', 'amsul/pickadate.js', 'andidittrich/node.cli-progress', 'andrelandgraf/react-ssml-dom', 'andrewdongminyoo/react-native-step-counter', 'andrewdongminyoo/segway-ble-manager', 'andrewusher/eslint-config', 'andrewusher/stylelint-config', 'andyperlitch/jsbn', 'ankit-gupta-1511/dlib-js', 'ankit2038/math-expression-evaluator', 'ankit31894/math-expression-evaluator', 'ankitverma0810/drv', 'ant-design/ant-design', 'ant-design/ant-design-icons', 'ant-design/pro-components', 'antelle/node-stream-zip', 'anteriovieira/doit', 'antfu/drauu', 'antfu/vite-plugin-md', 'antfu/vite-ssg', 'anthonygore/vuex-undo-redo', 'anthumchris/opus-stream-decoder', 'antonybudianto/cra-universal', 'anvaka/panzoom', 'apeswapfinance/apeswap-sdk', 'apollographql/apollo-link-state', 'appsignal/appsignal-javascript', 'aqkj/douhao-px2rpx', 'aqkj/douhao-singlefile', 'archergu/doubleshot', 'ardeshireshghi/react-scroll-tab', 'ardeshireshghi/vanilla-js-sidebar', 'arekinath/node-getpass', 'arekinath/node-sshpk', 'ariaminaei/dom-converter', 'ariaminaei/pretty-error', 'ariaminaei/renderkid', 'ariaminaei/utila', 'arisenio/dwebual-peepsid', 'ark-ecosystem-desktop-plugins/theme-template', 'arladmin/n8n-nodes-directus', 'arnesson/cordova-plugin-firebase', 'artema/grunt-compc', 'asbstty/tiny', 'aseemk/json5', 'ashtuchkin/iconv-lite', 'aspnetboilerplate/abp-ng2-module', 'asteriskzuo/react-native-create-thumbnail', 'astridlyre/fp', 'astridlyre/offhand', 'astroner/indexed-db', 'ateliershen/vue-scroll-trigger', 'atian25/alfred-plugin-projj', 'atlassian/cz-lerna-changelog', 'atomicpages/docusaurus-plugin-sass', 'atomicpages/eslint-config', 'atomicpages/pika-plugin-build-node', 'atomicpages/pika-plugin-build-web', 'atomicpages/pretty-checkbox', 'atomiks/tippyjs', 'ats1999/dsajs', 'atularen/ngx-monaco-editor', 'atyantik/pawjs', 'automattic/database', 'automattic/node-canvas', 'awesomeecosystem/ecosis', 'awesomeecosystem/scale', 'awilmoth/unicli', 'aws/aws-sdk-js', 'axiscommunications/media-stream-library-js', 'azlamsalam/sfpowerscripts', 'azure/azure-sdk-for-js', 'babel-utils/babel-plugin-tester', 'babel/babel', 'babel/babel-eslint', 'babel/babel-loader', 'babel/babel-preset-env', 'babel/babylon', 'bahamas10/css-color-names', 'baidu/san-devhook', 'baidu/san-devtool', 'balderdashy/sails-mongo', 'balsecaedwin/platzom', 'baoagency/polaris_view_components', 'bbecquet/leaflet.polylineoffset', 'bcoe/yargs', 'bct-taipei/react-native-dt-sdk', 'bct-taipei/react-native-sdk-ui', 'beatgammit/base64-js', 'becoswap/becoswap-sdk', 'becoswap/becoswap-toolkit', 'ben-eb/colormin', 'ben-eb/cssnano', 'ben-eb/postcss-charset', 'ben-eb/postcss-colormin', 'ben-eb/postcss-convert-values', 'ben-eb/postcss-discard-comments', 'ben-eb/postcss-discard-duplicates', 'ben-eb/postcss-discard-empty', 'ben-eb/postcss-discard-unused', 'ben-eb/postcss-merge-idents', 'ben-eb/postcss-merge-longhand', 'ben-eb/postcss-merge-rules', 'ben-eb/postcss-minify-gradients', 'ben-eb/postcss-minify-selectors', 'ben-eb/postcss-normalize-url', 'ben-eb/postcss-ordered-values', 'ben-eb/postcss-reduce-idents', 'ben-eb/postcss-reduce-initial', 'ben-eb/postcss-reduce-transforms', 'ben-eb/postcss-svgo', 'ben-eb/postcss-unique-selectors', 'ben-eb/postcss-zindex', 'ben-girardet/ecos-design-system', 'benawad/dogehouse', 'bencoveney/barrelsby', 'bencripps/react-redux-grid', 'benjamn/private', 'benmosher/eslint-plugin-import', 'bennodev19/dynamic-styles', 'berstend/puppeteer-extra', 'bestiejs/punycode.js', 'bevry/domain-browser']}, 'var_call_9rvkfNsWrcs7sbKXFwKeoet6': 'file_storage/call_9rvkfNsWrcs7sbKXFwKeoet6.json'}

exec(code, env_args)
