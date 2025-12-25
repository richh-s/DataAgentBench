code = """import json
import re

# Load data
with open(locals()['var_function-call-2321378797276803279'], 'r') as f:
    project_info_list = json.load(f)

with open(locals()['var_function-call-180380683268401631'], 'r') as f:
    ppv_list = json.load(f)

with open(locals()['var_function-call-12853757404557781536'], 'r') as f:
    package_list = json.load(f)

# 1. Parse Project Info
project_forks = {}

# Regex for Project Name
# "The project owner/repo ..."
# "The project named owner/repo ..."
# "The GitHub project owner/repo ..."
# "The GitHub project named owner/repo ..."
# "The project is hosted on GitHub under the name owner/repo ..."
name_patterns = [
    r"The project ([a-zA-Z0-9\-\_\.]+\/[a-zA-Z0-9\-\_\.]+) (?:is|on|currently)",
    r"The project named ([a-zA-Z0-9\-\_\.]+\/[a-zA-Z0-9\-\_\.]+) (?:is|on|currently)",
    r"The GitHub project ([a-zA-Z0-9\-\_\.]+\/[a-zA-Z0-9\-\_\.]+) currently",
    r"The GitHub project named ([a-zA-Z0-9\-\_\.]+\/[a-zA-Z0-9\-\_\.]+) currently",
    r"under the name ([a-zA-Z0-9\-\_\.]+\/[a-zA-Z0-9\-\_\.]+),? and"
]

# Regex for Forks
fork_patterns = [
    r"(\d+) forks",
    r"forks count of (\d+)"
]

for entry in project_info_list:
    text = entry.get('Project_Information', '')
    p_name = None
    for pat in name_patterns:
        m = re.search(pat, text)
        if m:
            p_name = m.group(1)
            # Clean up trailing punctuation if any (though regex should be safe-ish)
            if p_name.endswith('.'): p_name = p_name[:-1]
            break
    
    if not p_name:
        # Fallback or log? The text is usually very structured.
        # Let's try a simpler split if it fails, or just skip.
        # Given the examples, the patterns cover most.
        pass

    forks = 0
    for pat in fork_patterns:
        m = re.search(pat, text)
        if m:
            forks = int(m.group(1).replace(',', '')) # Handle commas like "1,234"
            break
    
    if p_name:
        project_forks[p_name] = forks

# 2. Build Mapping (pkg -> project)
# Only include projects we found info for
pkg_to_proj = {}
for row in ppv_list:
    p_name = row.get('ProjectName')
    if p_name in project_forks:
        key = (row.get('Name'), row.get('Version'))
        pkg_to_proj[key] = p_name

# 3. Filter Packages and Identify Projects
valid_projects = set()

for row in package_list:
    try:
        licenses = json.loads(row.get('Licenses', '[]'))
        v_info = json.loads(row.get('VersionInfo', '{}'))
        
        # Check License (MIT)
        has_mit = False
        if isinstance(licenses, list):
            if "MIT" in licenses:
                has_mit = True
        
        # Check Release
        is_release = v_info.get('IsRelease', False)
        
        if has_mit and is_release:
            key = (row.get('Name'), row.get('Version'))
            if key in pkg_to_proj:
                valid_projects.add(pkg_to_proj[key])
                
    except Exception as e:
        continue

# 4. Rank Projects
ranked_projects = []
for p in valid_projects:
    ranked_projects.append({
        "project": p,
        "forks": project_forks[p]
    })

ranked_projects.sort(key=lambda x: x['forks'], reverse=True)

top_5 = ranked_projects[:5]

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-3000242155009640436': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'Licenses': '[\n  "ISC"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_function-call-8788101717563845659': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}], 'var_function-call-4746618155146029496': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-2207444098387180737': [{'COUNT(*)': '176998'}], 'var_function-call-14668191835184779967': [{'count_star()': '597602'}], 'var_function-call-6870164088060052838': [{'count_star()': '770'}], 'var_function-call-2321378797276803279': 'file_storage/function-call-2321378797276803279.json', 'var_function-call-180380683268401631': 'file_storage/function-call-180380683268401631.json', 'var_function-call-12853757404557781536': 'file_storage/function-call-12853757404557781536.json'}

exec(code, env_args)
