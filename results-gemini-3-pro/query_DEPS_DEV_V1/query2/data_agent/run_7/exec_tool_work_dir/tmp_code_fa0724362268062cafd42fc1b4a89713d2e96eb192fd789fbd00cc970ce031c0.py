code = """import json
import re

# Load project_info
project_info_path = locals()['var_function-call-12636083601024099777']
with open(project_info_path, 'r') as f:
    project_info_data = json.load(f)

# Load packageinfo
package_info_path = locals()['var_function-call-12636083601024102070']
with open(package_info_path, 'r') as f:
    package_info_data = json.load(f)

# Load project_packageversion
ppv_path = locals()['var_function-call-12636083601024100267']
with open(ppv_path, 'r') as f:
    ppv_data = json.load(f)

# 1. Parse Project Info
project_stats = {} # {ProjectName: ForkCount}

# Regex for Project Name
name_patterns = [
    r"The project ([a-zA-Z0-9._-]+/[a-zA-Z0-9._-]+)",
    r"The GitHub project ([a-zA-Z0-9._-]+/[a-zA-Z0-9._-]+)",
    r"The project named ([a-zA-Z0-9._-]+/[a-zA-Z0-9._-]+)",
    r"under the name ([a-zA-Z0-9._-]+/[a-zA-Z0-9._-]+)",
    r"The project is a GitHub repository named ([a-zA-Z0-9._-]+/[a-zA-Z0-9._-]+)",
    r"project on GitHub, named ([a-zA-Z0-9._-]+/[a-zA-Z0-9._-]+)"
]

# Regex for Forks
fork_patterns = [
    r"(\d+) forks",
    r"forks count of (\d+)",
    r"forked (\d+) times"
]

def extract_project_data(text):
    p_name = None
    for pat in name_patterns:
        m = re.search(pat, text)
        if m:
            p_name = m.group(1)
            # Remove trailing punctuation if captured (though \w usually avoids it, but ._- are allowed)
            # Actually, sometimes it might capture a comma if not careful? 
            # The regex char class [a-zA-Z0-9._-]+ doesn't include comma.
            break
            
    # Fallback: look for "owner/repo" word that isn't a URL
    if not p_name:
        # heuristics
        pass
        
    forks = 0
    for pat in fork_patterns:
        m = re.search(pat, text)
        if m:
            forks = int(m.group(1).replace(',', '')) # Handle "1,234"
            break
            
    return p_name, forks

for row in project_info_data:
    info = row.get("Project_Information", "")
    name, forks = extract_project_data(info)
    if name:
        project_stats[name] = forks

# 2. Map (Name, Version) -> ProjectName
# Only for projects we have info for
valid_projects = set(project_stats.keys())
pkg_to_proj = {}

for row in ppv_data:
    # row keys: Name, Version, ProjectName
    p_name = row.get("ProjectName")
    if p_name in valid_projects:
        pkg_key = (row.get("Name"), row.get("Version"))
        pkg_to_proj[pkg_key] = p_name

# 3. Filter Packages
# Criteria: License = MIT, IsRelease = True
# And must map to a valid project

final_projects = set()

for row in package_info_data:
    name = row.get("Name")
    version = row.get("Version")
    
    # Fast check: is this package-version even relevant?
    if (name, version) not in pkg_to_proj:
        continue
        
    # Check License
    licenses_str = row.get("Licenses", "[]")
    try:
        licenses = json.loads(licenses_str)
    except:
        licenses = []
    
    if "MIT" not in licenses:
        continue
        
    # Check Release
    v_info_str = row.get("VersionInfo", "{}")
    try:
        v_info = json.loads(v_info_str)
    except:
        v_info = {}
        
    if v_info.get("IsRelease") is not True:
        continue
        
    # If we are here, it's a match
    final_projects.add(pkg_to_proj[(name, version)])

# 4. Rank
result_list = []
for p in final_projects:
    result_list.append({"Project": p, "Forks": project_stats[p]})

# Sort descending by Forks
result_list.sort(key=lambda x: x["Forks"], reverse=True)

top_5 = result_list[:5]

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-15717006704601482198': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'Licenses': '[\n  "ISC"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_function-call-15717006704601484137': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_function-call-15717006704601481980': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-1392147499637762147': [{'count(*)': '661372'}], 'var_function-call-1392147499637762118': [{'count_star()': '597602'}], 'var_function-call-1392147499637762089': [{'count_star()': '770'}], 'var_function-call-12636083601024099777': 'file_storage/function-call-12636083601024099777.json', 'var_function-call-12636083601024102070': 'file_storage/function-call-12636083601024102070.json', 'var_function-call-12636083601024100267': 'file_storage/function-call-12636083601024100267.json'}

exec(code, env_args)
