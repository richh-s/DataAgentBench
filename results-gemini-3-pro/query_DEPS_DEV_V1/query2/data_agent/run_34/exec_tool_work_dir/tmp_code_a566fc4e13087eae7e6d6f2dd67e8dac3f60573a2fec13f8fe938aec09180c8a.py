code = """import pandas as pd
import json
import re

# Load project info
try:
    with open(locals()['var_function-call-6610772750931230598'], 'r') as f:
        project_info_list = json.load(f)
except Exception as e:
    print(f"Error loading project info: {e}")
    project_info_list = []

project_metrics = {} # Name -> ForkCount

# Regex patterns
# Pattern for name: look for owner/repo
# Pattern for forks: look for number followed by forks
fork_pattern1 = re.compile(r"([\d,]+)\s+forks")
fork_pattern2 = re.compile(r"forks\s+count\s+of\s+([\d,]+)")
fork_pattern3 = re.compile(r"forked\s+([\d,]+)\s+times")

for entry in project_info_list:
    text = entry.get('Project_Information', '')
    if not text:
        continue
        
    # Extract Name heuristic: find token with single slash
    tokens = text.split()
    pname = None
    for t in tokens:
        # Remove trailing punctuation
        t_clean = t.rstrip(',.')
        if '/' in t_clean and 'http' not in t_clean and 'github.com' not in t_clean:
            if t_clean.count('/') == 1:
                # Validate parts are not empty
                parts = t_clean.split('/')
                if parts[0] and parts[1]:
                    pname = t_clean
                    break
    
    if not pname:
        continue 
        
    # Extract Fork Count
    forks = 0
    m1 = fork_pattern1.search(text)
    m2 = fork_pattern2.search(text)
    m3 = fork_pattern3.search(text)
    
    match = m1 or m2 or m3
    if match:
        try:
            forks = int(match.group(1).replace(',', ''))
        except:
            forks = 0
            
    project_metrics[pname] = forks

# Load project_packageversion
try:
    with open(locals()['var_function-call-16476595549001256447'], 'r') as f:
        ppv_list = json.load(f)
except Exception as e:
    print(f"Error loading ppv: {e}")
    ppv_list = []

# Map (Name, Version) -> ProjectName
# Only if ProjectName is in our metrics map (optimization)
relevant_projects = set(project_metrics.keys())
pkg_to_proj = {}

for p in ppv_list:
    # Normalize project name to lower case for comparison? 
    # Let's try exact match first.
    p_name = p.get('ProjectName')
    if p_name in relevant_projects:
        pkg_to_proj[(p['Name'], p['Version'])] = p_name

# Load packageinfo
try:
    with open(locals()['var_function-call-16512660750992326138'], 'r') as f:
        pkg_list = json.load(f)
except Exception as e:
    print(f"Error loading pkg list: {e}")
    pkg_list = []

valid_projects = set()

for p in pkg_list:
    name = p['Name']
    ver = p['Version']
    
    if (name, ver) not in pkg_to_proj:
        continue
        
    # Check License strict
    try:
        lic_str = p.get('Licenses', '[]')
        licenses = json.loads(lic_str)
        has_mit = False
        if isinstance(licenses, list):
            if 'MIT' in licenses:
                has_mit = True
        elif isinstance(licenses, str):
            if licenses == 'MIT':
                has_mit = True
        
        if not has_mit:
            continue
    except:
        continue
        
    # Check IsRelease
    try:
        vinfo_str = p.get('VersionInfo', '{}')
        vinfo = json.loads(vinfo_str)
        if not vinfo.get('IsRelease'):
            continue
    except:
        continue
        
    # If passed
    valid_projects.add(pkg_to_proj[(name, ver)])

# Result
final_results = []
for proj in valid_projects:
    final_results.append({'Project': proj, 'Forks': project_metrics[proj]})

final_results.sort(key=lambda x: x['Forks'], reverse=True)

print("__RESULT__:")
print(json.dumps([x['Project'] for x in final_results[:5]]))"""

env_args = {'var_function-call-13043447049557031291': ['project_info', 'project_packageversion'], 'var_function-call-9971134601992494114': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'Licenses': '[\n  "ISC"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_function-call-4732461387766603144': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_function-call-2474656492981176762': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-1835354971108125986': [{'COUNT(*)': '661372'}], 'var_function-call-9618436193157485648': [{'count_star()': '597602'}], 'var_function-call-18212815619311910110': [{'count_star()': '770'}], 'var_function-call-6610772750931230598': 'file_storage/function-call-6610772750931230598.json', 'var_function-call-16476595549001256447': 'file_storage/function-call-16476595549001256447.json', 'var_function-call-16512660750992326138': 'file_storage/function-call-16512660750992326138.json'}

exec(code, env_args)
