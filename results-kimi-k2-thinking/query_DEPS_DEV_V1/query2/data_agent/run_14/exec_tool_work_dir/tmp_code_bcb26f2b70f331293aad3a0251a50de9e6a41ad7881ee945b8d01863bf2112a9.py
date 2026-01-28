code = """import json
import pandas as pd
import re

# Load NPM packages data (from file, large)
packages_file = locals()['var_functions.query_db:44']
with open(packages_file, 'r') as f:
    packages = json.load(f)

# Load project versions data (from file, large)
versions_file = locals()['var_functions.query_db:8']
with open(versions_file, 'r') as f:
    versions = json.load(f)

# Load project info data (from direct result, small)
projects = locals()['var_functions.query_db:6']

# Convert to DataFrames
df_packages = pd.DataFrame(packages)
df_versions = pd.DataFrame(versions)
df_info = pd.DataFrame(projects)

print(f'Data loaded: {len(df_packages)} packages, {len(df_versions)} versions, {len(df_info)} projects')

# Filter for MIT license and release packages
mit_release_packages = []
for _, pkg in df_packages.iterrows():
    try:
        licenses = json.loads(pkg['Licenses'])
        ver_info = json.loads(pkg['VersionInfo'].replace('\n', '').strip())
        if pkg['System'] == 'NPM' and 'MIT' in licenses and ver_info.get('IsRelease', False) == True:
            mit_release_packages.append(pkg.to_dict())
    except:
        continue

print(f'Found {len(mit_release_packages)} MIT-licensed release NPM packages')

# Create lookup for project versions
version_lookup = {}
for _, ver in df_versions.iterrows():
    key = (ver['System'], ver['Name'], ver['Version'])
    version_lookup[key] = ver['ProjectName']

# Extract fork counts from project info
df_info['ForkCount'] = df_info['Project_Information'].apply(
    lambda x: int(re.search(r'(\d+)\s+forks', str(x), re.I).group(1)) 
    if re.search(r'(\d+)\s+forks', str(x), re.I) else 0
)

# Map package projects to fork counts
project_forks = {}
processed = set()

for pkg in mit_release_packages:
    key = (pkg['System'], pkg['Name'], pkg['Version'])
    project_name = version_lookup.get(key)
    
    if project_name and project_name not in processed:
        processed.add(project_name)
        # Find project info matching this project name
        for _, proj in df_info.iterrows():
            if project_name in str(proj['Project_Information']) and proj['ForkCount'] > 0:
                project_forks[project_name] = proj['ForkCount']
                break

# Get top 5 projects
sorted_projects = sorted(project_forks.items(), key=lambda x: x[1], reverse=True)[:5]

result = {
    'top_5': sorted_projects,
    'total_packages': len(mit_release_packages),
    'mapped_projects': len(project_forks)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:1': ['project_info', 'project_packageversion'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project is hosted on GitHub under the name learnfrontend-dc/product-cart, and it currently has 2 open issues. It has garnered a total of 11 stars and has been forked 12 times.', 'Licenses': '[]', 'Description': 'None', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The GitHub project ledgerproject/keypairoom currently has 3 open issues, 3 stars, and 0 forks.', 'Licenses': '[\n  "AGPL-3.0"\n]', 'Description': 'Component to generate and regenerate a keypair, in a deterministic and private way', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leebyron/jasmine-check is hosted on GitHub and currently has 0 open issues, 11 stars, and 3 forks.', 'Licenses': '[]', 'Description': 'Generative property testing for Jasmine', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leebyron/testcheck-js on GitHub has an open issues count of 29, a stars count of 1185, and a forks count of 58, making it a notable repository in the community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': 'Generative testing for JavaScript', 'Homepage': 'http://leebyron.com/testcheck-js', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leecade/react-native-swiper is hosted on GitHub and has a total of 786 open issues, along with an impressive 10,249 stars and 2,392 forks, making it a popular choice among developers for implementing swiping functionality in React Native applications.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'The best Swiper component for React Native.', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:34': [], 'var_functions.query_db:40': [{'ProjectName': 'dataminingsupply/dms-io'}, {'ProjectName': 'isacvale/fc'}, {'ProjectName': 'laihaojie/jie'}, {'ProjectName': 'laihaojie/jie'}, {'ProjectName': 'laihaojie/jie'}], 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json'}

exec(code, env_args)
