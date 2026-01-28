code = """import json
import pandas as pd
import re

# Load the data
pkg_path = locals()['var_functions.query_db:26']
ver_path = locals()['var_functions.query_db:8']
info_path = locals()['var_functions.query_db:6']

with open(pkg_path) as f:
    packages = json.load(f)
with open(ver_path) as f:
    versions = json.load(f)
with open(info_path) as f:
    projects = json.load(f)

df_pkg = pd.DataFrame(packages)
df_ver = pd.DataFrame(versions)
df_proj = pd.DataFrame(projects)

print('Data loaded:', len(df_pkg), 'packages,', len(df_ver), 'versions,', len(df_proj), 'projects')

# Filter packages: MIT license and Release
def has_mit_license(lic):
    try:
        return 'MIT' in json.loads(lic)
    except:
        return False

def is_release_version(ver_info):
    try:
        clean = ver_info.replace('\n', '').strip()
        return json.loads(clean).get('IsRelease', False) == True
    except:
        return False

df_mit_releases = df_pkg[df_pkg['Licenses'].apply(has_mit_license) & df_pkg['VersionInfo'].apply(is_release_version)]
print('MIT release packages:', len(df_mit_releases))

# Merge with versions to get project names
df_merged = pd.merge(df_mit_releases, df_ver[['System','Name','Version','ProjectName']], 
                     on=['System','Name','Version'], how='inner')
print('After merge with versions:', len(df_merged))

# Extract fork counts from project information
def extract_forks(proj_info):
    try:
        match = re.search(r'(\d+)\s+forks', str(proj_info), re.IGNORECASE)
        return int(match.group(1)) if match else 0
    except:
        return 0

df_proj['ForkCount'] = df_proj['Project_Information'].apply(extract_forks)

# Find projects for each package
project_forks = {}
for _, pkg in df_merged.iterrows():
    proj_name = pkg['ProjectName']
    if pd.isna(proj_name):
        continue
    
    # Find matching project
    matches = df_proj[df_proj['Project_Information'].str.contains(proj_name, na=False)]
    if len(matches) > 0:
        forks = matches.iloc[0]['ForkCount']
        project_forks[proj_name] = forks

# Get top 5 projects by fork count
top5 = sorted([(k, v) for k, v in project_forks.items() if v > 0], key=lambda x: x[1], reverse=True)[:5]

result = {
    'top_5_projects': top5,
    'total_packages': len(df_merged),
    'projects_mapped': len(project_forks)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:1': ['project_info', 'project_packageversion'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project is hosted on GitHub under the name learnfrontend-dc/product-cart, and it currently has 2 open issues. It has garnered a total of 11 stars and has been forked 12 times.', 'Licenses': '[]', 'Description': 'None', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The GitHub project ledgerproject/keypairoom currently has 3 open issues, 3 stars, and 0 forks.', 'Licenses': '[\n  "AGPL-3.0"\n]', 'Description': 'Component to generate and regenerate a keypair, in a deterministic and private way', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leebyron/jasmine-check is hosted on GitHub and currently has 0 open issues, 11 stars, and 3 forks.', 'Licenses': '[]', 'Description': 'Generative property testing for Jasmine', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leebyron/testcheck-js on GitHub has an open issues count of 29, a stars count of 1185, and a forks count of 58, making it a notable repository in the community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': 'Generative testing for JavaScript', 'Homepage': 'http://leebyron.com/testcheck-js', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leecade/react-native-swiper is hosted on GitHub and has a total of 786 open issues, along with an impressive 10,249 stars and 2,392 forks, making it a popular choice among developers for implementing swiping functionality in React Native applications.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'The best Swiper component for React Native.', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:34': []}

exec(code, env_args)
