code = """import json
import re
from collections import defaultdict

# Load MIT packages
mit_file = locals()['var_functions.query_db:48']
with open(mit_file, 'r') as f:
    mit_packages = json.load(f)

# Load project package versions  
ppv_file = locals()['var_functions.query_db:56']
with open(ppv_file, 'r') as f:
    ppv_data = json.load(f)

# Build MIT lookup
mit_lookup = set((pkg['Name'], pkg['Version']) for pkg in mit_packages)

# Find matching projects
project_packages = defaultdict(list)
for pkg in ppv_data:
    if (pkg['Name'], pkg['Version']) in mit_lookup:
        project_packages[pkg['ProjectName']].append(pkg)

projects = list(project_packages.keys())
print('Projects with MIT packages:', len(projects))

# Load project info
info_file = locals()['var_functions.query_db:84']
with open(info_file, 'r') as f:
    project_info = json.load(f)

# Build project info lookup
info_lookup = {}
for entry in project_info:
    text = entry['Project_Information']
    # Extract project name from text
    match = re.search(r'project\s+([a-zA-Z0-9_-]+/[a-zA-Z0-9_-]+)', text)
    if not match:
        match = re.search(r'named\s+([a-zA-Z0-9_-]+/[a-zA-Z0-9_-]+)', text)
    if match:
        proj_name = match.group(1)
        info_lookup[proj_name] = text

# Extract fork counts
fork_pattern = re.compile(r'([\d,]+)\s+forks')
project_forks = {}
for proj in projects:
    if proj in info_lookup:
        text = info_lookup[proj]
        match = fork_pattern.search(text)
        if match:
            forks = int(match.group(1).replace(',', ''))
            project_forks[proj] = forks
        else:
            project_forks[proj] = 0
    else:
        project_forks[proj] = 0

# Get top 5 by forks
top_5 = sorted(project_forks.items(), key=lambda x: x[1], reverse=True)[:5]

# Build result with package info
result = []
for proj, forks in top_5:
    packages = project_packages[proj]
    pkg_names = [p['Name'] for p in packages]
    result.append({
        'rank': len(result) + 1,
        'project': proj,
        'forks': forks,
        'packages': len(packages),
        'samples': pkg_names[:3]
    })

print('Top 5 projects:')
for item in result:
    print('{}. {} - {} forks ({} packages)'.format(item['rank'], item['project'], item['forks'], item['packages']))

final_output = {'top_projects': result}
print('__RESULT__:')
print(json.dumps(final_output))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.list_db:2': ['project_info', 'project_packageversion'], 'var_functions.query_db:5': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'Licenses': '[\n  "ISC"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_functions.query_db:14': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectName': 'dataminingsupply/dms-io'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectName': 'isacvale/fc'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectName': 'laihaojie/jie'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.execute_python:52': {'total': 176998, 'unique_names': 10486}, 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:56': 'file_storage/functions.query_db:56.json', 'var_functions.execute_python:58': {'mit_count': 176998, 'ppv_count': 597602, 'matches': 164782, 'unique_projects': 5477}, 'var_functions.execute_python:62': {'project_count': 5477, 'output_file': '/tmp/project_list.json', 'first_5': ['isacvale/fc', 'winup/dlcs-ng', 'dom-packages/fp', 'lohfu/domp-is', 'march08/duik']}, 'var_functions.query_db:66': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.'}, {'Project_Information': 'The GitHub project ledgerproject/keypairoom currently has 3 open issues, 3 stars, and 0 forks.'}, {'Project_Information': 'The project leebyron/jasmine-check is hosted on GitHub and currently has 0 open issues, 11 stars, and 3 forks.'}, {'Project_Information': 'The project leebyron/testcheck-js on GitHub has an open issues count of 29, a stars count of 1185, and a forks count of 58, making it a notable repository in the community.'}, {'Project_Information': 'The project leecade/react-native-swiper is hosted on GitHub and has a total of 786 open issues, along with an impressive 10,249 stars and 2,392 forks, making it a popular choice among developers for implementing swiping functionality in React Native applications.'}, {'Project_Information': 'The project legendjaden/aftablecolumn on GitHub currently has an open issues count of 35, a stars count of 136, and a forks count of 29.'}, {'Project_Information': 'The project lekoarts/gatsby-themes on GitHub currently has 11 open issues, 1836 stars, and 568 forks, making it a popular choice among developers looking for Gatsby themes.'}, {'Project_Information': 'The GitHub project lenconda/dollie currently has 0 open issues, 12 stars, and 3 forks, making it a noteworthy repository in its category.'}, {'Project_Information': 'The project leo-ran/easy-node-reflect is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks, indicating that it may be in its early stages or not yet widely recognized within the GitHub community.'}, {'Project_Information': 'The project named leo-ran/easy-node-server is hosted on GitHub and currently has an open issues count of 0, stars count of 0, and forks count of 0.'}, {'Project_Information': 'The project named leofelix077/bunchofnothing on GitHub currently has 40 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leoilab/react-native-analytics-segment-io on GitHub currently has 26 open issues, 71 stars, and 36 forks, making it a notable repository for those interested in integrating analytics into React Native applications.'}, {'Project_Information': 'The project on GitHub, named leonardparisi/easy-express-server, currently has an open issues count of 0, a stars count of 0, and a forks count of 0.'}, {'Project_Information': 'The project leoroese/template-cli is hosted on GitHub and currently has 1 open issue, along with a total of 17 stars and 13 forks.'}, {'Project_Information': 'The project is a GitHub repository named letrungdo/react-ui-component-lib, which currently has 0 open issues, 4 stars, and 0 forks.'}, {'Project_Information': 'The project levelkdev/dxswap-sdk on GitHub currently has 27 open issues, 8 stars, and 11 forks, making it a noteworthy resource for developers interested in its functionality and contributions.'}], 'var_functions.execute_python:70': {'project_count': 5477, 'sample_project': 'isacvale/fc'}, 'var_functions.query_db:72': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.'}], 'var_functions.query_db:76': 'file_storage/functions.query_db:76.json', 'var_functions.execute_python:82': {'mit_packages': 176998, 'project_versions': 597602, 'matches': 164782, 'unique_projects': 5477, 'sample': ['isacvale/fc', 'winup/dlcs-ng', 'dom-packages/fp', 'lohfu/domp-is', 'march08/duik']}, 'var_functions.query_db:84': 'file_storage/functions.query_db:84.json'}

exec(code, env_args)
