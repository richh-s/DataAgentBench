code = """import json
import pandas as pd
import re

# Get file paths
pkg_file = var_functions.query_db:4
pkg_version_file = var_functions.query_db:8
proj_info_file = var_functions.query_db:6

# Load data
with open(str(pkg_file), 'r') as f:
    packages = json.load(f)
with open(str(pkg_version_file), 'r') as f:
    pkgversions = json.load(f)
with open(str(proj_info_file), 'r') as f:
    projinfo = json.load(f)

# To DataFrames
df_packages = pd.DataFrame(packages)
df_pkgversions = pd.DataFrame(pkgversions)
df_projinfo = pd.DataFrame(projinfo)

# Filter for MIT license and release status
mit_packages = []
for _, pkg in df_packages.iterrows():
    if pkg['System'] != 'NPM':
        continue
    try:
        licenses = json.loads(pkg['Licenses'])
        version_info = json.loads(pkg['VersionInfo'].replace('\n', '').strip())
        if 'MIT' in licenses and version_info.get('IsRelease', False) == True:
            mit_packages.append(pkg)
    except:
        continue

df_mit = pd.DataFrame(mit_packages)
print('MIT release packages:', len(df_mit))

# Merge with project_packageversion
df_merged = pd.merge(df_mit, df_pkgversions, 
    on=['System', 'Name', 'Version'], how='inner')
print('After merge with project_packageversion:', len(df_merged))

# Extract fork counts
df_projinfo['ForkCount'] = df_projinfo['Project_Information'].apply(
    lambda x: int(re.search(r'(\d+)\s+forks?', str(x), re.I).group(1)) 
    if re.search(r'(\d+)\s+forks?', str(x), re.I) else 0
)

# Find matching projects and their fork counts
projects_forks = {}
for _, pkg in df_merged.iterrows():
    proj_name = pkg['ProjectName']
    if pd.isna(proj_name):
        continue
    
    # Find matching project info
    matches = df_projinfo[df_projinfo['Project_Information'].str.contains(proj_name, na=False)]
    if len(matches) > 0:
        fork_count = matches.iloc[0]['ForkCount']
        if fork_count > 0:
            if proj_name not in projects_forks:
                projects_forks[proj_name] = fork_count

# Get top 5 by fork count
sorted_projects = sorted(projects_forks.items(), key=lambda x: x[1], reverse=True)[:5]

result = {
    'top_5_projects': [(name, forks) for name, forks in sorted_projects],
    'total_mit_packages': len(df_mit),
    'total_merged': len(df_merged),
    'projects_with_forks': len(projects_forks)
}
print('__RESULT__:')
print(json.dumps(str(result)))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:1': ['project_info', 'project_packageversion'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project is hosted on GitHub under the name learnfrontend-dc/product-cart, and it currently has 2 open issues. It has garnered a total of 11 stars and has been forked 12 times.', 'Licenses': '[]', 'Description': 'None', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The GitHub project ledgerproject/keypairoom currently has 3 open issues, 3 stars, and 0 forks.', 'Licenses': '[\n  "AGPL-3.0"\n]', 'Description': 'Component to generate and regenerate a keypair, in a deterministic and private way', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leebyron/jasmine-check is hosted on GitHub and currently has 0 open issues, 11 stars, and 3 forks.', 'Licenses': '[]', 'Description': 'Generative property testing for Jasmine', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leebyron/testcheck-js on GitHub has an open issues count of 29, a stars count of 1185, and a forks count of 58, making it a notable repository in the community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': 'Generative testing for JavaScript', 'Homepage': 'http://leebyron.com/testcheck-js', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leecade/react-native-swiper is hosted on GitHub and has a total of 786 open issues, along with an impressive 10,249 stars and 2,392 forks, making it a popular choice among developers for implementing swiping functionality in React Native applications.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'The best Swiper component for React Native.', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
