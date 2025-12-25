code = """# (Previous code loaded data already, I can reuse lists if I didn't overwrite them, but reloading is safer or just assume they are in memory)
# Actually, the previous execution context is preserved if I don't overwrite variables?
# The tool says "All previous tool results are available as variables".
# It doesn't explicitly say the Python environment state persists. Usually it does NOT.
# But I can access the variable keys.

import json
import re

# Load data again to be safe
with open(locals()['var_function-call-1707458576280284598'], 'r') as f:
    project_info_list = json.load(f)

with open(locals()['var_function-call-4930162341382673899'], 'r') as f:
    package_info_list = json.load(f)

with open(locals()['var_function-call-4930162341382672658'], 'r') as f:
    project_package_list = json.load(f)

# 1. Parse Project Info
project_stars = {} 
for item in project_info_list:
    text = item.get('Project_Information', '')
    if not text:
        continue
    star_match = re.search(r'(\d{1,3}(?:,\d{3})*|\d+) stars', text)
    if not star_match:
        star_match = re.search(r'stars count of (\d{1,3}(?:,\d{3})*|\d+)', text)
    stars = 0
    if star_match:
        stars = int(star_match.group(1).replace(',', ''))
    
    # Extract Project Name
    name_match = re.search(r'The (?:GitHub )?project (?:named )?([^ ]+) (?:is|on|currently)', text)
    project_name = None
    if name_match:
        project_name = name_match.group(1).strip(',').strip()
    else:
        name_match = re.search(r'under the name ([^,]+),', text)
        if name_match:
            project_name = name_match.group(1).strip()
        else:
            name_match = re.search(r'repository named ([^,]+),', text)
            if name_match:
                project_name = name_match.group(1).strip()

    if project_name:
        project_stars[project_name] = stars

# 2. Identify Latest Version
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

# 3. Join
candidates = []
seen_packages = set()

for pp in project_package_list:
    p_name = pp['Name']
    p_ver = pp['Version']
    proj_name = pp['ProjectName']
    
    # Optimization: Check if package already processed? No, we need to check if it's the latest version first.
    if p_name in pkg_latest:
        latest_ver = pkg_latest[p_name][0]
        if p_ver == latest_ver:
            if proj_name in project_stars:
                stars = project_stars[proj_name]
                # Avoid duplicate entries for the same package
                if p_name not in seen_packages:
                    candidates.append({
                        "Package": p_name,
                        "Version": p_ver,
                        "Stars": stars,
                        "Project": proj_name
                    })
                    seen_packages.add(p_name)

# Sort
candidates.sort(key=lambda x: x['Stars'], reverse=True)

print("__RESULT__:")
print(json.dumps(candidates[:10]))"""

env_args = {'var_function-call-14318474474337643074': ['project_info', 'project_packageversion'], 'var_function-call-6580797317387853942': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-6580797317387854645': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-11130966236834603882': [{'count(*)': '661372'}], 'var_function-call-11130966236834603981': [{'count_star()': '597602'}], 'var_function-call-11130966236834604080': [{'count_star()': '770'}], 'var_function-call-1707458576280284598': 'file_storage/function-call-1707458576280284598.json', 'var_function-call-4930162341382673899': 'file_storage/function-call-4930162341382673899.json', 'var_function-call-4930162341382672658': 'file_storage/function-call-4930162341382672658.json', 'var_function-call-17895497843191770769': [{'Package': '@dylanvann/svelte', 'Version': '3.25.4', 'Stars': 73499, 'Project': 'sveltejs/svelte'}, {'Package': '@dylanvann/svelte', 'Version': '3.25.4', 'Stars': 73499, 'Project': 'sveltejs/svelte'}, {'Package': '@dumc11/tailwindcss', 'Version': '0.4.0', 'Stars': 73464, 'Project': 'tailwindcss/tailwindcss'}, {'Package': '@dumc11/tailwindcss', 'Version': '0.4.0', 'Stars': 73464, 'Project': 'tailwindcss/tailwindcss'}, {'Package': '@dman777/shadow-dom-quill-temp', 'Version': '1.0.0', 'Stars': 42407, 'Project': 'quilljs/quill'}, {'Package': '@dothq/styled-components', 'Version': '6.0.2-prealpha-dot', 'Stars': 39660, 'Project': 'styled-components/styled-components'}, {'Package': '@dothq/styled-components', 'Version': '6.0.2-prealpha-dot', 'Stars': 39660, 'Project': 'styled-components/styled-components'}, {'Package': '@dynasty/styled-components', 'Version': '3.2.1', 'Stars': 39660, 'Project': 'styled-components/styled-components'}, {'Package': '@dynasty/styled-components', 'Version': '3.2.1', 'Stars': 39660, 'Project': 'styled-components/styled-components'}, {'Package': '@ec-nordbund/leaflet', 'Version': '1.7.1-build-81dc2489', 'Stars': 38715, 'Project': 'leaflet/leaflet'}]}

exec(code, env_args)
