code = """import json, re, pandas as pd
# Load data from storage variables which may be file paths

def load_var(v):
    if isinstance(v, str):
        # assume it's a file path to json
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg = load_var(var_call_DAsj1afghdOxyu4gZAlVUMbk)
ppv = load_var(var_call_zivH4mVZy1XxxpT15d8JmV9c)
pinfo = load_var(var_call_OLdwQSKHqeRk4po9MwoYiSCZ)

# Filter NPM packages
pkg_npm = [r for r in pkg if r.get('System') == 'NPM']

# Helper to parse VersionInfo
import math

def parse_version_info(s):
    try:
        return json.loads(s)
    except Exception:
        try:
            # sometimes single quotes or malformed
            return eval(s)
        except Exception:
            return {}

# Build latest release per package (by UpstreamPublishedAt then Ordinal)
latest = {}
for r in pkg_npm:
    name = r.get('Name')
    ver = r.get('Version')
    vi = {}
    if r.get('VersionInfo'):
        vi = parse_version_info(r.get('VersionInfo'))
    is_release = bool(vi.get('IsRelease'))
    ordinal = vi.get('Ordinal') if vi.get('Ordinal') is not None else -1
    up = r.get('UpstreamPublishedAt')
    try:
        upv = float(up) if up is not None else float('nan')
    except Exception:
        upv = float('nan')
    # Only consider releases
    if not is_release:
        continue
    # choose best by UpstreamPublishedAt, fallback to Ordinal
    key = name
    if key not in latest:
        latest[key] = {'record': r, 'up': upv, 'ord': ordinal}
    else:
        cur = latest[key]
        # compare up values (nan treated as smaller)
        if (not math.isnan(upv) and (math.isnan(cur['up']) or upv > cur['up'])):
            latest[key] = {'record': r, 'up': upv, 'ord': ordinal}
        elif (math.isnan(upv) and upv == cur['up']):
            # both nan, compare ordinal
            if ordinal > cur['ord']:
                latest[key] = {'record': r, 'up': upv, 'ord': ordinal}
        else:
            # if upv equal or smaller, but ordinal bigger
            if upv == cur['up'] and ordinal > cur['ord']:
                latest[key] = {'record': r, 'up': upv, 'ord': ordinal}

# Build mapping from (Name,Version) -> ProjectName
map_ppv = {}
for r in ppv:
    if r.get('System') != 'NPM':
        continue
    key = (r.get('Name'), r.get('Version'))
    # if multiple, keep first
    if key not in map_ppv:
        map_ppv[key] = r.get('ProjectName')

# Parse project_info to get repo -> stars
repo_stars = {}
for r in pinfo:
    pi = r.get('Project_Information') or ''
    # find repo owner/name
    m = re.search(r'project\s+([A-Za-z0-9_.\-]+\/[A-Za-z0-9_.\-]+)', pi)
    repo = m.group(1) if m else None
    # find stars
    m2 = re.search(r'([0-9,]+)\s+stars', pi)
    stars = 0
    if m2:
        try:
            stars = int(m2.group(1).replace(',', ''))
        except:
            stars = 0
    else:
        # try alternative phrasing 'a total of X stars' or 'garnered a total of X stars'
        m3 = re.search(r'total of\s+([0-9,]+)\s+stars', pi)
        if m3:
            try:
                stars = int(m3.group(1).replace(',', ''))
            except:
                stars = 0
    if repo:
        if repo in repo_stars:
            if stars > repo_stars[repo]:
                repo_stars[repo] = stars
        else:
            repo_stars[repo] = stars

# Assemble list of latest packages with project and stars
rows = []
for name, v in latest.items():
    record = v['record']
    version = record.get('Version')
    proj = map_ppv.get((name, version))
    if not proj:
        continue
    stars = repo_stars.get(proj, 0)
    rows.append({'Name': name, 'Version': version, 'ProjectName': proj, 'Stars': stars})

# Sort by Stars desc and take top 5
rows_sorted = sorted(rows, key=lambda x: x['Stars'], reverse=True)
top5 = rows_sorted[:5]

# Prepare output
out = top5

import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_K2UJNqMMzTTp68j2z0F3gZav': ['packageinfo'], 'var_call_Isp3beDMlpPJHHWdj1eHRWH8': ['project_info', 'project_packageversion'], 'var_call_DAsj1afghdOxyu4gZAlVUMbk': 'file_storage/call_DAsj1afghdOxyu4gZAlVUMbk.json', 'var_call_zivH4mVZy1XxxpT15d8JmV9c': 'file_storage/call_zivH4mVZy1XxxpT15d8JmV9c.json', 'var_call_OLdwQSKHqeRk4po9MwoYiSCZ': 'file_storage/call_OLdwQSKHqeRk4po9MwoYiSCZ.json'}

exec(code, env_args)
