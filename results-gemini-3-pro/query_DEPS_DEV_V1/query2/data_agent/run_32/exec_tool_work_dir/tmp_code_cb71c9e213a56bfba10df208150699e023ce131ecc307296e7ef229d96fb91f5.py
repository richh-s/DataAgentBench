code = """import json
import re

# Load data files
with open(locals()['var_function-call-10548740809673999376'], 'r') as f:
    project_info_list = json.load(f)

with open(locals()['var_function-call-8046929099242269916'], 'r') as f:
    # This is a list of dicts [{"Name": "...", "Version": "..."}, ...]
    package_list = json.load(f)

with open(locals()['var_function-call-4589236967949451188'], 'r') as f:
    # This is a list of dicts [{"Name": "...", "Version": "...", "ProjectName": "..."}, ...]
    project_map_list = json.load(f)

# 1. Parse Project Info
project_forks = {}

# Regex for project name (owner/repo)
# Avoid http:// or https://
# Pattern: space or start of string, then owner/repo, then space or comma or end
# But strict regex might be better.
# Most appear as "The project owner/repo ..." or "The GitHub project owner/repo ..."
# Let's try to find a token with '/' that is not a URL.
def extract_forks(text):
    # Try different patterns for forks
    # 1. "and 5782 forks"
    # 2. "forks count of 988"
    # 3. "forked 12 times"
    # Remove commas
    clean_text = text.replace(',', '')
    
    m = re.search(r'(\d+)\s+forks', clean_text)
    if m: return int(m.group(1))
    
    m = re.search(r'forks\s+count\s+of\s+(\d+)', clean_text)
    if m: return int(m.group(1))
    
    m = re.search(r'forked\s+(\d+)\s+times', clean_text)
    if m: return int(m.group(1))
    
    return 0

def extract_name(text):
    # Find word with / in it
    words = text.split()
    for w in words:
        # cleanup punctuation
        w_clean = w.strip('.,')
        if '/' in w_clean and 'http' not in w_clean:
            return w_clean
    return None

for entry in project_info_list:
    info = entry.get('Project_Information', '')
    pname = extract_name(info)
    forks = extract_forks(info)
    if pname:
        project_forks[pname] = forks

# 2. Create set of valid packages (Name, Version)
valid_packages = set()
for p in package_list:
    valid_packages.add((p['Name'], p['Version']))

# 3. Filter projects
valid_projects = set()
for p in project_map_list:
    if (p['Name'], p['Version']) in valid_packages:
        # Check if project name is in our project_info map (or if we need to clean it)
        pname = p['ProjectName']
        if pname in project_forks:
            valid_projects.add(pname)

# 4. Get fork counts for valid projects
results = []
for pname in valid_projects:
    results.append({'ProjectName': pname, 'Forks': project_forks[pname]})

# Sort by Forks descending
results.sort(key=lambda x: x['Forks'], reverse=True)

# Top 5
top5 = results[:5]

print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_function-call-6754892704679282557': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.5', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'System': 'NPM', 'Name': '@douganderson444/panzoom-node', 'Version': '1.1.1', 'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'System': 'NPM', 'Name': '@dreamworld/dw-select', 'Version': '3.1.2-fix-double-click-issue.1', 'Licenses': '[\n  "ISC"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_function-call-4583479465290178389': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-16545873088892630769': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'Licenses': '[\n  "non-standard"\n]', 'Description': '🍃 JavaScript library for mobile-friendly interactive maps 🇺🇦', 'Homepage': 'https://leafletjs.com', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'Licenses': '[\n  "ISC"\n]', 'Description': 'A fullscreen control for Leaflet', 'Homepage': 'http://leaflet.github.io/Leaflet.fullscreen/', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'Marker Clustering plugin for Leaflet', 'Homepage': 'None', 'OSSFuzz': 'nan'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.', 'Licenses': '[\n  "MIT"\n]', 'Description': 'React.js Responsive Carousel (with Swipe)', 'Homepage': 'http://leandrowd.github.io/react-responsive-carousel/', 'OSSFuzz': 'nan'}], 'var_function-call-6867096304813560838': [{'count(*)': '661372'}], 'var_function-call-4042071709850949332': [{'count(*)': '176998'}], 'var_function-call-6051875745845266746': [{'count_star()': '597602'}], 'var_function-call-14428671641834964130': [{'count_star()': '770'}], 'var_function-call-10548740809673999376': 'file_storage/function-call-10548740809673999376.json', 'var_function-call-8046929099242269916': 'file_storage/function-call-8046929099242269916.json', 'var_function-call-4589236967949451188': 'file_storage/function-call-4589236967949451188.json'}

exec(code, env_args)
