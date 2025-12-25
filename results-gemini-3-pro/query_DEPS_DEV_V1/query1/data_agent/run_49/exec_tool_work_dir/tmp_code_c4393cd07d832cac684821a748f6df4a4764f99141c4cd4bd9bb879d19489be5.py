code = """import json
import re
import pandas as pd

# Load data
with open(locals()['var_function-call-8408606139573425985'], 'r') as f:
    latest_npm = json.load(f)

with open(locals()['var_function-call-11116674549221521774'], 'r') as f:
    project_info = json.load(f)

with open(locals()['var_function-call-16988697258105715588'], 'r') as f:
    ppv = json.load(f)

# 1. Parse Project Info
project_stars = {}
for p in project_info:
    info = p.get('Project_Information', '')
    
    # Extract Name
    name_match = re.search(r'The project ([a-zA-Z0-9_\-\.]+/[a-zA-Z0-9_\-\.]+)', info)
    if not name_match:
        name_match = re.search(r'The GitHub project ([a-zA-Z0-9_\-\.]+/[a-zA-Z0-9_\-\.]+)', info)
    if not name_match:
        name_match = re.search(r'under the name ([a-zA-Z0-9_\-\.]+/[a-zA-Z0-9_\-\.]+)', info)
    if not name_match:
        name_match = re.search(r'named ([a-zA-Z0-9_\-\.]+/[a-zA-Z0-9_\-\.]+)', info)
        
    if name_match:
        project_name = name_match.group(1)
        
        # Extract Stars
        # "38715 stars" or "stars count of 3761" or "0 stars"
        stars_match = re.search(r'(\d{1,3}(?:,\d{3})*|\d+)\s+stars', info)
        if not stars_match:
            stars_match = re.search(r'stars count of\s+(\d{1,3}(?:,\d{3})*|\d+)', info)
            
        if stars_match:
            stars_str = stars_match.group(1).replace(',', '')
            stars = int(stars_str)
            project_stars[project_name] = stars

# 2. Build mapping (Name, Version) -> ProjectName
# Only keep if ProjectName is in our parsed list (optimization)
target_projects = set(project_stars.keys())
pkg_ver_to_proj = {}

for row in ppv:
    if row['ProjectName'] in target_projects:
        key = (row['Name'], row['Version'])
        pkg_ver_to_proj[key] = row['ProjectName']

# 3. Match with Latest NPM Packages
results = []
for pkg in latest_npm:
    name = pkg['Name']
    ver = pkg['Version']
    key = (name, ver)
    
    if key in pkg_ver_to_proj:
        proj = pkg_ver_to_proj[key]
        stars = project_stars.get(proj, 0)
        results.append({
            'Package': name,
            'Version': ver,
            'Project': proj,
            'Stars': stars
        })

# 4. Sort
results.sort(key=lambda x: x['Stars'], reverse=True)

print("__RESULT__:")
print(json.dumps(results[:5]))"""

env_args = {'var_function-call-12056711365847256685': ['project_info', 'project_packageversion'], 'var_function-call-17510872982189609110': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-11271508823415308461': [{'count(*)': '661372'}], 'var_function-call-8408606139573425985': 'file_storage/function-call-8408606139573425985.json', 'var_function-call-1728007161148300545': [{'count_star()': '597602'}], 'var_function-call-11322711447800494046': [{'count_star()': '770'}], 'var_function-call-11116674549221521774': 'file_storage/function-call-11116674549221521774.json', 'var_function-call-16988697258105715588': 'file_storage/function-call-16988697258105715588.json'}

exec(code, env_args)
