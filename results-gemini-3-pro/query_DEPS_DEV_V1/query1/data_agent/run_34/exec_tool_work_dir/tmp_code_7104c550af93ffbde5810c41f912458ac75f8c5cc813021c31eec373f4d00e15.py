code = """import json
import re

# Load data
latest_pkgs_path = locals()['var_function-call-13513533907299260701']
pkg_mappings_path = locals()['var_function-call-13513533907299260750']
proj_info_path = locals()['var_function-call-13513533907299260799']

with open(latest_pkgs_path, 'r') as f:
    latest_pkgs_list = json.load(f)

with open(pkg_mappings_path, 'r') as f:
    pkg_mappings_list = json.load(f)

with open(proj_info_path, 'r') as f:
    proj_info_list = json.load(f)

# Create set of latest packages (Name, Version)
# Also keep a map for quick lookup if needed, but set is fine for filtering
latest_pkg_set = set()
for p in latest_pkgs_list:
    latest_pkg_set.add((p['Name'], p['Version']))

# Filter mappings
# We want to associate (Name, Version) -> ProjectName
# Only for those in latest_pkg_set
filtered_mappings = []
for m in pkg_mappings_list:
    if (m['Name'], m['Version']) in latest_pkg_set:
        filtered_mappings.append({
            'Name': m['Name'],
            'Version': m['Version'],
            'ProjectName': m['ProjectName']
        })

# Process Project Info to extract Name -> Stars
project_stars = {}

# Regex patterns
# Pattern for name: look for "project X", "named X", "name X"
# We'll use a generic pattern that captures the likely owner/repo format
# The samples showed "project owner/repo", "named owner/repo", "name owner/repo"
# We also need to be careful about trailing dots or punctuation if the text says "project owner/repo."
name_pattern = re.compile(r'(?:project|named|name)\s+([a-zA-Z0-9\-_\.]+\/[a-zA-Z0-9\-_\.]+)')
# Star patterns
star_pattern1 = re.compile(r'(\d{1,3}(?:,\d{3})*|\d+)\s+stars')
star_pattern2 = re.compile(r'stars\s+count\s+of\s+(\d{1,3}(?:,\d{3})*|\d+)')

for info in proj_info_list:
    text = info.get('Project_Information', '')
    if not text:
        continue
    
    # Extract Name
    # We might find multiple matches, but usually the first one after "project" is the subject.
    name_match = name_pattern.search(text)
    if not name_match:
        continue
    
    project_name = name_match.group(1).rstrip('.') # Remove trailing dot if picked up
    
    # Extract Stars
    stars = 0
    s_match1 = star_pattern1.search(text)
    s_match2 = star_pattern2.search(text)
    
    raw_stars = '0'
    if s_match1:
        raw_stars = s_match1.group(1)
    elif s_match2:
        raw_stars = s_match2.group(1)
        
    try:
        stars = int(raw_stars.replace(',', ''))
    except:
        stars = 0
        
    project_stars[project_name] = stars

# Join mappings with stars
results = []
for item in filtered_mappings:
    p_name = item['ProjectName']
    stars = project_stars.get(p_name, 0)
    # Check if maybe the extracted name was slightly different (e.g. case)? 
    # But usually Github is case insensitive, though the map is string based.
    # We'll trust the extraction for now.
    
    results.append({
        'Name': item['Name'],
        'Version': item['Version'],
        'ProjectName': p_name,
        'Stars': stars
    })

# Sort by Stars DESC
results.sort(key=lambda x: x['Stars'], reverse=True)

# Get top 5 unique packages
# (There shouldn't be duplicate packages in filtered_mappings if Name+Version is unique in the mapping list,
# but mapping list might have duplicates. The latest_pkg_set makes the pair unique, but mapping might have mult entries?)
# Let's deduplicate by Name just in case multiple versions were considered "latest" or mappings duped.
# But query asks for "Considering only the latest release versions". 
# So each Name should appear once.

seen_names = set()
top_5 = []
for r in results:
    if r['Name'] not in seen_names:
        top_5.append(r)
        seen_names.add(r['Name'])
    if len(top_5) >= 5:
        break

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-4217545890734281346': ['packageinfo'], 'var_function-call-4217545890734281715': ['project_info', 'project_packageversion'], 'var_function-call-14759841276058981358': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'UpstreamPublishedAt': '1699345351000000.0'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}', 'UpstreamPublishedAt': '1670271173000000.0'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}', 'UpstreamPublishedAt': '1654791421000000.0'}], 'var_function-call-14759841276058982811': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-14759841276058984264': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}], 'var_function-call-10149680995686984104': [{'column_name': 'Project_Information', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Licenses', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Homepage', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OSSFuzz', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-13513533907299260701': 'file_storage/function-call-13513533907299260701.json', 'var_function-call-13513533907299260750': 'file_storage/function-call-13513533907299260750.json', 'var_function-call-13513533907299260799': 'file_storage/function-call-13513533907299260799.json'}

exec(code, env_args)
