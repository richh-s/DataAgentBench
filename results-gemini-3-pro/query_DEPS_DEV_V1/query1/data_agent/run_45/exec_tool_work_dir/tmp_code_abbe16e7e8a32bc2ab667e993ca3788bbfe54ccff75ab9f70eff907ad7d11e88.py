code = """import json
import re
import pandas as pd

# Load data
with open(locals()['var_function-call-1707458576280284598'], 'r') as f:
    project_info_list = json.load(f)

with open(locals()['var_function-call-4930162341382673899'], 'r') as f:
    package_info_list = json.load(f)

with open(locals()['var_function-call-4930162341382672658'], 'r') as f:
    project_package_list = json.load(f)

# 1. Parse Project Info
project_stars = {} # ProjectName -> Stars

# We need to extract Project Name and Stars from the text.
# Let's first collect all known project names from project_package_list to help validation if needed, 
# but extracting from text is primary.

for item in project_info_list:
    text = item.get('Project_Information', '')
    if not text:
        continue
    
    # Extract Stars
    # Patterns: "38,715 stars", "38715 stars", "stars count of 3761"
    # Handling comma numbers
    star_match = re.search(r'(\d{1,3}(?:,\d{3})*|\d+) stars', text)
    if not star_match:
        star_match = re.search(r'stars count of (\d{1,3}(?:,\d{3})*|\d+)', text)
    
    stars = 0
    if star_match:
        stars_str = star_match.group(1).replace(',', '')
        stars = int(stars_str)
    
    # Extract Project Name
    # Patterns observed:
    # "The project lberrocal/npm-packages-template is..."
    # "The project named leo-ran/easy-node-server is..."
    # "The GitHub project named leviticusmb/divine-amd-loader currently..."
    # "The project is hosted on GitHub under the name learnfrontend-dc/product-cart,..."
    
    name_match = re.search(r'The (?:GitHub )?project (?:named )?([^ ]+) (?:is|on|currently)', text)
    project_name = None
    if name_match:
        project_name = name_match.group(1).strip(',').strip()
    else:
        # Try "under the name X,"
        name_match = re.search(r'under the name ([^,]+),', text)
        if name_match:
            project_name = name_match.group(1).strip()
        else:
            # Try "repository named X,"
            name_match = re.search(r'repository named ([^,]+),', text)
            if name_match:
                project_name = name_match.group(1).strip()

    if project_name:
        project_stars[project_name] = stars

# 2. Identify Latest Version for each Package
# Convert UpstreamPublishedAt to float
pkg_latest = {} # Name -> (Version, Timestamp)

for p in package_info_list:
    name = p['Name']
    ver = p['Version']
    try:
        ts = float(p['UpstreamPublishedAt'])
    except:
        ts = 0.0
    
    if name not in pkg_latest:
        pkg_latest[name] = (ver, ts)
    else:
        if ts > pkg_latest[name][1]:
            pkg_latest[name] = (ver, ts)

# 3. Join with Project Mapping
# We want: PackageName, Version, Stars
results = []

for pp in project_package_list:
    p_name = pp['Name']
    p_ver = pp['Version']
    proj_name = pp['ProjectName']
    
    # Check if this is the latest version
    if p_name in pkg_latest:
        latest_ver = pkg_latest[p_name][0]
        if p_ver == latest_ver:
            # Check if we have stars for this project
            if proj_name in project_stars:
                stars = project_stars[proj_name]
                results.append({
                    "Package": p_name,
                    "Version": p_ver,
                    "Stars": stars,
                    "Project": proj_name
                })

# Sort by Stars desc
results.sort(key=lambda x: x['Stars'], reverse=True)

print("__RESULT__:")
print(json.dumps(results[:10])) # Print top 10 to be sure"""

env_args = {'var_function-call-14318474474337643074': ['project_info', 'project_packageversion'], 'var_function-call-6580797317387853942': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-6580797317387854645': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-11130966236834603882': [{'count(*)': '661372'}], 'var_function-call-11130966236834603981': [{'count_star()': '597602'}], 'var_function-call-11130966236834604080': [{'count_star()': '770'}], 'var_function-call-1707458576280284598': 'file_storage/function-call-1707458576280284598.json', 'var_function-call-4930162341382673899': 'file_storage/function-call-4930162341382673899.json', 'var_function-call-4930162341382672658': 'file_storage/function-call-4930162341382672658.json'}

exec(code, env_args)
