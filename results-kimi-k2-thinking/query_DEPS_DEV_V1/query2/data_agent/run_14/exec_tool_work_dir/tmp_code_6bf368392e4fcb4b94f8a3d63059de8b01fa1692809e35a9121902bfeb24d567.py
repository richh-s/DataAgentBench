code = """import json
import pandas as pd

# Get the file paths from the storage variables
pkg_file_path = locals()['var_functions.query_db:4']
pkg_version_file_path = locals()['var_functions.query_db:8']
proj_info_file_path = locals()['var_functions.query_db:6']

# Load all the data
with open(pkg_file_path, 'r') as f:
    packageinfo_data = json.load(f)

with open(pkg_version_file_path, 'r') as f:
    pkg_version_data = json.load(f)

with open(proj_info_file_path, 'r') as f:
    proj_info_data = json.load(f)

# Convert to DataFrames
df_pkg = pd.DataFrame(packageinfo_data)
df_pkg_version = pd.DataFrame(pkg_version_data)
df_proj_info = pd.DataFrame(proj_info_data)

print(f"Loaded: {len(df_pkg)} packages, {len(df_pkg_version)} package versions, {len(df_proj_info)} project infos")

# Filter for MIT license and release status
def has_mit_license(licenses_str):
    try:
        licenses = json.loads(licenses_str)
        return 'MIT' in licenses
    except:
        return False

def is_release(version_info_str):
    try:
        clean_str = version_info_str.replace('\n', '').strip()
        version_info = json.loads(clean_str)
        return version_info.get('IsRelease', False) == True
    except:
        return False

# Apply filters
df_pkg_filtered = df_pkg[
    df_pkg['Licenses'].apply(has_mit_license) & 
    df_pkg['VersionInfo'].apply(is_release) &
    (df_pkg['System'] == 'NPM')
].copy()

print(f"Filtered to {len(df_pkg_filtered)} MIT-licensed NPM release packages")

# Merge with project_packageversion
df_merged = pd.merge(
    df_pkg_filtered,
    df_pkg_version,
    on=['System', 'Name', 'Version'],
    how='inner',
    suffixes=('_pkg', '_proj')
)

print(f"Merged with project_packageversion: {len(df_merged)} records")

# Extract fork count from Project_Information
def extract_fork_count(proj_info_str):
    try:
        import re
        match = re.search(r'(\d+)\s+forks?', str(proj_info_str), re.IGNORECASE)
        if match:
            return int(match.group(1))
        return 0
    except:
        return 0

df_proj_info['ForkCount'] = df_proj_info['Project_Information'].apply(extract_fork_count)

print(f"Extracted fork counts from {len(df_proj_info)} project info records")
print(f"Fork count stats: min={df_proj_info['ForkCount'].min()}, max={df_proj_info['ForkCount'].max()}, avg={df_proj_info['ForkCount'].mean():.1f}")

# Now we need to join df_merged with df_proj_info
# df_merged has ProjectName like 'dataminingsupply/dms-io'
# df_proj_info has Project_Information containing text like '...dataminingsupply/dms-io...'

# Let's create a mapping function to match ProjectName to Project_Information
def find_project_forks(project_name):
    if pd.isna(project_name):
        return 0
    
    # Try exact match in Project_Information
    matches = df_proj_info[df_proj_info['Project_Information'].str.contains(project_name, na=False)]
    
    if len(matches) > 0:
        return matches.iloc[0]['ForkCount']
    
    return 0

# Apply to get fork counts
print("Matching projects to get fork counts...")
df_merged['ForkCount'] = df_merged['ProjectName'].apply(find_project_forks)

# Filter out those with 0 forks (no match or no forks)
df_with_forks = df_merged[df_merged['ForkCount'] > 0]
print(f"Found {len(df_with_forks)} packages with matching projects that have forks")

# Get unique projects and their max fork counts
# Group by ProjectName to get unique projects
df_unique_projects = df_with_forks.groupby(['ProjectName', 'ForkCount']).size().reset_index(name='PackageCount')

# Sort by fork count descending and get top 5
top_5_projects = df_unique_projects.nlargest(5, 'ForkCount')

print(f"Top 5 projects by fork count:")
for idx, row in top_5_projects.iterrows():
    print(f"  {row['ProjectName']}: {row['ForkCount']} forks ({row['PackageCount']} packages)")

result = {
    "top_5_projects": top_5_projects[['ProjectName', 'ForkCount', 'PackageCount']].to_dict('records'),
    "total_packages_considered": len(df_pkg_filtered),
    "total_merged_projects": len(df_merged),
    "projects_with_forks": len(df_unique_projects),
    "top_fork_count": int(top_5_projects['ForkCount'].iloc[0]) if len(top_5_projects) > 0 else 0
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:1': ['project_info', 'project_packageversion'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project is hosted on GitHub under the name learnfrontend-dc/product-cart, and it currently has 2 open issues. It has garnered a total of 11 stars and has been forked 12 times.', 'Licenses': '[]', 'Description': 'None', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The GitHub project ledgerproject/keypairoom currently has 3 open issues, 3 stars, and 0 forks.', 'Licenses': '[\n  "AGPL-3.0"\n]', 'Description': 'Component to generate and regenerate a keypair, in a deterministic and private way', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leebyron/jasmine-check is hosted on GitHub and currently has 0 open issues, 11 stars, and 3 forks.', 'Licenses': '[]', 'Description': 'Generative property testing for Jasmine', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leebyron/testcheck-js on GitHub has an open issues count of 29, a stars count of 1185, and a forks count of 58, making it a notable repository in the community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': 'Generative testing for JavaScript', 'Homepage': 'http://leebyron.com/testcheck-js', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leecade/react-native-swiper is hosted on GitHub and has a total of 786 open issues, along with an impressive 10,249 stars and 2,392 forks, making it a popular choice among developers for implementing swiping functionality in React Native applications.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'The best Swiper component for React Native.', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
