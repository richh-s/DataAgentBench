code = """import json
import pandas as pd
import re

# Load all data file paths
package_file_path = locals()['var_functions.query_db:34']
project_pkg_file_path = locals()['var_functions.query_db:12']
project_info_file_path = locals()['var_functions.query_db:14']

print('Loading data files...')
with open(package_file_path, 'r') as f:
    packages = json.load(f)

with open(project_pkg_file_path, 'r') as f:
    project_packages = json.load(f)

with open(project_info_file_path, 'r') as f:
    project_info = json.load(f)

print(f'Loaded {len(packages)} packages, {len(project_packages)} project mappings, {len(project_info)} project info records')

# Create DataFrames
df_packages = pd.DataFrame(packages)
df_proj_pkg = pd.DataFrame(project_packages)
df_proj_info = pd.DataFrame(project_info)

# Parse VersionInfo field
def parse_version_info(vi_str):
    try:
        clean_str = vi_str.replace('\n', ' ').strip()
        parsed = json.loads(clean_str)
        return (parsed.get('IsRelease', False), parsed.get('Ordinal', 0))
    except:
        return (False, 0)

# Apply parsing
version_data = df_packages['VersionInfo'].apply(parse_version_info)
df_packages['IsRelease'] = [v[0] for v in version_data]
df_packages['Ordinal'] = [v[1] for v in version_data]

# Get latest release version for each package
print('Finding latest release versions...')
release_packages = df_packages[df_packages['IsRelease'] == True].copy()
latest_idx = release_packages.groupby('Name')['Ordinal'].idxmax()
latest_packages = release_packages.loc[latest_idx].reset_index(drop=True)

print(f'Found {len(latest_packages)} latest release packages')

# Merge with project_packageversion to get ProjectName
print('Mapping packages to GitHub projects...')
merged_df = pd.merge(
    latest_packages[['Name', 'Version', 'System']],
    df_proj_pkg[['Name', 'Version', 'System', 'ProjectName']],
    on=['Name', 'Version', 'System'],
    how='inner'
)

print(f'Mapped {len(merged_df)} packages to projects')

# Extract stars from project info
print('Extracting GitHub stars from project information...')
stars_list = []
for idx, row in df_proj_info.iterrows():
    info = str(row['Project_Information'])
    
    # Look for star count pattern
    stars_match = re.search(r'(\d[\d,]*)\s+stars', info, re.IGNORECASE)
    stars_count = 0
    if stars_match:
        stars_str = stars_match.group(1).replace(',', '')
        if stars_str.isdigit():
            stars_count = int(stars_str)
    
    # Look for project name
    proj_match = re.search(r'project\s+(\S+)', info)
    if proj_match:
        proj_name = proj_match.group(1).rstrip('.,')
        stars_list.append({'ProjectName': proj_name, 'Stars': stars_count})

stars_df = pd.DataFrame(stars_list)
print(f'Extracted stars for {len(stars_list)} projects')

# Final merge to get stars for packages
final_df = pd.merge(
    merged_df,
    stars_df,
    on='ProjectName',
    how='inner'
)

print(f'Final dataset contains {len(final_df)} packages with stars')

# Deduplicate by package name and sort by stars
unique_df = final_df.sort_values('Stars', ascending=False).drop_duplicates(subset=['Name'])

# Get top 5 packages
top5_df = unique_df.head(5)

print('Top 5 packages by GitHub stars:')
for idx, row in top5_df.iterrows():
    print(f"{row['Name']} v{row['Version']} - {row['Stars']} stars ({row['ProjectName']})")

# Prepare final result
result = []
for idx, row in top5_df.iterrows():
    result.append({
        'Name': row['Name'],
        'Version': row['Version'],
        'Stars': row['Stars'],
        'ProjectName': row['ProjectName']
    })

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:2': ['project_info', 'project_packageversion'], 'var_functions.query_db:5': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@ecl%2Ftwig-component-carousel/3.11.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'Hashes': '[\n  {\n    "Hash": "vH5da6eUZ94i1AcOsrC6VjSV88cMUe5A1w+CDHAt2aYXldR9sBNRCse27cIx51GnUjnj7dSe3o5A81TjraJ0Lw==",\n    "Type": "SHA512"\n  },\n  {\n    "Hash": "WZUWPp1jVp6nrUZ0n7vmthbB4OrtnLFNDOPPBBNp15I=",\n    "Type": "SHA256"\n  },\n  {\n    "Hash": "JbFslb4AeqQVI+LCXFeZKFrWmHI=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "zBm5Qvg5p2bQwUTcg6hZYA==",\n    "Type": "MD5"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1699345351000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'Licenses': '[]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@douganderson444%2Fpanzoom-node/v/1.1.5"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}', 'Hashes': '[\n  {\n    "Hash": "bn6jsFfgQaOqxYcxQLdn+w==",\n    "Type": "MD5"\n  },\n  {\n    "Hash": "Ag2muuzRUxbKTAR/H0qjiVGqd5E=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "Z2cdZL3dyM3mmLnEKE4HDFAFnE8OTVU1Lm36fasqZuFRlfjv+M8qkZs+ZAwOsR65FfhH1St2n1YvhihaMM5UEw==",\n    "Type": "SHA512"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '1', 'UpstreamPublishedAt': '1670271173000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'Licenses': '[]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@douganderson444%2Fpanzoom-node/v/1.1.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}', 'Hashes': '[\n  {\n    "Hash": "f882urh9+DaLLfg22vF4Dw==",\n    "Type": "MD5"\n  },\n  {\n    "Hash": "UavDKi+B1bjz5yL/IEUOzG5BIX0=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "Br/d41zpasemiy1jjn91jYmLFbgFFGo5+V+v5+LRxHeTg2MajAkwczkbMUyb3k8xD0UIubDfClv9roNgLIoOEQ==",\n    "Type": "SHA512"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '1', 'UpstreamPublishedAt': '1654791421000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'Licenses': '[\n  "ISC"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@dreamworld%2Fdw-select/3.1.2-fix-double-click-issue.1"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}', 'Hashes': '[\n  {\n    "Hash": "1e+/qEffZeAgXRtIOUmPqw==",\n    "Type": "MD5"\n  },\n  {\n    "Hash": "C3IyUAgv9Bs96QRmMOHUrQwBnS4=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "07tFydL0pzuqYZbHESf4n0N5gbgvaPZFBfRZmC+k4dqhaKjR2xRBXBpCyxji9W0kkkCVrgtiTrI/XzhgTBq80w==",\n    "Type": "SHA512"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1624260093000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'Links': '[\n  {\n    "Label": "ORIGIN",\n    "URL": "https://registry.npmjs.org/@discue%2Fui-components/0.13.0"\n  }\n]', 'Advisories': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}', 'Hashes': '[\n  {\n    "Hash": "9BaLXgrA89SmryO88KCXZg==",\n    "Type": "MD5"\n  },\n  {\n    "Hash": "1ehWf/vTvGu5BskEEAeiQL1rNcM=",\n    "Type": "SHA1"\n  },\n  {\n    "Hash": "UOcNM2Ee5byWKfgJ8Q9am9B369//NKxfLA9nr20EClco8KptuYrcBXZXqOpBk3jJByBoEaek8n47WqZMiB7TDA==",\n    "Type": "SHA512"\n  }\n]', 'DependenciesProcessed': '1', 'DependencyError': '0', 'UpstreamPublishedAt': '1656518476000000.0', 'Registries': '[]', 'SLSAProvenance': 'None', 'UpstreamIdentifiers': '[]', 'Purl': 'None'}], 'var_functions.query_db:9': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_functions.query_db:8': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:22': {'total_packages': 661372, 'release_packages': 337844, 'latest_packages': 15811}, 'var_functions.execute_python:24': [{'Name': '@discordx/music', 'Version': '6.0.2', 'ProjectName': 'discordx-ts/discordx'}, {'Name': '@discordx/music', 'Version': '6.0.2', 'ProjectName': 'discordx-ts/discordx'}, {'Name': '@discordx/pagination', 'Version': '3.4.1', 'ProjectName': 'discordx-ts/discordx'}, {'Name': '@discordx/pagination', 'Version': '3.4.1', 'ProjectName': 'discordx-ts/discordx'}, {'Name': '@discordx/utilities', 'Version': '5.2.1', 'ProjectName': 'discordx-ts/discordx'}], 'var_functions.query_db:28': [{'ProjectName': 'eclipse-scout/scout.rt'}, {'ProjectName': 'eco/ecomponents'}, {'ProjectName': 'edgeandnode/common'}, {'ProjectName': 'discordx-ts/discordx'}, {'ProjectName': 'dolittle/home'}], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:36': [{'Name': '@dylanvann/svelte', 'Version': '3.25.4', 'Stars': 73499, 'ProjectName': 'sveltejs/svelte'}, {'Name': '@dylanvann/svelte', 'Version': '3.25.4', 'Stars': 73499, 'ProjectName': 'sveltejs/svelte'}, {'Name': '@dumc11/tailwindcss', 'Version': '0.4.0', 'Stars': 73464, 'ProjectName': 'tailwindcss/tailwindcss'}, {'Name': '@dumc11/tailwindcss', 'Version': '0.4.0', 'Stars': 73464, 'ProjectName': 'tailwindcss/tailwindcss'}, {'Name': '@dman777/shadow-dom-quill-temp', 'Version': '1.0.0', 'Stars': 42407, 'ProjectName': 'quilljs/quill'}], 'var_functions.execute_python:42': [{'Name': '@dylanvann/svelte', 'Version': '3.25.4', 'Stars': 73499, 'ProjectName': 'sveltejs/svelte'}, {'Name': '@dumc11/tailwindcss', 'Version': '0.4.0', 'Stars': 73464, 'ProjectName': 'tailwindcss/tailwindcss'}, {'Name': '@dman777/shadow-dom-quill-temp', 'Version': '1.0.0', 'Stars': 42407, 'ProjectName': 'quilljs/quill'}]}

exec(code, env_args)
