code = """import json
import re

# Load project_info
with open(locals()['var_function-call-1956027927471822867'], 'r') as f:
    project_info = json.load(f)

projects = []

# Regex for ProjectName
# "The project <name> is hosted..." or "The project named <name> on GitHub..."
# "The project on GitHub, named <name>, ..."
name_patterns = [
    r"The project ([a-zA-Z0-9_\-\.]+/[a-zA-Z0-9_\-\.]+) is hosted",
    r"The project named ([a-zA-Z0-9_\-\.]+/[a-zA-Z0-9_\-\.]+) on GitHub",
    r"The project ([a-zA-Z0-9_\-\.]+/[a-zA-Z0-9_\-\.]+) on GitHub",
    r"The GitHub project ([a-zA-Z0-9_\-\.]+/[a-zA-Z0-9_\-\.]+) currently",
    r"The GitHub project named ([a-zA-Z0-9_\-\.]+/[a-zA-Z0-9_\-\.]+) currently",
    r"The project is hosted on GitHub under the name ([a-zA-Z0-9_\-\.]+/[a-zA-Z0-9_\-\.]+),",
    r"The project on GitHub, named ([a-zA-Z0-9_\-\.]+/[a-zA-Z0-9_\-\.]+),",
    r"The project named ([a-zA-Z0-9_\-\.]+/[a-zA-Z0-9_\-\.]+) is hosted", # Case: "The project named foo/bar is hosted"
]

# Regex for Forks
# "and <forks> forks"
# "forks count of <forks>"
fork_patterns = [
    r"and ([\d,]+) forks",
    r"forks count of ([\d,]+)"
]

for p in project_info:
    info = p.get('Project_Information', '')
    name = None
    forks = 0
    
    # Extract name
    for pat in name_patterns:
        m = re.search(pat, info)
        if m:
            name = m.group(1)
            break
            
    # Extract forks
    for pat in fork_patterns:
        m = re.search(pat, info)
        if m:
            forks_str = m.group(1).replace(',', '')
            try:
                forks = int(forks_str)
            except:
                forks = 0
            break
            
    if name:
        projects.append({'name': name, 'forks': forks})

# Sort by forks desc
projects.sort(key=lambda x: x['forks'], reverse=True)

# Return top 20 names for first batch
top_projects = [p['name'] for p in projects[:20]]

print('__RESULT__:')
print(json.dumps(top_projects))"""

env_args = {'var_function-call-13928812591632711456': ['project_info', 'project_packageversion'], 'var_function-call-12240981671246474953': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-15083778320079395426': [{'count_star()': '770'}], 'var_function-call-13555536260371993922': [{'count(*)': '0'}], 'var_function-call-10974219066575923235': [{'Licenses': '[\n  "EUPL-1.2"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}, {'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 18\n}'}, {'Licenses': '[]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 14\n}'}, {'Licenses': '[\n  "ISC"\n]', 'VersionInfo': '{\n  "IsRelease": false,\n  "Ordinal": 129\n}'}, {'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}'}], 'var_function-call-3039377634705238947': [{'count(*)': '391228'}], 'var_function-call-3831245586645931117': [{'count(*)': '176998'}], 'var_function-call-1956027927471822867': 'file_storage/function-call-1956027927471822867.json', 'var_function-call-490725464643764431': [{'count_star()': '597602'}]}

exec(code, env_args)
