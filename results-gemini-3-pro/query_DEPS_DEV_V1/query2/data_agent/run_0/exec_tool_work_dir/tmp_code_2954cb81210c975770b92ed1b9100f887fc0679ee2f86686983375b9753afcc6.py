code = """import json
import re

# 1. Parse Project Info
project_info_file = locals()['var_function-call-421180672045231177']
with open(project_info_file, 'r') as f:
    project_info_data = json.load(f)

project_forks = {}
name_pattern = re.compile(r"(?:project|named|name)\s+([a-zA-Z0-9_\-\.]+/[a-zA-Z0-9_\-\.]+)")
forks_pattern1 = re.compile(r"(\d+[\d,]*)\s+forks")
forks_pattern2 = re.compile(r"forks count of\s+(\d+[\d,]*)")
forks_pattern3 = re.compile(r"forked\s+(\d+[\d,]*)\s+times")

for entry in project_info_data:
    info = entry.get('Project_Information', '')
    name_match = name_pattern.search(info)
    project_name = None
    if name_match:
        project_name = name_match.group(1).strip().rstrip(',')
    
    fork_count = 0
    f_match1 = forks_pattern1.search(info)
    f_match2 = forks_pattern2.search(info)
    f_match3 = forks_pattern3.search(info)
    
    if f_match1:
        fork_count = int(f_match1.group(1).replace(',', ''))
    elif f_match2:
        fork_count = int(f_match2.group(1).replace(',', ''))
    elif f_match3:
        fork_count = int(f_match3.group(1).replace(',', ''))
        
    if project_name:
        project_forks[project_name] = fork_count

# 2. Process Package Info (MIT and Release)
package_info_file = locals()['var_function-call-9358634597367205821']
with open(package_info_file, 'r') as f:
    package_data = json.load(f)

released_packages = set()
for p in package_data:
    try:
        # Strict License check
        licenses = json.loads(p.get('Licenses', '[]'))
        if 'MIT' not in licenses:
            continue
            
        vi = json.loads(p.get('VersionInfo', '{}'))
        if vi.get('IsRelease') == True:
            released_packages.add((p['Name'], p['Version']))
    except:
        pass

# 3. Process Project Mapping
pp_file = locals()['var_function-call-10523838729228317055']
with open(pp_file, 'r') as f:
    pp_data = json.load(f)

candidate_projects = {}

for row in pp_data:
    name = row.get('Name')
    version = row.get('Version')
    p_name = row.get('ProjectName')
    
    if (name, version) in released_packages:
        if p_name in project_forks:
            # We found a match
            candidate_projects[p_name] = project_forks[p_name]

# 4. Sort and Top 5
sorted_projects = sorted(candidate_projects.items(), key=lambda x: x[1], reverse=True)
top_5 = sorted_projects[:5]

result_list = [p[0] for p in top_5]

print("__RESULT__:")
print(json.dumps(result_list))"""

env_args = {'var_function-call-17213754139236442950': ['packageinfo'], 'var_function-call-17213754139236444897': ['project_info', 'project_packageversion'], 'var_function-call-1918822351202714235': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'Licenses': '[\n  "ISC"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_function-call-1918822351202715212': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_function-call-1918822351202716189': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-15649627940094015412': [{'COUNT(*)': '391228'}], 'var_function-call-15649627940094014791': [{'count_star()': '597602'}], 'var_function-call-15649627940094014170': [{'count_star()': '770'}], 'var_function-call-421180672045231177': 'file_storage/function-call-421180672045231177.json', 'var_function-call-14939327544472257550': 'file_storage/function-call-14939327544472257550.json', 'var_function-call-9599635150417822581': 754, 'var_function-call-16659806926880017442': 'file_storage/function-call-16659806926880017442.json', 'var_function-call-9358634597367205821': 'file_storage/function-call-9358634597367205821.json', 'var_function-call-10523838729228317055': 'file_storage/function-call-10523838729228317055.json', 'var_function-call-12495425520773648543': ['mui-org/material-ui', 'moment/moment', 'lodash/lodash', 'semantic-org/semantic-ui', 'react-native-elements/react-native-elements'], 'var_function-call-8348421500948450907': [['mui-org/material-ui', 30522], ['moment/moment', 7201], ['lodash/lodash', 7109], ['semantic-org/semantic-ui', 4955], ['react-native-elements/react-native-elements', 4623]]}

exec(code, env_args)
