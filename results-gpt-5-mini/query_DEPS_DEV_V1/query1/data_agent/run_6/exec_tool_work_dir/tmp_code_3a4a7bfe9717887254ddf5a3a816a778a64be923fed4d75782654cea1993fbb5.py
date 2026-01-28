code = """import json
import pandas as pd
import re

# Load data from storage file paths
with open(var_call_XRcda6SBZJgihMrwYHRLEGxb, 'r', encoding='utf-8') as f:
    package_rows = json.load(f)
with open(var_call_UUtqoNyEiArLTMXivlFnRpJi, 'r', encoding='utf-8') as f:
    ppv_rows = json.load(f)
with open(var_call_tWshAERaIGG0OzJWhGI8OkDB, 'r', encoding='utf-8') as f:
    pinfo_rows = json.load(f)

# Parse VersionInfo and select latest release (IsRelease==true) by highest Ordinal per package Name
latest = {}
for r in package_rows:
    name = r.get('Name')
    vi_raw = r.get('VersionInfo')
    try:
        vi = json.loads(vi_raw) if vi_raw else {}
    except Exception:
        # sometimes VersionInfo may be malformed; skip
        vi = {}
    is_release = vi.get('IsRelease', False)
    ordinal = vi.get('Ordinal')
    if not is_release or ordinal is None:
        continue
    cur = latest.get(name)
    if (cur is None) or (ordinal > cur['Ordinal']):
        latest[name] = {
            'System': r.get('System'),
            'Name': name,
            'Version': r.get('Version'),
            'Ordinal': ordinal,
            'UpstreamPublishedAt': r.get('UpstreamPublishedAt')
        }

# Build mapping from (System,Name,Version) to list of ProjectName (only GITHUB)
ppv_map = {}
for r in ppv_rows:
    if r.get('ProjectType','').upper() != 'GITHUB':
        continue
    key = (r.get('System'), r.get('Name'), r.get('Version'))
    ppv_map.setdefault(key, []).append(r.get('ProjectName'))

# Preprocess project_info: we'll search for occurrences of repo and star counts
# Build list of tuples (text)
pinfo_texts = [r.get('Project_Information','') for r in pinfo_rows]

# Helper to extract stars from a text
star_re = re.compile(r"([0-9]{1,3}(?:,[0-9]{3})*)\s+stars", re.IGNORECASE)

def extract_stars_from_text(text):
    m = star_re.search(text)
    if not m:
        return None
    s = m.group(1).replace(',', '')
    try:
        return int(s)
    except:
        return None

# For each latest package, find associated projects and star counts
results = []
for name, info in latest.items():
    key = (info['System'], name, info['Version'])
    projects = ppv_map.get(key, [])
    if not projects:
        continue
    best = None  # tuple (stars, project, matched_text)
    for proj in projects:
        stars_candidates = []
        # First, try to find exact project string inside project_info texts
        for text in pinfo_texts:
            if proj in text:
                st = extract_stars_from_text(text)
                if st is not None:
                    stars_candidates.append((st, text))
        # If we found candidates, take max
        if stars_candidates:
            st_max = max(stars_candidates, key=lambda x: x[0])[0]
            if (best is None) or (st_max > best[0]):
                best = (st_max, proj, None)
    if best is None:
        # Could not find star info for any project; skip
        continue
    results.append({
        'Package': name,
        'Version': info['Version'],
        'Project': best[1],
        'Stars': best[0]
    })

# Sort by Stars desc and select top 5
results_sorted = sorted(results, key=lambda x: x['Stars'], reverse=True)[:5]

# Prepare final output
output = results_sorted

import json
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_gfgN6wnlA1R4Upj8T5n5yXSv': ['packageinfo'], 'var_call_LLsaSoIve8C3uqFmxm5mgoZc': ['project_info', 'project_packageversion'], 'var_call_XRcda6SBZJgihMrwYHRLEGxb': 'file_storage/call_XRcda6SBZJgihMrwYHRLEGxb.json', 'var_call_UUtqoNyEiArLTMXivlFnRpJi': 'file_storage/call_UUtqoNyEiArLTMXivlFnRpJi.json', 'var_call_tWshAERaIGG0OzJWhGI8OkDB': 'file_storage/call_tWshAERaIGG0OzJWhGI8OkDB.json'}

exec(code, env_args)
