code = """import json
import re

# Load data
package_path = locals()['var_functions.query_db:0']
project_mapping_path = locals()['var_functions.query_db:9']

with open(package_path, 'r') as f:
    packages = json.load(f)

with open(project_mapping_path, 'r') as f:
    project_mappings = json.load(f)

# Create lookup dictionaries for efficient matching
# Package key: (System, Name, Version) -> package
package_dict = {(p['System'], p['Name'], p['Version']): p for p in packages}

# Filter project mappings to only include NPM GITHUB projects that match our packages
# and create ProjectName -> package mappings
project_to_packages = {}
matched_count = 0
for mapping in project_mappings:
    key = (mapping['System'], mapping['Name'], mapping['Version'])
    if key in package_dict:
        project_name = mapping['ProjectName']
        if project_name not in project_to_packages:
            project_to_packages[project_name] = []
        project_to_packages[project_name].append(package_dict[key])
        matched_count += 1

print('__RESULT__:')
print(json.dumps({
    'total_packages_with_mit_license_and_release': len(packages),
    'total_npm_projects': len(project_mappings),
    'matched_projects': len(project_to_packages),
    'matched_package_versions': matched_count
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'count': 176998, 'first_3_records': [{'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'System': 'NPM', 'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'System': 'NPM', 'Name': '@eclipsejs/cli', 'Version': '1.0.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}'}]}, 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:8': {'package_count': 176998, 'project_count': 591699, 'sample_package': {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, 'sample_project': {'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectName': 'dataminingsupply/dms-io'}}, 'var_functions.query_db:10': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]'}]}

exec(code, env_args)
