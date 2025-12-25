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
    text = text.replace(',', '')
    # patterns
    # "X stars"
    # "stars count of X"
    m = re.search(r'(\d+)\s+stars', text)
    if m: return int(m.group(1))
    m = re.search(r'stars count of (\d+)', text)
    if m: return int(m.group(1))
    return 0

def parse_name(text):
    # Try to find "project owner/repo"
    # Regex for owner/repo
    repo_pat = r'([a-zA-Z0-9\-\._]+/[a-zA-Z0-9\-\._]+)'
    
    # Priority patterns
    patterns = [
        r'project\s+(?:named\s+)?' + repo_pat,
        r'named\s+' + repo_pat,
        r'project\s+(?:on GitHub\s*,?\s*)?(?:named\s+)?' + repo_pat
    ]
    
    for p in patterns:
        m = re.search(p, text, re.IGNORECASE)
        if m:
            return m.group(1)
            
    # Fallback: look for generic repo pattern that is not a url
    # We want to avoid matching "github.com/owner/repo" if possible, or extract from it.
    # But text usually says "hosted on GitHub under the name owner/repo"
    m = re.search(r'name\s+' + repo_pat, text, re.IGNORECASE)
    if m: return m.group(1)
    
    # Last resort: first "word/word"
    m = re.search(r'\b' + repo_pat + r'\b', text)
    if m: return m.group(1)
    
    return None

for item in project_infos:
    desc = item.get('Project_Information', '')
    name = parse_name(desc)
    stars = parse_stars(desc)
    if name:
        # Check if name is valid repo format (contains /)
        if '/' in name:
            project_stars[name] = stars

# 2. Filter mappings
relevant_projects = set(project_stars.keys())
pkg_to_proj = {}
# We need to handle that one package might have multiple versions mapping to different projects (unlikely) 
# or multiple projects (unlikely).
# But mostly we need to filter down to relevant ones.
for row in project_packageversions:
    p_name = row.get('ProjectName')
    if p_name in relevant_projects:
        pkg = row.get('Name')
        ver = row.get('Version')
        # Store mapping. 
        # Note: (Name, Version) is unique in project_packageversion usually?
        # If not, last one wins? Or we collect?
        # Let's assume (Name, Version) maps to one project.
        pkg_to_proj[(pkg, ver)] = p_name

# 3. Find latest version for each package
pkg_latest = {} # Name -> (Version, Date)
for row in packageinfos:
    name = row.get('Name')
    ver = row.get('Version')
    ts = row.get('UpstreamPublishedAt')
    
    if ts is None: continue
    try:
        ts = float(ts)
    except: continue
    
    if name not in pkg_latest or ts > pkg_latest[name][1]:
        pkg_latest[name] = (ver, ts)

# 4. Join
# For each distinct package (Name), get latest version.
# Check if (Name, LatestVersion) has a project mapping.
final_list = []
for name, (ver, _) in pkg_latest.items():
    if (name, ver) in pkg_to_proj:
        p_name = pkg_to_proj[(name, ver)]
        stars = project_stars.get(p_name, 0)
        final_list.append({
            "Name": name,
            "Version": ver,
            "Stars": stars,
            "Project": p_name
        })

# 5. Top 5
final_list.sort(key=lambda x: x['Stars'], reverse=True)
top5 = final_list[:5]

print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_function-call-2104816414074645109': ['project_info', 'project_packageversion'], 'var_function-call-14664713132353813279': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-8178938550089235046': [{'column_name': 'Project_Information', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Licenses', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Homepage', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OSSFuzz', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-17121204838242963000': [{'COUNT(*)': '661372'}], 'var_function-call-6528540733988721374': [{'count_star()': '597602'}], 'var_function-call-14481277320679772207': [{'count_star()': '770'}], 'var_function-call-9764513274838904182': 'file_storage/function-call-9764513274838904182.json', 'var_function-call-3321855864541705019': 'file_storage/function-call-3321855864541705019.json', 'var_function-call-9225123913888599835': 'file_storage/function-call-9225123913888599835.json', 'var_function-call-14894778918987677894': [{'Name': '@dmrvos/infrajs>0.0.5>typescript', 'Version': '2.6.2', 'Stars': 94931, 'Project': 'microsoft/typescript'}, {'Name': '@dmrvos/infrajs>0.0.6>typescript', 'Version': '2.6.2', 'Stars': 94931, 'Project': 'microsoft/typescript'}, {'Name': '@dylanvann/svelte', 'Version': '3.25.4', 'Stars': 73499, 'Project': 'sveltejs/svelte'}, {'Name': '@dumc11/tailwindcss', 'Version': '0.4.0', 'Stars': 73464, 'Project': 'tailwindcss/tailwindcss'}, {'Name': '@dwarvesf/react-scripts>0.7.0>lodash._baseclone', 'Version': '3.3.0', 'Stars': 57779, 'Project': 'lodash/lodash'}], 'var_function-call-2413438923957306137': [], 'var_function-call-4265799210448540397': [{'Name': '@ecl/twig-component-carousel'}, {'Name': '@douganderson444/panzoom-node'}, {'Name': '@douganderson444/panzoom-node'}, {'Name': '@dreamworld/dw-select'}, {'Name': '@discue/ui-components'}, {'Name': '@dvcol/web-extension-utils'}, {'Name': '@dxos/client'}, {'Name': '@dxos/client'}, {'Name': '@edgedev/firebase'}, {'Name': '@eden-network/data'}, {'Name': '@dyoshikawa/mentor-php-env'}, {'Name': '@eclipsejs/cli'}, {'Name': '@dytesdk/electron-main'}, {'Name': '@dxos/client'}, {'Name': '@dxos/client'}, {'Name': '@ebot7/edem-react'}, {'Name': '@e4a/irmaseal-wasm-bindings'}, {'Name': '@ebury/chameleon-components'}, {'Name': '@dxos/console-app'}, {'Name': '@dxos/console-app'}], 'var_function-call-5877041137848195737': []}

exec(code, env_args)
