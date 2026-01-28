code = """import json
import re

# Load release packages
releases_file = locals()['var_functions.query_db:22']
with open(releases_file, 'r') as f:
    releases = json.load(f)

# Parse release packages and find latest version per name based on Ordinal
latest_by_name = {}
for pkg in releases:
    try:
        version_info = json.loads(pkg['VersionInfo'])
        if not version_info.get('IsRelease'):
            continue
    except Exception:
        continue
    name = pkg['Name']
    version = pkg['Version']
    ordinal = version_info.get('Ordinal', 0)
    # Keep the highest ordinal
    if name not in latest_by_name or ordinal > latest_by_name[name]['Ordinal']:
        latest_by_name[name] = {'Version': version, 'Ordinal': ordinal}

# Load project_packageversion mapping
mapping_file = locals()['var_functions.query_db:18']
with open(mapping_file, 'r') as f:
    project_mappings = json.load(f)

# Build dict for quick lookup: key (Name, Version) -> ProjectName
lookup = {}
for entry in project_mappings:
    if entry.get('System') != 'NPM':
        continue
    key = (entry['Name'], entry['Version'])
    # There could be duplicate entries; just take the first encountered
    if key not in lookup:
        lookup[key] = entry.get('ProjectName')

# Load project_info for star counts
info_file = locals()['var_functions.query_db:20']
with open(info_file, 'r') as f:
    project_info_list = json.load(f)

# Build dict ProjectName -> stars
stars_by_project = {}
star_pattern = re.compile(r'(\d+) stars?')
for info in project_info_list:
    proj_text = info.get('Project_Information', '')
    # extract project name (first part before spaces? after "The project " maybe)
    # Extract stars
    m = star_pattern.search(proj_text)
    if m:
        stars = int(m.group(1))
        # Get project name: typical format "The project <project_name> on GitHub ..." or just "<project_name>" followed by spaces
        # Let's extract name after "The project " until first space or maybe until " on GitHub"
        # Use simple heuristic: after "The project " up to " on GitHub"
        if "The project " in proj_text:
            start = proj_text.find("The project ") + len("The project ")
            end = proj_text.find(" on GitHub", start)
            if end == -1:
                end = proj_text.find(" ", start)
                if end == -1:
                    end = None
            proj_name = proj_text[start:end].strip()
        else:
            # fallback: first word before spaces?
            proj_name = proj_text.split()[0]
        stars_by_project[proj_name] = stars

# For each latest package, find its project and stars, collect results
results = []
for name, data in latest_by_name.items():
    version = data['Version']
    proj_name = lookup.get((name, version))
    if not proj_name:
        # No mapping for this version
        continue
    stars = stars_by_project.get(proj_name)
    if stars is None:
        # No star count info
        continue
    results.append({'PackageName': name, 'Version': version, 'ProjectName': proj_name, 'Stars': stars})

# Sort by Stars descending, take top 5
top5 = sorted(results, key=lambda x: x['Stars'], reverse=True)[:5]

print('__RESULT__:')
print(json.dumps(top5, indent=2))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.query_db:2': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@ecl%2Ftwig-component-carousel/3.11.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'Hashes': '[\n  {\n    "Hash": "vH5da6eUZ94i1AcOsrC6VjSV88cMUe5A1w+CDHAt2aYXldR9sBNRCse27cIx51GnUjnj7dSe3o5A81TjraJ0Lw==",\n    "Type": "SHA512"\n  },\n  {\n    "Hash": "WZUWPp1jVp6nrUZ0n7vmthbB4OrtnLFNDOPPBBNp15I=",\n    "Type": "SHA256"\n  },\n  {\n    "Hash": "JbFslb4AeqQVI+LCXFeZKFrWmHI=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "zBm5Qvg5p2bQwUTcg6hZYA==",\n    "Type": "MD5"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1699345351000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'Licenses': '[]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@douganderson444%2Fpanzoom-node/v/1.1.5"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}', 'Hashes': '[\n  {\n    "Hash": "bn6jsFfgQaOqxYcxQLdn+w==",\n    "Type": "MD5"\n  },\n  {\n    "Hash": "Ag2muuzRUxbKTAR/H0qjiVGqd5E=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "Z2cdZL3dyM3mmLnEKE4HDFAFnE8OTVU1Lm36fasqZuFRlfjv+M8qkZs+ZAwOsR65FfhH1St2n1YvhihaMM5UEw==",\n    "Type": "SHA512"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '1', 'UpstreamPublishedAt': '1670271173000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'Licenses': '[]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@douganderson444%2Fpanzoom-node/v/1.1.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}', 'Hashes': '[\n  {\n    "Hash": "f882urh9+DaLLfg22vF4Dw==",\n    "Type": "MD5"\n  },\n  {\n    "Hash": "UavDKi+B1bjz5yL/IEUOzG5BIX0=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "Br/d41zpasemiy1jjn91jYmLFbgFFGo5+V+v5+LRxHeTg2MajAkwczkbMUyb3k8xD0UIubDfClv9roNgLIoOEQ==",\n    "Type": "SHA512"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '1', 'UpstreamPublishedAt': '1654791421000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'Licenses': '[\n  "ISC"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@dreamworld%2Fdw-select/3.1.2-fix-double-click-issue.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}', 'Hashes': '[\n  {\n    "Hash": "1e+/qEffZeAgXRtIOUmPqw==",\n    "Type": "MD5"\n  },\n  {\n    "Hash": "C3IyUAgv9Bs96QRmMOHUrQwBnS4=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "07tFydL0pzuqYZbHESf4n0N5gbgvaPZFBfRZmC+k4dqhaKjR2xRBXBpCyxji9W0kkkCVrgtiTrI/XzhgTBq80w==",\n    "Type": "SHA512"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1624260093000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@discue%2Fui-components/0.13.0"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}', 'Hashes': '[\n  {\n    "Hash": "9BaLXgrA89SmryO88KCXZg==",\n    "Type": "MD5"\n  },\n  {\n    "Hash": "1ehWf/vTvGu5BskEEAeiQL1rNcM=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "UOcNM2Ee5byWKfgJ8Q9am9B369//NKxfLA9nr20EClco8KptuYrcBXZXqOpBk3jJByBoEaek8n47WqZMiB7TDA==",\n    "Type": "SHA512"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1656518476000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}], 'var_functions.list_db:5': ['project_info', 'project_packageversion'], 'var_functions.query_db:6': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Ordinal': 29}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.2.2', 'Ordinal': 25}, {'Name': '@discue/ui-components', 'Version': '0.38.2', 'Ordinal': 45}, {'Name': '@dvcol/web-extension-utils', 'Version': '2.3.4', 'Ordinal': 27}, {'Name': '@edgedev/firebase', 'Version': '2.0.20', 'Ordinal': 133}, {'Name': '@dyoshikawa/mentor-php-env', 'Version': '0.1.0', 'Ordinal': 15}, {'Name': '@eclipsejs/cli', 'Version': '1.1.0', 'Ordinal': 14}, {'Name': '@dytesdk/electron-main', 'Version': '1.1.0', 'Ordinal': 13}, {'Name': '@ebot7/edem-react', 'Version': '0.24.1', 'Ordinal': 89}, {'Name': '@e4a/irmaseal-wasm-bindings', 'Version': '0.2.3', 'Ordinal': 19}, {'Name': '@ebury/chameleon-components', 'Version': '2.4.1', 'Ordinal': 343}, {'Name': '@e-group/material-form', 'Version': '7.41.4', 'Ordinal': 355}, {'Name': '@e-group/material-layout', 'Version': '7.40.2', 'Ordinal': 201}, {'Name': '@edgeros/jsre-types', 'Version': '2.2.4', 'Ordinal': 113}, {'Name': '@dxos/client', 'Version': '2.33.8', 'Ordinal': 1716}, {'Name': '@edgeandnode/components', 'Version': '27.5.2', 'Ordinal': 613}, {'Name': '@dkoerner/propertyui', 'Version': '0.1.70', 'Ordinal': 108}, {'Name': '@dspworkplace/ui', 'Version': '1.5.47', 'Ordinal': 180}, {'Name': '@ditojs/router', 'Version': '2.10.5', 'Ordinal': 291}, {'Name': '@ditojs/ui', 'Version': '2.10.5', 'Ordinal': 344}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
