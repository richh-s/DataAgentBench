code = """import json, re
from pathlib import Path
# Load files
pck_path = var_call_JLX8fJISuf0VC1Ing7Ys81b2
ppv_path = var_call_zATBQxYiBHWJjzdye9isrU7I
proj_info_path = var_call_HugYPThvuL8C04qfahztTSK3

with open(pck_path, 'r', encoding='utf-8') as f:
    packages = json.load(f)
with open(ppv_path, 'r', encoding='utf-8') as f:
    ppvs = json.load(f)
with open(proj_info_path, 'r', encoding='utf-8') as f:
    proj_infos = json.load(f)

# Build set of package keys (System,Name,Version)
pkg_keys = set((p['System'], p['Name'], p['Version']) for p in packages)
# Find matching ppvs
matches = [r for r in ppvs if (r['System'], r['Name'], r['Version']) in pkg_keys]
matched_projects = {r['ProjectName'] for r in matches if r.get('ProjectName')}

# Parse project_info to extract repo and forks
repo_forks = {}
for rec in proj_infos:
    info = rec.get('Project_Information') or ''
    # find repo pattern owner/repo (allow dots, dashes, underscores, numbers)
    m_repo = re.search(r'([A-Za-z0-9_.\-]+\/[A-Za-z0-9_.\-]+)', info)
    if not m_repo:
        continue
    repo = m_repo.group(1)
    # try multiple patterns for forks
    forks = None
    # patterns like: 'and 5782 forks' or 'has 5782 forks' or 'forks count of 11' or 'and has been forked 11 times'
    patterns = [r'([0-9][0-9,]*)\s+forks', r'forks count of\s*([0-9][0-9,]*)', r'([0-9][0-9,]*)\s+fork', r'forked\s+([0-9][0-9,]*)']
    for pat in patterns:
        m = re.search(pat, info)
        if m:
            try:
                forks = int(m.group(1).replace(',', ''))
                break
            except:
                pass
    if forks is None:
        # try to find numbers near 'fork'
        m2 = re.search(r'([0-9,]{1,9}).{0,20}fork', info)
        if m2:
            try:
                forks = int(m2.group(1).replace(',', ''))
            except:
                forks = None
    if forks is None:
        # fallback: skip
        continue
    # keep max if multiple entries
    if repo in repo_forks:
        repo_forks[repo] = max(repo_forks[repo], forks)
    else:
        repo_forks[repo] = forks

# Now filter to matched_projects
# Note: matched_projects may include entries like 'owner/repo' or full URLs? Use only exact matches
filtered = {repo: forks for repo, forks in repo_forks.items() if repo in matched_projects}

# If none matched due to mismatch, try loosen: match repo ending with repo name in matched_projects
if not filtered:
    # build set of repo names from matched_projects last part
    matched_last = {}
    for pname in matched_projects:
        if not pname or '/' not in pname:
            continue
        matched_last.setdefault(pname.split('/')[-1], set()).add(pname)
    for repo, forks in repo_forks.items():
        last = repo.split('/')[-1]
        if last in matched_last:
            # assign to all possible matched_project names
            for mp in matched_last[last]:
                filtered[mp] = forks

# Get top 5 by forks
top5 = sorted(filtered.items(), key=lambda x: x[1], reverse=True)[:5]

# Prepare output
out = [{'ProjectName': repo, 'Forks': forks} for repo, forks in top5]

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_JLX8fJISuf0VC1Ing7Ys81b2': 'file_storage/call_JLX8fJISuf0VC1Ing7Ys81b2.json', 'var_call_zATBQxYiBHWJjzdye9isrU7I': 'file_storage/call_zATBQxYiBHWJjzdye9isrU7I.json', 'var_call_DTNFCjZsYUoWiZsvoLRc68Y2': {'num_packages_filtered': 176998, 'num_ppv_rows': 597602, 'num_matches': 164782, 'num_unique_project_names': 5477, 'project_names_sample': ['/crislin2046', '/robpethick', '0x1ance/soulbound', '0x1ance/wishport', '0xsalah/tete', '1394/manipula', '1728954833/project-manager', '20lives/scad-js', '286810/react-native-switch-box', '431910864/dumi-antd-components', '4catalyzer/theme', '4x-sas/create-react-app', '6km/minify-css', '776a0a/dus', '7rulnik/postcss-flexibility', 'a5hik/ng-sortable', 'a7650/vue3-draggable-resizable', 'a916856595/react-dropdown', 'aareksio/koa-history-api-fallback', 'aareksio/node-steam-client', 'aaronjwang/redux-websocket', 'abacritt/angularx-social-login', 'abrcdf1023/egroup-material', 'abrcdf1023/egroup-redux', 'abrcdf1023/egroup-utils', 'abuinitski/redux-bundler-async-resources', 'accenture/sfpowerscripts', 'actorapp/react-scroll', 'adamhalasz/uniqid', 'aduth/preact-jsx-runtime', 'adyatlov/behold', 'aeb-labs/graphql-weaver', 'aelbore/esbuild-jest', 'age-bijkaart/cbuf', 'agenciaed3/event-emitter', 'agenciaed3/helix-hooks', 'agenciaed3/helix-style', 'agenciaed3/utils', 'agenciaed3/vtex-api', 'agtenr/typescript-storagefactory', 'agustinramos/react-orgchart', 'aheckmann/mquery', 'aheissenberger/serverless-appsync-offline', 'ahmadnassri/node-har-validator', 'ahmadreza-s/dotlottie-player', 'ahmadreza-s/xmlparser', 'ahomu/grunt-data-uri', 'ahram-dolphin/cli', 'ai/audio-recorder-polyfill', 'ai/browserslist', 'airbnb/babel-plugin-dynamic-import-node', 'airdwing/node-dwing-azure-iot-device-mqtt', 'airdwing/node-dwing-common', 'airtable/blocks', 'akiran/react-slick', 'akserg/ng2-dnd', 'akvelon/react-native-sms-user-consent', 'akveo/ng2-smart-table', 'alecramsay/district-analytics', 'alex3165/react-mapbox-gl', 'alexguan/node-zookeeper-client', 'alexindigo/asynckit', 'alexn400/mui-storybook', 'alexxandergrib/yoomoney-sdk', 'algolia/docsearch', 'algolia/react-element-to-jsx-string', 'alibaba/butterfly', 'alihamza1214/nuxt-multiple-fb-pixel-module', 'alioguzhan/react-editext', 'alpox/config-pug', 'alsmill/easy3wui', 'amadormf/dr-configuration', 'amadousysada/easypay_sdk', 'amasad/sane', 'aminebenkeroum/toggle-switch-react-native', 'ampedandwired/html-webpack-plugin', 'amruthpillai/fireup-cli', 'amsul/pickadate.js', 'andidittrich/node.cli-progress', 'andrelandgraf/react-ssml-dom', 'andrewdongminyoo/react-native-step-counter', 'andrewdongminyoo/segway-ble-manager', 'andrewusher/eslint-config', 'andrewusher/stylelint-config', 'andyperlitch/jsbn', 'ankit-gupta-1511/dlib-js', 'ankit2038/math-expression-evaluator', 'ankit31894/math-expression-evaluator', 'ankitverma0810/drv', 'ant-design/ant-design', 'ant-design/ant-design-icons', 'ant-design/pro-components', 'antelle/node-stream-zip', 'anteriovieira/doit', 'antfu/drauu', 'antfu/vite-plugin-md', 'antfu/vite-ssg', 'anthonygore/vuex-undo-redo', 'anthumchris/opus-stream-decoder', 'antonybudianto/cra-universal', 'anvaka/panzoom', 'apeswapfinance/apeswap-sdk', 'apollographql/apollo-link-state', 'appsignal/appsignal-javascript', 'aqkj/douhao-px2rpx', 'aqkj/douhao-singlefile', 'archergu/doubleshot', 'ardeshireshghi/react-scroll-tab', 'ardeshireshghi/vanilla-js-sidebar', 'arekinath/node-getpass', 'arekinath/node-sshpk', 'ariaminaei/dom-converter', 'ariaminaei/pretty-error', 'ariaminaei/renderkid', 'ariaminaei/utila', 'arisenio/dwebual-peepsid', 'ark-ecosystem-desktop-plugins/theme-template', 'arladmin/n8n-nodes-directus', 'arnesson/cordova-plugin-firebase', 'artema/grunt-compc', 'asbstty/tiny', 'aseemk/json5', 'ashtuchkin/iconv-lite', 'aspnetboilerplate/abp-ng2-module', 'asteriskzuo/react-native-create-thumbnail', 'astridlyre/fp', 'astridlyre/offhand', 'astroner/indexed-db', 'ateliershen/vue-scroll-trigger', 'atian25/alfred-plugin-projj', 'atlassian/cz-lerna-changelog', 'atomicpages/docusaurus-plugin-sass', 'atomicpages/eslint-config', 'atomicpages/pika-plugin-build-node', 'atomicpages/pika-plugin-build-web', 'atomicpages/pretty-checkbox', 'atomiks/tippyjs', 'ats1999/dsajs', 'atularen/ngx-monaco-editor', 'atyantik/pawjs', 'automattic/database', 'automattic/node-canvas', 'awesomeecosystem/ecosis', 'awesomeecosystem/scale', 'awilmoth/unicli', 'aws/aws-sdk-js', 'axiscommunications/media-stream-library-js', 'azlamsalam/sfpowerscripts', 'azure/azure-sdk-for-js', 'babel-utils/babel-plugin-tester', 'babel/babel', 'babel/babel-eslint', 'babel/babel-loader', 'babel/babel-preset-env', 'babel/babylon', 'bahamas10/css-color-names', 'baidu/san-devhook', 'baidu/san-devtool', 'balderdashy/sails-mongo', 'balsecaedwin/platzom', 'baoagency/polaris_view_components', 'bbecquet/leaflet.polylineoffset', 'bcoe/yargs', 'bct-taipei/react-native-dt-sdk', 'bct-taipei/react-native-sdk-ui', 'beatgammit/base64-js', 'becoswap/becoswap-sdk', 'becoswap/becoswap-toolkit', 'ben-eb/colormin', 'ben-eb/cssnano', 'ben-eb/postcss-charset', 'ben-eb/postcss-colormin', 'ben-eb/postcss-convert-values', 'ben-eb/postcss-discard-comments', 'ben-eb/postcss-discard-duplicates', 'ben-eb/postcss-discard-empty', 'ben-eb/postcss-discard-unused', 'ben-eb/postcss-merge-idents', 'ben-eb/postcss-merge-longhand', 'ben-eb/postcss-merge-rules', 'ben-eb/postcss-minify-gradients', 'ben-eb/postcss-minify-selectors', 'ben-eb/postcss-normalize-url', 'ben-eb/postcss-ordered-values', 'ben-eb/postcss-reduce-idents', 'ben-eb/postcss-reduce-initial', 'ben-eb/postcss-reduce-transforms', 'ben-eb/postcss-svgo', 'ben-eb/postcss-unique-selectors', 'ben-eb/postcss-zindex', 'ben-girardet/ecos-design-system', 'benawad/dogehouse', 'bencoveney/barrelsby', 'bencripps/react-redux-grid', 'benjamn/private', 'benmosher/eslint-plugin-import', 'bennodev19/dynamic-styles', 'berstend/puppeteer-extra', 'bestiejs/punycode.js', 'bevry/domain-browser']}, 'var_call_HugYPThvuL8C04qfahztTSK3': 'file_storage/call_HugYPThvuL8C04qfahztTSK3.json'}

exec(code, env_args)
