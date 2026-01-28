code = """import json, re
# Load data from storage variables
# var_call_Salsn0VgV4UJooucDUib8GVk, var_call_WyBe2gg69QEa1t1KJA7oY9XT, var_call_Vp08IlHrIyDQF3uzCXf22IzN

def load_var(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

data_latest = load_var(var_call_Salsn0VgV4UJooucDUib8GVk)
data_ppv = load_var(var_call_WyBe2gg69QEa1t1tKJA7oY9XT) if 'var_call_WyBe2gg69QEa1t1KJA7oY9XT' not in globals() else load_var(var_call_WyBe2gg69QEa1t1KJA7oY9XT)
# The above line had a typo in variable name; ensure correct

# Better to directly reference the known variable name provided by the tool call
data_ppv = load_var(var_call_WyBe2gg69QEa1t1KJA7oY9XT)
data_projinfo = load_var(var_call_Vp08IlHrIyDQF3uzCXf22IzN)

# Build set of latest package (Name,Version)
latest_set = set((rec['Name'], rec['Version']) for rec in data_latest)

# Map package (Name,Version) -> set of ProjectName
pkg_to_projects = {}
for rec in data_ppv:
    if rec.get('System') != 'NPM':
        continue
    key = (rec.get('Name'), rec.get('Version'))
    if key in latest_set:
        pkg_to_projects.setdefault(key, set()).add(rec.get('ProjectName'))

# Build repo (owner/repo) -> stars mapping by parsing Project_Information
repo_to_stars = {}
for rec in data_projinfo:
    s = rec.get('Project_Information') or ''
    # find repo-like tokens
    repos = re.findall(r'([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)', s)
    m = re.search(r'([0-9,]+)\s+stars', s, flags=re.IGNORECASE)
    if repos and m:
        stars = int(m.group(1).replace(',', ''))
        # choose the first repo candidate
        repo = repos[0]
        repo_to_stars[repo] = stars

# For each latest package, determine max stars across its projects
results = []
for name, version in latest_set:
    projects = pkg_to_projects.get((name, version), set())
    max_stars = 0
    project_used = None
    for p in projects:
        stars = repo_to_stars.get(p)
        if stars is None:
            # try variations: sometimes project_info may use lowercase or different separators; try lowercase
            stars = repo_to_stars.get(p.lower())
        if stars is None:
            stars = 0
        if stars > max_stars:
            max_stars = stars
            project_used = p
    results.append({'Name': name, 'Version': version, 'Stars': max_stars, 'ProjectName': project_used})

# Sort by Stars desc, then Name
results_sorted = sorted(results, key=lambda x: (-x['Stars'], x['Name']))
top5 = results_sorted[:5]

print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_call_Salsn0VgV4UJooucDUib8GVk': 'file_storage/call_Salsn0VgV4UJooucDUib8GVk.json', 'var_call_gheUnDIDzFulnp4xoS6DighS': ['project_info', 'project_packageversion'], 'var_call_WyBe2gg69QEa1t1KJA7oY9XT': 'file_storage/call_WyBe2gg69QEa1t1KJA7oY9XT.json', 'var_call_Vp08IlHrIyDQF3uzCXf22IzN': 'file_storage/call_Vp08IlHrIyDQF3uzCXf22IzN.json'}

exec(code, env_args)
