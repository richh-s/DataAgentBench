code = """import json
import re

# Load project_info
with open(locals()['var_function-call-4237171323808415774'], 'r') as f:
    project_info_data = json.load(f)

project_map = {}
for entry in project_info_data:
    info = entry.get('Project_Information', '')
    name = None
    name_patterns = [
        r"The project ([a-zA-Z0-9_\-\.]+/[a-zA-Z0-9_\-\.]+) (is|on|currently|has)",
        r"The GitHub project ([a-zA-Z0-9_\-\.]+/[a-zA-Z0-9_\-\.]+) currently",
        r"The project is hosted on GitHub under the name ([a-zA-Z0-9_\-\.]+/[a-zA-Z0-9_\-\.]+),",
        r"The project named ([a-zA-Z0-9_\-\.]+/[a-zA-Z0-9_\-\.]+) (is|on|currently)",
        r"The GitHub project named ([a-zA-Z0-9_\-\.]+/[a-zA-Z0-9_\-\.]+) currently"
    ]
    for pat in name_patterns:
        m = re.search(pat, info)
        if m:
            name = m.group(1)
            break
    
    stars = 0
    star_patterns = [
        r" (\d{1,3}(?:,\d{3})*|\d+) stars",
        r"stars count of (\d{1,3}(?:,\d{3})*|\d+)"
    ]
    for pat in star_patterns:
        m = re.search(pat, info)
        if m:
            s_str = m.group(1).replace(',', '')
            stars = int(s_str)
            break
            
    if name:
        project_map[name] = stars

# Load project_packageversion
with open(locals()['var_function-call-1592086679515618240'], 'r') as f:
    pp_data = json.load(f)

# Filter
filtered_packages = []
unique_names = set()

for row in pp_data:
    pname = row.get('ProjectName')
    if pname in project_map:
        filtered_packages.append(row)
        unique_names.add(row.get('Name'))

# Output
result = {
    "unique_names": list(unique_names),
    "candidate_packages_count": len(filtered_packages)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-5406566919456308796': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'UpstreamPublishedAt': '1699345351000000.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'UpstreamPublishedAt': '1670271173000000.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'UpstreamPublishedAt': '1654791421000000.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'UpstreamPublishedAt': '1624260093000000.0', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'Name': '@discue/ui-components', 'Version': '0.13.0', 'UpstreamPublishedAt': '1656518476000000.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_function-call-5406566919456308857': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-5406566919456308918': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_function-call-11390147187098348839': [{'COUNT(*)': '661372'}], 'var_function-call-11390147187098345998': [{'count_star()': '597602'}], 'var_function-call-11390147187098347253': [{'count_star()': '770'}], 'var_function-call-4237171323808415774': 'file_storage/function-call-4237171323808415774.json', 'var_function-call-7699301061311368426': 'file_storage/function-call-7699301061311368426.json', 'var_function-call-7818665909907823651': 'file_storage/function-call-7818665909907823651.json', 'var_function-call-1592086679515618240': 'file_storage/function-call-1592086679515618240.json'}

exec(code, env_args)
