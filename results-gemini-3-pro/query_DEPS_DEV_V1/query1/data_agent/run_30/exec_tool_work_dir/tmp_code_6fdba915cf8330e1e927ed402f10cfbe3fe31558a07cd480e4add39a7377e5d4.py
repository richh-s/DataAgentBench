code = """import json

# Load project_info (stars)
# Use the file from the first query
with open(locals()['var_function-call-17822456806728829320'], 'r') as f:
    project_info_list = json.load(f)

# Parse stars again
import re
project_stars = {}
for entry in project_info_list:
    text = entry.get('Project_Information', '')
    stars = 0
    stars_match = re.search(r'(\d{1,3}(?:,\d{3})*|\d+) stars', text)
    if stars_match:
        stars_str = stars_match.group(1).replace(',', '')
        stars = int(stars_str)
    
    # Extract project name.
    # I used a heuristic before. Let's use the same one or even simpler if I trust the parser.
    # However, I need to match the ProjectName from project_packageversion.
    # The project_packageversion has explicit ProjectName e.g., 'facebook/relay'.
    # project_info doesn't have explicit ProjectName column.
    # I must assume the ProjectName can be extracted from Project_Information.
    # "The project facebook/relay on GitHub..."
    
    # Let's try to map keys.
    # The previous parser worked well.
    
    tokens = text.split()
    project_name = None
    for token in tokens:
        token_clean = token.rstrip(',.')
        if '/' in token_clean and '://' not in token_clean:
            if re.match(r'^[A-Za-z0-9\._-]+/[A-Za-z0-9\._-]+$', token_clean):
                project_name = token_clean
                break
    
    if project_name:
        project_stars[project_name] = stars

# Load project_packageversion mappings
with open(locals()['var_function-call-16811222412829511630'], 'r') as f:
    ppv_list = json.load(f)

# Join
package_stars = []
for item in ppv_list:
    pkg_name = item['Name']
    proj_name = item['ProjectName']
    
    # Filter weird names
    if '>' in pkg_name:
        continue
    
    # Get stars
    if proj_name in project_stars:
        stars = project_stars[proj_name]
        package_stars.append({'Name': pkg_name, 'ProjectName': proj_name, 'Stars': stars})

# Sort by Stars DESC
package_stars.sort(key=lambda x: x['Stars'], reverse=True)

# Pick top 5
# There might be duplicates if multiple packages map to same project.
# I should maybe group by ProjectName or just list distinct packages.
# "Which packages are the top 5 most popular".
# I'll just take the top 5 distinct packages.

unique_top_packages = []
seen = set()
for p in package_stars:
    if p['Name'] not in seen:
        unique_top_packages.append(p)
        seen.add(p['Name'])
    if len(unique_top_packages) >= 20: # Get top 20 to verify
        break

print("__RESULT__:")
print(json.dumps(unique_top_packages))"""

