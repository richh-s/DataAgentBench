code = """import json
import re

# 1. Parse Project Info
file_path_info = locals()['var_function-call-17095026802948898039']
with open(file_path_info, 'r') as f:
    project_info_list = json.load(f)

project_stars = {}
name_patterns = [
    r"The project ([^\s]+) (?:on GitHub|is hosted on GitHub|is hosted on GITHUB)",
    r"The GitHub project ([^\s]+) currently",
    r"The GitHub project named ([^\s]+) currently",
    r"The project named ([^\s]+) on GitHub",
    r"The project named ([^\s]+) is hosted",
    r"The project is hosted on GitHub under the name ([^\s,]+)",
    r"The project on GitHub, named ([^\s,]+),",
    r"The project ([^\s]+) has"
]
star_pattern = r"(\d+(?:,\d+)*) stars"

for entry in project_info_list:
    text = entry.get('Project_Information', '')
    star_match = re.search(star_pattern, text)
    stars = int(star_match.group(1).replace(',', '')) if star_match else 0
    
    name = None
    for pat in name_patterns:
        match = re.search(pat, text)
        if match:
            name = match.group(1).rstrip(',')
            if '/' in name: break
    if name:
        project_stars[name] = stars

# 2. Map Package -> Stars
file_path_map = locals()['var_function-call-18131054269574121192']
with open(file_path_map, 'r') as f:
    mapping_list = json.load(f)

package_stars = {}

for row in mapping_list:
    pkg = row.get('Name')
    proj = row.get('ProjectName')
    
    if pkg and proj and proj in project_stars:
        stars = project_stars[proj]
        if stars > package_stars.get(pkg, -1):
            package_stars[pkg] = stars

# 3. Top 5
top_packages = sorted(package_stars.items(), key=lambda x: x[1], reverse=True)[:5]

print("__RESULT__:")
print(json.dumps(top_packages))"""

env_args = {'var_function-call-3426217086508878109': ['project_info', 'project_packageversion'], 'var_function-call-14361327731076746203': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}], 'var_function-call-802867660549840356': [{'COUNT(*)': '661372'}], 'var_function-call-17118522439532025906': [{'count_star()': '770'}], 'var_function-call-13698533078275415391': [{'count_star()': '597602'}], 'var_function-call-17095026802948898039': 'file_storage/function-call-17095026802948898039.json', 'var_function-call-2683278215389969689': 'file_storage/function-call-2683278215389969689.json', 'var_function-call-2730800807703072015': 'file_storage/function-call-2730800807703072015.json', 'var_function-call-17651735690782060279': 'file_storage/function-call-17651735690782060279.json', 'var_function-call-10680397873260525171': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1'}, {'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1'}, {'Name': '@discue/ui-components', 'Version': '0.13.0'}], 'var_function-call-9739407454114692563': [{'RelationType': 'ISSUE_TRACKER_TYPE'}, {'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-3178896390383634755': [{'Name': '@dms/io', 'Version': '0.9.0', 'ProjectName': 'dataminingsupply/dms-io'}, {'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectName': 'isacvale/fc'}, {'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectName': 'laihaojie/jie'}, {'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectName': 'laihaojie/jie'}, {'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectName': 'laihaojie/jie'}, {'Name': '@djie/ws', 'Version': '1.0.10', 'ProjectName': 'laihaojie/jie'}, {'Name': '@djie/ws', 'Version': '1.0.17', 'ProjectName': 'laihaojie/jie'}, {'Name': '@dlcs/ng', 'Version': '1.0.0', 'ProjectName': 'winup/dlcs-ng'}, {'Name': '@dms/cli', 'Version': '1.0.1', 'ProjectName': 'dataminingsupply/dms-cli'}, {'Name': '@dms/cli', 'Version': '1.0.0', 'ProjectName': 'dataminingsupply/dms-cli'}], 'var_function-call-18131054269574121192': 'file_storage/function-call-18131054269574121192.json'}

exec(code, env_args)
