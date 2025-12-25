code = """import json
from packaging.version import parse as parse_version

# Load previous results
file_path_info = locals()['var_function-call-9958536016874276289'] # Project Info
file_path_map = locals()['var_function-call-17472800988890789756'] # Mapping
file_path_pkgs = locals()['var_function-call-16310798205590959367'] # Package Versions

# 1. Project Stars
with open(file_path_info, 'r') as f:
    data_info = json.load(f)

project_stars = {}
for entry in data_info:
    info = entry.get('Project_Information', '')
    # Extract Stars (same logic)
    import re
    stars_match = re.search(r'([\d,]+) stars', info)
    if stars_match:
        stars = int(stars_match.group(1).replace(',', ''))
        
        # Extract Name
        name = None
        prefixes = [
            r"The project named ([^\s,]+)",
            r"The GitHub project named ([^\s,]+)",
            r"under the name ([^\s,]+)",
            r"The project ([^\s,]+) is",
            r"The project ([^\s,]+) on",
            r"The GitHub project ([^\s,]+) currently",
        ]
        for p in prefixes:
            m = re.search(p, info)
            if m:
                name = m.group(1).rstrip('.')
                break
        if not name:
            candidates = re.findall(r'(?<!https://)(?<!http://)(?:github\.com/)?([a-zA-Z0-9_\-\.]+/[a-zA-Z0-9_\-\.]+)', info)
            for c in candidates:
                if c not in ['github.com', 'open-source']:
                    name = c
                    break
        if name and stars > 0:
            project_stars[name] = stars

# 2. Map Projects to Packages
with open(file_path_map, 'r') as f:
    data_map = json.load(f)

package_to_project = {}
for entry in data_map:
    pkg = entry.get('Name')
    proj = entry.get('ProjectName')
    if proj in project_stars:
        # If a package maps to multiple projects, we take the max stars? 
        # Or just one? Usually one package -> one project.
        # But here we have the reverse: one project -> many packages.
        # We want to associate the package with the project's stars.
        current_stars = project_stars[proj]
        if pkg in package_to_project:
             if current_stars > package_to_project[pkg]['Stars']:
                 package_to_project[pkg] = {'Project': proj, 'Stars': current_stars}
        else:
            package_to_project[pkg] = {'Project': proj, 'Stars': current_stars}

# 3. Get Latest Version for Packages
with open(file_path_pkgs, 'r') as f:
    data_pkgs = json.load(f)

latest_versions = {}
# Group by Name
from collections import defaultdict
pkg_versions = defaultdict(list)
for entry in data_pkgs:
    pkg_versions[entry['Name']].append(entry)

for name, versions in pkg_versions.items():
    # Filter valid versions?
    # Sort by UpstreamPublishedAt desc
    # If nan, treat as 0 or use version string
    
    def sort_key(v):
        ts = v.get('UpstreamPublishedAt')
        if ts is None or ts == 'nan':
            ts = 0.0
        else:
            ts = float(ts)
        return ts

    versions.sort(key=sort_key, reverse=True)
    
    # Check if we have valid timestamps
    if versions and (versions[0].get('UpstreamPublishedAt') == 'nan' or versions[0].get('UpstreamPublishedAt') is None):
        # Fallback to version string parsing
        try:
            versions.sort(key=lambda x: parse_version(x['Version']), reverse=True)
        except:
            pass # Keep original order or random
            
    if versions:
        latest = versions[0]
        latest_versions[name] = latest['Version']

# 4. Combine
final_list = []
for pkg, info in package_to_project.items():
    if pkg in latest_versions:
        final_list.append({
            'Package': pkg,
            'Version': latest_versions[pkg],
            'Stars': info['Stars'],
            'Project': info['Project']
        })

# 5. Sort and Top 5
final_list.sort(key=lambda x: x['Stars'], reverse=True)
top_5 = final_list[:5]

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-1166278330031295683': ['project_info', 'project_packageversion'], 'var_function-call-1166278330031292934': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_function-call-7576608018762177383': [{'COUNT(*)': '661372'}], 'var_function-call-7576608018762178154': [{'count_star()': '597602'}], 'var_function-call-7576608018762174829': [{'count_star()': '770'}], 'var_function-call-9958536016874276289': 'file_storage/function-call-9958536016874276289.json', 'var_function-call-12598818839012444368': [{'ProjectName': 'mui-org/material-ui', 'Stars': 89398}, {'ProjectName': 'sveltejs/svelte', 'Stars': 73499}, {'ProjectName': 'tailwindcss/tailwindcss', 'Stars': 73464}, {'ProjectName': 'strapi/strapi', 'Stars': 57236}, {'ProjectName': 'quilljs/quill', 'Stars': 42407}, {'ProjectName': 'styled-components/styled-components', 'Stars': 39660}, {'ProjectName': 'leaflet/leaflet', 'Stars': 38715}, {'ProjectName': 'microsoft/monaco-editor', 'Stars': 36025}, {'ProjectName': 'mobxjs/mobx', 'Stars': 26802}, {'ProjectName': 'react-native-elements/react-native-elements', 'Stars': 24814}, {'ProjectName': 'svg/svgo', 'Stars': 19768}, {'ProjectName': 'tmpvar/jsdom', 'Stars': 19356}, {'ProjectName': 'theia-ide/theia', 'Stars': 18526}, {'ProjectName': 'motdotla/dotenv', 'Stars': 17836}, {'ProjectName': 'thejameskyle/react-loadable', 'Stars': 16576}, {'ProjectName': 'mjmlio/mjml', 'Stars': 15829}, {'ProjectName': 'shelljs/shelljs', 'Stars': 14202}, {'ProjectName': 'rjsf-team/react-jsonschema-form', 'Stars': 13923}, {'ProjectName': 'mozilla-services/react-jsonschema-form', 'Stars': 13134}, {'ProjectName': 'tj/co', 'Stars': 11862}], 'var_function-call-16858975681660090751': [{'ProjectName': 'mjmlio/mjml', 'Name': '@ecomailcz/mjml-table'}, {'ProjectName': 'strapi/strapi', 'Name': '@edgarai/strapi-provider-upload-local'}, {'ProjectName': 'react-native-elements/react-native-elements', 'Name': '@dplus/themed'}, {'ProjectName': 'mobxjs/mobx', 'Name': '@dudadev/mobx-react'}, {'ProjectName': 'mjmlio/mjml', 'Name': '@ecomailcz/mjml-spacer'}, {'ProjectName': 'tj/co', 'Name': '@dollarshaveclub/cli>1.5.1>co'}, {'ProjectName': 'tj/co', 'Name': '@dollarshaveclub/cli>1.1.0>co'}, {'ProjectName': 'tj/co', 'Name': '@dollarshaveclub/cli>1.2.0>co'}, {'ProjectName': 'mui-org/material-ui', 'Name': '@docly/web'}, {'ProjectName': 'mjmlio/mjml', 'Name': '@ecomailcz/mjml-button'}, {'ProjectName': 'tmpvar/jsdom', 'Name': '@dwarvesf/react-scripts>0.7.0>jsdom'}, {'ProjectName': 'tj/co', 'Name': '@dollarshaveclub/cli>1.11.1>co'}, {'ProjectName': 'theia-ide/theia', 'Name': '@dongjiang/textmate-grammars'}, {'ProjectName': 'rjsf-team/react-jsonschema-form', 'Name': '@docknetwork/rsjf-material-ui'}, {'ProjectName': 'mjmlio/mjml', 'Name': '@ecomailcz/mjml-cli'}, {'ProjectName': 'mjmlio/mjml', 'Name': '@ecomailcz/mjml-accordion'}, {'ProjectName': 'motdotla/dotenv', 'Name': '@do-while-for-each/env>1.0.7>dotenv'}, {'ProjectName': 'tj/co', 'Name': '@dollarshaveclub/cli>1.11.2>co'}, {'ProjectName': 'shelljs/shelljs', 'Name': '@dwarvesf/react-scripts>0.7.0>shelljs'}, {'ProjectName': 'mjmlio/mjml', 'Name': '@ecomailcz/mjml-section'}, {'ProjectName': 'svg/svgo', 'Name': '@dpoineau/react-scripts>1.0.0>svgo'}, {'ProjectName': 'mjmlio/mjml', 'Name': '@ecomailcz/mjml-social'}, {'ProjectName': 'mjmlio/mjml', 'Name': '@ecomailcz/mjml-text'}, {'ProjectName': 'mjmlio/mjml', 'Name': '@ecomailcz/mjml-wrapper'}, {'ProjectName': 'tj/co', 'Name': '@dollarshaveclub/cli>1.9.1>co'}, {'ProjectName': 'tj/co', 'Name': '@dollarshaveclub/cli>1.7.1>co'}, {'ProjectName': 'mozilla-services/react-jsonschema-form', 'Name': '@distums/react-jsonschema-form'}, {'ProjectName': 'mjmlio/mjml', 'Name': '@ecomailcz/mjml'}, {'ProjectName': 'tmpvar/jsdom', 'Name': '@dpoineau/react-scripts>1.0.0>jsdom'}, {'ProjectName': 'mjmlio/mjml', 'Name': '@ecomailcz/mjml-image'}, {'ProjectName': 'tj/co', 'Name': '@dollarshaveclub/cli>1.8.0>co'}, {'ProjectName': 'microsoft/monaco-editor', 'Name': '@docid/monaco-editor'}, {'ProjectName': 'mjmlio/mjml', 'Name': '@ecomailcz/mjml-head-style'}, {'ProjectName': 'mjmlio/mjml', 'Name': '@ecomailcz/mjml-core'}, {'ProjectName': 'shelljs/shelljs', 'Name': '@dpoineau/react-scripts>1.0.0>shelljs'}, {'ProjectName': 'mjmlio/mjml', 'Name': '@ecomailcz/mjml-body'}, {'ProjectName': 'tj/co', 'Name': '@dollarshaveclub/cli>1.5.4>co'}, {'ProjectName': 'tj/co', 'Name': '@dollarshaveclub/cli>1.0.0>co'}, {'ProjectName': 'react-native-elements/react-native-elements', 'Name': '@dplus/rn-ui'}, {'ProjectName': 'tj/co', 'Name': '@dollarshaveclub/cli>1.5.0>co'}, {'ProjectName': 'tj/co', 'Name': '@dpoineau/react-scripts>1.0.0>co'}, {'ProjectName': 'tj/co', 'Name': '@dollarshaveclub/cli>1.11.0>co'}, {'ProjectName': 'mjmlio/mjml', 'Name': '@ecomailcz/mjml-navbar'}, {'ProjectName': 'sveltejs/svelte', 'Name': '@dylanvann/svelte'}, {'ProjectName': 'mjmlio/mjml', 'Name': '@ecomailcz/mjml-raw'}, {'ProjectName': 'motdotla/dotenv', 'Name': '@do-while-for-each/env>1.0.5>dotenv'}, {'ProjectName': 'leaflet/leaflet', 'Name': '@ec-nordbund/leaflet'}, {'ProjectName': 'mjmlio/mjml', 'Name': '@ecomailcz/mjml-head'}, {'ProjectName': 'react-native-elements/react-native-elements', 'Name': '@dplus/base'}, {'ProjectName': 'svg/svgo', 'Name': '@dwarvesf/react-scripts>0.7.0>svgo'}, {'ProjectName': 'styled-components/styled-components', 'Name': '@dynasty/styled-components'}, {'ProjectName': 'tj/co', 'Name': '@dollarshaveclub/cli>1.5.5>co'}, {'ProjectName': 'tj/co', 'Name': '@dollarshaveclub/cli>1.6.0>co'}, {'ProjectName': 'tj/co', 'Name': '@dollarshaveclub/cli>1.3.0>co'}, {'ProjectName': 'motdotla/dotenv', 'Name': '@do-while-for-each/env>1.0.6>dotenv'}, {'ProjectName': 'mjmlio/mjml', 'Name': '@ecomailcz/mjml-head-font'}, {'ProjectName': 'mjmlio/mjml', 'Name': '@ecomailcz/mjml-head-preview'}, {'ProjectName': 'tj/co', 'Name': '@dollarshaveclub/cli>1.5.7>co'}, {'ProjectName': 'tj/co', 'Name': '@dollarshaveclub/cli>1.10.0>co'}, {'ProjectName': 'tj/co', 'Name': '@dollarshaveclub/cli>1.10.1>co'}, {'ProjectName': 'mjmlio/mjml', 'Name': '@ecomailcz/mjml-validator'}, {'ProjectName': 'tj/co', 'Name': '@dollarshaveclub/cli>1.5.2>co'}, {'ProjectName': 'tj/co', 'Name': '@dollarshaveclub/cli>1.11.4>co'}, {'ProjectName': 'motdotla/dotenv', 'Name': '@do-while-for-each/env>1.0.4>dotenv'}, {'ProjectName': 'tailwindcss/tailwindcss', 'Name': '@dumc11/tailwindcss'}, {'ProjectName': 'thejameskyle/react-loadable', 'Name': '@docusaurus/react-loadable'}, {'ProjectName': 'mjmlio/mjml', 'Name': '@ecomailcz/mjml-parser-xml'}, {'ProjectName': 'mjmlio/mjml', 'Name': '@ecomailcz/mjml-hero'}, {'ProjectName': 'mjmlio/mjml', 'Name': '@ecomailcz/mjml-column'}, {'ProjectName': 'mjmlio/mjml', 'Name': '@ecomailcz/mjml-migrate'}, {'ProjectName': 'tj/co', 'Name': '@dwarvesf/react-scripts>0.7.0>co'}, {'ProjectName': 'tj/co', 'Name': '@dollarshaveclub/cli>1.5.3>co'}, {'ProjectName': 'quilljs/quill', 'Name': '@dman777/shadow-dom-quill-temp'}, {'ProjectName': 'mjmlio/mjml', 'Name': '@ecomailcz/mjml-group'}, {'ProjectName': 'mjmlio/mjml', 'Name': '@ecomailcz/mjml-carousel'}, {'ProjectName': 'mjmlio/mjml', 'Name': '@ecomailcz/mjml-head-title'}, {'ProjectName': 'tj/co', 'Name': '@dollarshaveclub/cli>1.11.3>co'}, {'ProjectName': 'motdotla/dotenv', 'Name': '@dpoineau/react-scripts>1.0.0>dotenv'}, {'ProjectName': 'mjmlio/mjml', 'Name': '@ecomailcz/mjml-divider'}, {'ProjectName': 'styled-components/styled-components', 'Name': '@dothq/styled-components'}, {'ProjectName': 'motdotla/dotenv', 'Name': '@dwarvesf/react-scripts>0.7.0>dotenv'}, {'ProjectName': 'mjmlio/mjml', 'Name': '@ecomailcz/mjml-head-attributes'}, {'ProjectName': 'mjmlio/mjml', 'Name': '@ecomailcz/mjml-head-breakpoint'}, {'ProjectName': 'tj/co', 'Name': '@dollarshaveclub/cli>1.9.0>co'}, {'ProjectName': 'tj/co', 'Name': '@dollarshaveclub/cli>1.5.6>co'}], 'var_function-call-11550502442095427689': [], 'var_function-call-11550502442095428926': [], 'var_function-call-11450524877001607985': [{'System': 'NPM'}], 'var_function-call-17472800988890789756': 'file_storage/function-call-17472800988890789756.json', 'var_function-call-4085139226816001667': ['@docly/web', '@dylanvann/svelte', '@dumc11/tailwindcss', '@edgarai/strapi-provider-upload-local', '@dman777/shadow-dom-quill-temp', '@dynasty/styled-components', '@dothq/styled-components', '@ec-nordbund/leaflet', '@docid/monaco-editor', '@dudadev/mobx-react', '@dplus/rn-ui', '@dplus/themed', '@dplus/base', '@dpoineau/react-scripts>1.0.0>svgo', '@dwarvesf/react-scripts>0.7.0>svgo', '@dpoineau/react-scripts>1.0.0>jsdom', '@dwarvesf/react-scripts>0.7.0>jsdom', '@dongjiang/textmate-grammars', '@do-while-for-each/env>1.0.6>dotenv', '@do-while-for-each/env>1.0.7>dotenv'], 'var_function-call-7164235446718216646': {'svelte': [], 'leaflet': [], 'react': [], 'vue': [], 'tailwindcss': [], 'material-ui': [], '@material-ui/core': []}, 'var_function-call-12569508223983704312': [{'Name': '@docly/web', 'Version': '0.1.371', 'UpstreamPublishedAt': '1545991781000000.0'}, {'Name': '@docly/web', 'Version': '0.1.371', 'UpstreamPublishedAt': '1545991781000000.0'}, {'Name': '@docly/web', 'Version': '0.2.0', 'UpstreamPublishedAt': '1547129862000000.0'}, {'Name': '@docly/web', 'Version': '0.2.0', 'UpstreamPublishedAt': '1547129862000000.0'}, {'Name': '@docly/web', 'Version': '0.0.1', 'UpstreamPublishedAt': '1538641264000000.0'}, {'Name': '@docly/web', 'Version': '0.0.1', 'UpstreamPublishedAt': '1538641264000000.0'}, {'Name': '@dman777/shadow-dom-quill-temp', 'Version': '1.0.0', 'UpstreamPublishedAt': '1616780038000000.0'}, {'Name': '@dman777/shadow-dom-quill-temp', 'Version': '1.0.0', 'UpstreamPublishedAt': '1616780038000000.0'}, {'Name': '@docly/web', 'Version': '0.0.2', 'UpstreamPublishedAt': '1538649015000000.0'}, {'Name': '@docly/web', 'Version': '0.0.2', 'UpstreamPublishedAt': '1538649015000000.0'}, {'Name': '@docly/web', 'Version': '0.2.1', 'UpstreamPublishedAt': '1549357582000000.0'}, {'Name': '@docly/web', 'Version': '0.2.1', 'UpstreamPublishedAt': '1549357582000000.0'}, {'Name': '@dylanvann/svelte', 'Version': '3.25.3', 'UpstreamPublishedAt': '1600151525000000.0'}, {'Name': '@dylanvann/svelte', 'Version': '3.25.3', 'UpstreamPublishedAt': '1600151525000000.0'}, {'Name': '@docly/web', 'Version': '0.1.381', 'UpstreamPublishedAt': '1546500487000000.0'}, {'Name': '@docly/web', 'Version': '0.1.381', 'UpstreamPublishedAt': '1546500487000000.0'}, {'Name': '@dylanvann/svelte', 'Version': '3.25.1', 'UpstreamPublishedAt': '1600149780000000.0'}, {'Name': '@dylanvann/svelte', 'Version': '3.25.1', 'UpstreamPublishedAt': '1600149780000000.0'}, {'Name': '@edgarai/strapi-provider-upload-local', 'Version': '3.6.3-devgar-fork.1', 'UpstreamPublishedAt': '1622625209000000.0'}, {'Name': '@edgarai/strapi-provider-upload-local', 'Version': '3.6.3-devgar-fork.1', 'UpstreamPublishedAt': '1622625209000000.0'}, {'Name': '@docly/web', 'Version': '0.2.2', 'UpstreamPublishedAt': '1549531828000000.0'}, {'Name': '@docly/web', 'Version': '0.2.2', 'UpstreamPublishedAt': '1549531828000000.0'}, {'Name': '@docly/web', 'Version': '0.2.3', 'UpstreamPublishedAt': '1552997178000000.0'}, {'Name': '@docly/web', 'Version': '0.2.3', 'UpstreamPublishedAt': '1552997178000000.0'}, {'Name': '@dylanvann/svelte', 'Version': '3.25.0', 'UpstreamPublishedAt': '1600148797000000.0'}, {'Name': '@dylanvann/svelte', 'Version': '3.25.0', 'UpstreamPublishedAt': '1600148797000000.0'}, {'Name': '@docly/web', 'Version': '0.1.362', 'UpstreamPublishedAt': '1544806738000000.0'}, {'Name': '@docly/web', 'Version': '0.1.362', 'UpstreamPublishedAt': '1544806738000000.0'}, {'Name': '@dumc11/tailwindcss', 'Version': '0.4.0', 'UpstreamPublishedAt': '1564590501000000.0'}, {'Name': '@dumc11/tailwindcss', 'Version': '0.4.0', 'UpstreamPublishedAt': '1564590501000000.0'}, {'Name': '@edgarai/strapi-provider-upload-local', 'Version': '3.6.3-devgar-fork.2', 'UpstreamPublishedAt': '1622625480000000.0'}, {'Name': '@edgarai/strapi-provider-upload-local', 'Version': '3.6.3-devgar-fork.2', 'UpstreamPublishedAt': '1622625480000000.0'}, {'Name': '@dylanvann/svelte', 'Version': '3.25.2', 'UpstreamPublishedAt': '1600150983000000.0'}, {'Name': '@dylanvann/svelte', 'Version': '3.25.2', 'UpstreamPublishedAt': '1600150983000000.0'}, {'Name': '@docly/web', 'Version': '0.0.362', 'UpstreamPublishedAt': '1544709142000000.0'}, {'Name': '@docly/web', 'Version': '0.0.362', 'UpstreamPublishedAt': '1544709142000000.0'}, {'Name': '@dylanvann/svelte', 'Version': '3.25.4', 'UpstreamPublishedAt': '1600151642000000.0'}, {'Name': '@dylanvann/svelte', 'Version': '3.25.4', 'UpstreamPublishedAt': '1600151642000000.0'}], 'var_function-call-17145688401764467711': [{'Name': '@dpoineau/react-scripts>1.0.0>svgo'}], 'var_function-call-16310798205590959367': 'file_storage/function-call-16310798205590959367.json'}

exec(code, env_args)
