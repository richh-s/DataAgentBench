code = """import json, re
from pathlib import Path

# Load tool results from storage variables
def load_var(v):
    if isinstance(v, str) and Path(v).exists():
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg = load_var(var_call_9iQTzaFRWoqtyrW4eWn3BhHC)
ppv = load_var(var_call_6cLsemcWC4vDh5lgLEkrlojp)
pinfo = load_var(var_call_peOddskcnxsPI36XG3fNukON)

# Build lookup from package tuple to project names
lookup = {}
for r in ppv:
    key = (r.get('System'), r.get('Name'), r.get('Version'))
    lookup.setdefault(key, set()).add(r.get('ProjectName'))

# Collect all ProjectNames for the filtered packages
projects = set()
for r in pkg:
    key = (r.get('System'), r.get('Name'), r.get('Version'))
    pnames = lookup.get(key, set())
    for p in pnames:
        if p:
            projects.add(p)

# Parse project_info to get repo => forks mapping
repo_forks = {}

# Regex patterns to extract forks
patterns = [
    r'forks count of (\d[\d,]*)',
    r'forked (\d[\d,]*) times',
    r'has been forked (\d[\d,]*) times',
    r'has been forked (\d[\d,]*)',
    r'(\d[\d,]*)\s+forks',
    r'forks count is (\d[\d,]*)',
]
repo_regex = re.compile(r'([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)')

for rec in pinfo:
    text = rec.get('Project_Information') or ''
    # find repo (first occurrence)
    m = repo_regex.search(text)
    if not m:
        continue
    repo = m.group(1)
    num = None
    for pat in patterns:
        mm = re.search(pat, text, flags=re.IGNORECASE)
        if mm:
            num = mm.group(1)
            break
    if num:
        try:
            val = int(num.replace(',', ''))
        except:
            continue
        # Keep the maximum observed forks for a repo
        if repo in repo_forks:
            repo_forks[repo] = max(repo_forks[repo], val)
        else:
            repo_forks[repo] = val

# Now intersect projects with repo_forks
rows = []
for p in projects:
    if p in repo_forks:
        rows.append({'ProjectName': p, 'Forks': repo_forks[p]})

# Sort and take top 5
rows_sorted = sorted(rows, key=lambda x: x['Forks'], reverse=True)[:5]

import json
print("__RESULT__:")
print(json.dumps(rows_sorted))"""

env_args = {'var_call_aYbKBvWhi5hwc4rBDwPSY3Sg': ['packageinfo'], 'var_call_XYilLFtpFzkJD7zLGr71GQlG': ['project_info', 'project_packageversion'], 'var_call_9iQTzaFRWoqtyrW4eWn3BhHC': 'file_storage/call_9iQTzaFRWoqtyrW4eWn3BhHC.json', 'var_call_6cLsemcWC4vDh5lgLEkrlojp': 'file_storage/call_6cLsemcWC4vDh5lgLEkrlojp.json', 'var_call_peOddskcnxsPI36XG3fNukON': 'file_storage/call_peOddskcnxsPI36XG3fNukON.json'}

exec(code, env_args)
