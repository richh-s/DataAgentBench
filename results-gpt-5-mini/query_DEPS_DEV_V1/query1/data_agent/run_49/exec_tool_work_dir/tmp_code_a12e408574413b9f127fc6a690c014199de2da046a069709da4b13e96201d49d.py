code = """import json
import re

# Load data from provided storage file paths
with open(var_call_sGsVRF7dDJsdPDDZdmSkHXPR, 'r') as f:
    pkg_rows = json.load(f)
with open(var_call_p9AEWSoIB7RXQ4feUIVtBFIr, 'r') as f:
    ppv_rows = json.load(f)
with open(var_call_OKuY11s6LzkiWEeXzwvS6p5J, 'r') as f:
    pinfo_rows = json.load(f)

# Parse VersionInfo to determine IsRelease and Ordinal if present
import math

def parse_versioninfo(s):
    try:
        return json.loads(s)
    except Exception:
        # try to extract booleans and numbers with regex
        res = {}
        m_is = re.search(r'"IsRelease"\s*:\s*(true|false)', s, re.IGNORECASE)
        if m_is:
            res['IsRelease'] = m_is.group(1).lower() == 'true'
        m_ord = re.search(r'"Ordinal"\s*:\s*(\d+)', s)
        if m_ord:
            res['Ordinal'] = int(m_ord.group(1))
        return res

# Build mapping for latest release version per package Name
latest = {}  # name -> row
for r in pkg_rows:
    if r.get('System') != 'NPM':
        continue
    vi = r.get('VersionInfo')
    parsed = parse_versioninfo(vi if vi is not None else '')
    is_release = parsed.get('IsRelease', None)
    # Only consider release versions (explicit true)
    if is_release is not True:
        continue
    name = r.get('Name')
    # UpstreamPublishedAt might be string/float; convert to float if possible
    up = r.get('UpstreamPublishedAt')
    try:
        up_f = float(up)
    except Exception:
        up_f = -math.inf
    # choose max UpstreamPublishedAt
    existing = latest.get(name)
    if existing is None or up_f > existing['_up']:
        nr = dict(r)
        nr['_up'] = up_f
        latest[name] = nr

# Now join with project_packageversion to get ProjectName(s) per (Name, Version)
# Build mapping from (Name, Version) -> list of ProjectName
pv_map = {}
for r in ppv_rows:
    if r.get('System') != 'NPM':
        continue
    key = (r.get('Name'), r.get('Version'))
    pv_map.setdefault(key, []).append(r.get('ProjectName'))

# Build mapping from project_name -> stars by scanning project_info.Project_Information
proj_stars = {}
star_re = re.compile(r'([0-9,]+)\s+stars', re.IGNORECASE)
for r in pinfo_rows:
    pi = r.get('Project_Information') or ''
    # find pattern 'owner/repo' at start or within
    # also extract stars
    m = star_re.search(pi)
    if m:
        num = int(m.group(1).replace(',', ''))
        # Extract owner/repo between 'project ' and ' on GitHub' or after 'The project '
        # Simpler: find something like 'project X/Y' in the string
        m_proj = re.search(r'project\s+([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)', pi)
        if m_proj:
            pname = m_proj.group(1)
            # store max stars if multiple entries
            proj_stars[pname] = max(proj_stars.get(pname, 0), num)
        else:
            # try alternative: find pattern like 'The GitHub project X/Y' or 'hosted on GitHub under the name X/Y'
            m2 = re.search(r'([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)', pi)
            if m2:
                pname = m2.group(1)
                proj_stars[pname] = max(proj_stars.get(pname, 0), num)

# For each latest package, find possible project names and associated stars
results = []
for name, row in latest.items():
    version = row.get('Version')
    key = (name, version)
    projects = pv_map.get(key, [])
    best_stars = None
    best_project = None
    for p in projects:
        s = proj_stars.get(p)
        if s is not None:
            if best_stars is None or s > best_stars:
                best_stars = s
                best_project = p
    if best_stars is not None:
        results.append({'Name': name, 'Version': version, 'Stars': int(best_stars), 'Project': best_project})

# Sort descending by stars and take top 5
results_sorted = sorted(results, key=lambda x: x['Stars'], reverse=True)[:5]

# Prepare output: list of dicts with Name, Version, Stars
out = [{'Name': r['Name'], 'Version': r['Version'], 'Stars': r['Stars'], 'Project': r['Project']} for r in results_sorted]

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_BKLwyI3EydRsNdVJxiB7SoKG': ['packageinfo'], 'var_call_weemRySmuox4tknDNEyvStlV': ['project_info', 'project_packageversion'], 'var_call_sGsVRF7dDJsdPDDZdmSkHXPR': 'file_storage/call_sGsVRF7dDJsdPDDZdmSkHXPR.json', 'var_call_p9AEWSoIB7RXQ4feUIVtBFIr': 'file_storage/call_p9AEWSoIB7RXQ4feUIVtBFIr.json', 'var_call_OKuY11s6LzkiWEeXzwvS6p5J': 'file_storage/call_OKuY11s6LzkiWEeXzwvS6p5J.json'}

exec(code, env_args)
