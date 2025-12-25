code = """import json
import re

# Load the project info
with open(locals()['var_function-call-1471500386682973587'], 'r') as f:
    project_infos = json.load(f)

projects = []

# Regex for ProjectName
# "The project lberrocal/npm-packages-template is..."
# "The project is hosted on GitHub under the name learnfrontend-dc/product-cart..."
# "The GitHub project ledgerproject/keypairoom currently..."
# "The project named leo-ran/easy-node-server..."

# Combined regex to capture the name
# We look for "project" followed by optional words, then the name (owner/repo).
# The name typically contains a slash.
name_pattern = re.compile(r'(?:project|name)\s+(?:is\s+)?(?:named\s+)?(?:hosted\s+on\s+GitHub\s+under\s+the\s+name\s+)?([a-zA-Z0-9\-\._]+/[a-zA-Z0-9\-\._]+)')

# Regex for Forks
# "and 0 forks"
# "forks count of 988"
# "forked 12 times"
fork_pattern = re.compile(r'(\d+(?:,\d+)*)\s+forks|forks\s+count\s+of\s+(\d+(?:,\d+)*)|forked\s+(\d+(?:,\d+)*)\s+times')

for entry in project_infos:
    info = entry['Project_Information']
    
    # Extract Name
    name_match = name_pattern.search(info)
    project_name = None
    if name_match:
        project_name = name_match.group(1)
        # Clean up trailing punctuation if any (though \w shouldn't match punctuation except . - _)
        project_name = project_name.rstrip('.')
    
    # Extract Forks
    fork_match = fork_pattern.search(info)
    fork_count = 0
    if fork_match:
        # group 1, 2, or 3
        num_str = next((g for g in fork_match.groups() if g is not None), "0")
        fork_count = int(num_str.replace(',', ''))
        
    if project_name:
        projects.append({
            'ProjectName': project_name,
            'ForkCount': fork_count,
            'OriginalInfo': info
        })

# Sort by ForkCount desc
projects.sort(key=lambda x: x['ForkCount'], reverse=True)

# Print top 10 to verify
print("__RESULT__:")
print(json.dumps(projects[:20]))"""

env_args = {'var_function-call-15658495277080614072': [{'count(*)': '0'}], 'var_function-call-14520015677156172560': [{'Licenses': '[\n  "EUPL-1.2"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'Licenses': '[\n  "ISC"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_function-call-14844316716015021897': [{'count(*)': '176998'}], 'var_function-call-5982475280709802701': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.'}], 'var_function-call-6154509699607560829': [{'count_star()': '770'}], 'var_function-call-9861313264739213710': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-1471500386682973587': 'file_storage/function-call-1471500386682973587.json', 'var_function-call-14572250849748707492': ['project_info', 'project_packageversion']}

exec(code, env_args)
