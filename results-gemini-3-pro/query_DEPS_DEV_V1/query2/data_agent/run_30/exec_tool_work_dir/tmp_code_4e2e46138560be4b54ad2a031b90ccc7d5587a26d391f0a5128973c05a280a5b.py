code = """import json
import re

# Load project_info
with open(locals()['var_function-call-16500369102885230562'], 'r') as f:
    projects = json.load(f)

# Regex for Project Name
# Formats:
# "The project lberrocal/npm-packages-template ..."
# "The GitHub project ledgerproject/keypairoom ..."
# "The project named leo-ran/easy-node-server ..."
# "The project is hosted on GitHub under the name learnfrontend-dc/product-cart ..."
name_pattern = re.compile(r"^The (?:GitHub )?project (?:is hosted on GitHub under the name |named )?([^\s,]+)")

# Regex for Forks
# Formats:
# "... and 5782 forks"
# "... forks count of 988"
# "... forked 12 times"
forks_pattern_1 = re.compile(r"([\d,]+)\s+forks")
forks_pattern_2 = re.compile(r"forks\s+count\s+of\s+([\d,]+)")
forks_pattern_3 = re.compile(r"forked\s+([\d,]+)\s+times")

parsed_projects = []

for p in projects:
    # Check License first
    # Licenses is a JSON string
    try:
        licenses = json.loads(p.get('Licenses', '[]'))
    except:
        licenses = []
    
    # Check for MIT
    if not any('MIT' in l for l in licenses):
        continue

    text = p.get('Project_Information', '')
    
    # Extract Name
    name_match = name_pattern.match(text)
    if not name_match:
        continue
    project_name = name_match.group(1)
    
    # Extract Forks
    forks = 0
    f1 = forks_pattern_1.search(text)
    f2 = forks_pattern_2.search(text)
    f3 = forks_pattern_3.search(text)
    
    if f1:
        forks = int(f1.group(1).replace(',', ''))
    elif f2:
        forks = int(f2.group(1).replace(',', ''))
    elif f3:
        forks = int(f3.group(1).replace(',', ''))
    
    parsed_projects.append({
        'ProjectName': project_name,
        'Forks': forks,
        'OriginalText': text
    })

# Sort by Forks
parsed_projects.sort(key=lambda x: x['Forks'], reverse=True)

# Return top 20 candidates
print("__RESULT__:")
print(json.dumps(parsed_projects[:20]))"""

env_args = {'var_function-call-14086403419687674887': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'Licenses': '[\n  "ISC"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_function-call-14086403419687676318': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-14086403419687677749': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_function-call-11527240255502869441': [{'count_star()': '770'}], 'var_function-call-5722963796345229615': [{'count_star()': '597602'}], 'var_function-call-16500369102885230562': 'file_storage/function-call-16500369102885230562.json'}

exec(code, env_args)
