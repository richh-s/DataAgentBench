code = """import json
import re

# Load all NPM packages from package_database
packages_file = locals()['var_functions.query_db:26']
with open(packages_file, 'r') as f:
    packages = json.load(f)

# Find latest release version for each package based on Ordinal
latest_by_name = {}
for pkg in packages:
    try:
        version_info = json.loads(pkg['VersionInfo'])
        if not version_info.get('IsRelease'):
            continue
    except:
        continue
    name = pkg['Name']
    version = pkg['Version']
    ordinal = version_info.get('Ordinal', 0)
    if name not in latest_by_name or ordinal > latest_by_name[name]['Ordinal']:
        latest_by_name[name] = {'Version': version, 'Ordinal': ordinal}

print(f"Found {len(latest_by_name)} NPM packages with release versions")

# Load project_packageversion mappings
mapping_file = locals()['var_functions.query_db:18']
with open(mapping_file, 'r') as f:
    mappings = json.load(f)

# Build lookup: (Name, Version) -> ProjectName
lookup = {}
for entry in mappings:
    if entry.get('System') != 'NPM':
        continue
    key = (entry['Name'], entry['Version'])
    if key not in lookup:
        lookup[key] = entry.get('ProjectName')

print(f"Found {len(lookup)} package-to-project mappings")

# Load project_info for star counts
info_file = locals()['var_functions.query_db:20']
with open(info_file, 'r') as f:
    project_infos = json.load(f)

# Build project name to stars mapping (more robust parsing)
stars_by_project = {}
star_pattern = re.compile(r'(\d+) stars?')

for info in project_infos:
    text = info.get('Project_Information', '')
    if not text:
        continue
    
    # Extract stars
    star_match = star_pattern.search(text)
    if not star_match:
        continue
    stars = int(star_match.group(1))
    
    # Extract project name - handle different formats
    proj_name = None
    
    # Format 1: "The project <name> on GitHub..."
    if 'The project ' in text and ' on GitHub' in text:
        start = text.find('The project ') + len('The project ')
        end = text.find(' on GitHub', start)
        if end > start:
            proj_name = text[start:end].strip()
    
    # Format 2: "The project <name> is hosted on GitHub..."
    elif 'The project ' in text and ' is hosted on GitHub' in text:
        start = text.find('The project ') + len('The project ')
        end = text.find(' is hosted on GitHub', start)
        if end > start:
            proj_name = text[start:end].strip()
    
    # Format 3: Just starts with project name
    else:
        # Take first word-like token that looks like owner/repo
        parts = text.split()
        for part in parts[:5]:  # Check first 5 words
            if '/' in part and len(part) < 100:  # Looks like a repo name
                proj_name = part
                break
    
    if proj_name and proj_name != 'on':
        stars_by_project[proj_name] = stars

print(f"Found star info for {len(stars_by_project)} projects")

# Match packages with projects and stars
matched = []
for name, data in latest_by_name.items():
    version = data['Version']
    project_name = lookup.get((name, version))
    if not project_name:
        continue
    stars = stars_by_project.get(project_name)
    if stars is None:
        continue
    matched.append({
        'PackageName': name,
        'Version': version,
        'ProjectName': project_name,
        'Stars': stars
    })

print(f"Matched {len(matched)} packages with star information")

# Sort and get top 5
top5 = sorted(matched, key=lambda x: x['Stars'], reverse=True)[:5]

print('__RESULT__:')
print(json.dumps(top5, indent=2))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.query_db:2': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@ecl%2Ftwig-component-carousel/3.11.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'Hashes': '[\n  {\n    "Hash": "vH5da6eUZ94i1AcOsrC6VjSV88cMUe5A1w+CDHAt2aYXldR9sBNRCse27cIx51GnUjnj7dSe3o5A81TjraJ0Lw==",\n    "Type": "SHA512"\n  },\n  {\n    "Hash": "WZUWPp1jVp6nrUZ0n7vmthbB4OrtnLFNDOPPBBNp15I=",\n    "Type": "SHA256"\n  },\n  {\n    "Hash": "JbFslb4AeqQVI+LCXFeZKFrWmHI=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "zBm5Qvg5p2bQwUTcg6hZYA==",\n    "Type": "MD5"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1699345351000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'Licenses': '[]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@douganderson444%2Fpanzoom-node/v/1.1.5"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}', 'Hashes': '[\n  {\n    "Hash": "bn6jsFfgQaOqxYcxQLdn+w==",\n    "Type": "MD5"\n  },\n  {\n    "Hash": "Ag2muuzRUxbKTAR/H0qjiVGqd5E=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "Z2cdZL3dyM3mmLnEKE4HDFAFnE8OTVU1Lm36fasqZuFRlfjv+M8qkZs+ZAwOsR65FfhH1St2n1YvhihaMM5UEw==",\n    "Type": "SHA512"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '1', 'UpstreamPublishedAt': '1670271173000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'Licenses': '[]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@douganderson444%2Fpanzoom-node/v/1.1.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}', 'Hashes': '[\n  {\n    "Hash": "f882urh9+DaLLfg22vF4Dw==",\n    "Type": "MD5"\n  },\n  {\n    "Hash": "UavDKi+B1bjz5yL/IEUOzG5BIX0=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "Br/d41zpasemiy1jjn91jYmLFbgFFGo5+V+v5+LRxHeTg2MajAkwczkbMUyb3k8xD0UIubDfClv9roNgLIoOEQ==",\n    "Type": "SHA512"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '1', 'UpstreamPublishedAt': '1654791421000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'Licenses': '[\n  "ISC"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@dreamworld%2Fdw-select/3.1.2-fix-double-click-issue.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}', 'Hashes': '[\n  {\n    "Hash": "1e+/qEffZeAgXRtIOUmPqw==",\n    "Type": "MD5"\n  },\n  {\n    "Hash": "C3IyUAgv9Bs96QRmMOHUrQwBnS4=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "07tFydL0pzuqYZbHESf4n0N5gbgvaPZFBfRZmC+k4dqhaKjR2xRBXBpCyxji9W0kkkCVrgtiTrI/XzhgTBq80w==",\n    "Type": "SHA512"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1624260093000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@discue%2Fui-components/0.13.0"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}', 'Hashes': '[\n  {\n    "Hash": "9BaLXgrA89SmryO88KCXZg==",\n    "Type": "MD5"\n  },\n  {\n    "Hash": "1ehWf/vTvGu5BskEEAeiQL1rNcM=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "UOcNM2Ee5byWKfgJ8Q9am9B369//NKxfLA9nr20EClco8KptuYrcBXZXqOpBk3jJByBoEaek8n47WqZMiB7TDA==",\n    "Type": "SHA512"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1656518476000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}], 'var_functions.list_db:5': ['project_info', 'project_packageversion'], 'var_functions.query_db:6': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Ordinal': 29}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.2.2', 'Ordinal': 25}, {'Name': '@discue/ui-components', 'Version': '0.38.2', 'Ordinal': 45}, {'Name': '@dvcol/web-extension-utils', 'Version': '2.3.4', 'Ordinal': 27}, {'Name': '@edgedev/firebase', 'Version': '2.0.20', 'Ordinal': 133}, {'Name': '@dyoshikawa/mentor-php-env', 'Version': '0.1.0', 'Ordinal': 15}, {'Name': '@eclipsejs/cli', 'Version': '1.1.0', 'Ordinal': 14}, {'Name': '@dytesdk/electron-main', 'Version': '1.1.0', 'Ordinal': 13}, {'Name': '@ebot7/edem-react', 'Version': '0.24.1', 'Ordinal': 89}, {'Name': '@e4a/irmaseal-wasm-bindings', 'Version': '0.2.3', 'Ordinal': 19}, {'Name': '@ebury/chameleon-components', 'Version': '2.4.1', 'Ordinal': 343}, {'Name': '@e-group/material-form', 'Version': '7.41.4', 'Ordinal': 355}, {'Name': '@e-group/material-layout', 'Version': '7.40.2', 'Ordinal': 201}, {'Name': '@edgeros/jsre-types', 'Version': '2.2.4', 'Ordinal': 113}, {'Name': '@dxos/client', 'Version': '2.33.8', 'Ordinal': 1716}, {'Name': '@edgeandnode/components', 'Version': '27.5.2', 'Ordinal': 613}, {'Name': '@dkoerner/propertyui', 'Version': '0.1.70', 'Ordinal': 108}, {'Name': '@dspworkplace/ui', 'Version': '1.5.47', 'Ordinal': 180}, {'Name': '@ditojs/router', 'Version': '2.10.5', 'Ordinal': 291}, {'Name': '@ditojs/ui', 'Version': '2.10.5', 'Ordinal': 344}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:24': [{'PackageName': '@ec-nordbund/leaflet', 'Version': '1.7.1', 'ProjectName': 'leaflet/leaflet', 'Stars': 38715}, {'PackageName': '@dongjiang/textmate-grammars', 'Version': '0.0.5', 'ProjectName': 'theia-ide/theia', 'Stars': 18526}, {'PackageName': '@dpoineau/react-scripts>1.0.0>node-sass', 'Version': '3.10.1', 'ProjectName': 'sass/node-sass', 'Stars': 8498}, {'PackageName': '@dollarshaveclub/cli>1.3.0>qs', 'Version': '6.5.1', 'ProjectName': 'ljharb/qs', 'Stars': 8073}, {'PackageName': '@dwarvesf/react-scripts>0.7.0>qs', 'Version': '6.3.0', 'ProjectName': 'ljharb/qs', 'Stars': 8073}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
