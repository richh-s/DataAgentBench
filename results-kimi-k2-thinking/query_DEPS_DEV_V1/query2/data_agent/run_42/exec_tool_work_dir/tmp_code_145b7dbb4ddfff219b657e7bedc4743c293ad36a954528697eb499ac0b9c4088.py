code = """import json
import pandas as pd
import re

# Load all data
with open(locals()['var_functions.query_db:38'], 'r') as f:
    package_data = json.load(f)

with open(locals()['var_functions.query_db:26'], 'r') as f:
    project_pv_data = json.load(f)

with open(locals()['var_functions.query_db:32'], 'r') as f:
    project_info_data = json.load(f)

# Convert to DataFrames
df_packages = pd.DataFrame(package_data)
df_project_pv = pd.DataFrame(project_pv_data)
df_project_info = pd.DataFrame(project_info_data)

# Filter for MIT license and release versions
print("Filtering packages...")
mit_release_packages = []
for _, row in df_packages.iterrows():
    try:
        if 'MIT' in str(row['Licenses']) and '"IsRelease": true' in str(row['VersionInfo']):
            mit_release_packages.append({
                'System': row['System'],
                'Name': row['Name'],
                'Version': row['Version']
            })
    except:
        continue

mit_df = pd.DataFrame(mit_release_packages)
print(f"MIT release packages: {len(mit_df)}")

# Merge with project_packageversion
merged_pv = pd.merge(
    mit_df,
    df_project_pv[['System', 'Name', 'Version', 'ProjectName']],
    on=['System', 'Name', 'Version'],
    how='inner'
)
print(f"Matching project versions: {len(merged_pv)}")

# Get unique projects
unique_projects = merged_pv[['ProjectName']].drop_duplicates()
print(f"Unique projects: {len(unique_projects)}")

# Extract fork counts from project_info
project_info_extracted = []
for _, row in df_project_info.iterrows():
    try:
        proj_info = row['Project_Information']
        # Extract project name
        name_match = re.search(r'The project (\S+?) on GitHub', proj_info)
        forks_match = re.search(r'(\d+) forks', proj_info)
        
        if name_match and forks_match:
            project_name = name_match.group(1)
            forks = int(forks_match.group(1))
            project_info_extracted.append({
                'ProjectName': project_name,
                'Forks': forks
            })
    except:
        continue

project_info_df = pd.DataFrame(project_info_extracted)
print(f"Project info records with fork data: {len(project_info_df)}")

# Find top 5 projects
final_merged = pd.merge(
    unique_projects,
    project_info_df,
    on='ProjectName',
    how='inner'
)

# Sort and get top 5
top_5 = final_merged.nlargest(5, 'Forks')

# Verify these projects come from MIT licensed NPM packages
result = []
for _, project_row in top_5.iterrows():
    project_name = project_row['ProjectName']
    forks = project_row['Forks']
    
    # Find matching package(s)
    matching_packages = merged_pv[merged_pv['ProjectName'] == project_name]
    
    result.append({
        'project': project_name,
        'forks': forks,
        'package_count': len(matching_packages),
        'sample_packages': matching_packages.head(3).to_dict('records')
    })

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': {'total_mit_release_packages': 330, 'unique_packages': 145, 'sample_packages': [{'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0'}, {'System': 'NPM', 'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1'}, {'System': 'NPM', 'Name': '@eclipsejs/cli', 'Version': '1.0.0'}, {'System': 'NPM', 'Name': '@ebot7/edem-react', 'Version': '0.18.8'}, {'System': 'NPM', 'Name': '@e4a/irmaseal-wasm-bindings', 'Version': '0.0.1'}, {'System': 'NPM', 'Name': '@ebury/chameleon-components', 'Version': '0.1.103'}, {'System': 'NPM', 'Name': '@e-group/material-form', 'Version': '7.39.13'}, {'System': 'NPM', 'Name': '@e-group/material-layout', 'Version': '3.4.5'}, {'System': 'NPM', 'Name': '@dspworkplace/ui', 'Version': '1.0.8'}, {'System': 'NPM', 'Name': '@ditojs/router', 'Version': '0.96.0'}]}, 'var_functions.list_db:16': ['project_info', 'project_packageversion'], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_functions.execute_python:24': {'packages_count': 391228, 'project_pv_count': 5, 'package_columns': ['System', 'Name', 'Version', 'Licenses', 'VersionInfo'], 'project_pv_columns': ['System', 'Name', 'Version', 'ProjectType', 'ProjectName', 'RelationProvenance', 'RelationType']}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:28': {'mit_release_packages': 176170, 'matching_projects': 381414, 'unique_projects': 5430, 'sample_projects': [{'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'ProjectType': 'GITHUB', 'ProjectName': 'discue/ui-components', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'ProjectType': 'GITHUB', 'ProjectName': 'dvcol/web-extension-utils', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@eclipsejs/cli', 'Version': '1.0.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dlesage25/eclipse-cli', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@ebot7/edem-react', 'Version': '0.18.8', 'ProjectType': 'GITHUB', 'ProjectName': 'ebot7/edem', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@e4a/irmaseal-wasm-bindings', 'Version': '0.0.1', 'ProjectType': 'GITHUB', 'ProjectName': 'encryption4all/irmaseal', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@ebury/chameleon-components', 'Version': '0.1.46', 'ProjectType': 'GITHUB', 'ProjectName': 'ebury/chameleon', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@e-group/material-form', 'Version': '3.13.9', 'ProjectType': 'GITHUB', 'ProjectName': 'egroupai/egroup-material', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dspworkplace/ui', 'Version': '1.0.3', 'ProjectType': 'GITLAB', 'ProjectName': 'dsp-workplace/dsp-npm', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@ditojs/router', 'Version': '0.125.0', 'ProjectType': 'GITHUB', 'ProjectName': 'ditojs/dito', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dsrv/kms', 'Version': '0.2.2', 'ProjectType': 'GITHUB', 'ProjectName': 'dsrvlabs/kms', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}]}, 'var_functions.query_db:30': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project is hosted on GitHub under the name learnfrontend-dc/product-cart, and it currently has 2 open issues. It has garnered a total of 11 stars and has been forked 12 times.', 'Licenses': '[]', 'Description': 'None', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The GitHub project ledgerproject/keypairoom currently has 3 open issues, 3 stars, and 0 forks.', 'Licenses': '[\n  "AGPL-3.0"\n]', 'Description': 'Component to generate and regenerate a keypair, in a deterministic and private way', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leebyron/jasmine-check is hosted on GitHub and currently has 0 open issues, 11 stars, and 3 forks.', 'Licenses': '[]', 'Description': 'Generative property testing for Jasmine', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leebyron/testcheck-js on GitHub has an open issues count of 29, a stars count of 1185, and a forks count of 58, making it a notable repository in the community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': 'Generative testing for JavaScript', 'Homepage': 'http://leebyron.com/testcheck-js', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leecade/react-native-swiper is hosted on GitHub and has a total of 786 open issues, along with an impressive 10,249 stars and 2,392 forks, making it a popular choice among developers for implementing swiping functionality in React Native applications.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'The best Swiper component for React Native.', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.execute_python:34': {'packages': 391228, 'project_pv': 597602, 'project_info': 770, 'sample_project_info': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}]}, 'var_functions.execute_python:36': [{'ProjectName': 'sass/node-sass', 'Forks': 1326}, {'ProjectName': 'ternjs/acorn', 'Forks': 944}, {'ProjectName': 'thejameskyle/react-loadable', 'Forks': 857}, {'ProjectName': 'tailwindcss/tailwindcss', 'Forks': 848}, {'ProjectName': 'mono/mono', 'Forks': 845}], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json'}

exec(code, env_args)
