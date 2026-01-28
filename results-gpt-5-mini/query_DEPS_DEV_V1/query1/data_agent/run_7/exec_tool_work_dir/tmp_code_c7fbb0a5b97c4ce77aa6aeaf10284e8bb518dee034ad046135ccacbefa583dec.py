code = """import json, re

# Load files
with open(var_call_zrluJU3ZETPcFFrWrV6bwh6x, 'r') as f:
    latest_pkg = json.load(f)
with open(var_call_ZpPIHO070TBScmHqfH3e0QiQ, 'r') as f:
    pkg_map = json.load(f)
with open(var_call_F1Cr1axxD8GaZB9t17l1WRvC, 'r') as f:
    proj_info = json.load(f)

# Build repo->stars mapping from project_info
repo_stars = {}
pattern_repo = re.compile(r"project\s+([A-Za-z0-9_.\-]+\/[A-Za-z0-9_.\-]+)")
pattern_stars = re.compile(r"([0-9,]+)\s+stars")

for entry in proj_info:
    pi = entry.get('Project_Information') or ''
    mrepo = pattern_repo.search(pi)
    mstars = pattern_stars.search(pi)
    if mrepo and mstars:
        repo = mrepo.group(1)
        stars = int(mstars.group(1).replace(',', ''))
        if repo in repo_stars:
            if stars > repo_stars[repo]:
                repo_stars[repo] = stars
        else:
            repo_stars[repo] = stars

# Prepare set of latest packages
latest_set = set((p['Name'], p['Version']) for p in latest_pkg)

# Map (Name,Version) to list of ProjectNames
pkg_to_projects = { (n,v): [] for (n,v) in latest_set }
for rec in pkg_map:
    try:
        if rec.get('System') != 'NPM':
            continue
        key = (rec.get('Name'), rec.get('Version'))
        if key in pkg_to_projects:
            pn = rec.get('ProjectName')
            if pn and pn not in pkg_to_projects[key]:
                pkg_to_projects[key].append(pn)
    except Exception:
        continue

# For each latest package compute max stars across its project mappings
pkg_records = []
for (name, version), proj_list in pkg_to_projects.items():
    stars_vals = [repo_stars.get(pn) for pn in proj_list if repo_stars.get(pn) is not None]
    stars = max(stars_vals) if stars_vals else 0
    pkg_records.append({'Name': name, 'Version': version, 'Stars': int(stars), 'ProjectNames': proj_list})

# Sort and take top 5
top5 = sorted(pkg_records, key=lambda x: x['Stars'], reverse=True)[:5]

print('__RESULT__:')
print(json.dumps(top5))"""

env_args = {'var_call_vEKisZqJWopddbWQzMRd4RTg': ['packageinfo'], 'var_call_eYZ4JKovm4apy0FR8ztQOSAQ': ['project_info', 'project_packageversion'], 'var_call_zrluJU3ZETPcFFrWrV6bwh6x': 'file_storage/call_zrluJU3ZETPcFFrWrV6bwh6x.json', 'var_call_ZpPIHO070TBScmHqfH3e0QiQ': 'file_storage/call_ZpPIHO070TBScmHqfH3e0QiQ.json', 'var_call_F1Cr1axxD8GaZB9t17l1WRvC': 'file_storage/call_F1Cr1axxD8GaZB9t17l1WRvC.json', 'var_call_81CTjVJ50QDhfpabUOxCx691': 'file_storage/call_81CTjVJ50QDhfpabUOxCx691.json'}

exec(code, env_args)
