code = """import json

# Load data
with open(locals()['var_function-call-7163331856028641188'], 'r') as f: # ppv_data
    ppv_data = json.load(f)

with open(locals()['var_function-call-7138533570424954933'], 'r') as f: # pkg_data
    pkg_data = json.load(f)

top_projects = locals()['var_function-call-2944740537218165476']
project_star_map = {p['ProjectName']: p['Stars'] for p in top_projects}

# 1. Determine latest version for each package
# Group pkg_data by Name
pkg_versions = {}
for row in pkg_data:
    name = row['Name']
    ver = row['Version']
    v_info_str = row['VersionInfo']
    try:
        v_info = json.loads(v_info_str)
        is_release = v_info.get('IsRelease', False)
        ordinal = v_info.get('Ordinal', 0)
        
        if name not in pkg_versions:
            pkg_versions[name] = []
        pkg_versions[name].append({
            'Version': ver,
            'IsRelease': is_release,
            'Ordinal': ordinal
        })
    except:
        continue

latest_versions = {} # {Name: Version}
for name, versions in pkg_versions.items():
    # Filter for IsRelease if possible
    releases = [v for v in versions if v['IsRelease']]
    if not releases:
        releases = versions # Fallback if no release marked
    
    if not releases:
        continue
        
    # Sort by Ordinal descending
    releases.sort(key=lambda x: x['Ordinal'], reverse=True)
    latest_versions[name] = releases[0]['Version']

# 2. Filter ppv_data for latest versions and map to stars
package_stars = []

# Create a set of (Name, Version) for latest releases
latest_set = set()
for name, ver in latest_versions.items():
    latest_set.add((name, ver))

seen_packages = set()

for row in ppv_data:
    name = row['Name']
    ver = row['Version']
    proj = row['ProjectName']
    
    # Check if this is the latest version
    if (name, ver) in latest_set:
        if proj in project_star_map:
            stars = project_star_map[proj]
            # Avoid duplicates (if multiple projects map to same package, or multiple entries)
            # We'll take the max stars for a package if it appears multiple times
            # But here we just append and then group/deduplicate
            package_stars.append({
                'Name': name,
                'Version': ver,
                'Stars': stars,
                'Project': proj
            })

# Deduplicate: If a package appears multiple times (mapped to different projects?), take highest star count
unique_pkg_stars = {}
for item in package_stars:
    name = item['Name']
    if name not in unique_pkg_stars or item['Stars'] > unique_pkg_stars[name]['Stars']:
        unique_pkg_stars[name] = item

# Convert to list and sort
final_list = list(unique_pkg_stars.values())
final_list.sort(key=lambda x: x['Stars'], reverse=True)

# Top 5
top_5 = final_list[:5]

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-10108647606675870329': ['packageinfo'], 'var_function-call-10108647606675872212': ['project_info', 'project_packageversion'], 'var_function-call-1420295833218764681': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_function-call-1420295833218762508': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_function-call-1420295833218764431': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-1392887978617341216': [{'Count(*)': '661372'}], 'var_function-call-1392887978617342035': [{'count_star()': '597602'}], 'var_function-call-1392887978617342854': [{'count_star()': '770'}], 'var_function-call-584623543129131853': 'file_storage/function-call-584623543129131853.json', 'var_function-call-2944740537218165476': [{'ProjectName': 'mui-org/material-ui', 'Stars': 89398}, {'ProjectName': 'sveltejs/svelte', 'Stars': 73499}, {'ProjectName': 'tailwindcss/tailwindcss', 'Stars': 73464}, {'ProjectName': 'strapi/strapi', 'Stars': 57236}, {'ProjectName': 'quilljs/quill', 'Stars': 42407}, {'ProjectName': 'styled-components/styled-components', 'Stars': 39660}, {'ProjectName': 'microsoft/monaco-editor', 'Stars': 36025}, {'ProjectName': 'mobxjs/mobx', 'Stars': 26802}, {'ProjectName': 'react-native-elements/react-native-elements', 'Stars': 24814}, {'ProjectName': 'svg/svgo', 'Stars': 19768}, {'ProjectName': 'snowpackjs/snowpack', 'Stars': 19583}, {'ProjectName': 'tmpvar/jsdom', 'Stars': 19356}, {'ProjectName': 'motdotla/dotenv', 'Stars': 17836}, {'ProjectName': 'thejameskyle/react-loadable', 'Stars': 16576}, {'ProjectName': 'mjmlio/mjml', 'Stars': 15829}, {'ProjectName': 'shelljs/shelljs', 'Stars': 14202}, {'ProjectName': 'rjsf-team/react-jsonschema-form', 'Stars': 13923}, {'ProjectName': 'mozilla-services/react-jsonschema-form', 'Stars': 13134}, {'ProjectName': 'tj/co', 'Stars': 11862}, {'ProjectName': 'matt-esch/virtual-dom', 'Stars': 11564}, {'ProjectName': 'react-icons/react-icons', 'Stars': 11295}, {'ProjectName': 'mono/mono', 'Stars': 10630}, {'ProjectName': 'leecade/react-native-swiper', 'Stars': 10249}, {'ProjectName': 'rebilly/redoc', 'Stars': 9951}, {'ProjectName': 'marmelab/gremlins.js', 'Stars': 8973}, {'ProjectName': 'sockjs/sockjs-client', 'Stars': 8401}, {'ProjectName': 'terkelg/prompts', 'Stars': 8357}, {'ProjectName': 'microsoft/web-build-tools', 'Stars': 5338}, {'ProjectName': 'react-native-community/react-native-tab-view', 'Stars': 5137}, {'ProjectName': 'request/request-promise', 'Stars': 4769}], 'var_function-call-963153107397894205': "SELECT Name, Version, ProjectName FROM project_packageversion WHERE System='NPM' AND ProjectName IN ('mui-org/material-ui', 'sveltejs/svelte', 'tailwindcss/tailwindcss', 'strapi/strapi', 'quilljs/quill', 'styled-components/styled-components', 'microsoft/monaco-editor', 'mobxjs/mobx', 'react-native-elements/react-native-elements', 'svg/svgo', 'snowpackjs/snowpack', 'tmpvar/jsdom', 'motdotla/dotenv', 'thejameskyle/react-loadable', 'mjmlio/mjml', 'shelljs/shelljs', 'rjsf-team/react-jsonschema-form', 'mozilla-services/react-jsonschema-form', 'tj/co', 'matt-esch/virtual-dom', 'react-icons/react-icons', 'mono/mono', 'leecade/react-native-swiper', 'rebilly/redoc', 'marmelab/gremlins.js', 'sockjs/sockjs-client', 'terkelg/prompts', 'microsoft/web-build-tools', 'react-native-community/react-native-tab-view', 'request/request-promise')", 'var_function-call-7163331856028641188': 'file_storage/function-call-7163331856028641188.json', 'var_function-call-16836790718312778724': "SELECT Name, Version, VersionInfo FROM packageinfo WHERE System='NPM' AND Name IN ('@dollarshaveclub/cli>2.2.2>request-promise'', ''@dothq/styled-components'', ''@dollarshaveclub/cli>1.9.1>co'', ''@dollarshaveclub/cli>1.11.4>co'', ''@do-while-for-each/env>1.0.4>dotenv'', ''@dpoineau/react-scripts>1.0.0>svgo'', ''@dwarvesf/react-hooks'', ''@dollarshaveclub/cli>1.0.0>co'', ''@dollarshaveclub/cli>1.10.1>request-promise'', ''@ecomailcz/mjml-head-title'', ''@dollarshaveclub/cli>1.5.2>request-promise'', ''@dollarshaveclub/cli>1.2.0>request-promise'', ''@dollarshaveclub/cli>2.0.0>request-promise'', ''@dollarshaveclub/cli>1.5.0>request-promise'', ''@dollarshaveclub/cli>2.2.0>request-promise'', ''@dollarshaveclub/cli>1.11.3>request-promise'', ''@ecomailcz/mjml-head-font'', ''@dsch/react-icons'', ''@docusaurus/react-loadable'', ''@dollarshaveclub/cli>1.5.3>request-promise'', ''@dylanvann/svelte'', ''@dwarvesf/react-scripts>0.7.0>dotenv'', ''@dollarshaveclub/cli>2.1.0>request-promise'', ''@ecomailcz/mjml-wrapper'', ''@ecomailcz/mjml-head-breakpoint'', ''@dollarshaveclub/cli>1.13.1>request-promise'', ''@edgarai/strapi-provider-upload-local'', ''@dynasty/styled-components'', ''@do-while-for-each/env>1.0.6>dotenv'', ''@ecomailcz/mjml-core'', ''@dollarshaveclub/cli>1.1.0>request-promise'', ''@dollarshaveclub/cli>2.0.1>request-promise'', ''@ecollect/redoc-cli'', ''@discourse/virtual-dom'', ''@dplus/base'', ''@dollarshaveclub/cli>1.9.0>request-promise'', ''@do-while-for-each/env>1.0.5>dotenv'', ''@dollarshaveclub/cli>1.7.1>request-promise'', ''@dollarshaveclub/cli>1.5.4>request-promise'', ''@dollarshaveclub/cli>1.6.0>request-promise'', ''@ecomailcz/mjml-migrate'', ''@dollarshaveclub/cli>1.5.2>co'', ''@dollarshaveclub/cli>1.1.0>co'', ''@dpoineau/react-scripts>1.0.0>shelljs'', ''@ecomailcz/mjml-image'', ''@ecomailcz/mjml-validator'', ''@docid/monaco-editor'', ''@dollarshaveclub/cli>2.1.1>request-promise'', ''@dollarshaveclub/cli>1.11.2>co'', ''@ecomailcz/mjml-column'', ''@dollarshaveclub/cli>1.5.3>co'', ''@dollarshaveclub/cli>1.0.0>request-promise'', ''@dpwolfe/react-native-tab-view'', ''@dollarshaveclub/cli>1.5.5>co'', ''@dollarshaveclub/cli>1.6.0>co'', ''@ecomailcz/mjml-head-attributes'', ''@ecomailcz/mjml-head-style'', ''@dollarshaveclub/cli>1.10.1>co'', ''@dollarshaveclub/cli>1.13.0>request-promise'', ''@dollarshaveclub/cli>1.5.0>co'', ''@dvsmedeiros/prompts'', ''@dollarshaveclub/cli>1.10.0>co'', ''@dollarshaveclub/cli>1.9.0>co'', ''@dollarshaveclub/cli>1.2.0>co'', ''@ecomailcz/mjml-section'', ''@dollarshaveclub/cli>1.5.6>request-promise'', ''@dollarshaveclub/cli>1.10.0>request-promise'', ''@dollarshaveclub/cli>1.11.1>co'', ''@dwarvesf/react-scripts>0.7.0>svgo'', ''@eddyw-tsdx/react'', ''@ecomailcz/mjml-table'', ''@drptbl/gremlins.js'', ''@dpoineau/react-scripts>1.0.0>sockjs-client'', ''@ecomailcz/mjml-group'', ''@ecollect/redoc'', ''@dollarshaveclub/cli>1.11.5>request-promise'', ''@dollarshaveclub/cli>2.2.1>request-promise'', ''@dplus/rn-ui'', ''@ecomailcz/mjml-hero'', ''@dollarshaveclub/cli>1.5.5>request-promise'', ''@dollarshaveclub/cli>1.11.0>request-promise'', ''@dollarshaveclub/cli>1.11.2>request-promise'', ''@dpwolfe/react-native-swiper'', ''@ecomailcz/mjml-divider'', ''@dwarvesf/react-eslint-config'', ''@dumc11/tailwindcss'', ''@dollarshaveclub/cli>1.12.0>request-promise'', ''@dollarshaveclub/cli>1.11.4>request-promise'', ''@distums/react-jsonschema-form'', ''@dplus/themed'', ''@ecomailcz/mjml-cli'', ''@dollarshaveclub/cli>1.3.0>request-promise'', ''@dollarshaveclub/cli>1.11.3>co'', ''@ecomailcz/mjml-button'', ''@ecomailcz/mjml-text'', ''@ecomailcz/mjml-parser-xml'', ''@dylanvann/api-extractor'', ''@ecomailcz/mjml'', ''@dollarshaveclub/cli>1.8.0>request-promise'', ''@docly/web'', ''@ecomailcz/mjml-social'', ''@ecomailcz/mjml-navbar'', ''@dollarshaveclub/cli>1.11.1>request-promise'', ''@dollarshaveclub/cli>1.5.7>co'', ''@dollarshaveclub/cli>1.3.0>co'', ''@docknetwork/rsjf-material-ui'', ''@dman777/shadow-dom-quill-temp'', ''@dpoineau/react-scripts>1.0.0>jsdom'', ''@dwarvesf/react-scripts>0.7.0>sockjs-client'', ''@dollarshaveclub/cli>1.5.7>request-promise'', ''@dudadev/mobx-react'', ''@ecomailcz/mjml-accordion'', ''@ecomailcz/mjml-head-preview'', ''@ecomailcz/mjml-carousel'', ''@dollarshaveclub/cli>1.8.0>co'', ''@dollarshaveclub/cli>1.11.0>co'', ''@dollarshaveclub/cli>1.5.1>request-promise'', ''@dwarvesf/react-scripts>0.7.0>co'', ''@ecomailcz/mjml-spacer'', ''@dpoineau/react-scripts>1.0.0>co'', ''@dwarvesf/react-scripts>0.7.0>shelljs'', ''@ecomailcz/mjml-raw'', ''@ecomailcz/mjml-head'', ''@dishuostec/snowpack'', ''@dollarshaveclub/cli>1.5.6>co'', ''@dollarshaveclub/cli>1.5.1>co'', ''@dollarshaveclub/cli>1.7.1>co'', ''@dollarshaveclub/cli>1.5.4>co'', ''@dollarshaveclub/cli>1.9.1>request-promise'', ''@dpoineau/react-scripts>1.0.0>dotenv'', ''@dwarvesf/react-scripts>0.7.0>jsdom'', ''@do-while-for-each/env>1.0.7>dotenv'', ''@ecomailcz/mjml-body'', ''@dollarshaveclub/cli>1.11.5-rc.1>request-promise')", 'var_function-call-7138533570424954933': 'file_storage/function-call-7138533570424954933.json'}

exec(code, env_args)
