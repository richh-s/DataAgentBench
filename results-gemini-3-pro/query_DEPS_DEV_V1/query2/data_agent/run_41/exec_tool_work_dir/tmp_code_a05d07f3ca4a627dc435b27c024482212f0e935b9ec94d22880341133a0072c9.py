code = """import json
import re

path_pkg = locals()['var_function-call-2678515795771401501']
path_pv = locals()['var_function-call-8867938047833477408']
path_info = locals()['var_function-call-10398229597847549706']

with open(path_info, 'r') as f:
    project_info_data = json.load(f)

# 1. Parse Project Info
proj_forks = {}
name_pattern = re.compile(r'([a-zA-Z0-9\-\.]+\/[a-zA-Z0-9\-\.]+)')
fork_patterns = [
    re.compile(r'and ([\d,]+) forks'),
    re.compile(r'forks count of ([\d,]+)'),
    re.compile(r'forked ([\d,]+) times'),
    re.compile(r'([\d,]+) forks')
]

for row in project_info_data:
    info = row.get('Project_Information', '')
    if not info:
        continue
    
    # Extract name
    matches = name_pattern.findall(info)
    # Filter matches
    valid_matches = [m for m in matches if '/' in m and not m.startswith('github.com') and len(m) > 3]
    if not valid_matches:
        continue
    
    # Heuristic: use the first valid match as project name
    proj_name = valid_matches[0]
    
    # Extract forks
    forks = 0
    found_fork = False
    for pat in fork_patterns:
        m = pat.search(info)
        if m:
            try:
                forks = int(m.group(1).replace(',', ''))
                found_fork = True
                break
            except:
                pass
    
    # If forks not explicitly found but text exists, maybe it's 0 if pattern didn't match?
    # Some patterns cover "0 forks".
    # If no pattern matches, we might assume 0 or skip? 
    # Let's assume we captured it if it's there. 
    # If not found, maybe skip to be safe, or assume 0?
    # Inspecting samples: "0 forks" matches "([\d,]+) forks".
    if found_fork:
        proj_forks[proj_name] = forks
    else:
        # Check if "0 forks" is in text literally? covered by regex 4.
        pass

print(f"Projects found in info: {len(proj_forks)}")

# 2. Filter Project Package Version
with open(path_pv, 'r') as f:
    project_pv_data = json.load(f)

# We need to find packages for these projects
# Map: (Name, Version) -> ProjectName
pkg_to_proj = {}
target_projects = set(proj_forks.keys())

for row in project_pv_data:
    pname = row.get('ProjectName')
    if pname in target_projects:
        pkg_to_proj[(row['Name'], row['Version'])] = pname

print(f"Packages associated with target projects: {len(pkg_to_proj)}")

# 3. Filter Package Info (MIT + Release)
with open(path_pkg, 'r') as f:
    package_data = json.load(f)

valid_projects = set()

for pkg in package_data:
    key = (pkg['Name'], pkg['Version'])
    if key not in pkg_to_proj:
        continue
    
    # Check License
    licenses = pkg.get('Licenses', '[]')
    if 'MIT' not in licenses:
        continue
    
    # Check IsRelease
    vinfo = pkg.get('VersionInfo', '{}')
    is_release = False
    if isinstance(vinfo, str):
        if '"IsRelease": true' in vinfo or '"IsRelease":true' in vinfo:
             is_release = True
        elif 'true' in vinfo: 
             try:
                 v_obj = json.loads(vinfo)
                 if v_obj.get('IsRelease'):
                     is_release = True
             except:
                 pass
    else:
        if vinfo.get('IsRelease'):
            is_release = True
            
    if is_release:
        valid_projects.add(pkg_to_proj[key])

print(f"Valid projects (MIT + Release): {len(valid_projects)}")

# 4. Get Top 5
final_list = []
for p in valid_projects:
    final_list.append({'Project': p, 'Forks': proj_forks[p]})

final_list.sort(key=lambda x: x['Forks'], reverse=True)
top_5 = [x['Project'] for x in final_list[:5]]

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-11065893993173379102': ['project_info', 'project_packageversion'], 'var_function-call-15361139508270201429': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-40608375882137146': [{'cid': '0', 'name': 'Project_Information', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '1', 'name': 'Licenses', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '2', 'name': 'Description', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '3', 'name': 'Homepage', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '4', 'name': 'OSSFuzz', 'type': 'DOUBLE', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}], 'var_function-call-2678515795771401501': 'file_storage/function-call-2678515795771401501.json', 'var_function-call-8867938047833477408': 'file_storage/function-call-8867938047833477408.json', 'var_function-call-10398229597847549706': 'file_storage/function-call-10398229597847549706.json', 'var_function-call-12200236935107415748': [], 'var_function-call-15138716392146612001': 'debug done', 'var_function-call-5922763594562684266': {'total_packages': 391228, 'valid_packages': 85158, 'candidate_projects': 5477, 'sample_candidates': ['ecomclub/search-engine', 'sindresorhus/caller-path', 'dobuzi/nooks', 'economist-components/react-i13n-tealium', 'donotjs/donot-transform-stylus'], 'matched_projects_in_info': 0, 'total_info_rows': 770, 'sample_info_row': {'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}}, 'var_function-call-2797303438942603563': [{'count_star()': '770'}], 'var_function-call-7236527520819872720': [], 'var_function-call-410307400399065482': 'debug regex done', 'var_function-call-11916057350067449838': {'test_match': [], 'matches_count': 0, 'sample_matches': []}, 'var_function-call-7758136215557866197': {'test_match': ['lberrocal/npm-packages-template'], 'matches_count': 769, 'sample_matches': [['lberrocal/npm-packages-template'], ['leaflet/leaflet'], ['leaflet/leaflet.fullscreen'], ['leaflet/leaflet.markercluster'], ['leandrowd/react-responsive-carousel']]}}

exec(code, env_args)
