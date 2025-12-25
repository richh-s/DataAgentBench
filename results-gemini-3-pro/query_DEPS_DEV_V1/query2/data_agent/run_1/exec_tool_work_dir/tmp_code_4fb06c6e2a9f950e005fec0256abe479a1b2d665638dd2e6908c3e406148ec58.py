code = """import json
import re

with open(locals()['var_function-call-8269337059431774859'], 'r') as f:
    project_info_list = json.load(f)

projects = []
for p in project_info_list:
    text = p.get('Project_Information', '')
    licenses_str = p.get('Licenses', '[]')
    try:
        licenses = json.loads(licenses_str)
    except:
        licenses = []
    
    if 'MIT' not in licenses:
        continue
        
    name = None
    # "The project NAME is..."
    # "The project NAME on GitHub..."
    # "The GitHub project NAME currently..."
    # "The project named NAME on GitHub..."
    # "The project is hosted on GitHub under the name NAME, ..."
    
    # Improved regex for name
    # Look for patterns that precede the name
    match = re.search(r'(?:The (?:GitHub )?project (?:named )?|under the name )([^\s,]+)(?: on GitHub|, which)?', text)
    if match:
        name = match.group(1)
        # Clean up trailing punctuation if any (though regex excludes comma)
        if name.endswith('.'): name = name[:-1]
    
    if not name:
        continue
        
    forks = 0
    # Handle commas in numbers
    # "30,522 forks"
    # "forks count of 988"
    # "forked 12 times"
    
    fork_match = re.search(r'([\d,]+) forks?', text)
    if fork_match:
        forks_str = fork_match.group(1).replace(',', '')
        if forks_str.isdigit():
            forks = int(forks_str)
    else:
        fork_match = re.search(r'forks count of ([\d,]+)', text)
        if fork_match:
            forks_str = fork_match.group(1).replace(',', '')
            if forks_str.isdigit():
                forks = int(forks_str)
        else:
            fork_match = re.search(r'forked ([\d,]+) times', text)
            if fork_match:
                forks_str = fork_match.group(1).replace(',', '')
                if forks_str.isdigit():
                    forks = int(forks_str)
    
    projects.append({'ProjectName': name, 'Forks': forks})

projects.sort(key=lambda x: x['Forks'], reverse=True)

# Keep top 50 to verify releases
print("__RESULT__:")
print(json.dumps(projects[:50]))"""

env_args = {'var_function-call-3436161164968496315': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'Licenses': '[\n  "ISC"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}, {'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}'}, {'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'Name': '@dxos/client', 'Version': '2.28.20-dev.a2e143d3', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 1514\n}'}, {'Name': '@edgedev/firebase', 'Version': '1.0.12', 'Licenses': '[\n  "ISC"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}'}, {'Name': '@eden-network/data', 'Version': '1.0.9-sev.5', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 14\n}'}], 'var_function-call-2177733471281710808': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-9342949852591978240': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_function-call-9156077512885907759': [{'count(*)': '176998'}], 'var_function-call-2788890825204551107': [{'count_star()': '770'}], 'var_function-call-8269337059431774859': 'file_storage/function-call-8269337059431774859.json', 'var_function-call-10130397877091586317': 'file_storage/function-call-10130397877091586317.json'}

exec(code, env_args)
