code = """import json, re

def load_var(v):
    # v may be a filepath string to a json file or already a list
    if isinstance(v, str):
        try:
            if v.endswith('.json'):
                with open(v, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except Exception:
            pass
    return v

pkgs = load_var(var_call_rFrclieBgM6E6FGBu7icp7dv)
projects = load_var(var_call_YGFSYD20r71zqcAiaiqkWlh3)
proj_info = load_var(var_call_a7VV9Fy9RgIWWmy3igFmCjOJ)

# Build latest release per package name
latest = {}
for r in pkgs:
    name = r.get('Name')
    ver = r.get('Version')
    vi_raw = r.get('VersionInfo')
    is_release = False
    ordinal = 0
    try:
        if vi_raw:
            vi = json.loads(vi_raw)
            is_release = bool(vi.get('IsRelease'))
            ordinal = int(vi.get('Ordinal') or 0)
    except Exception:
        is_release = False
    # Only consider releases
    if not is_release:
        continue
    up = r.get('UpstreamPublishedAt')
    try:
        up_val = float(up)
    except Exception:
        up_val = 0.0
    # store max by UpstreamPublishedAt
    if name not in latest or up_val > latest[name]['up']:
        latest[name] = {'Version': ver, 'up': up_val, 'ordinal': ordinal}

# Build mapping from package key to project names
pkg_to_projects = {}
for p in projects:
    try:
        if p.get('System') != 'NPM':
            continue
        key = (p.get('System'), p.get('Name'), p.get('Version'))
        pkg_to_projects.setdefault((p.get('Name'), p.get('Version')), []).append(p.get('ProjectName'))
    except Exception:
        continue

# Prepare index of project_info entries by lowercased Project_Information
proj_info_list = proj_info

# For each latest package, find project(s) and extract stars
results = []
star_regex = re.compile(r"([0-9][0-9,]*)\s+stars")
for name, info in latest.items():
    ver = info['Version']
    project_names = pkg_to_projects.get((name, ver), [])
    max_stars = None
    best_project = None
    for pname in project_names:
        if not pname:
            continue
        pname_lower = pname.lower()
        # search in proj_info entries
        for entry in proj_info_list:
            pi = entry.get('Project_Information') or ''
            if pname_lower in pi.lower():
                m = star_regex.search(pi.lower())
                if m:
                    try:
                        stars = int(m.group(1).replace(',', ''))
                    except:
                        continue
                    if (max_stars is None) or (stars > max_stars):
                        max_stars = stars
                        best_project = pname
    if max_stars is not None:
        results.append({'Name': name, 'Version': ver, 'Stars': max_stars, 'ProjectName': best_project})

# Sort and take top 5
results_sorted = sorted(results, key=lambda x: x['Stars'], reverse=True)[:5]

print("__RESULT__:")
print(json.dumps(results_sorted))"""

env_args = {'var_call_rFrclieBgM6E6FGBu7icp7dv': 'file_storage/call_rFrclieBgM6E6FGBu7icp7dv.json', 'var_call_YGFSYD20r71zqcAiaiqkWlh3': 'file_storage/call_YGFSYD20r71zqcAiaiqkWlh3.json', 'var_call_a7VV9Fy9RgIWWmy3igFmCjOJ': 'file_storage/call_a7VV9Fy9RgIWWmy3igFmCjOJ.json'}

exec(code, env_args)
