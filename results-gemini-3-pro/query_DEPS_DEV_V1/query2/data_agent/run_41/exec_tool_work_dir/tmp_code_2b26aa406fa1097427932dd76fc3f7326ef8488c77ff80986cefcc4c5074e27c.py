code = """import json
import re

# Access file paths from local variables
path_pkg = locals()['var_function-call-2678515795771401501']
path_pv = locals()['var_function-call-8867938047833477408']
path_info = locals()['var_function-call-10398229597847549706']

# Load data
with open(path_pkg, 'r') as f:
    package_data = json.load(f)

with open(path_pv, 'r') as f:
    project_pv_data = json.load(f)

with open(path_info, 'r') as f:
    project_info_data = json.load(f)

# Step 1: Filter packages
valid_packages = set()
for pkg in package_data:
    # Check License
    licenses = pkg.get('Licenses', '[]')
    if 'MIT' not in licenses:
        continue
    
    # Check IsRelease
    vinfo = pkg.get('VersionInfo', '{}')
    try:
        # Check if "IsRelease": true (or true with spacing) is in string
        if isinstance(vinfo, str):
            if '"IsRelease": true' in vinfo or '"IsRelease":true' in vinfo:
                 valid_packages.add((pkg['Name'], pkg['Version']))
            elif 'true' in vinfo: # fallback parsing
                 v_obj = json.loads(vinfo)
                 if v_obj.get('IsRelease'):
                     valid_packages.add((pkg['Name'], pkg['Version']))
        else:
            if vinfo.get('IsRelease'):
                valid_packages.add((pkg['Name'], pkg['Version']))
    except:
        continue

# Step 2: Get Project Names
candidate_projects = set()
for row in project_pv_data:
    if (row['Name'], row['Version']) in valid_packages:
        if row.get('ProjectName'):
            candidate_projects.add(row['ProjectName'])

# Step 3: Parse Project Info and Match
project_forks = {}

# Regexes
fork_patterns = [
    re.compile(r'and ([\d,]+) forks'),
    re.compile(r'forks count of ([\d,]+)'),
    re.compile(r'forked ([\d,]+) times'),
    re.compile(r'([\d,]+) forks')
]

# Regex to find project names (owner/repo)
# We look for strings that are in our candidate set.
# To handle potential large text, we can just iterate.
# But iterating candidates for each text is slow.
# Instead, extract potential "owner/repo" strings from text and check if in candidates.
name_pattern = re.compile(r'\b([a-zA-Z0-9\-\.]+\/[a-zA-Z0-9\-\.]+)\b')

for row in project_info_data:
    info = row.get('Project_Information', '')
    if not info:
        continue
    
    # Check if this row is about one of our candidates
    # Extract potential names
    found_names_in_text = set(name_pattern.findall(info))
    matched_candidates = found_names_in_text.intersection(candidate_projects)
    
    if not matched_candidates:
        continue

    # Extract forks
    forks = 0
    for pat in fork_patterns:
        m = pat.search(info)
        if m:
            try:
                forks = int(m.group(1).replace(',', ''))
                break # found it
            except:
                pass
    
    # Assign forks to matched projects
    for proj in matched_candidates:
        # Avoid overwriting with 0 if we already found a higher number (duplicate entries?)
        # Or just overwrite. The description usually refers to the current state.
        if proj not in project_forks or forks > project_forks[proj]:
             project_forks[proj] = forks

# Step 4: Sort and Top 5
sorted_projects = sorted(project_forks.items(), key=lambda x: x[1], reverse=True)
top_5 = [p[0] for p in sorted_projects[:5]]

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-11065893993173379102': ['project_info', 'project_packageversion'], 'var_function-call-15361139508270201429': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-40608375882137146': [{'cid': '0', 'name': 'Project_Information', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '1', 'name': 'Licenses', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '2', 'name': 'Description', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '3', 'name': 'Homepage', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '4', 'name': 'OSSFuzz', 'type': 'DOUBLE', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}], 'var_function-call-2678515795771401501': 'file_storage/function-call-2678515795771401501.json', 'var_function-call-8867938047833477408': 'file_storage/function-call-8867938047833477408.json', 'var_function-call-10398229597847549706': 'file_storage/function-call-10398229597847549706.json'}

exec(code, env_args)
