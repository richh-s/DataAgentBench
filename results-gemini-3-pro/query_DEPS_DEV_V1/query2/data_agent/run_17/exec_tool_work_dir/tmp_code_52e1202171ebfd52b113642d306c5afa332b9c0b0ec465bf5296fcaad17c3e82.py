code = """import json
import re
import pandas as pd

# 1. Load project_info and extract candidates
with open(locals()['var_function-call-3287875694004794152'], 'r') as f:
    project_info_data = json.load(f)

projects = []
name_patterns = [
    r"The project ([a-zA-Z0-9\-_]+/[a-zA-Z0-9\-_]+) is hosted on GitHub",
    r"The project ([a-zA-Z0-9\-_]+/[a-zA-Z0-9\-_]+) on GitHub",
    r"The project named ([a-zA-Z0-9\-_]+/[a-zA-Z0-9\-_]+) is hosted on GitHub",
    r"The GitHub project ([a-zA-Z0-9\-_]+/[a-zA-Z0-9\-_]+) currently has",
    r"The GitHub project named ([a-zA-Z0-9\-_]+/[a-zA-Z0-9\-_]+) currently has",
    r"under the name ([a-zA-Z0-9\-_]+/[a-zA-Z0-9\-_]+),",
    r"repository named ([a-zA-Z0-9\-_]+/[a-zA-Z0-9\-_]+),",
    r"The project ([a-zA-Z0-9\-_]+/[a-zA-Z0-9\-_]+) has an open issues count"
]
fork_patterns = [
    r"(\d+) forks",
    r"forks count of (\d+)",
    r"forked (\d+) times"
]

for entry in project_info_data:
    info = entry['Project_Information']
    project_name = None
    for pat in name_patterns:
        match = re.search(pat, info)
        if match:
            project_name = match.group(1)
            break
            
    fork_count = 0
    for pat in fork_patterns:
        match = re.search(pat, info)
        if match:
            fork_count = int(match.group(1).replace(',', ''))
            break
            
    if project_name:
        projects.append({'ProjectName': project_name, 'ForkCount': fork_count})

df_projects = pd.DataFrame(projects)
df_projects = df_projects.sort_values('ForkCount', ascending=False)
top_candidates = df_projects.head(50)['ProjectName'].tolist()

# 2. Load valid packages (MIT + Release)
with open(locals()['var_function-call-14961903004356817007'], 'r') as f:
    valid_packages_list = json.load(f)

# Create a set of (Name, Version) for fast lookup
# Licenses check: The query already filtered for LIKE '%MIT%'.
# I'll double check just in case, but rely on query mostly.
# Parse licenses?
valid_pkg_set = set()
for p in valid_packages_list:
    # Optional: strict check on licenses if needed.
    # p['Licenses'] is a string representation of list.
    # But usually LIKE '%MIT%' is good enough as primary filter.
    valid_pkg_set.add((p['Name'], p['Version']))

# 3. Load project mappings
with open(locals()['var_function-call-16269685256432633863'], 'r') as f:
    mapping_data = json.load(f)

# Group mappings by ProjectName
project_mappings = {}
for m in mapping_data:
    pn = m['ProjectName']
    if pn not in project_mappings:
        project_mappings[pn] = []
    project_mappings[pn].append((m['Name'], m['Version']))

# 4. Check candidates
final_winners = []
for proj in top_candidates:
    mappings = project_mappings.get(proj, [])
    # Check if any mapping is in valid_pkg_set
    is_valid = False
    for name, ver in mappings:
        if (name, ver) in valid_pkg_set:
            is_valid = True
            break
    
    if is_valid:
        final_winners.append(proj)
    
    if len(final_winners) == 5:
        break

print("__RESULT__:")
print(json.dumps(final_winners))"""

env_args = {'var_function-call-10990463094796803696': ['project_info', 'project_packageversion'], 'var_function-call-16203476491851295557': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-16203476491851292806': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}], 'var_function-call-782849471539256194': [{'count(*)': '176998'}], 'var_function-call-13120823261827482365': [{'count_star()': '597602'}], 'var_function-call-13120823261827482850': [{'count_star()': '770'}], 'var_function-call-3287875694004794152': 'file_storage/function-call-3287875694004794152.json', 'var_function-call-3547681825379929915': ['rails/rails', 'microsoft/typescript', 'swagger-api/swagger-ui', 'moment/moment', 'lodash/lodash', 'leaflet/leaflet', 'react-navigation/react-navigation', 'semantic-org/semantic-ui', 'tencent/vconsole', 'react-native-community/react-native-webview', 'theia-ide/theia', 'mapbox/mapbox-gl-js', 'reactive-extensions/rxjs', 'medusajs/medusa', 'sass/node-sass', 'shaka-project/shaka-player', 'microsoft/typescript-website', 'shopify/polaris-react', 'mishoo/uglifyjs2', 'mbrn/material-table', 'rrag/react-stockcharts', 'ternjs/acorn', 'mjmlio/mjml', 'solana-labs/wallet-adapter', 'schmich/instascan', 'tj/co', 'thejameskyle/react-loadable', 'matt-esch/virtual-dom', 'tailwindcss/tailwindcss', 'mono/mono', 'n4kz/react-native-material-textfield', 'mapbox/node-sqlite3', 'mobxjs/mobx', 'react-component/slider', 'ljharb/qs', 'react-icons/react-icons', 'shelljs/shelljs', 'tmpvar/jsdom', 'leandrowd/react-responsive-carousel', 'supasate/connected-react-router', 'securingsincity/react-ace', 'malte-wessel/react-custom-scrollbars', 'marcbachmann/node-html-pdf', 'namespace-ee/react-calendar-timeline', 'microsoft/web-build-tools', 'lekoarts/gatsby-themes', 'signavio/react-mentions', 'mapbox/mapbox-gl-draw', 'mui-org/material-ui', 'mozilla/pdfjs-dist'], 'var_function-call-16269685256432633863': 'file_storage/function-call-16269685256432633863.json', 'var_function-call-9922111886931549426': 'file_storage/function-call-9922111886931549426.json', 'var_function-call-14575413263545373728': [{'System': 'NPM', 'Name': '@dollarshaveclub/cli>1.5.0>qs', 'Version': '6.5.1', 'Licenses': '[\n  "BSD-3-Clause"\n]', 'Links': '[\n  {\n    "Label": "SOURCE_REPO",\n    "URL": "git+https://github.com/ljharb/qs.git"\n  },\n  {\n    "Label": "ISSUE_TRACKER",\n    "URL": "https://github.com/ljharb/qs/issues"\n  },\n  {\n    "Label": "HOMEPAGE",\n    "URL": "https://github.com/ljharb/qs"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 1\n}', 'Hashes': '[]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': 'None', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@dollarshaveclub/cli>1.5.0>qs', 'Version': '6.5.1', 'Licenses': '[\n  "BSD-3-Clause"\n]', 'Links': '[\n  {\n    "Label": "SOURCE_REPO",\n    "URL": "git+https://github.com/ljharb/qs.git"\n  },\n  {\n    "Label": "ISSUE_TRACKER",\n    "URL": "https://github.com/ljharb/qs/issues"\n  },\n  {\n    "Label": "HOMEPAGE",\n    "URL": "https://github.com/ljharb/qs"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 1\n}', 'Hashes': '[]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': 'None', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}], 'var_function-call-14961903004356817007': 'file_storage/function-call-14961903004356817007.json'}

exec(code, env_args)
