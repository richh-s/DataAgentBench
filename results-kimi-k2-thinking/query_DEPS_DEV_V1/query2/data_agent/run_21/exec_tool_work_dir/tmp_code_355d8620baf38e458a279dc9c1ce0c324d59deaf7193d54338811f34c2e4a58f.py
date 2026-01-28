code = """import json
import pandas as pd
import re

# Load the comprehensive data
packages_path = locals()['var_functions.query_db:0']
ppv_path = locals()['var_functions.query_db:2']
proj_info_path = locals()['var_functions.query_db:24']

with open(packages_path, 'r') as f:
    packages_data = json.load(f)

with open(ppv_path, 'r') as f:
    ppv_data = json.load(f)

with open(proj_info_path, 'r') as f:
    proj_info_data = json.load(f)

# Create DataFrames
packages_df = pd.DataFrame(packages_data)
ppv_df = pd.DataFrame(ppv_data)
proj_info_df = pd.DataFrame(proj_info_data)

# Filter packages: NPM + MIT license + IsRelease=true
mit_release_packages = []

for _, row in packages_df.iterrows():
    try:
        # Check MIT license
        licenses_str = str(row['Licenses']) if row['Licenses'] not in [None, 'None', ''] else '[]'
        licenses = json.loads(licenses_str)
        if 'MIT' in licenses:
            # Check IsRelease
            version_info_str = str(row['VersionInfo']) if row['VersionInfo'] not in [None, 'None', ''] else '{}'
            version_info = json.loads(version_info_str)
            if version_info.get('IsRelease', False):
                mit_release_packages.append({
                    'System': row['System'],
                    'Name': row['Name'],
                    'Version': row['Version']
                })
    except:
        continue

mit_df = pd.DataFrame(mit_release_packages)

# Merge with project_packageversion
merged_df = pd.merge(
    mit_df,
    ppv_df[['System', 'Name', 'Version', 'ProjectName']],
    on=['System', 'Name', 'Version'],
    how='inner'
)

# Extract project name from Project_Information
def extract_project_name(text):
    if not isinstance(text, str):
        return None
    match = re.search(r'The project (\S+?) on GitHub', text)
    return match.group(1) if match else None

proj_info_df['Extracted_ProjectName'] = proj_info_df['Project_Information'].apply(extract_project_name)

# Merge with project_info
final_df = pd.merge(
    merged_df,
    proj_info_df[['Extracted_ProjectName', 'Project_Information']],
    left_on='ProjectName',
    right_on='Extracted_ProjectName',
    how='inner'
)

# Extract fork count
def extract_fork_count(text):
    if not isinstance(text, str):
        return 0
    match = re.search(r'(\d+) forks', text)
    return int(match.group(1)) if match else 0

final_df['ForkCount'] = final_df['Project_Information'].apply(extract_fork_count)

# Get top 5 projects by fork count
top_5 = final_df.nlargest(5, 'ForkCount')[['ProjectName', 'ForkCount']].to_dict('records')

print('__RESULT__:')
print(json.dumps(top_5, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:14': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_functions.execute_python:22': {'packages_count': 661372, 'ppv_count': 597602, 'proj_info_count': 5, 'packages_df_cols': ['System', 'Name', 'Version', 'Licenses', 'Links', 'Advisories', 'VersionInfo', 'Hashes', 'DependenciesProcessed', 'DependencyError', 'UpstreamPublishedAt', 'Registries', 'SLSAProvenance', 'UpstreamIdentifiers', 'Purl'], 'ppv_df_cols': ['System', 'Name', 'Version', 'ProjectType', 'ProjectName', 'RelationProvenance', 'RelationType'], 'proj_info_df_cols': ['Project_Information', 'Licenses', 'Description', 'Homepage', 'OSSFuzz']}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
