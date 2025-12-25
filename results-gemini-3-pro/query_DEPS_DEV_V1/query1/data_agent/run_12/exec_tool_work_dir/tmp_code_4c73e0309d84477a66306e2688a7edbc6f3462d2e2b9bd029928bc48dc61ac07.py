code = """import json
import re

# Load project info
with open('var_function-call-17690710326741471451.json', 'r') as f:
    project_info_list = json.load(f)

project_stars = {}
project_names = []

# Regex to capture project name and stars
# Examples:
# "The project lberrocal/npm-packages-template is hosted..." -> lberrocal/npm-packages-template
# "The project leaflet/leaflet on GitHub..." -> leaflet/leaflet
# "The project named leo-ran/easy-node-server is hosted..." -> leo-ran/easy-node-server
# "... has 0 stars ..."
# "... stars count of 3761 ..."
# "... a stars count of 1185 ..."
# "... 10,249 stars ..."

# Refined Regex
# Name: `project (?:named |is hosted on GitHub under the name )?([a-zA-Z0-9\-\._]+/[a-zA-Z0-9\-\._]+)`
# Stars: `(\d{1,3}(?:,\d{3})*|\d+) stars` OR `stars count of (\d{1,3}(?:,\d{3})*|\d+)`

name_pattern = re.compile(r"project (?:is hosted on GitHub under the name |named )?([a-zA-Z0-9\-\._]+/[a-zA-Z0-9\-\._]+)")
stars_pattern1 = re.compile(r"(\d{1,3}(?:,\d{3})*|\d+) stars")
stars_pattern2 = re.compile(r"stars count of (\d{1,3}(?:,\d{3})*|\d+)")

for entry in project_info_list:
    text = entry.get('Project_Information', '')
    
    # Extract Name
    name_match = name_pattern.search(text)
    if name_match:
        p_name = name_match.group(1)
        
        # Extract Stars
        stars = 0
        s_match1 = stars_pattern1.search(text)
        s_match2 = stars_pattern2.search(text)
        
        s_str = "0"
        if s_match1:
            s_str = s_match1.group(1)
        elif s_match2:
            s_str = s_match2.group(1)
            
        stars = int(s_str.replace(',', ''))
        
        project_stars[p_name] = stars
        project_names.append(p_name)

print("__RESULT__:")
print(json.dumps({"project_names": project_names, "project_stars": project_stars}))"""

env_args = {'var_function-call-16797402016528186588': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'UpstreamPublishedAt': '1699345351000000.0'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}', 'UpstreamPublishedAt': '1670271173000000.0'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}', 'UpstreamPublishedAt': '1654791421000000.0'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}', 'UpstreamPublishedAt': '1624260093000000.0'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}', 'UpstreamPublishedAt': '1656518476000000.0'}], 'var_function-call-16797402016528183559': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-16797402016528184626': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_function-call-4617755983227880318': [{'column_name': 'Project_Information', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Licenses', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Homepage', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OSSFuzz', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-8077350152332979729': [{'COUNT(*)': '661372'}], 'var_function-call-8077350152332977860': [{'count_star()': '770'}], 'var_function-call-2611174948222811424': [{'count_star()': '597602'}], 'var_function-call-17690710326741471451': 'file_storage/function-call-17690710326741471451.json'}

exec(code, env_args)
