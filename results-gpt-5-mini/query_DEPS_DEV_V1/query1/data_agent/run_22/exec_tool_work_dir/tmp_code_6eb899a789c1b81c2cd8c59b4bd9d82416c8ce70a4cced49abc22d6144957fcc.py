code = """import json, re

def load_var(v):
    # v may be a filepath (str) or already a list
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

packages = load_var(var_call_cI1IgLplT4t0GR9eLieRluyO)
ppv = load_var(var_call_KZgbAWYYJFkxwuwkmHSxk6rT)
proj_info = load_var(var_call_lKteuyt2uwJkzFLbhUwvzuj3)

# Build set of latest packages (Name, Version)
pkg_set = set()
for r in packages:
    if r.get('System') == 'NPM':
        pkg_set.add((r.get('Name'), r.get('Version')))

# Map (Name,Version) -> list of project names
mapping = {}
for r in ppv:
    if r.get('System') != 'NPM':
        continue
    key = (r.get('Name'), r.get('Version'))
    if key in pkg_set:
        mapping.setdefault(key, set()).add(r.get('ProjectName'))

# Prepare list of project_info strings
proj_texts = [p.get('Project_Information','') for p in proj_info]

# Helper to extract stars from project_info text for a given projectName
star_regex = re.compile(r"(\d[\d,]*)\s+stars", re.IGNORECASE)
star_regex2 = re.compile(r"stars count of\s*(\d[\d,]*)", re.IGNORECASE)

def extract_stars_for_projectname(projectname):
    # search proj_texts for any text containing projectname
    candidates = [text for text in proj_texts if projectname and projectname in text]
    max_stars = None
    for text in candidates:
        m = star_regex.search(text)
        if not m:
            m = star_regex2.search(text)
        if m:
            try:
                num = int(m.group(1).replace(',',''))
            except:
                num = 0
            if max_stars is None or num > max_stars:
                max_stars = num
    return max_stars

# For each package, get associated project names and stars
results = []
for key in pkg_set:
    name, version = key
    projectnames = sorted(mapping.get(key, []))
    stars_list = []
    for pn in projectnames:
        s = extract_stars_for_projectname(pn)
        if s is not None:
            stars_list.append((pn, s))
    # If no mapping or no stars found, attempt to find any proj_info text that contains repo name without owner
    if not stars_list and projectnames:
        for pn in projectnames:
            repo = pn.split('/',1)[-1]
            s = None
            for text in proj_texts:
                if repo and repo in text:
                    m = star_regex.search(text) or star_regex2.search(text)
                    if m:
                        try:
                            num = int(m.group(1).replace(',',''))
                        except:
                            num = 0
                        if s is None or num > s:
                            s = num
            if s is not None:
                stars_list.append((pn, s))
    # Determine stars: max of stars_list or 0
    if stars_list:
        max_pair = max(stars_list, key=lambda x: x[1])
        stars = max_pair[1]
    else:
        stars = 0
    results.append({
        'Name': name,
        'Version': version,
        'Stars': stars,
        'ProjectNames': projectnames
    })

# Sort by Stars desc, then Name
results_sorted = sorted(results, key=lambda x: (-x['Stars'], x['Name']))
# Take top 5
top5 = results_sorted[:5]

print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_call_cI1IgLplT4t0GR9eLieRluyO': 'file_storage/call_cI1IgLplT4t0GR9eLieRluyO.json', 'var_call_dmtcPdpOIXaoI2mADi3kR0CS': 'file_storage/call_dmtcPdpOIXaoI2mADi3kR0CS.json', 'var_call_KZgbAWYYJFkxwuwkmHSxk6rT': 'file_storage/call_KZgbAWYYJFkxwuwkmHSxk6rT.json', 'var_call_lKteuyt2uwJkzFLbhUwvzuj3': 'file_storage/call_lKteuyt2uwJkzFLbhUwvzuj3.json'}

exec(code, env_args)
