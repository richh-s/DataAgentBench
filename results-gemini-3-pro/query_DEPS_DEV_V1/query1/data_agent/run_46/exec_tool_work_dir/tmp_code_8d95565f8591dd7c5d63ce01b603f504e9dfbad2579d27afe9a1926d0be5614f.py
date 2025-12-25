code = """import pandas as pd
import json
import re

# Load project_info
try:
    with open(locals()['var_function-call-8338850596070908383'], 'r') as f:
        project_info_data = json.load(f)
except Exception as e:
    print(f"Error loading project_info: {e}")
    project_info_data = []

project_stars = {}
for entry in project_info_data:
    text = entry.get('Project_Information', '')
    
    # Extract Project Name
    name_match = re.search(r'(?:GitHub\s+)?project\s+(?:is\s+hosted\s+on\s+GitHub\s+under\s+the\s+name\s+|on\s+GitHub,?\s+(?:named\s+)?|named\s+|)([A-Za-z0-9\-\._]+/[A-Za-z0-9\-\._]+)', text, re.IGNORECASE)
    
    # Extract Stars
    # Case 1: "1,234 stars"
    # Case 2: "stars count of 1,234"
    stars_match = re.search(r'(?:(\d+(?:,\d+)*)\s+stars|stars\s+count\s+of\s+(\d+(?:,\d+)*))', text, re.IGNORECASE)
    
    if name_match and stars_match:
        p_name = name_match.group(1)
        
        # Determine which group captured the stars
        s1 = stars_match.group(1)
        s2 = stars_match.group(2)
        stars_str = s1 if s1 else s2
        
        if stars_str:
            stars_str = stars_str.replace(',', '')
            try:
                stars = int(stars_str)
                project_stars[p_name] = stars
            except:
                pass

# Load project_packageversion
try:
    with open(locals()['var_function-call-2217359814551860824'], 'r') as f:
        pp_data = json.load(f)
except Exception as e:
    print(f"Error loading project_packageversion: {e}")
    pp_data = []

pkg_ver_to_proj = {}
for row in pp_data:
    key = (row['Name'], row['Version'])
    pkg_ver_to_proj[key] = row['ProjectName']

# Load packageinfo
try:
    with open(locals()['var_function-call-7269832412204370936'], 'r') as f:
        pkg_data = json.load(f)
except Exception as e:
    print(f"Error loading packageinfo: {e}")
    pkg_data = []

# Find latest version for each package
packages = {}
for row in pkg_data:
    name = row['Name']
    ver = row['Version']
    v_info_str = row['VersionInfo']
    try:
        v_info = json.loads(v_info_str)
        is_release = v_info.get('IsRelease', False)
        ordinal = v_info.get('Ordinal', -1)
        
        if is_release:
            if name not in packages:
                packages[name] = (ver, ordinal)
            else:
                current_ver, current_ord = packages[name]
                if ordinal > current_ord:
                    packages[name] = (ver, ordinal)
    except:
        pass

# Match with stars
results = []
for name, (ver, ordinal) in packages.items():
    proj_name = pkg_ver_to_proj.get((name, ver))
    if proj_name:
        stars = project_stars.get(proj_name, 0)
        # Note: Some projects might have 0 stars, but usually we look for "popular" ones.
        # But if the user asks for top 5, we just take the highest.
        results.append({'Name': name, 'Version': ver, 'Stars': stars})

# Sort
results.sort(key=lambda x: x['Stars'], reverse=True)
top5 = results[:5]

print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_function-call-1408542683940284424': [{'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'UpstreamPublishedAt': '1699345351000000.0'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}', 'UpstreamPublishedAt': '1670271173000000.0'}, {'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}', 'UpstreamPublishedAt': '1654791421000000.0'}, {'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}', 'UpstreamPublishedAt': '1624260093000000.0'}, {'Name': '@discue/ui-components', 'Version': '0.13.0', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}', 'UpstreamPublishedAt': '1656518476000000.0'}], 'var_function-call-8292094668782506700': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-15646645973311808053': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_function-call-7914375991274540249': [{'COUNT(*)': '661372'}], 'var_function-call-18401968775269942803': [{'count_star()': '597602'}], 'var_function-call-9328553064761695381': [{'count_star()': '770'}], 'var_function-call-8338850596070908383': 'file_storage/function-call-8338850596070908383.json', 'var_function-call-2217359814551860824': 'file_storage/function-call-2217359814551860824.json', 'var_function-call-7269832412204370936': 'file_storage/function-call-7269832412204370936.json'}

exec(code, env_args)
