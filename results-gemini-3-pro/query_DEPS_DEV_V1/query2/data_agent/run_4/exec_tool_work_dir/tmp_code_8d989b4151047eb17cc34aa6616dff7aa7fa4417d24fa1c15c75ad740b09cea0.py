code = """import json

# Load project_packageversion result
with open(locals()['var_function-call-11230850855521488863'], 'r') as f:
    pp_data = json.load(f)

unique_names = list(set(item['Name'] for item in pp_data))

# Escape names for SQL (single quotes)
sql_names = "', '".join(name.replace("'", "''") for name in unique_names)
sql_clause = f"'{sql_names}'"

print('__RESULT__:')
print(json.dumps(sql_clause))"""

env_args = {'var_function-call-13928812591632711456': ['project_info', 'project_packageversion'], 'var_function-call-12240981671246474953': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-15083778320079395426': [{'count_star()': '770'}], 'var_function-call-13555536260371993922': [{'count(*)': '0'}], 'var_function-call-10974219066575923235': [{'Licenses': '[\n  "EUPL-1.2"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'Licenses': '[\n  "ISC"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_function-call-3039377634705238947': [{'count(*)': '391228'}], 'var_function-call-3831245586645931117': [{'count(*)': '176998'}], 'var_function-call-1956027927471822867': 'file_storage/function-call-1956027927471822867.json', 'var_function-call-490725464643764431': [{'count_star()': '597602'}], 'var_function-call-9076153025003162607': ['mui-org/material-ui', 'rails/rails', 'mozilla/pdf.js', 'swagger-api/swagger-ui', 'moment/moment', 'lodash/lodash', 'leaflet/leaflet', 'react-navigation/react-navigation', 'semantic-org/semantic-ui', 'sveltejs/svelte', 'tailwindcss/tailwindcss', 'mono/mono', 'microsoft/monaco-editor', 'quilljs/quill', 'tencent/vconsole', 'react-native-community/react-native-webview', 'sortablejs/vue.draggable', 'styled-components/styled-components', 'theia-ide/theia', 'leecade/react-native-swiper'], 'var_function-call-11230850855521488863': 'file_storage/function-call-11230850855521488863.json', 'var_function-call-12276919263954392758': [{'System': 'NPM', 'Name': '@dollarshaveclub/cli>1.5.2>moment', 'Version': '2.20.1', 'Licenses': '[\n  "MIT"\n]', 'Links': '[\n  {\n    "Label": "SOURCE_REPO",\n    "URL": "git+https://github.com/moment/moment.git"\n  },\n  {\n    "Label": "ISSUE_TRACKER",\n    "URL": "https://github.com/moment/moment/issues"\n  },\n  {\n    "Label": "HOMEPAGE",\n    "URL": "http://momentjs.com"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 1\n}', 'Hashes': '[]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': 'None', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}], 'var_function-call-15338417879240143896': 'file_storage/function-call-15338417879240143896.json', 'var_function-call-13969883004575775392': 149}

exec(code, env_args)
