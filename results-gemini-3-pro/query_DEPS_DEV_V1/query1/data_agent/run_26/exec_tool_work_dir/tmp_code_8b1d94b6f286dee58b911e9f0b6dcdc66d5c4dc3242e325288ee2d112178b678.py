code = """import json
import pandas as pd
import re

# Load data
top_projects = locals()['var_function-call-18063043881055894313']
# Create map Project -> Stars
proj_stars = {p['ProjectName']: p['Stars'] for p in top_projects}

file_path = locals()['var_function-call-4389154146235398041']
with open(file_path, 'r') as f:
    mappings = json.load(f)

# Helper for version parsing
def parse_version(v_str):
    # Remove leading/trailing
    v_str = v_str.strip()
    # Extract numeric part (major.minor.patch)
    # Handle '1.2.3-beta' -> [1, 2, 3]
    # Handle '1.2' -> [1, 2, 0]
    parts = re.split(r'[.-]', v_str)
    nums = []
    for p in parts:
        if p.isdigit():
            nums.append(int(p))
        else:
            # stop at first non-digit (e.g. beta) for simple comparison
            # or treat as -1?
            # Let's try to capture as many leading numeric parts as possible
            break
    # Pad to 3
    while len(nums) < 3:
        nums.append(0)
    return tuple(nums)

candidates = {} # Name -> {Version: str, ParsedVersion: tuple, Project: str, Stars: int}

for m in mappings:
    proj = m['ProjectName']
    if proj not in proj_stars:
        continue
        
    raw_name = m['Name']
    # Clean name
    if '>' in raw_name:
        clean_name = raw_name.split('>')[-1]
    else:
        clean_name = raw_name
        
    # Ignore names that look like files or internal paths if necessary
    if '/' in clean_name and not clean_name.startswith('@'):
        # e.g. "lodash/fp" -> treat as sub-package? Or "lodash"?
        # Usually package names are "lodash" or "@scope/pkg".
        # If it has / but no @, it might be a subpath.
        # But keep it simple for now.
        pass

    version_str = m['Version']
    parsed_v = parse_version(version_str)
    
    if clean_name not in candidates:
        candidates[clean_name] = {
            'Version': version_str,
            'ParsedVersion': parsed_v,
            'Project': proj,
            'Stars': proj_stars[proj]
        }
    else:
        # Compare versions
        if parsed_v > candidates[clean_name]['ParsedVersion']:
            candidates[clean_name] = {
                'Version': version_str,
                'ParsedVersion': parsed_v,
                'Project': proj,
                'Stars': proj_stars[proj]
            }

# Convert to list
result_list = []
for name, data in candidates.items():
    result_list.append({
        'Name': name,
        'Version': data['Version'],
        'Stars': data['Stars']
    })

# Sort by Stars desc
result_list.sort(key=lambda x: x['Stars'], reverse=True)

# Take top 5
top_5 = result_list[:5]

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-14807880816465806524': ['packageinfo'], 'var_function-call-14807880816465807177': ['project_info', 'project_packageversion'], 'var_function-call-9877596124832240625': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'UpstreamPublishedAt': '1699345351000000.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'UpstreamPublishedAt': '1670271173000000.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'UpstreamPublishedAt': '1654791421000000.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'UpstreamPublishedAt': '1624260093000000.0', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'UpstreamPublishedAt': '1656518476000000.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_function-call-9877596124832242030': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-9877596124832243435': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_function-call-12415826041567387791': [{'count_star()': '770'}], 'var_function-call-14590165289199872650': [{'COUNT(*)': '661372'}], 'var_function-call-10419144386249284902': [{'count_star()': '597602'}], 'var_function-call-16403426750612213154': 'file_storage/function-call-16403426750612213154.json', 'var_function-call-18063043881055894313': [{'ProjectName': 'microsoft/typescript', 'Stars': 94931}, {'ProjectName': 'mui-org/material-ui', 'Stars': 89398}, {'ProjectName': 'sveltejs/svelte', 'Stars': 73499}, {'ProjectName': 'tailwindcss/tailwindcss', 'Stars': 73464}, {'ProjectName': 'lodash/lodash', 'Stars': 57779}, {'ProjectName': 'strapi/strapi', 'Stars': 57236}, {'ProjectName': 'rails/rails', 'Stars': 55319}, {'ProjectName': 'semantic-org/semantic-ui', 'Stars': 51069}, {'ProjectName': 'moment/moment', 'Stars': 47549}, {'ProjectName': 'mozilla/pdf.js', 'Stars': 44231}, {'ProjectName': 'quilljs/quill', 'Stars': 42407}, {'ProjectName': 'styled-components/styled-components', 'Stars': 39660}, {'ProjectName': 'leaflet/leaflet', 'Stars': 38715}, {'ProjectName': 'microsoft/monaco-editor', 'Stars': 36025}, {'ProjectName': 'mobxjs/mobx', 'Stars': 26802}, {'ProjectName': 'request/request', 'Stars': 25691}, {'ProjectName': 'tj/commander.js', 'Stars': 25437}, {'ProjectName': 'react-native-elements/react-native-elements', 'Stars': 24814}, {'ProjectName': 'swagger-api/swagger-ui', 'Stars': 24753}, {'ProjectName': 'react-navigation/react-navigation', 'Stars': 23394}], 'var_function-call-6822567794378688536': "SELECT Name, Version, ProjectName FROM project_packageversion WHERE System='NPM' AND ProjectName IN ('microsoft/typescript', 'mui-org/material-ui', 'sveltejs/svelte', 'tailwindcss/tailwindcss', 'lodash/lodash', 'strapi/strapi', 'rails/rails', 'semantic-org/semantic-ui', 'moment/moment', 'mozilla/pdf.js', 'quilljs/quill', 'styled-components/styled-components', 'leaflet/leaflet', 'microsoft/monaco-editor', 'mobxjs/mobx', 'request/request', 'tj/commander.js', 'react-native-elements/react-native-elements', 'swagger-api/swagger-ui', 'react-navigation/react-navigation')", 'var_function-call-4389154146235398041': 'file_storage/function-call-4389154146235398041.json', 'var_function-call-15242189350481318146': "SELECT Name, Version, UpstreamPublishedAt, VersionInfo FROM packageinfo WHERE System='NPM' AND Name IN ('@dolsem/actioncable', '@dumc11/tailwindcss', '@ec-nordbund/leaflet', '@dongls/pdfjs-dist', '@dreampie/semantic-ui', '@dplus/rn-ui', '@dynasty/styled-components', '@docly/web', '@dplus/themed', '@docid/monaco-editor', '@dplus/base', '@dpwolfe/react-navigation', '@dman777/shadow-dom-quill-temp', '@dudadev/mobx-react', '@domdomegg/swagger-ui', '@dothq/styled-components', '@dylanvann/svelte', '@edgarai/strapi-provider-upload-local')", 'var_function-call-10946717603380336064': {'lodash_total': 190, 'lodash_sample': [{'Name': '@dummmy/pack-cli>1.0.8>lodash', 'Version': '4.17.19', 'ProjectName': 'lodash/lodash'}, {'Name': '@dummmy/pack-cli>1.0.9>lodash', 'Version': '4.17.19', 'ProjectName': 'lodash/lodash'}, {'Name': '@dummmy/webpack-cli>1.0.3>lodash', 'Version': '4.17.19', 'ProjectName': 'lodash/lodash'}, {'Name': '@dollarshaveclub/cli>1.0.0>lodash', 'Version': '4.17.4', 'ProjectName': 'lodash/lodash'}, {'Name': '@dollarshaveclub/cli>1.5.1>lodash', 'Version': '4.17.4', 'ProjectName': 'lodash/lodash'}], 'lodash_clean': [], 'ts_total': 4, 'ts_clean': []}, 'var_function-call-11310623478654770109': [], 'var_function-call-11310623478654769072': [], 'var_function-call-1233100819505802062': [], 'var_function-call-11966814569905558164': [{'System': 'NPM'}], 'var_function-call-16704600265961913164': [{'Name': '@dwarvesf/react-scripts>0.7.0>lodash._baseclone'}, {'Name': '@dwarvesf/react-scripts>0.7.0>lodash._baseclone'}, {'Name': '@dummmy/webpack-cli>1.0.2>lodash'}, {'Name': '@dummmy/webpack-cli>1.0.2>lodash'}, {'Name': '@dollarshaveclub/cli>1.10.0>lodash'}, {'Name': '@dollarshaveclub/cli>1.10.0>lodash'}, {'Name': '@dpoineau/react-scripts>1.0.0>lodash.camelcase'}, {'Name': '@dpoineau/react-scripts>1.0.0>lodash.camelcase'}, {'Name': '@dpoineau/react-scripts>1.0.0>http-proxy-middleware>lodash'}, {'Name': '@dpoineau/react-scripts>1.0.0>http-proxy-middleware>lodash'}], 'var_function-call-16704600265961911601': [{'Name': '@dummmy/pack-cli>1.0.8>lodash'}, {'Name': '@dummmy/pack-cli>1.0.9>lodash'}, {'Name': '@dummmy/webpack-cli>1.0.3>lodash'}, {'Name': '@dollarshaveclub/cli>1.0.0>lodash'}, {'Name': '@dollarshaveclub/cli>1.5.1>lodash'}, {'Name': '@dollarshaveclub/cli>1.7.1>lodash'}, {'Name': '@dollarshaveclub/cli>1.8.0>lodash'}, {'Name': '@dollarshaveclub/cli>2.2.1>lodash'}, {'Name': '@dollarshaveclub/cli>1.11.5-rc.1>lodash'}, {'Name': '@dpoineau/react-scripts>1.0.0>lodash._root'}], 'var_function-call-12481128306301240327': [{'System': 'NPM', 'Name': '@dmrvos/infrajs>0.0.5>typescript', 'Version': '2.6.2', 'ProjectType': 'GITHUB', 'ProjectName': 'microsoft/typescript', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dmrvos/infrajs>0.0.5>typescript', 'Version': '2.6.2', 'ProjectType': 'GITHUB', 'ProjectName': 'microsoft/typescript', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'ISSUE_TRACKER_TYPE'}, {'System': 'NPM', 'Name': '@dmrvos/infrajs>0.0.6>typescript', 'Version': '2.6.2', 'ProjectType': 'GITHUB', 'ProjectName': 'microsoft/typescript', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'ISSUE_TRACKER_TYPE'}, {'System': 'NPM', 'Name': '@dmrvos/infrajs>0.0.6>typescript', 'Version': '2.6.2', 'ProjectType': 'GITHUB', 'ProjectName': 'microsoft/typescript', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-12481128306301243152': [{'System': 'NPM', 'Name': '@docly/web', 'Version': '0.1.381', 'ProjectType': 'GITHUB', 'ProjectName': 'mui-org/material-ui', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'ISSUE_TRACKER_TYPE'}, {'System': 'NPM', 'Name': '@docly/web', 'Version': '0.1.371', 'ProjectType': 'GITHUB', 'ProjectName': 'mui-org/material-ui', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'ISSUE_TRACKER_TYPE'}, {'System': 'NPM', 'Name': '@docly/web', 'Version': '0.0.2', 'ProjectType': 'GITHUB', 'ProjectName': 'mui-org/material-ui', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'ISSUE_TRACKER_TYPE'}, {'System': 'NPM', 'Name': '@docly/web', 'Version': '0.2.0', 'ProjectType': 'GITHUB', 'ProjectName': 'mui-org/material-ui', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'ISSUE_TRACKER_TYPE'}, {'System': 'NPM', 'Name': '@docly/web', 'Version': '0.0.1', 'ProjectType': 'GITHUB', 'ProjectName': 'mui-org/material-ui', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'ISSUE_TRACKER_TYPE'}], 'var_function-call-12481128306301241881': [{'System': 'NPM', 'Name': '@dummmy/pack-cli>1.0.8>lodash', 'Version': '4.17.19', 'ProjectType': 'GITHUB', 'ProjectName': 'lodash/lodash', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dummmy/pack-cli>1.0.9>lodash', 'Version': '4.17.19', 'ProjectType': 'GITHUB', 'ProjectName': 'lodash/lodash', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dummmy/webpack-cli>1.0.3>lodash', 'Version': '4.17.19', 'ProjectType': 'GITHUB', 'ProjectName': 'lodash/lodash', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dollarshaveclub/cli>1.0.0>lodash', 'Version': '4.17.4', 'ProjectType': 'GITHUB', 'ProjectName': 'lodash/lodash', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dollarshaveclub/cli>1.5.1>lodash', 'Version': '4.17.4', 'ProjectType': 'GITHUB', 'ProjectName': 'lodash/lodash', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-14275529738787216093': [{'System': 'NPM', 'Name': '@dmrvos/infrajs>0.0.5>typescript', 'Version': '2.6.2', 'Licenses': '[\n  "Apache-2.0"\n]', 'Links': '[\n  {\n    "Label": "SOURCE_REPO",\n    "URL": "git+https://github.com/Microsoft/TypeScript.git"\n  },\n  {\n    "Label": "ISSUE_TRACKER",\n    "URL": "https://github.com/Microsoft/TypeScript/issues"\n  },\n  {\n    "Label": "HOMEPAGE",\n    "URL": "http://typescriptlang.org/"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 1\n}', 'Hashes': '[]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': 'None', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}]}

exec(code, env_args)