env_args = {'var_function-call-15914319689598668120': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@ecl%2Ftwig-component-carousel/3.11.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'Hashes': '[\n  {\n    "Hash": "vH5da6eUZ94i1AcOsrC6VjSV88cMUe5A1w+CDHAt2aYXldR9sBNRCse27cIx51GnUjnj7dSe3o5A81TjraJ0Lw==",\n    "Type": "SHA512"\n  },\n  {\n    "Hash": "WZUWPp1jVp6nrUZ0n7vmthbB4OrtnLFNDOPPBBNp15I=",\n    "Type": "SHA256"\n  },\n  {\n    "Hash": "JbFslb4AeqQVI+LCXFeZKFrWmHI=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "zBm5Qvg5p2bQwUTcg6hZYA==",\n    "Type": "MD5"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1699345351000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'Licenses': '[]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@douganderson444%2Fpanzoom-node/v/1.1.5"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}', 'Hashes': '[\n  {\n    "Hash": "bn6jsFfgQaOqxYcxQLdn+w==",\n    "Type": "MD5"\n  },\n  {\n    "Hash": "Ag2muuzRUxbKTAR/H0qjiVGqd5E=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "Z2cdZL3dyM3mmLnEKE4HDFAFnE8OTVU1Lm36fasqZuFRlfjv+M8qkZs+ZAwOsR65FfhH1St2n1YvhihaMM5UEw==",\n    "Type": "SHA512"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '1', 'UpstreamPublishedAt': '1670271173000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'Licenses': '[]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@douganderson444%2Fpanzoom-node/v/1.1.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}', 'Hashes': '[\n  {\n    "Hash": "f882urh9+DaLLfg22vF4Dw==",\n    "Type": "MD5"\n  },\n  {\n    "Hash": "UavDKi+B1bjz5yL/IEUOzG5BIX0=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "Br/d41zpasemiy1jjn91jYmLFbgFFGo5+V+v5+LRxHeTg2MajAkwczkbMUyb3k8xD0UIubDfClv9roNgLIoOEQ==",\n    "Type": "SHA512"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '1', 'UpstreamPublishedAt': '1654791421000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'Licenses': '[\n  "ISC"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@dreamworld%2Fdw-select/3.1.2-fix-double-click-issue.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}', 'Hashes': '[\n  {\n    "Hash": "1e+/qEffZeAgXRtIOUmPqw==",\n    "Type": "MD5"\n  },\n  {\n    "Hash": "C3IyUAgv9Bs96QRmMOHUrQwBnS4=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "07tFydL0pzuqYZbHESf4n0N5gbgvaPZFBfRZmC+k4dqhaKjR2xRBXBpCyxji9W0kkkCVrgtiTrI/XzhgTBq80w==",\n    "Type": "SHA512"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1624260093000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@discue%2Fui-components/0.13.0"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}', 'Hashes': '[\n  {\n    "Hash": "9BaLXgrA89SmryO88KCXZg==",\n    "Type": "MD5"\n  },\n  {\n    "Hash": "1ehWf/vTvGu5BskEEAeiQL1rNcM=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "UOcNM2Ee5byWKfgJ8Q9am9B369//NKxfLA9nr20EClco8KptuYrcBXZXqOpBk3jJByBoEaek8n47WqZMiB7TDA==",\n    "Type": "SHA512"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1656518476000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}], 'var_function-call-15914319689598666853': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-15914319689598665586': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_function-call-10233798522283782408': [{'COUNT(*)': '661372'}], 'var_function-call-10233798522283783023': [{'count_star()': '597602'}], 'var_function-call-10233798522283783638': [{'count_star()': '770'}], 'var_function-call-17822456806728829320': 'file_storage/function-call-17822456806728829320.json', 'var_function-call-9298755348871748827': [{'ProjectName': 'mui-org/material-ui', 'Stars': 89398}, {'ProjectName': 'sveltejs/svelte', 'Stars': 73499}, {'ProjectName': 'tailwindcss/tailwindcss', 'Stars': 73464}, {'ProjectName': 'strapi/strapi', 'Stars': 57236}, {'ProjectName': 'quilljs/quill', 'Stars': 42407}, {'ProjectName': 'styled-components/styled-components', 'Stars': 39660}, {'ProjectName': 'leaflet/leaflet', 'Stars': 38715}, {'ProjectName': 'microsoft/monaco-editor', 'Stars': 36025}, {'ProjectName': 'mobxjs/mobx', 'Stars': 26802}, {'ProjectName': 'react-native-elements/react-native-elements', 'Stars': 24814}, {'ProjectName': 'svg/svgo', 'Stars': 19768}, {'ProjectName': 'tmpvar/jsdom', 'Stars': 19356}, {'ProjectName': 'theia-ide/theia', 'Stars': 18526}, {'ProjectName': 'motdotla/dotenv', 'Stars': 17836}, {'ProjectName': 'thejameskyle/react-loadable', 'Stars': 16576}, {'ProjectName': 'mjmlio/mjml', 'Stars': 15829}, {'ProjectName': 'shelljs/shelljs', 'Stars': 14202}, {'ProjectName': 'rjsf-team/react-jsonschema-form', 'Stars': 13923}, {'ProjectName': 'mozilla-services/react-jsonschema-form', 'Stars': 13134}, {'ProjectName': 'tj/co', 'Stars': 11862}], 'var_function-call-8702053101027841911': "'mui-org/material-ui', 'sveltejs/svelte', 'tailwindcss/tailwindcss', 'strapi/strapi', 'quilljs/quill', 'styled-components/styled-components', 'leaflet/leaflet', 'microsoft/monaco-editor', 'mobxjs/mobx', 'react-native-elements/react-native-elements', 'svg/svgo', 'tmpvar/jsdom', 'theia-ide/theia', 'motdotla/dotenv', 'thejameskyle/react-loadable', 'mjmlio/mjml', 'shelljs/shelljs', 'rjsf-team/react-jsonschema-form', 'mozilla-services/react-jsonschema-form', 'tj/co'", 'var_function-call-6603806072529876387': 'file_storage/function-call-6603806072529876387.json', 'var_function-call-9808195780650801386': ['@dudadev/mobx-react', '@ecomailcz/mjml-head-style', '@dylanvann/svelte', '@dollarshaveclub/cli>1.5.3>co', '@ecomailcz/mjml-carousel', '@dynasty/styled-components', '@ecomailcz/mjml-migrate', '@docly/web', '@ecomailcz/mjml-head-title', '@ecomailcz/mjml-head-font', '@dollarshaveclub/cli>1.10.1>co', '@do-while-for-each/env>1.0.5>dotenv', '@dollarshaveclub/cli>1.7.1>co', '@dollarshaveclub/cli>1.5.7>co', '@dongjiang/textmate-grammars', '@docid/monaco-editor', '@ecomailcz/mjml-social', '@dollarshaveclub/cli>1.11.3>co', '@ecomailcz/mjml-text', '@ecomailcz/mjml-parser-xml', '@dollarshaveclub/cli>1.10.0>co', '@dpoineau/react-scripts>1.0.0>jsdom', '@dwarvesf/react-scripts>0.7.0>jsdom', '@edgarai/strapi-provider-upload-local', '@ecomailcz/mjml-body', '@dwarvesf/react-scripts>0.7.0>svgo', '@ecomailcz/mjml-head-breakpoint', '@dpoineau/react-scripts>1.0.0>shelljs', '@ecomailcz/mjml', '@dumc11/tailwindcss', '@dplus/rn-ui', '@dollarshaveclub/cli>1.5.4>co', '@dollarshaveclub/cli>1.1.0>co', '@ecomailcz/mjml-group', '@dollarshaveclub/cli>1.3.0>co', '@dwarvesf/react-scripts>0.7.0>dotenv', '@dplus/base', '@ecomailcz/mjml-wrapper', '@dollarshaveclub/cli>1.8.0>co', '@dollarshaveclub/cli>1.5.1>co', '@ecomailcz/mjml-head-attributes', '@ecomailcz/mjml-table', '@dwarvesf/react-scripts>0.7.0>shelljs', '@ecomailcz/mjml-column', '@ec-nordbund/leaflet', '@dollarshaveclub/cli>1.0.0>co', '@dwarvesf/react-scripts>0.7.0>co', '@ecomailcz/mjml-navbar', '@ecomailcz/mjml-section', '@dollarshaveclub/cli>1.5.0>co', '@dollarshaveclub/cli>1.9.1>co', '@dollarshaveclub/cli>1.5.5>co', '@dpoineau/react-scripts>1.0.0>svgo', '@do-while-for-each/env>1.0.7>dotenv', '@dothq/styled-components', '@dpoineau/react-scripts>1.0.0>co', '@ecomailcz/mjml-raw', '@ecomailcz/mjml-image', '@ecomailcz/mjml-divider', '@ecomailcz/mjml-validator', '@dollarshaveclub/cli>1.5.2>co', '@dollarshaveclub/cli>1.11.1>co', '@dollarshaveclub/cli>1.2.0>co', '@docknetwork/rsjf-material-ui', '@dollarshaveclub/cli>1.9.0>co', '@dollarshaveclub/cli>1.11.4>co', '@do-while-for-each/env>1.0.4>dotenv', '@dplus/themed', '@dollarshaveclub/cli>1.11.0>co', '@ecomailcz/mjml-head-preview', '@ecomailcz/mjml-accordion', '@dollarshaveclub/cli>1.5.6>co', '@docusaurus/react-loadable', '@do-while-for-each/env>1.0.6>dotenv', '@ecomailcz/mjml-button', '@ecomailcz/mjml-cli', '@ecomailcz/mjml-core', '@dpoineau/react-scripts>1.0.0>dotenv', '@dman777/shadow-dom-quill-temp', '@dollarshaveclub/cli>1.6.0>co', '@ecomailcz/mjml-hero', '@ecomailcz/mjml-head', '@dollarshaveclub/cli>1.11.2>co', '@ecomailcz/mjml-spacer', '@distums/react-jsonschema-form'], 'var_function-call-4630520499945781790': {'count_total': 85, 'count_clean': 47, 'found_expected': [], 'sample_clean': ['@dplus/themed', '@ecomailcz/mjml-head-font', '@ecomailcz/mjml-head-breakpoint', '@dplus/base', '@docknetwork/rsjf-material-ui', '@ecomailcz/mjml-spacer', '@ecomailcz/mjml-divider', '@ecomailcz/mjml-head-title', '@ecomailcz/mjml-section', '@docusaurus/react-loadable', '@ecomailcz/mjml-head-style', '@dudadev/mobx-react', '@ecomailcz/mjml-social', '@dynasty/styled-components', '@ecomailcz/mjml-group', '@ecomailcz/mjml-button', '@ecomailcz/mjml-validator', '@ecomailcz/mjml-wrapper', '@ecomailcz/mjml-text', '@dumc11/tailwindcss']}, 'var_function-call-5912484552573923313': [], 'var_function-call-15460047695023523836': [], 'var_function-call-16811222412829511630': 'file_storage/function-call-16811222412829511630.json'}

exec(code, env_args)
