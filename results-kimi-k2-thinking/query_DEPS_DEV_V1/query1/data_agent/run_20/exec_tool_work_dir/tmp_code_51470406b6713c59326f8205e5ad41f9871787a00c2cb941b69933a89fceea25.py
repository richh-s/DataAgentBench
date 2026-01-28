code = """import json
import re

# Check what we have in storage
print('Storage keys check:')
print('var_functions.query_db:70 type:', type(locals()['var_functions.query_db:70']))
print('var_functions.query_db:66 type:', type(locals()['var_functions.query_db:66']))

# Load data - handle both direct data and file paths
def load_data(storage_var):
    data = locals()[storage_var]
    if isinstance(data, str) and data.endswith('.json'):
        with open(data, 'r') as f:
            return json.load(f)
    return data

package_data = load_data('var_functions.query_db:70')
project_data = load_data('var_functions.query_db:66')

print('Packages loaded: ' + str(len(package_data)))
print('Projects loaded: ' + str(len(project_data)))

# Find latest release version for each package
latest_packages = {}
for pkg in package_data:
    try:
        name = pkg['Name']
        version = pkg['Version']
        ordinal = int(pkg['Ordinal']) if pkg['Ordinal'] else 0
        
        if name not in latest_packages or ordinal > latest_packages[name]['ordinal']:
            latest_packages[name] = {'version': version, 'ordinal': ordinal}
    except Exception as e:
        pass

print('Latest releases count: ' + str(len(latest_packages)))

# Parse star counts from project information  
project_stars = {}
for project in project_data:
    try:
        info = project['Project_Information']
        stars_match = re.search(r'(\d+) stars', info)
        if stars_match:
            stars = int(stars_match.group(1))
            repo_match = re.search(r'project ([^\s]+/[^\s]+)', info)
            if repo_match:
                repo = repo_match.group(1)
                project_stars[repo] = stars
    except Exception as e:
        pass

print('Projects with stars: ' + str(len(project_stars)))

print('__RESULT__:')
result = {
    'latest_packages': len(latest_packages),
    'projects_with_stars': len(project_stars)
}
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:2': ['project_info', 'project_packageversion'], 'var_functions.query_db:5': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_functions.query_db:9': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:36': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': [{'Name': '@discordx/music', 'Version': '6.0.2', 'Ordinal': '213'}, {'Name': '@discordx/music', 'Version': '6.0.2', 'Ordinal': '213'}, {'Name': '@discordx/music', 'Version': '6.0.1', 'Ordinal': '212'}, {'Name': '@discordx/music', 'Version': '6.0.1', 'Ordinal': '212'}, {'Name': '@discordx/music', 'Version': '6.0.0', 'Ordinal': '211'}, {'Name': '@discordx/music', 'Version': '6.0.0', 'Ordinal': '211'}, {'Name': '@discordx/music', 'Version': '5.0.2', 'Ordinal': '209'}, {'Name': '@discordx/music', 'Version': '5.0.2', 'Ordinal': '209'}, {'Name': '@discordx/music', 'Version': '5.0.1', 'Ordinal': '208'}, {'Name': '@discordx/music', 'Version': '5.0.1', 'Ordinal': '208'}], 'var_functions.query_db:42': [{'Name': '@discordx/music', 'Version': '6.0.2', 'Ordinal': '213'}, {'Name': '@discordx/pagination', 'Version': '4.0.0-dev.1670073642.4821b1ea', 'Ordinal': '44'}, {'Name': '@discordx/utilities', 'Version': '6.0.0-dev.1674756406.d6dc0b9d', 'Ordinal': '266'}, {'Name': '@discoteam/vueify', 'Version': '9.4.1', 'Ordinal': '2'}, {'Name': '@discourse/babel-plugin-debug-macros', 'Version': '0.4.0-pre1', 'Ordinal': '1'}], 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json', 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:56': 'file_storage/functions.query_db:56.json', 'var_functions.query_db:64': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}], 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:68': 'file_storage/functions.query_db:68.json', 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json'}

exec(code, env_args)
