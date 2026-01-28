code = """import json
import re

# Load MIT release packages
mit_packages_file = locals()['var_functions.query_db:50']
with open(mit_packages_file, 'r') as f:
    mit_packages = json.load(f)

# Load project mappings
project_mappings_file = locals()['var_functions.query_db:38']
with open(project_mappings_file, 'r') as f:
    project_mappings = json.load(f)

# Load project info
project_info_file = locals()['var_functions.query_db:48']
with open(project_info_file, 'r') as f:
    project_info_raw = json.load(f)

# Parse project info to extract repo name and fork counts
project_forks = {}
for item in project_info_raw:
    info = item.get('Info', '')
    
    # Extract repo name 
    repo_name = None
    patterns = [
        r'project\s+([\w\-\.]+/[\w\-\.]+)\s+on\s+GitHub',
        r'project\s+([\w\-\.]+/[\w\-\.]+)\s+is\s+hosted',
        r'repository\s+([\w\-\.]+/[\w\-\.]+)\s+on\s+GitHub',
        r'named\s+([\w\-\.]+/[\w\-\.]+)\s+on\s+GitHub'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, info, re.IGNORECASE)
        if match:
            repo_name = match.group(1)
            break
    
    # Extract fork count
    forks = 0
    fork_match = re.search(r'(\d+(?:,\d+)*)\s+forks?\b', info, re.IGNORECASE)
    if fork_match:
        forks_str = fork_match.group(1).replace(',', '')
        try:
            forks = int(forks_str)
        except:
            forks = 0
    
    if repo_name:
        project_forks[repo_name] = forks

# Debug: Check sample project mappings
print('__RESULT__:')
print(json.dumps({
    'total_mit_packages': len(mit_packages),
    'sample_packages': mit_packages[:3],
    'total_mappings': len(project_mappings),
    'sample_mappings': project_mappings[:3],
    'total_projects_with_forks': len(project_forks),
    'sample_project_forks': dict(list(project_forks.items())[:3])
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:7': {'packages_count': 100, 'projects_count': 100}, 'var_functions.execute_python:12': {'total_packages': 100, 'npm_packages': 100, 'mit_release_packages': 0, 'sample': []}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:18': ['project_info', 'project_packageversion'], 'var_functions.query_db:20': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_functions.query_db:22': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectName': 'dataminingsupply/dms-io'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectName': 'isacvale/fc'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectName': 'laihaojie/jie'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:32': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectName': 'dataminingsupply/dms-io'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectName': 'isacvale/fc'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.10', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.17', 'ProjectName': 'laihaojie/jie'}, {'System': 'NPM', 'Name': '@dlcs/ng', 'Version': '1.0.0', 'ProjectName': 'winup/dlcs-ng'}, {'System': 'NPM', 'Name': '@dms/cli', 'Version': '1.0.1', 'ProjectName': 'dataminingsupply/dms-cli'}, {'System': 'NPM', 'Name': '@dms/cli', 'Version': '1.0.0', 'ProjectName': 'dataminingsupply/dms-cli'}], 'var_functions.execute_python:36': {'count': 176998, 'sample': [{'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'System': 'NPM', 'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}]}, 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:42': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_functions.execute_python:46': {'mit_packages_count': 176998, 'project_mappings_count': 597602}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:52': [{'count': '597602'}], 'var_functions.execute_python:54': {'total_projects_with_forks': 0, 'top_10_projects': []}, 'var_functions.execute_python:56': {'sample_items': [{'Info': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'Info': 'The project libertydsnp/activity-content on GitHub currently has 1 open issue, 1 star, and 0 forks.'}, {'Info': 'The project libertyequalitydata/dynamic-data is hosted on GitHub and currently has 0 open issues, 31 stars, and 11 forks.'}, {'Info': 'The project ljharb/has-symbols on GitHub currently has 1 open issue, 14 stars, and 3 forks.'}, {'Info': 'The project lohfu/domp-create is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}], 'total_items': 770}, 'var_functions.execute_python:58': {'total_packages_processed': 176998, 'total_projects_found': 0, 'top_5_projects': []}}

exec(code, env_args)
