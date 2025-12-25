code = """import json

# Load data
with open(locals()['var_function-call-10728563634535047619'], 'r') as f:
    data = json.load(f)
    relevant_packages_set = set(data['relevant_packages'])
    package_to_project = data['package_to_project']

with open(locals()['var_function-call-14099074286049646692'], 'r') as f:
    parsed_info = json.load(f)
    project_stars = parsed_info['project_stars']

with open(locals()['var_function-call-1085841354208842563'], 'r') as f:
    package_rows = json.load(f)

# 1. Group by Name to find latest version
# We only care about packages in relevant_packages_set
package_max_time = {}
package_latest_version = {}

for row in package_rows:
    name = row['Name']
    if name not in relevant_packages_set:
        continue
        
    version = row['Version']
    try:
        ts = float(row['UpstreamPublishedAt'])
    except:
        ts = 0.0
        
    if name not in package_max_time or ts > package_max_time[name]:
        package_max_time[name] = ts
        package_latest_version[name] = version

# 2. Link to Stars
results = []
for pkg_name, version in package_latest_version.items():
    proj_name = package_to_project.get(pkg_name)
    if proj_name:
        stars = project_stars.get(proj_name, 0)
        results.append({
            "Package": pkg_name,
            "Version": version,
            "Project": proj_name,
            "Stars": stars
        })

# 3. Sort by stars
results.sort(key=lambda x: x['Stars'], reverse=True)

# 4. Top 5
top_5 = results[:5]

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-16797402016528186588': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'UpstreamPublishedAt': '1699345351000000.0'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}', 'UpstreamPublishedAt': '1670271173000000.0'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}', 'UpstreamPublishedAt': '1654791421000000.0'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}', 'UpstreamPublishedAt': '1624260093000000.0'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}', 'UpstreamPublishedAt': '1656518476000000.0'}], 'var_function-call-16797402016528183559': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-16797402016528184626': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_function-call-4617755983227880318': [{'column_name': 'Project_Information', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Licenses', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Homepage', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OSSFuzz', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-8077350152332979729': [{'COUNT(*)': '661372'}], 'var_function-call-8077350152332977860': [{'count_star()': '770'}], 'var_function-call-2611174948222811424': [{'count_star()': '597602'}], 'var_function-call-17690710326741471451': 'file_storage/function-call-17690710326741471451.json', 'var_function-call-14099074286049646692': 'file_storage/function-call-14099074286049646692.json', 'var_function-call-12865363144215804574': 'file_storage/function-call-12865363144215804574.json', 'var_function-call-1184373776930898268': 'file_storage/function-call-1184373776930898268.json', 'var_function-call-10728563634535047619': 'file_storage/function-call-10728563634535047619.json', 'var_function-call-15015072818511019238': 'file_storage/function-call-15015072818511019238.json', 'var_function-call-1085841354208842563': 'file_storage/function-call-1085841354208842563.json'}

exec(code, env_args)
