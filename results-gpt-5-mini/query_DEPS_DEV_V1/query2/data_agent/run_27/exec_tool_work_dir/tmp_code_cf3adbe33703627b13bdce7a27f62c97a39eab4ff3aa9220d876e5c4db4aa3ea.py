code = """import json, re

# Load data from previous query results stored as file paths
with open(var_call_S5kAoiLQdSOlImC6zd28VPpZ, 'r') as f:
    pkg_records = json.load(f)
with open(var_call_FMbMUgiT4l6cZkndJf2alfWN, 'r') as f:
    proj_pkg_records = json.load(f)
with open(var_call_ldidmCmwEdbBIcZgSPRo9mxI, 'r') as f:
    proj_info_records = json.load(f)

# Build set of package tuples (System, Name, Version)
pkg_set = set((r['System'], r['Name'], r['Version']) for r in pkg_records)

# Map packages to project names
matched_projects = set()
for r in proj_pkg_records:
    key = (r.get('System'), r.get('Name'), r.get('Version'))
    if key in pkg_set:
        pname = r.get('ProjectName')
        if pname:
            matched_projects.add(pname)

# Parse project_info entries into mapping repo -> (forks, licenses)
repo_info = {}

# regex patterns
repo_pattern = re.compile(r'([A-Za-z0-9_.\-]+/[A-Za-z0-9_.\-]+)')
# various fork patterns
fork_patterns = [
    re.compile(r'([0-9]{1,3}(?:,[0-9]{3})*)\s+forks'),
    re.compile(r'forks count of\s*([0-9]{1,3}(?:,[0-9]{3})*)'),
    re.compile(r'has been forked\s*([0-9]{1,3}(?:,[0-9]{3})*)\s+times'),
    re.compile(r'forked\s*([0-9]{1,3}(?:,[0-9]{3})*)\s+times'),
    re.compile(r'and\s*([0-9]{1,3}(?:,[0-9]{3})*)\s+forks'),
    re.compile(r'has garnered a total of\s*([0-9]{1,3}(?:,[0-9]{3})*)\s+stars and\s*([0-9]{1,3}(?:,[0-9]{3})*)\s+forks'),
]

for rec in proj_info_records:
    info = rec.get('Project_Information') or ''
    licenses = rec.get('Licenses') or ''
    # find first repo-like token
    repo_matches = repo_pattern.findall(info)
    repo = None
    if repo_matches:
        # choose the first match that looks like owner/repo (avoid matching URLs with github.com/... maybe picks the path)
        repo = repo_matches[0]
    # find fork count
    forks = None
    # try specific pattern with two groups (stars and forks)
    m = re.search(r'([0-9]{1,3}(?:,[0-9]{3})*)\s+stars(?:,|\s+and)?\s+(?:and\s+)?([0-9]{1,3}(?:,[0-9]{3})*)\s+forks', info)
    if m:
        forks = m.group(2)
    else:
        for p in fork_patterns:
            m = p.search(info)
            if m:
                # Some patterns capture stars then forks; handle accordingly
                forks = m.group(1)
                # If pattern captured stars and forks in groups, handle above
                break
    if forks:
        forks = int(forks.replace(',', ''))
    # store if we have a repo
    if repo:
        existing = repo_info.get(repo)
        # prefer non-None forks
        if existing:
            # update forks to max if present
            ex_forks = existing.get('forks')
            if forks is not None:
                if ex_forks is None or forks > ex_forks:
                    existing['forks'] = forks
        else:
            repo_info[repo] = {'forks': forks, 'licenses': licenses}

# Now, filter matched_projects by those present in repo_info and having MIT license
results = []
for proj in matched_projects:
    info = repo_info.get(proj)
    if not info:
        continue
    lic = info.get('licenses') or ''
    # simple check for MIT in license string
    if 'MIT' in lic:
        forks = info.get('forks') if info.get('forks') is not None else 0
        results.append({'ProjectName': proj, 'Forks': int(forks)})

# sort by forks desc and take top 5
results_sorted = sorted(results, key=lambda x: x['Forks'], reverse=True)[:5]

import json
print("__RESULT__:")
print(json.dumps(results_sorted))"""

env_args = {'var_call_S5kAoiLQdSOlImC6zd28VPpZ': 'file_storage/call_S5kAoiLQdSOlImC6zd28VPpZ.json', 'var_call_FMbMUgiT4l6cZkndJf2alfWN': 'file_storage/call_FMbMUgiT4l6cZkndJf2alfWN.json', 'var_call_ldidmCmwEdbBIcZgSPRo9mxI': 'file_storage/call_ldidmCmwEdbBIcZgSPRo9mxI.json'}

exec(code, env_args)
