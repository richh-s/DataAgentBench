code = """import json
import re
import pandas as pd

# Load project_info
path_proj_info = locals()['var_function-call-6539420380694691408']
with open(path_proj_info, 'r') as f:
    project_info_data = json.load(f)

# Parse project info
projects = []
for entry in project_info_data:
    info = entry.get('Project_Information', '')
    name = None
    p1 = re.search(r'project (?:is hosted on GitHub under the name |named |is a GitHub repository named )?([A-Za-z0-9\-\._]+/[A-Za-z0-9\-\._]+)', info)
    if p1:
        name = p1.group(1)
    
    forks = 0
    forks_match = re.search(r'([\d,]+) forks|forks count of ([\d,]+)|forked ([\d,]+) times', info)
    if name:
        if forks_match:
            f_str = forks_match.group(1) or forks_match.group(2) or forks_match.group(3)
            forks = int(f_str.replace(',', ''))
        projects.append({'ProjectName': name, 'Forks': forks})

df_projects = pd.DataFrame(projects).drop_duplicates()

# Load project_packageversion (top 100)
path_proj_ver = locals()['var_function-call-14821065375111072163']
with open(path_proj_ver, 'r') as f:
    proj_ver_data = json.load(f)
df_proj_ver = pd.DataFrame(proj_ver_data)

# Load packageinfo (NPM + MIT + Release)
path_pkg_info = locals()['var_function-call-8324090277572239767']
with open(path_pkg_info, 'r') as f:
    pkg_info_data = json.load(f)
df_pkg_info = pd.DataFrame(pkg_info_data)

# Join
# 1. Filter project_packageversion to only those in packageinfo (valid packages)
#    Merge on Name and Version
df_valid_pkgs = pd.merge(df_proj_ver, df_pkg_info[['Name', 'Version']], on=['Name', 'Version'], how='inner')

# 2. Get unique ProjectNames from valid packages
valid_project_names = df_valid_pkgs['ProjectName'].unique()

# 3. Filter df_projects to these names
df_final = df_projects[df_projects['ProjectName'].isin(valid_project_names)].copy()

# 4. Sort and top 5
df_final = df_final.sort_values('Forks', ascending=False).head(5)

result = df_final[['ProjectName', 'Forks']].to_dict(orient='records')
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-7179101092357015596': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@ecl%2Ftwig-component-carousel/3.11.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'Hashes': '[\n  {\n    "Hash": "vH5da6eUZ94i1AcOsrC6VjSV88cMUe5A1w+CDHAt2aYXldR9sBNRCse27cIx51GnUjnj7dSe3o5A81TjraJ0Lw==",\n    "Type": "SHA512"\n  },\n  {\n    "Hash": "WZUWPp1jVp6nrUZ0n7vmthbB4OrtnLFNDOPPBBNp15I=",\n    "Type": "SHA256"\n  },\n  {\n    "Hash": "JbFslb4AeqQVI+LCXFeZKFrWmHI=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "zBm5Qvg5p2bQwUTcg6hZYA==",\n    "Type": "MD5"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1699345351000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}], 'var_function-call-7179101092357015271': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-7179101092357014946': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-2936867257169916719': [{'COUNT(*)': '176170'}], 'var_function-call-2936867257169916638': [{'count_star()': '597602'}], 'var_function-call-2936867257169916557': [{'count_star()': '770'}], 'var_function-call-6539420380694691408': 'file_storage/function-call-6539420380694691408.json', 'var_function-call-12313832699212497409': 'file_storage/function-call-12313832699212497409.json', 'var_function-call-5616184914363530156': 'file_storage/function-call-5616184914363530156.json', 'var_function-call-11511442993304706373': "'mui-org/material-ui', 'rails/rails', 'microsoft/typescript', 'mozilla/pdf.js', 'swagger-api/swagger-ui', 'strapi/strapi', 'moment/moment', 'lodash/lodash', 'leaflet/leaflet', 'react-navigation/react-navigation', 'semantic-org/semantic-ui', 'react-native-elements/react-native-elements', 'sveltejs/svelte', 'tailwindcss/tailwindcss', 'mono/mono', 'microsoft/monaco-editor', 'quilljs/quill', 'request/request', 'tencent/vconsole', 'react-native-community/react-native-webview', 'sortablejs/vue.draggable', 'styled-components/styled-components', 'theia-ide/theia', 'leecade/react-native-swiper', 'mapbox/mapbox-gl-js', 'rjsf-team/react-jsonschema-form', 'mozilla-services/react-jsonschema-form', 'reactive-extensions/rxjs', 'mobxjs/mobx', 'tj/commander.js', 'medusajs/medusa', 'tmpvar/jsdom', 'svg/svgo', 'sass/node-sass', 'shaka-project/shaka-player', 'microsoft/typescript-website', 'sockjs/sockjs-client', 'sboudrias/inquirer.js', 'react-native-webrtc/react-native-webrtc', 'shopify/polaris-react', 'rebilly/redoc', 'mishoo/uglifyjs2', 'react-native-community/react-native-tab-view', 'mbrn/material-table', 'leaflet/leaflet.markercluster', 'react-toolbox/react-toolbox', 'rrag/react-stockcharts', 'snowpackjs/snowpack', 'ternjs/acorn', 'mjmlio/mjml', 'solana-labs/wallet-adapter', 'motdotla/dotenv', 'schmich/instascan', 'tj/co', 'thejameskyle/react-loadable', 'matt-esch/virtual-dom', 'n4kz/react-native-material-textfield', 'mapbox/node-sqlite3', 'react-component/slider', 'ljharb/qs', 'react-icons/react-icons', 'shelljs/shelljs', 'mpetroff/pannellum', 'leandrowd/react-responsive-carousel', 'supasate/connected-react-router', 'securingsincity/react-ace', 'malte-wessel/react-custom-scrollbars', 'marcbachmann/node-html-pdf', 'namespace-ee/react-calendar-timeline', 'microsoft/web-build-tools', 'lekoarts/gatsby-themes', 'signavio/react-mentions', 'mapbox/mapbox-gl-draw', 'mozilla/pdfjs-dist', 'marmelab/gremlins.js', 'riophae/vue-treeselect', 'naoufal/react-native-touch-id', 'marak/colors.js', 'redux-observable/redux-observable', 'react-component/select', 'serverless-nextjs/serverless-next.js', 'sveltejs/sapper', 'sindresorhus/query-string', 'searchkit/searchkit', 'naoufal/react-native-payments', 'mikemcl/big.js', 'react-qr-reader/react-qr-reader', 'mengxiong10/vue2-datepicker', 'salesforce/lwc', 'spite/three.meshline', 'siimon/prom-client', 'mozilla/source-map', 'remaxjs/remax', 'semantic-org/semantic-ui-css', 'mikaelbr/node-notifier', 'sourcey/spectacle', 'terkelg/prompts', 'then/promise', 'sockjs/sockjs-node', 'react-materialize/react-materialize'", 'var_function-call-14821065375111072163': 'file_storage/function-call-14821065375111072163.json', 'var_function-call-13460428235849738737': 'file_storage/function-call-13460428235849738737.json', 'var_function-call-8324090277572239767': 'file_storage/function-call-8324090277572239767.json'}

exec(code, env_args)
