code = """import json

# Load parsed projects (ProjectName, Forks, Licenses)
path_projects = locals()['var_function-call-18121043840044295917']
with open(path_projects, 'r') as f:
    all_projects = json.load(f)

# Filter for MIT
mit_projects_map = {}
for p in all_projects:
    if 'MIT' in p.get('Licenses', ''):
        mit_projects_map[p['ProjectName']] = p['Forks']

mit_project_names = set(mit_projects_map.keys())

# Load project_packageversion (Name, Version, ProjectName)
path_ppv = locals()['var_function-call-2837916796279180854']
with open(path_ppv, 'r') as f:
    ppv_data = json.load(f)

# Filter ppv to keep only MIT projects
# And build a set of (Name, Version) candidates
candidate_packages = set()
candidate_package_to_project = {}

for row in ppv_data:
    p_name = row['ProjectName']
    if p_name in mit_project_names:
        pkg_key = (row['Name'], row['Version'])
        candidate_packages.add(pkg_key)
        # Store mapping. One package version maps to one project usually.
        candidate_package_to_project[pkg_key] = p_name

# Load packageinfo (Name, Version) - these are releases
path_pkg = locals()['var_function-call-2837916796279180229']
with open(path_pkg, 'r') as f:
    pkg_data = json.load(f)

# Check which candidates are releases
released_projects = set()

for row in pkg_data:
    pkg_key = (row['Name'], row['Version'])
    if pkg_key in candidate_package_to_project:
        p_name = candidate_package_to_project[pkg_key]
        released_projects.add(p_name)

# Now retrieve forks for released_projects and sort
result_list = []
for p_name in released_projects:
    forks = mit_projects_map[p_name]
    result_list.append({'ProjectName': p_name, 'Forks': forks})

# Sort by Forks desc
result_list.sort(key=lambda x: x['Forks'], reverse=True)

# Get top 5
top_5 = [x['ProjectName'] for x in result_list[:5]]

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-3274994336544418363': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'Licenses': '[\n  "ISC"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_function-call-3274994336544419364': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_function-call-3274994336544416269': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-6768500076049649554': 'file_storage/function-call-6768500076049649554.json', 'var_function-call-2393682192099088018': [{'count_star()': '597602'}], 'var_function-call-2393682192099088175': [{'count_star()': '770'}], 'var_function-call-16469042340273471507': 'file_storage/function-call-16469042340273471507.json', 'var_function-call-16469042340273473368': [{'count(*)': '337844'}], 'var_function-call-18121043840044295917': 'file_storage/function-call-18121043840044295917.json', 'var_function-call-18040209124635840306': 'file_storage/function-call-18040209124635840306.json', 'var_function-call-902577907771911571': 'file_storage/function-call-902577907771911571.json', 'var_function-call-2837916796279180854': 'file_storage/function-call-2837916796279180854.json', 'var_function-call-2837916796279180229': 'file_storage/function-call-2837916796279180229.json'}

exec(code, env_args)
