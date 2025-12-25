code = """import json

# 1. Load project_packageversion data
with open(locals()['var_function-call-11230850855521488863'], 'r') as f:
    pp_data = json.load(f)

# Map ProjectName -> list of (Name, Version)
project_packages = {}
for row in pp_data:
    pname = row['ProjectName']
    if pname not in project_packages:
        project_packages[pname] = []
    project_packages[pname].append((row['Name'], row['Version']))

# 2. Load packageinfo data
with open(locals()['var_function-call-2860890206341780174'], 'r') as f:
    pi_data = json.load(f)

# Map (Name, Version) -> {Licenses, VersionInfo}
pkg_info_map = {}
for row in pi_data:
    key = (row['Name'], row['Version'])
    pkg_info_map[key] = {
        'Licenses': row['Licenses'],
        'VersionInfo': row['VersionInfo']
    }

# 3. Top 20 projects list (ordered by fork count)
top_projects = ["mui-org/material-ui", "rails/rails", "mozilla/pdf.js", "swagger-api/swagger-ui", "moment/moment", "lodash/lodash", "leaflet/leaflet", "react-navigation/react-navigation", "semantic-org/semantic-ui", "sveltejs/svelte", "tailwindcss/tailwindcss", "mono/mono", "microsoft/monaco-editor", "quilljs/quill", "tencent/vconsole", "react-native-community/react-native-webview", "sortablejs/vue.draggable", "styled-components/styled-components", "theia-ide/theia", "leecade/react-native-swiper"]

results = []

for proj in top_projects:
    packages = project_packages.get(proj, [])
    
    # Check if any package meets criteria
    is_valid_project = False
    for (name, version) in packages:
        info = pkg_info_map.get((name, version))
        if info:
            # Check License
            # Licenses is a JSON string array, e.g. '["MIT"]'
            licenses_str = info['Licenses']
            # Check Release
            # VersionInfo is JSON string, e.g. '{"IsRelease": true, ...}'
            vinfo_str = info['VersionInfo']
            
            # Simple string check for efficiency and robustness against malformed JSON
            has_mit = 'MIT' in licenses_str
            is_release = '"IsRelease": true' in vinfo_str or '"IsRelease":true' in vinfo_str
            
            if has_mit and is_release:
                is_valid_project = True
                break
    
    if is_valid_project:
        results.append(proj)
        if len(results) >= 5:
            break

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_function-call-13928812591632711456': ['project_info', 'project_packageversion'], 'var_function-call-12240981671246474953': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-15083778320079395426': [{'count_star()': '770'}], 'var_function-call-13555536260371993922': [{'count(*)': '0'}], 'var_function-call-10974219066575923235': [{'Licenses': '[\n  "EUPL-1.2"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'Licenses': '[\n  "ISC"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_function-call-3039377634705238947': [{'count(*)': '391228'}], 'var_function-call-3831245586645931117': [{'count(*)': '176998'}], 'var_function-call-1956027927471822867': 'file_storage/function-call-1956027927471822867.json', 'var_function-call-490725464643764431': [{'count_star()': '597602'}], 'var_function-call-9076153025003162607': ['mui-org/material-ui', 'rails/rails', 'mozilla/pdf.js', 'swagger-api/swagger-ui', 'moment/moment', 'lodash/lodash', 'leaflet/leaflet', 'react-navigation/react-navigation', 'semantic-org/semantic-ui', 'sveltejs/svelte', 'tailwindcss/tailwindcss', 'mono/mono', 'microsoft/monaco-editor', 'quilljs/quill', 'tencent/vconsole', 'react-native-community/react-native-webview', 'sortablejs/vue.draggable', 'styled-components/styled-components', 'theia-ide/theia', 'leecade/react-native-swiper'], 'var_function-call-11230850855521488863': 'file_storage/function-call-11230850855521488863.json', 'var_function-call-12276919263954392758': [{'System': 'NPM', 'Name': '@dollarshaveclub/cli>1.5.2>moment', 'Version': '2.20.1', 'Licenses': '[\n  "MIT"\n]', 'Links': '[\n  {\n    "Label": "SOURCE_REPO",\n    "URL": "git+https://github.com/moment/moment.git"\n  },\n  {\n    "Label": "ISSUE_TRACKER",\n    "URL": "https://github.com/moment/moment/issues"\n  },\n  {\n    "Label": "HOMEPAGE",\n    "URL": "http://momentjs.com"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 1\n}', 'Hashes': '[]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': 'None', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}], 'var_function-call-15338417879240143896': 'file_storage/function-call-15338417879240143896.json', 'var_function-call-13969883004575775392': 149, 'var_function-call-17321656562260675118': "'@dpwolfe/react-native-swiper', '@dollarshaveclub/cli>2.2.0>lodash', '@dmrvos/infrajs>0.0.6>moment', '@dummmy/webpack-cli>1.0.4>lodash', '@dxp-dc/vuedraggable', '@dollarshaveclub/cli>1.9.1>lodash', '@dollarshaveclub/cli>2.0.1>lodash', '@dollarshaveclub/cli>1.5.6>lodash', '@dollarshaveclub/cli>2.2.2>lodash', '@dylanvann/svelte', '@dollarshaveclub/cli>1.13.1>lodash', '@dollarshaveclub/cli>1.11.5>moment', '@dollarshaveclub/cli>1.9.1>moment', '@dpoineau/react-scripts>1.0.0>node-notifier>lodash.clonedeep', '@dollarshaveclub/cli>2.1.1>moment', '@dwarvesf/react-scripts>0.7.0>lodash._basefor', '@dollarshaveclub/cli>1.2.0>lodash', '@dwarvesf/react-scripts>0.7.0>lodash._basecopy', '@dwarvesf/react-scripts>0.7.0>lodash.words', '@dpoineau/react-scripts>1.0.0>http-proxy-middleware>lodash', '@dollarshaveclub/cli>1.13.0>lodash', '@dollarshaveclub/cli>2.2.1>lodash', '@eddyw-tsdx/react', '@dongls/pdfjs-dist', '@dummmy/pack-cli>1.0.8>lodash', '@dmrvos/infrajs>0.0.5>moment', '@dpoineau/react-scripts>1.0.0>lodash.words', '@dollarshaveclub/cli>1.9.0>lodash', '@dollarshaveclub/cli>1.9.0>moment', '@dwarvesf/react-scripts>0.7.0>lodash.clonedeep', '@dollarshaveclub/cli>2.0.0>moment', '@dwarvesf/react-scripts>0.7.0>lodash._getnative', '@dollarshaveclub/cli>1.5.2>lodash', '@dummmy/webpack-cli>1.0.7>lodash', '@dwarvesf/react-scripts>0.7.0>lodash.deburr', '@dpoineau/react-scripts>1.0.0>lodash._bindcallback', '@dollarshaveclub/cli>1.13.1>moment', '@dollarshaveclub/cli>1.3.0>lodash', '@dollarshaveclub/cli>1.5.2>moment', '@dummmy/webpack-cli>1.0.5>lodash', '@dollarshaveclub/cli>1.11.5-rc.1>lodash', '@dollarshaveclub/cli>1.10.1>moment', '@dollarshaveclub/cli>1.5.3>lodash', '@dpoineau/react-scripts>1.0.0>lodash.isarguments', '@dwarvesf/react-scripts>0.7.0>lodash.isarray', '@dpoineau/react-scripts>1.0.0>lodash.camelcase', '@dollarshaveclub/cli>2.2.0>moment', '@dollarshaveclub/cli>1.11.5>lodash', '@dollarshaveclub/cli>1.11.4>moment', '@dollarshaveclub/cli>1.5.5>moment', '@dreampie/semantic-ui', '@dpoineau/react-scripts>1.0.0>lodash.assign', '@dollarshaveclub/cli>1.5.1>lodash', '@dwarvesf/react-scripts>0.7.0>lodash.pickby', '@dman777/shadow-dom-quill-temp', '@dothq/styled-components', '@docid/monaco-editor', '@dollarshaveclub/cli>1.5.0>lodash', '@dynasty/styled-components', '@dollarshaveclub/cli>1.11.2>lodash', '@dollarshaveclub/cli>1.5.7>moment', '@dummmy/pack-cli>1.0.9>lodash', '@dpoineau/react-scripts>1.0.0>lodash._root', '@dwarvesf/react-scripts>0.7.0>lodash._createcompounder', '@dongjiang/textmate-grammars', '@dollarshaveclub/cli>1.11.3>lodash', '@dollarshaveclub/cli>1.11.0>lodash', '@dollarshaveclub/cli>2.1.0>moment', '@dollarshaveclub/cli>1.10.0>moment', '@dwarvesf/react-scripts>0.7.0>lodash.camelcase', '@dlwlrma00/react-native-webview-bypass-ssl', '@dpoineau/react-scripts>1.0.0>lodash.keys', '@dummmy/webpack-cli>1.0.6>lodash', '@dwarvesf/react-scripts>0.7.0>lodash', '@dolsem/actioncable', '@dollarshaveclub/cli>1.11.5-rc.1>moment', '@dollarshaveclub/cli>1.11.3>moment', '@dpoineau/react-scripts>1.0.0>lodash._baseclone', '@dwdjs/vconsole', '@dollarshaveclub/cli>1.11.2>moment', '@dpoineau/react-scripts>1.0.0>lodash', '@dollarshaveclub/cli>1.5.4>moment', '@dpoineau/react-scripts>1.0.0>lodash._baseassign', '@dollarshaveclub/cli>1.5.7>lodash', '@dollarshaveclub/cli>1.11.4>lodash', '@dpoineau/react-scripts>1.0.0>lodash.pickby', '@dollarshaveclub/cli>2.2.2>moment', '@dollarshaveclub/cli>1.5.0>moment', '@dpoineau/react-scripts>1.0.0>lodash._arrayeach', '@dwarvesf/react-scripts>0.7.0>lodash._baseclone', '@dollarshaveclub/cli>1.13.0>moment', '@dpoineau/react-scripts>1.0.0>lodash.find', '@dollarshaveclub/cli>2.1.0>lodash', '@dpwolfe/react-navigation', '@dollarshaveclub/cli>2.2.1>moment', '@dpoineau/react-scripts>1.0.0>html-webpack-plugin>lodash', '@dollarshaveclub/cli>1.7.1>lodash', '@dwarvesf/react-scripts>0.7.0>lodash.cond', '@dollarshaveclub/cli>1.11.1>moment', '@dpoineau/react-scripts>1.0.0>lodash.isarray', '@dollarshaveclub/cli>2.0.0>lodash', '@dwarvesf/react-scripts>0.7.0>lodash.keys', '@dpoineau/react-scripts>1.0.0>lodash.deburr', '@dpoineau/react-scripts>1.0.0>lodash.findindex', '@dollarshaveclub/cli>1.10.1>lodash', '@dpoineau/react-scripts>1.0.0>lodash.endswith', '@dpoineau/react-scripts>1.0.0>lodash.cond', '@dollarshaveclub/cli>1.6.0>lodash', '@dpoineau/react-scripts>1.0.0>lodash._basecopy', '@dpoineau/react-scripts>1.0.0>lodash.clonedeep', '@dwarvesf/react-scripts>0.7.0>lodash._arraycopy', '@dwarvesf/react-eslint-config', '@dummmy/webpack-cli>1.0.3>lodash', '@dwarvesf/react-scripts>0.7.0>lodash._arrayeach', '@dollarshaveclub/cli>1.10.0>lodash', '@dwarvesf/react-scripts>0.7.0>lodash.isarguments', '@dollarshaveclub/cli>1.5.5>lodash', '@domdomegg/swagger-ui', '@dollarshaveclub/cli>1.11.1>lodash', '@dwarvesf/react-scripts>0.7.0>lodash.indexof', '@dollarshaveclub/cli>1.5.1>moment', '@dwarvesf/react-scripts>0.7.0>lodash._root', '@dpoineau/react-scripts>1.0.0>lodash._basefor', '@dollarshaveclub/cli>1.12.0>lodash', '@dollarshaveclub/cli>2.1.1>lodash', '@dwarvesf/react-scripts>0.7.0>lodash._baseassign', '@dollarshaveclub/cli>1.5.3>moment', '@dollarshaveclub/cli>1.1.0>lodash', '@dollarshaveclub/cli>1.7.1>moment', '@dollarshaveclub/cli>1.8.0>lodash', '@dollarshaveclub/cli>1.5.4>lodash', '@dpoineau/react-scripts>1.0.0>lodash._createcompounder', '@dumc11/tailwindcss', '@dollarshaveclub/cli>1.0.0>lodash', '@dollarshaveclub/cli>1.12.0>moment', '@dollarshaveclub/cli>1.8.0>moment', '@dwarvesf/react-scripts>0.7.0>lodash.assign', '@docly/web', '@dpoineau/react-scripts>1.0.0>eslint-plugin-flowtype>lodash', '@dollarshaveclub/cli>1.5.6>moment', '@dollarshaveclub/cli>1.11.0>moment', '@dummmy/webpack-cli>1.0.2>lodash', '@dpoineau/react-scripts>1.0.0>lodash.indexof', '@ec-nordbund/leaflet', '@dollarshaveclub/cli>2.0.1>moment', '@dwarvesf/react-scripts>0.7.0>lodash._bindcallback', '@dpoineau/react-scripts>1.0.0>lodash._arraycopy', '@dwarvesf/react-hooks', '@dpoineau/react-scripts>1.0.0>lodash._getnative'", 'var_function-call-2860890206341780174': 'file_storage/function-call-2860890206341780174.json'}

exec(code, env_args)
