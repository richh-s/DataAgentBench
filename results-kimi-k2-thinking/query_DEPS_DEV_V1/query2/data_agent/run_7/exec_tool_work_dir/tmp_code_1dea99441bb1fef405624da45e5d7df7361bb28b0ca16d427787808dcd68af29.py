code = """import json
import pandas as pd
import re

# Load all the data
packages_file = locals()['var_functions.query_db:8']
packageversions_file = locals()['var_functions.query_db:16']
projectinfo_file = locals()['var_functions.query_db:24']

with open(packages_file, 'r') as f:
    packages_data = json.load(f)

with open(packageversions_file, 'r') as f:
    packageversions_data = json.load(f)

with open(projectinfo_file, 'r') as f:
    projectinfo_data = json.load(f)

# Create DataFrames
df_packages = pd.DataFrame(packages_data)
df_pkgversions = pd.DataFrame(packageversions_data)
df_projects = pd.DataFrame(projectinfo_data)

# Merge packages with packageversions
df_pkgversions['key'] = df_pkgversions['Name'] + '|' + df_pkgversions['Version']
df_packages['key'] = df_packages['Name'] + '|' + df_packages['Version']

# Merge
merged = pd.merge(df_packages, df_pkgversions, on='key', how='inner', suffixes=('', '_pkg'))
merged = merged[merged['System'] == 'NPM']

# Extract fork counts more robustly
def extract_forks(info_text):
    if not info_text:
        return 0
    
    # Look for patterns like "X forks" or "forks count of X"
    patterns = [
        r'forks count of\s*(\d+)',
        r'(\d+)\s*forks',
        r'forks[,\s]*(\d+)',
        r'forks\D+(\d+)',
        r'forks count\D+(\d+)'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, info_text, re.IGNORECASE)
        if match:
            try:
                return int(match.group(1).replace(',', ''))
            except:
                continue
    
    return 0

# Process all project info to extract fork counts
df_projects['ForkCount'] = df_projects['Project_Information'].apply(extract_forks)

# Create a mapping from repository name to fork count
# Try to find the repository name in the Project_Information text
repo_fork_map = {}

for idx, row in df_projects.iterrows():
    info = row['Project_Information']
    forks = row['ForkCount']
    
    # Try to extract repo name from the text
    # Look for patterns like "project owner/repo" or "project named owner/repo"
    repo_patterns = [
        r'project\s+([a-zA-Z0-9._-]+/[a-zA-Z0-9._-]+)\s+is hosted',
        r'project\s+([a-zA-Z0-9._-]+/[a-zA-Z0-9._-]+)\s+on GitHub',
        r'project\s+named\s+([a-zA-Z0-9._-]+/[a-zA-Z0-9._-]+)',
        r'project\s+([a-zA-Z0-9._-]+/[a-zA-Z0-9._-]+)',
        r'repository\s+named\s+([a-zA-Z0-9._-]+/[a-zA-Z0-9._-]+)'
    ]
    
    repo_name = None
    for pattern in repo_patterns:
        match = re.search(pattern, info, re.IGNORECASE)
        if match:
            repo_name = match.group(1)
            break
    
    if repo_name:
        repo_fork_map[repo_name.lower()] = forks

# Now match the merged data with fork counts
merged['RepoKey'] = merged['ProjectName'].str.lower()
merged['ForkCount'] = merged['RepoKey'].map(repo_fork_map)

# Fill missing fork counts with 0
merged['ForkCount'] = merged['ForkCount'].fillna(0).astype(int)

# Get top 5 projects by fork count
top_5 = merged.nlargest(5, 'ForkCount')[['Name', 'Version', 'ProjectName', 'ForkCount']]

# Also get some stats
stats = {
    'total_mit_release_packages': len(merged),
    'packages_with_project_info': len(merged[merged['ForkCount'] > 0]),
    'top_5': top_5.to_dict('records')
}

print('__RESULT__:')
print(json.dumps(stats, indent=2))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:2': ['project_info', 'project_packageversion'], 'var_functions.query_db:5': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'Licenses': '[\n  "ISC"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'Name': '@edgedev/firebase', 'Version': '1.0.12', 'Licenses': '[\n  "ISC"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}'}, {'Name': '@eden-network/data', 'Version': '1.0.9-sev.5', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 14\n}'}], 'var_functions.query_db:6': [{'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'Name': '@eden-network/data', 'Version': '1.0.9-sev.5', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 14\n}'}, {'Name': '@eclipsejs/cli', 'Version': '1.0.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}'}, {'Name': '@dxos/client', 'Version': '2.31.8-dev.dcd68d50', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1605\n}'}, {'Name': '@dxos/client', 'Version': '2.31.8-dev.dcd68d50', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1605\n}'}, {'Name': '@ebot7/edem-react', 'Version': '0.18.8', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 55\n}'}, {'Name': '@e4a/irmaseal-wasm-bindings', 'Version': '0.0.1', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 1\n}'}, {'Name': '@ebury/chameleon-components', 'Version': '0.1.46', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 46\n}'}, {'Name': '@eddeee888/gcg-typescript-resolver-files', 'Version': '0.0.0-pr9-run20-1-20221027114308', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 60\n}'}, {'Name': '@e-group/material-form', 'Version': '3.13.9', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'Name': '@e-group/material-layout', 'Version': '3.4.5', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 6\n}'}, {'Name': '@dspworkplace/ui', 'Version': '1.0.3', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 4\n}'}, {'Name': '@ditojs/router', 'Version': '0.125.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 87\n}'}, {'Name': '@ditojs/ui', 'Version': '0.113.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 107\n}'}, {'Name': '@ditojs/admin', 'Version': '0.155.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 164\n}'}, {'Name': '@dsrv/kms', 'Version': '0.2.2', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'Name': '@domojs/rfx-parsers', 'Version': '1.5.9', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 23\n}'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'total_packages': 176998, 'sample_packages': [{'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'Name': '@eclipsejs/cli', 'Version': '1.0.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}'}]}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'packages_count': 176998, 'packageversions_count': 1000, 'sample_packages': [{'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'Name': '@eclipsejs/cli', 'Version': '1.0.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}'}], 'sample_packageversions': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectName': 'dataminingsupply/dms-io'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectName': 'isacvale/fc'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectName': 'laihaojie/jie'}]}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'packages_shape': [176998, 4], 'pkgversions_shape': [597602, 4], 'packages_columns': ['Name', 'Version', 'Licenses', 'VersionInfo'], 'pkgversions_columns': ['System', 'Name', 'Version', 'ProjectName'], 'sample_packages': [{'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}], 'sample_pkgversions': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectName': 'dataminingsupply/dms-io'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectName': 'isacvale/fc'}]}, 'var_functions.query_db:20': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.'}], 'var_functions.query_db:22': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.'}, {'Project_Information': 'The project is hosted on GitHub under the name learnfrontend-dc/product-cart, and it currently has 2 open issues. It has garnered a total of 11 stars and has been forked 12 times.'}, {'Project_Information': 'The GitHub project ledgerproject/keypairoom currently has 3 open issues, 3 stars, and 0 forks.'}, {'Project_Information': 'The project leebyron/jasmine-check is hosted on GitHub and currently has 0 open issues, 11 stars, and 3 forks.'}, {'Project_Information': 'The project leebyron/testcheck-js on GitHub has an open issues count of 29, a stars count of 1185, and a forks count of 58, making it a notable repository in the community.'}, {'Project_Information': 'The project leecade/react-native-swiper is hosted on GitHub and has a total of 786 open issues, along with an impressive 10,249 stars and 2,392 forks, making it a popular choice among developers for implementing swiping functionality in React Native applications.'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'total_packages': 176998, 'total_pkgversions': 597602, 'total_projects': 669, 'sample_merged': [{'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}', 'key': '@discue/ui-components|0.13.0', 'System': 'NPM', 'Name_pkg': '@discue/ui-components', 'Version_pkg': '0.13.0', 'ProjectName': 'discue/ui-components'}, {'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}', 'key': '@dvcol/web-extension-utils|1.1.1', 'System': 'NPM', 'Name_pkg': '@dvcol/web-extension-utils', 'Version_pkg': '1.1.1', 'ProjectName': 'dvcol/web-extension-utils'}, {'Name': '@eclipsejs/cli', 'Version': '1.0.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}', 'key': '@eclipsejs/cli|1.0.0', 'System': 'NPM', 'Name_pkg': '@eclipsejs/cli', 'Version_pkg': '1.0.0', 'ProjectName': 'dlesage25/eclipse-cli'}], 'unique_projects_in_merged': 5477, 'sample_project_info': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'ForkCount': 0, 'RepoName': 'lberrocal/npm-packages-template'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'ForkCount': 5782, 'RepoName': 'leaflet/leaflet'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'ForkCount': 118, 'RepoName': 'leaflet/leaflet.fullscreen'}], 'nonzero_forks': 429}}

exec(code, env_args)
