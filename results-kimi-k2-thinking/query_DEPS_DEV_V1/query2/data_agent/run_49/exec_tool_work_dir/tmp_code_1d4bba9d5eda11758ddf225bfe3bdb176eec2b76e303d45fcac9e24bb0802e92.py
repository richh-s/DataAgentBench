code = """import json
import re

# Read project_info data
with open(locals()['var_functions.query_db:6'], 'r') as f:
    project_info_data = json.load(f)

# Extract fork counts
project_forks = []
fork_pattern = r'(\d+) forks'

for item in project_info_data:
    info = item['Project_Information']
    match = re.search(fork_pattern, info)
    if match:
        forks = int(match.group(1))
        # Extract project name from the text
        # Usually it's "The project <owner/repo> ..."
        name_match = re.search(r'The project ([\w\-]+/[\w\-]+)', info)
        if name_match:
            project_name = name_match.group(1)
            project_forks.append({
                'ProjectName': project_name,
                'Forks': forks,
                'OriginalText': info
            })

# Sort by fork count
top_projects = sorted(project_forks, key=lambda x: x['Forks'], reverse=True)[:10]

print('__RESULT__:')
print(json.dumps({
    'total_projects_with_forks': len(project_forks),
    'top_10_forks': top_projects
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:8': 'Loaded 176998 package records', 'var_functions.execute_python:10': {'project_packageversion_count': 597602, 'project_info_count': 770, 'sample_project_pkg': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectName': 'dataminingsupply/dms-io'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectName': 'isacvale/fc'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectName': 'laihaojie/jie'}], 'sample_project_info': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.'}]}, 'var_functions.execute_python:12': {'packages': 176998, 'project_versions': 597602, 'project_infos': 770}, 'var_functions.execute_python:14': 'Loaded 176998 packages, 597602 project versions, 770 project infos'}

exec(code, env_args)
