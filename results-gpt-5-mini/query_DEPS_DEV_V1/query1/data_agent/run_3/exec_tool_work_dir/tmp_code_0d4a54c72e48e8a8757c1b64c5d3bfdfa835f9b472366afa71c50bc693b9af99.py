code = """import json, re, os

# Load variables from storage
def load_var(v):
    if isinstance(v, str) and os.path.exists(v):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

latest = load_var(var_call_HhhYHySXJCdHBnehqAJdXEgS)
proj_pkg = load_var(var_call_l0IHZCQxuch54l3erCtQzqR1)
proj_info = load_var(var_call_AXx1kE6gciDBxzHDtgitBIAb)

# Normalize latest: keep unique per Name (if duplicates with same version, keep one)
latest_by_name = {}
for r in latest:
    name = r.get('Name')
    ver = r.get('Version')
    ts = r.get('UpstreamPublishedAt')
    # If multiple entries, prefer one (they should be same version)
    if name not in latest_by_name:
        latest_by_name[name] = {'Name': name, 'Version': ver, 'UpstreamPublishedAt': ts}

# Build mapping from (Name,Version) to list of ProjectName
map_pkg_to_projects = {}
for r in proj_pkg:
    if r.get('System') != 'NPM':
        continue
    key = (r.get('Name'), r.get('Version'))
    map_pkg_to_projects.setdefault(key, []).append(r.get('ProjectName'))

# Preprocess project_info strings for faster search: build list of tuples (text, original)
proj_info_texts = []
for r in proj_info:
    txt = r.get('Project_Information')
    if txt:
        proj_info_texts.append(txt)

# Function to extract stars from a project_info string
def extract_stars(text):
    if not text or not isinstance(text, str):
        return None
    patterns = [r"([\d,]+)\s+stars?",
                r"stars count of\s*([\d,]+)",
                r"a total of\s*([\d,]+)\s+stars",
                r"garnered .*?([\d,]+)\s+stars",
                r"has garnered .*?([\d,]+)\s+stars",
                r"currently has .*?stars.*?([\d,]+)",
               ]
    for p in patterns:
        m = re.search(p, text, flags=re.I)
        if m:
            s = m.group(1)
            try:
                return int(s.replace(',', ''))
            except:
                continue
    # fallback: look for any number followed by 'stars' earlier/later
    m = re.search(r"([\d,]+).*?stars?", text, flags=re.I)
    if m:
        try:
            return int(m.group(1).replace(',', ''))
        except:
            return None
    return None

results = []
for name, info in latest_by_name.items():
    ver = info['Version']
    key = (name, ver)
    project_names = map_pkg_to_projects.get(key, [])
    best_stars = None
    best_project = None
    # For each associated project name, try to find matching project_info entries
    for pn in project_names:
        if not pn:
            continue
        # Search project_info texts that contain the project name
        matches = [t for t in proj_info_texts if pn in t]
        # If no direct match, also try matching just repo part after '/'
        if not matches and '/' in pn:
            repo_part = pn.split('/')[-1]
            matches = [t for t in proj_info_texts if repo_part in t]
        for t in matches:
            stars = extract_stars(t)
            if stars is None:
                continue
            if best_stars is None or stars > best_stars:
                best_stars = stars
                best_project = pn
    # If no project_names matched or no stars found, try a broader search across all project_info texts for package name
    if best_stars is None:
        # try to find any project_info that mentions the package name (without scope @)
        search_name = name
        if name.startswith('@'):
            search_name = name[1:]
        matches = [t for t in proj_info_texts if search_name in t]
        for t in matches:
            stars = extract_stars(t)
            if stars is None:
                continue
            if best_stars is None or stars > best_stars:
                best_stars = stars
                best_project = None
    if best_stars is None:
        best_stars = 0
    results.append({'Name': name, 'Version': ver, 'Stars': best_stars, 'ProjectName': best_project})

# Sort by Stars desc and take top 5
results_sorted = sorted(results, key=lambda x: x['Stars'], reverse=True)
top5 = results_sorted[:5]

import json
print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_call_HhhYHySXJCdHBnehqAJdXEgS': 'file_storage/call_HhhYHySXJCdHBnehqAJdXEgS.json', 'var_call_l0IHZCQxuch54l3erCtQzqR1': 'file_storage/call_l0IHZCQxuch54l3erCtQzqR1.json', 'var_call_AXx1kE6gciDBxzHDtgitBIAb': 'file_storage/call_AXx1kE6gciDBxzHDtgitBIAb.json'}

exec(code, env_args)
