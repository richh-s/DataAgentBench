code = """import json
import re
import pandas as pd

# Load all the data
releases_file = 'file_storage/functions.query_db:36.json'
ppv_file = 'file_storage/functions.query_db:21.json'
project_file = 'file_storage/functions.query_db:38.json'

with open(releases_file, 'r') as f:
    releases = json.load(f)

with open(ppv_file, 'r') as f:
    ppv_mappings = json.load(f)

with open(project_file, 'r') as f:
    project_info = json.load(f)

print(f'Loaded {len(releases)} releases, {len(ppv_mappings)} mappings, {len(project_info)} projects')

# Parse VersionInfo to extract Ordinal properly
for pkg in releases:
    try:
        # The VersionInfo is already a JSON string, just load it
        vi_str = pkg['VersionInfo'].strip()
        vi = json.loads(vi_str)
        pkg['Ordinal'] = int(vi.get('Ordinal', 0))
    except Exception as e:
        pkg['Ordinal'] = 0

# Convert to DataFrame
df_releases = pd.DataFrame(releases)
print(f'Releases DataFrame shape: {df_releases.shape}')

# Find latest release for each package (max Ordinal)
latest_releases = df_releases.loc[df_releases.groupby('Name')['Ordinal'].idxmax()]
print(f'Latest releases: {len(latest_releases)}')

# Filter project mappings for NPM only and clean up project names
df_ppv = pd.DataFrame(ppv_mappings)
df_ppv_npm = df_ppv[df_ppv['System'] == 'NPM'][['Name', 'Version', 'ProjectName']].copy()
df_ppv_npm['ProjectName'] = df_ppv_npm['ProjectName'].str.replace(r'^/', '', regex=True)

# Only keep valid project names (should contain '/')
df_ppv_npm = df_ppv_npm[df_ppv_npm['ProjectName'].str.contains('/', na=False)]
print(f'Valid NPM mappings: {len(df_ppv_npm)}')

# Merge to find matches - use inner join to only keep matched packages
df_merged = latest_releases.merge(
    df_ppv_npm,
    on=['Name', 'Version'],
    how='inner'
)
print(f'Matched packages: {len(df_merged)}')

# Extract stars from project information
def extract_stars(info_text):
    if not info_text or pd.isna(info_text):
        return 0
    
    patterns = [
        r'(\d{1,3}(?:,\d{3})*)\s+stars?',
        r'stars\s+count\s+of\s+(\d{1,3}(?:,\d{3})*)',
        r'has\s+(\d{1,3}(?:,\d{3})*)\s+stars',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, info_text, re.IGNORECASE)
        if match:
            star_str = match.group(1).replace(',', '')
            return int(star_str)
    
    return 0

# Process project info
df_project = pd.DataFrame(project_info)
df_project['Stars'] = df_project['Project_Information'].apply(extract_stars)

# Create mapping from project name to stars
project_to_stars = {}
for _, row in df_project.iterrows():
    info = row['Project_Information']
    stars = row['Stars']
    
    if stars > 0:
        # Extract project name
        match = re.search(r'project\s+([\w\-\.]+/[\w\-\.]+)', info)
        if match:
            project_name = match.group(1).lower()
            project_to_stars[project_name] = stars

print(f'Project-star mappings: {len(project_to_stars)}')

# Add stars to merged data
df_merged['Stars'] = df_merged['ProjectName'].str.lower().map(project_to_stars).fillna(0).astype(int)

# Filter for packages with stars > 0
df_with_stars = df_merged[df_merged['Stars'] > 0]
print(f'Packages with stars > 0: {len(df_with_stars)}')

# Get top 5
if len(df_with_stars) > 0:
    top_5 = df_with_stars.nlargest(5, 'Stars')[['Name', 'Version', 'Stars']]
    result = top_5.to_dict('records')
else:
    # Check a few sample projects to debug
    sample_projects = list(project_to_stars.items())[:10]
    sample_packages = df_merged['ProjectName'].unique()[:10].tolist()
    result = {'error': 'No matches found', 'sample_projects': sample_projects, 'sample_packages': sample_packages}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:2': ['project_info', 'project_packageversion'], 'var_functions.execute_python:4': [], 'var_functions.query_db:6': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@ecl%2Ftwig-component-carousel/3.11.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'Hashes': '[\n  {\n    "Hash": "vH5da6eUZ94i1AcOsrC6VjSV88cMUe5A1w+CDHAt2aYXldR9sBNRCse27cIx51GnUjnj7dSe3o5A81TjraJ0Lw==",\n    "Type": "SHA512"\n  },\n  {\n    "Hash": "WZUWPp1jVp6nrUZ0n7vmthbB4OrtnLFNDOPPBBNp15I=",\n    "Type": "SHA256"\n  },\n  {\n    "Hash": "JbFslb4AeqQVI+LCXFeZKFrWmHI=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "zBm5Qvg5p2bQwUTcg6hZYA==",\n    "Type": "MD5"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1699345351000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'Licenses': '[]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@douganderson444%2Fpanzoom-node/v/1.1.5"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}', 'Hashes': '[\n  {\n    "Hash": "bn6jsFfgQaOqxYcxQLdn+w==",\n    "Type": "MD5"\n  },\n  {\n    "Hash": "Ag2muuzRUxbKTAR/H0qjiVGqd5E=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "Z2cdZL3dyM3mmLnEKE4HDFAFnE8OTVU1Lm36fasqZuFRlfjv+M8qkZs+ZAwOsR65FfhH1St2n1YvhihaMM5UEw==",\n    "Type": "SHA512"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '1', 'UpstreamPublishedAt': '1670271173000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'Licenses': '[]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@douganderson444%2Fpanzoom-node/v/1.1.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}', 'Hashes': '[\n  {\n    "Hash": "f882urh9+DaLLfg22vF4Dw==",\n    "Type": "MD5"\n  },\n  {\n    "Hash": "UavDKi+B1bjz5yL/IEUOzG5BIX0=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "Br/d41zpasemiy1jjn91jYmLFbgFFGo5+V+v5+LRxHeTg2MajAkwczkbMUyb3k8xD0UIubDfClv9roNgLIoOEQ==",\n    "Type": "SHA512"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '1', 'UpstreamPublishedAt': '1654791421000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'Licenses': '[\n  "ISC"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@dreamworld%2Fdw-select/3.1.2-fix-double-click-issue.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}', 'Hashes': '[\n  {\n    "Hash": "1e+/qEffZeAgXRtIOUmPqw==",\n    "Type": "MD5"\n  },\n  {\n    "Hash": "C3IyUAgv9Bs96QRmMOHUrQwBnS4=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "07tFydL0pzuqYZbHESf4n0N5gbgvaPZFBfRZmC+k4dqhaKjR2xRBXBpCyxji9W0kkkCVrgtiTrI/XzhgTBq80w==",\n    "Type": "SHA512"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1624260093000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@discue%2Fui-components/0.13.0"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}', 'Hashes': '[\n  {\n    "Hash": "9BaLXgrA89SmryO88KCXZg==",\n    "Type": "MD5"\n  },\n  {\n    "Hash": "1ehWf/vTvGu5BskEEAeiQL1rNcM=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "UOcNM2Ee5byWKfgJ8Q9am9B369//NKxfLA9nr20EClco8KptuYrcBXZXqOpBk3jJByBoEaek8n47WqZMiB7TDA==",\n    "Type": "SHA512"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1656518476000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:21': 'file_storage/functions.query_db:21.json', 'var_functions.execute_python:26': {'npm_packages_count': 661372, 'project_packageversions_count': 597602}, 'var_functions.query_db:28': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_functions.execute_python:34': {'file_path': 'file_storage/functions.query_db:18.json', 'record_count': 661372, 'sample_records': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}]}, 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.execute_python:44': {'total_release_packages': 337844, 'sample': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}]}, 'var_functions.execute_python:48': {'top_5_packages': [{'Name': '@dmrvos/infrajs>0.0.5>typescript', 'Version': '2.6.2', 'Stars': 94931, 'ProjectName': 'microsoft/typescript'}, {'Name': '@dmrvos/infrajs>0.0.6>typescript', 'Version': '2.6.2', 'Stars': 94931, 'ProjectName': 'microsoft/typescript'}, {'Name': '@dollarshaveclub/cli>1.0.0>lodash', 'Version': '4.17.4', 'Stars': 57779, 'ProjectName': 'lodash/lodash'}, {'Name': '@dollarshaveclub/cli>1.1.0>lodash', 'Version': '4.17.4', 'Stars': 57779, 'ProjectName': 'lodash/lodash'}, {'Name': '@dollarshaveclub/cli>1.10.0>lodash', 'Version': '4.17.5', 'Stars': 57779, 'ProjectName': 'lodash/lodash'}], 'total_packages_with_stars': 1773, 'total_latest_releases': 15811}, 'var_functions.execute_python:50': {'top_5_packages': [{'Name': '@dmrvos/infrajs>0.0.5>typescript', 'Version': '2.6.2', 'Stars': 94931, 'ProjectName_clean': 'microsoft/typescript'}, {'Name': '@dmrvos/infrajs>0.0.6>typescript', 'Version': '2.6.2', 'Stars': 94931, 'ProjectName_clean': 'microsoft/typescript'}, {'Name': '@dollarshaveclub/cli>1.0.0>lodash', 'Version': '4.17.4', 'Stars': 57779, 'ProjectName_clean': 'lodash/lodash'}, {'Name': '@dollarshaveclub/cli>1.1.0>lodash', 'Version': '4.17.4', 'Stars': 57779, 'ProjectName_clean': 'lodash/lodash'}, {'Name': '@dollarshaveclub/cli>1.10.0>lodash', 'Version': '4.17.5', 'Stars': 57779, 'ProjectName_clean': 'lodash/lodash'}], 'total_packages_with_stars': 1773, 'total_latest_releases': 15811, 'sample_projects': [['ledgerproject/keypairoom', 3], ['lenconda/dollie', 12], ['mafintosh/is-my-json-valid', 953], ['mapbox/shp-write', 253], ['marcelklehr/toposort', 295], ['markcellus/wait-for-element-transition', 18], ['markhughes/droppy', 86], ['mathiasbynens/jsesc', 685], ['mathiasbynens/regenerate', 353], ['medikoo/d', 43]]}, 'var_functions.query_db:52': [{'ProjectName': 'felixge/node-delayed-stream'}, {'ProjectName': 'harthur/color-string'}, {'ProjectName': 'ben-eb/postcss-svgo'}, {'ProjectName': 'webpack/style-loader'}, {'ProjectName': 'analog-nico/stealthy-require'}, {'ProjectName': 'ljharb/define-properties'}, {'ProjectName': 'mikeal/forever-agent'}, {'ProjectName': 'doctaridev/eslint-config-doctari'}, {'ProjectName': 'financial-times/dotcom-reliability-kit'}, {'ProjectName': 'stefanpenner/get-caller-file'}, {'ProjectName': 'devongovett/browserify-zlib'}, {'ProjectName': 'isaacs/rimraf'}, {'ProjectName': 'edgetechnologiesinc/generator-edge-vis-adapter'}, {'ProjectName': 'definitelytyped/definitelytyped'}, {'ProjectName': 'npm/fstream'}, {'ProjectName': 'eclipse-glsp/glsp-server-node'}, {'ProjectName': 'eddienko/jupyterlab-colabinspired-theme-light'}, {'ProjectName': 'diwotech/react-leaflet-distortableimage'}, {'ProjectName': 'dword-design/suppress-babel-register-esm-warning'}, {'ProjectName': 'fb55/domutils'}]}

exec(code, env_args)
