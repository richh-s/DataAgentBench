code = """import json
import re

# Load files
with open(locals()['var_function-call-9764513274838904182'], 'r') as f:
    project_infos = json.load(f)

with open(locals()['var_function-call-3321855864541705019'], 'r') as f:
    project_packageversions = json.load(f)

with open(locals()['var_function-call-9225123913888599835'], 'r') as f:
    packageinfos = json.load(f)

# 1. Parse Project Info
project_stars = {}

def parse_stars(text):
    text = text.replace(',', '') # remove commas
    # "38715 stars"
    m = re.search(r'(\d+)\s+stars', text)
    if m: return int(m.group(1))
    # "stars count of 3761"
    m = re.search(r'stars count of (\d+)', text)
    if m: return int(m.group(1))
    return 0

def parse_name(text):
    # "The project owner/repo is..."
    # "The project named owner/repo..."
    # "The project on GitHub, named owner/repo..."
    m = re.search(r'(?:project|named)\s+(?:on GitHub\s*,?\s*)?(?:named\s+)?([a-zA-Z0-9\-\._]+/[a-zA-Z0-9\-\._]+)', text, re.IGNORECASE)
    if m:
        return m.group(1)
    
    # Fallback: look for any owner/repo pattern
    candidates = re.findall(r'\b([a-zA-Z0-9\-\._]+/[a-zA-Z0-9\-\._]+)\b', text)
    # Filter out common false positives if any? usually they are valid in this dataset context
    if candidates:
        return candidates[0]
    return None

for item in project_infos:
    desc = item.get('Project_Information', '')
    name = parse_name(desc)
    stars = parse_stars(desc)
    if name:
        project_stars[name] = stars

# 2. Filter mappings
# We only care about mappings that point to projects we have info for.
# (Wait, maybe we don't have info for all projects?
# The user provided project_database with limited project_info.
# I should assume only those with info are "popular" or relevant for the "top 5" query.
# If a project is not in project_info, we assume we don't know its stars or it has 0 stars).
relevant_projects = set(project_stars.keys())

# Map (Name, Version) -> ProjectName
pkg_to_proj = {}
for row in project_packageversions:
    p_name = row.get('ProjectName')
    if p_name in relevant_projects:
        pkg = row.get('Name')
        ver = row.get('Version')
        key = (pkg, ver)
        # In case of duplicates, just overwrite or keep list. 
        # Assuming one repo per package version usually.
        pkg_to_proj[key] = p_name

# 3. Find latest version for each package
# Group by Name
pkg_versions = {}
for row in packageinfos:
    name = row.get('Name')
    ver = row.get('Version')
    published = row.get('UpstreamPublishedAt')
    
    if published is None:
        continue
        
    try:
        published = float(published)
    except:
        continue
        
    if name not in pkg_versions:
        pkg_versions[name] = (ver, published)
    else:
        if published > pkg_versions[name][1]:
            pkg_versions[name] = (ver, published)

# 4. Link everything
results = []
for name, (latest_ver, _) in pkg_versions.items():
    key = (name, latest_ver)
    if key in pkg_to_proj:
        proj = pkg_to_proj[key]
        stars = project_stars.get(proj, 0)
        results.append({
            "Name": name,
            "Version": latest_ver,
            "Stars": stars,
            "Project": proj
        })

# 5. Sort and take top 5
results.sort(key=lambda x: x['Stars'], reverse=True)
top5 = results[:5]

print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_function-call-2104816414074645109': ['project_info', 'project_packageversion'], 'var_function-call-14664713132353813279': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-8178938550089235046': [{'column_name': 'Project_Information', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Licenses', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Homepage', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OSSFuzz', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-17121204838242963000': [{'COUNT(*)': '661372'}], 'var_function-call-6528540733988721374': [{'count_star()': '597602'}], 'var_function-call-14481277320679772207': [{'count_star()': '770'}], 'var_function-call-9764513274838904182': 'file_storage/function-call-9764513274838904182.json', 'var_function-call-3321855864541705019': 'file_storage/function-call-3321855864541705019.json', 'var_function-call-9225123913888599835': 'file_storage/function-call-9225123913888599835.json'}

exec(code, env_args)
