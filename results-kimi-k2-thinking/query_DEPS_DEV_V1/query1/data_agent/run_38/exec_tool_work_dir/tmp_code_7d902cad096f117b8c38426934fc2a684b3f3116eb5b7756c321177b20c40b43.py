code = """import json
import pandas as pd
import re

# Load all data file paths
package_file = locals()['var_functions.query_db:34']
project_pkg_file = locals()['var_functions.query_db:12']
project_info_file = locals()['var_functions.query_db:14']

# Load data
print("Loading data...")
with open(package_file, 'r') as f:
    packages = json.load(f)

with open(project_pkg_file, 'r') as f:
    project_packages = json.load(f)

with open(project_info_file, 'r') as f:
    project_info = json.load(f)

print(f"Loaded {len(packages)} packages, {len(project_packages)} mappings, {len(project_info)} project records")

# Create DataFrames
df_packages = pd.DataFrame(packages)
df_proj_pkg = pd.DataFrame(project_packages)
df_proj_info = pd.DataFrame(project_info)

# Parse VersionInfo
def parse_version_info(vi_str):
    try:
        # Clean up JSON string
        vi_clean = vi_str.replace('\n', ' ').replace('  ', ' ').strip()
        vi_obj = json.loads(vi_clean)
        return {
            'IsRelease': bool(vi_obj.get('IsRelease', False)),
            'Ordinal': int(vi_obj.get('Ordinal', 0))
        }
    except Exception as e:
        return {'IsRelease': False, 'Ordinal': 0}

version_data = df_packages['VersionInfo'].apply(parse_version_info)
df_packages['IsRelease'] = [v['IsRelease'] for v in version_data]
df_packages['Ordinal'] = [v['Ordinal'] for v in version_data]

# Filter for release versions and find latest for each package
print("Finding latest release versions...")
df_release = df_packages[df_packages['IsRelease'] == True].copy()
# Group by Name and get the row with max Ordinal for each
idx = df_release.groupby('Name')['Ordinal'].idxmax()
df_latest = df_release.loc[idx].reset_index(drop=True)

print(f"Found {len(df_latest)} latest release packages")

# Merge with project_packageversion to get ProjectName
print("Mapping to GitHub projects...")
# Need to include System in the join
merged = pd.merge(
    df_latest[['Name', 'Version', 'System']],
    df_proj_pkg[['Name', 'Version', 'System', 'ProjectName']],
    on=['Name', 'Version', 'System'],
    how='inner'
)

print(f"Mapped {len(merged)} packages to projects")

# Parse Project_Information for stars and project names
print("Extracting GitHub stars...")
project_stars = []
for _, row in df_proj_info.iterrows():
    info = str(row['Project_Information'])
    
    # Extract stars - look for pattern like "X stars"
    stars_match = re.search(r'(\d[\d,]*)\s+stars?', info, re.IGNORECASE)
    stars = 0
    if stars_match:
        stars_str = stars_match.group(1).replace(',', '')
        try:
            stars = int(stars_str)
        except:
            stars = 0
    
    # Extract project name - look for "project X on GitHub" or "project named X"
    proj_match = re.search(r'project\s+(\S+?)\s+on\s+GitHub', info, re.IGNORECASE)
    if not proj_match:
        proj_match = re.search(r'project\s+named\s+(\S+)', info, re.IGNORECASE)
    if not proj_match:
        proj_match = re.search(r'project\s+(\S+?)\s+is\s+hosted', info, re.IGNORECASE)
    if not proj_match:
        # Last resort - take first word after "project"
        proj_match = re.search(r'project\s+(\S+)', info)
    
    if proj_match:
        proj_name = proj_match.group(1).rstrip('.,')
        project_stars.append({
            'ProjectName': proj_name,
            'Stars': stars
        })

# Create DataFrame of project stars
df_stars = pd.DataFrame(project_stars)
# Remove duplicates, keeping the first
#df_stars = df_stars.drop_duplicates(subset=['ProjectName'], keep='first')

print(f"Extracted stars for {len(df_stars)} projects")

# Merge packages with stars
final = pd.merge(
    merged,
    df_stars,
    on='ProjectName',
    how='inner'
)

print(f"Final dataset: {len(final)} packages")

# Remove duplicates (some packages might map to same project)
# and get top 5 by stars
top_packages = final.sort_values('Stars', ascending=False).drop_duplicates(subset=['Name']).head(5)

print("Top 5 packages:")
print(top_packages[['Name', 'Version', 'Stars', 'ProjectName']])

result = top_packages[['Name', 'Version', 'Stars', 'ProjectName']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:2': ['project_info', 'project_packageversion'], 'var_functions.query_db:5': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@ecl%2Ftwig-component-carousel/3.11.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'Hashes': '[\n  {\n    "Hash": "vH5da6eUZ94i1AcOsrC6VjSV88cMUe5A1w+CDHAt2aYXldR9sBNRCse27cIx51GnUjnj7dSe3o5A81TjraJ0Lw==",\n    "Type": "SHA512"\n  },\n  {\n    "Hash": "WZUWPp1jVp6nrUZ0n7vmthbB4OrtnLFNDOPPBBNp15I=",\n    "Type": "SHA256"\n  },\n  {\n    "Hash": "JbFslb4AeqQVI+LCXFeZKFrWmHI=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "zBm5Qvg5p2bQwUTcg6hZYA==",\n    "Type": "MD5"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1699345351000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'Licenses': '[]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@douganderson444%2Fpanzoom-node/v/1.1.5"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}', 'Hashes': '[\n  {\n    "Hash": "bn6jsFfgQaOqxYcxQLdn+w==",\n    "Type": "MD5"\n  },\n  {\n    "Hash": "Ag2muuzRUxbKTAR/H0qjiVGqd5E=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "Z2cdZL3dyM3mmLnEKE4HDFAFnE8OTVU1Lm36fasqZuFRlfjv+M8qkZs+ZAwOsR65FfhH1St2n1YvhihaMM5UEw==",\n    "Type": "SHA512"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '1', 'UpstreamPublishedAt': '1670271173000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'Licenses': '[]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@douganderson444%2Fpanzoom-node/v/1.1.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}', 'Hashes': '[\n  {\n    "Hash": "f882urh9+DaLLfg22vF4Dw==",\n    "Type": "MD5"\n  },\n  {\n    "Hash": "UavDKi+B1bjz5yL/IEUOzG5BIX0=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "Br/d41zpasemiy1jjn91jYmLFbgFFGo5+V+v5+LRxHeTg2MajAkwczkbMUyb3k8xD0UIubDfClv9roNgLIoOEQ==",\n    "Type": "SHA512"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '1', 'UpstreamPublishedAt': '1654791421000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'Licenses': '[\n  "ISC"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@dreamworld%2Fdw-select/3.1.2-fix-double-click-issue.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}', 'Hashes': '[\n  {\n    "Hash": "1e+/qEffZeAgXRtIOUmPqw==",\n    "Type": "MD5"\n  },\n  {\n    "Hash": "C3IyUAgv9Bs96QRmMOHUrQwBnS4=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "07tFydL0pzuqYZbHESf4n0N5gbgvaPZFBfRZmC+k4dqhaKjR2xRBXBpCyxji9W0kkkCVrgtiTrI/XzhgTBq80w==",\n    "Type": "SHA512"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1624260093000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@discue%2Fui-components/0.13.0"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}', 'Hashes': '[\n  {\n    "Hash": "9BaLXgrA89SmryO88KCXZg==",\n    "Type": "MD5"\n  },\n  {\n    "Hash": "1ehWf/vTvGu5BskEEAeiQL1rNcM=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "UOcNM2Ee5byWKfgJ8Q9am9B369//NKxfLA9nr20EClco8KptuYrcBXZXqOpBk3jJByBoEaek8n47WqZMiB7TDA==",\n    "Type": "SHA512"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1656518476000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}], 'var_functions.query_db:9': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_functions.query_db:8': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:22': {'total_packages': 661372, 'release_packages': 337844, 'latest_packages': 15811}, 'var_functions.execute_python:24': [{'Name': '@discordx/music', 'Version': '6.0.2', 'ProjectName': 'discordx-ts/discordx'}, {'Name': '@discordx/music', 'Version': '6.0.2', 'ProjectName': 'discordx-ts/discordx'}, {'Name': '@discordx/pagination', 'Version': '3.4.1', 'ProjectName': 'discordx-ts/discordx'}, {'Name': '@discordx/pagination', 'Version': '3.4.1', 'ProjectName': 'discordx-ts/discordx'}, {'Name': '@discordx/utilities', 'Version': '5.2.1', 'ProjectName': 'discordx-ts/discordx'}], 'var_functions.query_db:28': [{'ProjectName': 'eclipse-scout/scout.rt'}, {'ProjectName': 'eco/ecomponents'}, {'ProjectName': 'edgeandnode/common'}, {'ProjectName': 'discordx-ts/discordx'}, {'ProjectName': 'dolittle/home'}], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:36': [{'Name': '@dylanvann/svelte', 'Version': '3.25.4', 'Stars': 73499, 'ProjectName': 'sveltejs/svelte'}, {'Name': '@dylanvann/svelte', 'Version': '3.25.4', 'Stars': 73499, 'ProjectName': 'sveltejs/svelte'}, {'Name': '@dumc11/tailwindcss', 'Version': '0.4.0', 'Stars': 73464, 'ProjectName': 'tailwindcss/tailwindcss'}, {'Name': '@dumc11/tailwindcss', 'Version': '0.4.0', 'Stars': 73464, 'ProjectName': 'tailwindcss/tailwindcss'}, {'Name': '@dman777/shadow-dom-quill-temp', 'Version': '1.0.0', 'Stars': 42407, 'ProjectName': 'quilljs/quill'}]}

exec(code, env_args)
