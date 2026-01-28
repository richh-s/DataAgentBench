code = """import json
import re
import pandas as pd

# Read all data  
with open(locals()['var_functions.query_db:0'], 'r') as f:
    package_data = json.load(f)

with open(locals()['var_functions.query_db:2'], 'r') as f:
    project_pkg_data = json.load(f)

with open(locals()['var_functions.query_db:6'], 'r') as f:
    project_info_data = json.load(f)

# Parse project_info to extract ProjectName and Forks
project_forks = []
for item in project_info_data:
    info = item['Project_Information']
    # Extract fork count
    fork_match = re.search(r'(\d+) forks', info)
    # Extract project name - look for patterns like "owner/repo"
    name_match = re.search(r'([a-zA-Z0-9_.-]+/[a-zA-Z0-9_.-]+)', info)
    if fork_match and name_match:
        forks = int(fork_match.group(1))
        project_name = name_match.group(1)
        project_forks.append({
            'ProjectName': project_name,
            'Forks': forks
        })

# Create DataFrames
df_packages = pd.DataFrame(package_data)
df_project_pkg = pd.DataFrame(project_pkg_data)
df_project_forks = pd.DataFrame(project_forks)

# Merge packages with project_packageversion to get ProjectName
merged = df_packages.merge(
    df_project_pkg[['System', 'Name', 'Version', 'ProjectName']],
    on=['System', 'Name', 'Version'],
    how='inner'
)

# Count unique projects
unique_projects = merged[['ProjectName']].drop_duplicates()

# Merge with fork data to get fork counts
final = unique_projects.merge(
    df_project_forks,
    on='ProjectName',
    how='inner'
)

# Sort by fork count and get top 5
top_5 = final.sort_values('Forks', ascending=False).head(5)

print('__RESULT__:')
print(top_5.to_json(orient='records'))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:8': 'Loaded 176998 package records', 'var_functions.execute_python:10': {'project_packageversion_count': 597602, 'project_info_count': 770, 'sample_project_pkg': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectName': 'dataminingsupply/dms-io'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectName': 'isacvale/fc'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectName': 'laihaojie/jie'}], 'sample_project_info': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.'}]}, 'var_functions.execute_python:12': {'packages': 176998, 'project_versions': 597602, 'project_infos': 770}, 'var_functions.execute_python:14': 'Loaded 176998 packages, 597602 project versions, 770 project infos', 'var_functions.execute_python:16': {'total_projects_with_forks': 363, 'top_10_forks': [{'ProjectName': 'leaflet/leaflet', 'Forks': 5782, 'OriginalText': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'ProjectName': 'semantic-org/semantic-ui', 'Forks': 4955, 'OriginalText': 'The project semantic-org/semantic-ui is hosted on GitHub and currently has an open issues count of 1076, along with a notable stars count of 51069 and 4955 forks.'}, {'ProjectName': 'react-native-community/react-native-webview', 'Forks': 2962, 'OriginalText': 'The project react-native-community/react-native-webview is hosted on GitHub and currently has 87 open issues, 6345 stars, and 2962 forks.'}, {'ProjectName': 'theia-ide/theia', 'Forks': 2451, 'OriginalText': 'The project theia-ide/theia on GitHub is an open-source IDE with an open issues count of 1359, and it has garnered a significant following, evident from its 18526 stars and 2451 forks.'}, {'ProjectName': 'sass/node-sass', 'Forks': 1326, 'OriginalText': 'The project sass/node-sass on GitHub currently has 189 open issues, 8498 stars, and 1326 forks, making it a popular choice among developers for managing stylesheets with Sass.'}, {'ProjectName': 'shaka-project/shaka-player', 'Forks': 1319, 'OriginalText': 'The project shaka-project/shaka-player on GitHub is a well-regarded open-source initiative, currently featuring 110 open issues, 6949 stars, and 1319 forks, reflecting its popularity and active development within the community.'}, {'ProjectName': 'mbrn/material-table', 'Forks': 1035, 'OriginalText': 'The project mbrn/material-table is hosted on GitHub and currently has 23 open issues, 3464 stars, and 1035 forks, making it a popular choice among developers looking for a material design data table solution.'}, {'ProjectName': 'ternjs/acorn', 'Forks': 944, 'OriginalText': 'The project ternjs/acorn on GitHub is a popular repository with a remarkable stars count of 9841 and a total of 944 forks. Currently, it has an open issues count of 15, indicating ongoing development and community engagement.'}, {'ProjectName': 'mjmlio/mjml', 'Forks': 937, 'OriginalText': 'The project mjmlio/mjml on GitHub is a popular repository that currently has 75 open issues, 15,829 stars, and 937 forks.'}, {'ProjectName': 'thejameskyle/react-loadable', 'Forks': 857, 'OriginalText': 'The project thejameskyle/react-loadable on GitHub is a popular repository with a total of 16,576 stars and 857 forks, currently having 36 open issues.'}]}}

exec(code, env_args)
