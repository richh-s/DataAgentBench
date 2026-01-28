code = """import json
import pandas as pd
import re

# Read data from files
with open(locals()['var_functions.query_db:18'], 'r') as f:
    package_data = json.load(f)

with open(locals()['var_functions.query_db:26'], 'r') as f:
    project_pv_data = json.load(f)

# Convert to DataFrames
df_packages = pd.DataFrame(package_data)
df_project_pv = pd.DataFrame(project_pv_data)

# Filter for MIT license and release versions
mit_release_packages = []
for _, row in df_packages.iterrows():
    try:
        licenses = json.loads(row['Licenses'])
        version_info = json.loads(row['VersionInfo'])
        if 'MIT' in licenses and version_info.get('IsRelease', False):
            mit_release_packages.append({
                'System': row['System'],
                'Name': row['Name'],
                'Version': row['Version']
            })
    except:
        continue

mit_df = pd.DataFrame(mit_release_packages)

# Merge with project_packageversion
merged = pd.merge(
    mit_df, 
    df_project_pv, 
    on=['System', 'Name', 'Version'], 
    how='inner'
)

# Get unique projects (by ProjectName)
unique_projects = merged.drop_duplicates(subset=['ProjectName'])

print('__RESULT__:')
print(json.dumps({
    'mit_release_packages': len(mit_df),
    'matching_projects': len(merged),
    'unique_projects': len(unique_projects),
    'sample_projects': unique_projects.head(10).to_dict('records')
}))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': {'total_mit_release_packages': 330, 'unique_packages': 145, 'sample_packages': [{'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0'}, {'System': 'NPM', 'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1'}, {'System': 'NPM', 'Name': '@eclipsejs/cli', 'Version': '1.0.0'}, {'System': 'NPM', 'Name': '@ebot7/edem-react', 'Version': '0.18.8'}, {'System': 'NPM', 'Name': '@e4a/irmaseal-wasm-bindings', 'Version': '0.0.1'}, {'System': 'NPM', 'Name': '@ebury/chameleon-components', 'Version': '0.1.103'}, {'System': 'NPM', 'Name': '@e-group/material-form', 'Version': '7.39.13'}, {'System': 'NPM', 'Name': '@e-group/material-layout', 'Version': '3.4.5'}, {'System': 'NPM', 'Name': '@dspworkplace/ui', 'Version': '1.0.8'}, {'System': 'NPM', 'Name': '@ditojs/router', 'Version': '0.96.0'}]}, 'var_functions.list_db:16': ['project_info', 'project_packageversion'], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_functions.execute_python:24': {'packages_count': 391228, 'project_pv_count': 5, 'package_columns': ['System', 'Name', 'Version', 'Licenses', 'VersionInfo'], 'project_pv_columns': ['System', 'Name', 'Version', 'ProjectType', 'ProjectName', 'RelationProvenance', 'RelationType']}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
