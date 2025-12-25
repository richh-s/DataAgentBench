code = """import json
import re

# Load packageinfo
pkg_file = locals()['var_function-call-16958096142863539625']
with open(pkg_file, 'r') as f:
    packages = json.load(f)

# Filter packages
relevant_pkgs = set()
for p in packages:
    # System is already filtered in query as NPM
    # Licenses is already filtered in query as LIKE '%MIT%'
    # Check IsRelease
    try:
        vi = json.loads(p['VersionInfo'])
        if vi.get('IsRelease') is True:
            relevant_pkgs.add((p['Name'], p['Version']))
    except:
        pass

# Load project_packageversion
ppv_file = locals()['var_function-call-13600886298149106604']
with open(ppv_file, 'r') as f:
    ppv_data = json.load(f)

# Map project names
# We only care about packages that are in relevant_pkgs
project_names = set()
for entry in ppv_data:
    if (entry['Name'], entry['Version']) in relevant_pkgs:
        project_names.add(entry['ProjectName'])

# Load project_info
pi_file = locals()['var_function-call-11740735201857814016']
with open(pi_file, 'r') as f:
    project_info_data = json.load(f)

# Parse project_info
project_forks = {}

# Regex patterns
# Name extraction
name_patterns = [
    r"The project ([^\s]+) is hosted on GitHub",
    r"The project ([^\s]+) on GitHub",
    r"The GitHub project ([^\s]+) currently",
    r"The project named ([^\s]+) on GitHub",
    r"The project is hosted on GitHub under the name ([^\s,]+)",
    r"The project is a GitHub repository named ([^\s,]+)",
    r"The project ([^\s]+) is hosted on GITHUB"
]

# Fork extraction
fork_patterns = [
    r"and ([0-9,]+) forks",
    r"forks count of ([0-9,]+)",
    r"forked ([0-9,]+) times"
]

for entry in project_info_data:
    info = entry.get('Project_Information', '')
    if not info:
        continue
    
    # Extract Name
    p_name = None
    for pat in name_patterns:
        m = re.search(pat, info)
        if m:
            p_name = m.group(1)
            break
    
    if not p_name:
        # Fallback: check if any of our target project_names is a substring of info
        # This is expensive but project_info is small (770 rows)
        # But wait, exact name matching is safer.
        # Maybe the name is just the first non-trivial token? No.
        # Let's rely on the patterns first.
        # If we can't parse the name, we can't link it.
        # Check specific failure cases if any.
        continue

    # Extract Forks
    forks = 0
    for pat in fork_patterns:
        m = re.search(pat, info)
        if m:
            forks = int(m.group(1).replace(',', ''))
            break
            
    # Store
    project_forks[p_name] = forks

# Filter relevant projects and sort
final_list = []
for pname in project_names:
    if pname in project_forks:
        final_list.append({'ProjectName': pname, 'Forks': project_forks[pname]})
    # Try case insensitive match if needed, or minor adjustments
    # But usually exact match is expected.

# Sort by Forks desc
final_list.sort(key=lambda x: x['Forks'], reverse=True)

print("__RESULT__:")
print(json.dumps(final_list[:5]))"""

env_args = {'var_function-call-9171127104533416275': ['project_info', 'project_packageversion'], 'var_function-call-1746030028695285050': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-8715118461453016779': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_function-call-11641874808337570807': [{'column_name': 'Project_Information', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Licenses', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Homepage', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OSSFuzz', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-16958096142863539625': 'file_storage/function-call-16958096142863539625.json', 'var_function-call-16494533686035943323': [{'count_star()': '770'}], 'var_function-call-6402659800050562030': [{'count_star()': '597602'}], 'var_function-call-13600886298149106604': 'file_storage/function-call-13600886298149106604.json', 'var_function-call-11740735201857814016': 'file_storage/function-call-11740735201857814016.json'}

exec(code, env_args)
