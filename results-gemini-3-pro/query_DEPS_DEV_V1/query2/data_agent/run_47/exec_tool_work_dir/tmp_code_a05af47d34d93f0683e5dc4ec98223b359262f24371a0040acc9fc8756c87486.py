code = """import json
import re
import pandas as pd

# Load packageinfo result
path_packages = locals()['var_function-call-9214087162642903738']
with open(path_packages, 'r') as f:
    packages_list = json.load(f)

# Load project_packageversion result
path_mappings = locals()['var_function-call-959700558423308150']
with open(path_mappings, 'r') as f:
    mappings_list = json.load(f)

# Load project_info result
path_projects = locals()['var_function-call-959700558423310015']
with open(path_projects, 'r') as f:
    projects_list = json.load(f)

# 1. Create set of valid (Name, Version)
valid_pkg_set = set()
for p in packages_list:
    valid_pkg_set.add((p['Name'], p['Version']))

# 2. Filter mappings to find valid ProjectNames
valid_projects = set()
for m in mappings_list:
    if (m['Name'], m['Version']) in valid_pkg_set:
        valid_projects.add(m['ProjectName'])

# 3. Parse project_info
parsed_projects = []
for p in projects_list:
    info = p['Project_Information']
    # Extract Name
    # Patterns observed:
    # "The project lberrocal/npm-packages-template is hosted..."
    # "The project is hosted on GitHub under the name learnfrontend-dc/product-cart..."
    # "The GitHub project ledgerproject/keypairoom currently..."
    # "The project named leofelix077/bunchofnothing on GitHub..."
    
    name_match = re.search(r"The (?:GitHub )?project (?:is hosted on GitHub under the name |named )?([^\s,]+)", info)
    
    if name_match:
        name = name_match.group(1)
        # Remove trailing 's if accidentally matched "project's"? No, regex [^\s]+ handles it usually unless punctuation.
        # But wait, "project named X on GitHub".
        # If pattern is "The project named X on GitHub", name is X.
        
        # Refine regex:
        # 1. "The project X is..."
        # 2. "The project X on GitHub..."
        # 3. "The project is hosted on GitHub under the name X..."
        # 4. "The GitHub project X currently..."
        # 5. "The GitHub project named X currently..."
        
        # Let's clean the name if it has trailing punctuation?
        # The regex [^\s,]+ excludes commas but might include dots if at end of sentence? 
        # But usually name is followed by "is" or "on" or "currently".
        
        # Check fork count
        # Patterns: 
        # "... and 5782 forks,"
        # "... forks count of 988."
        # "... and 0 forks."
        
        forks_match = re.search(r"(\d+(?:,\d+)*) forks", info)
        forks_match2 = re.search(r"forks count of (\d+(?:,\d+)*)", info)
        
        forks = 0
        if forks_match:
            forks = int(forks_match.group(1).replace(',', ''))
        elif forks_match2:
            forks = int(forks_match2.group(1).replace(',', ''))
            
        parsed_projects.append({'ProjectName': name, 'Forks': forks})

# 4. Filter parsed projects by valid_projects
final_list = []
for p in parsed_projects:
    if p['ProjectName'] in valid_projects:
        final_list.append(p)

# 5. Sort
final_list.sort(key=lambda x: x['Forks'], reverse=True)

print("__RESULT__:")
print(json.dumps(final_list[:10]))"""

env_args = {'var_function-call-10891024517374253840': ['project_info', 'project_packageversion'], 'var_function-call-10891024517374251209': ['packageinfo'], 'var_function-call-13453572739538398591': [{'column_name': 'Project_Information', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Licenses', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Homepage', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OSSFuzz', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-13453572739538398584': [{'column_name': 'System', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Name', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Version', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'ProjectType', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'ProjectName', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'RelationProvenance', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'RelationType', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-13453572739538398577': [{'cid': '0', 'name': 'System', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '1', 'name': 'Name', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '2', 'name': 'Version', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '3', 'name': 'Licenses', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '4', 'name': 'Links', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '5', 'name': 'Advisories', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '6', 'name': 'VersionInfo', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '7', 'name': 'Hashes', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '8', 'name': 'DependenciesProcessed', 'type': 'INTEGER', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '9', 'name': 'DependencyError', 'type': 'INTEGER', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '10', 'name': 'UpstreamPublishedAt', 'type': 'REAL', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '11', 'name': 'Registries', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '12', 'name': 'SLSAProvenance', 'type': 'REAL', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '13', 'name': 'UpstreamIdentifiers', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '14', 'name': 'Purl', 'type': 'REAL', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}], 'var_function-call-5250516404492133489': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'Licenses': '[\n  "ISC"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_function-call-5250516404492135700': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-5250516404492133815': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_function-call-9214087162642903738': 'file_storage/function-call-9214087162642903738.json', 'var_function-call-9954226891964078564': [{'count_star()': '597602'}], 'var_function-call-14552565389635943591': [{'count_star()': '770'}], 'var_function-call-959700558423308150': 'file_storage/function-call-959700558423308150.json', 'var_function-call-959700558423310015': 'file_storage/function-call-959700558423310015.json'}

exec(code, env_args)
