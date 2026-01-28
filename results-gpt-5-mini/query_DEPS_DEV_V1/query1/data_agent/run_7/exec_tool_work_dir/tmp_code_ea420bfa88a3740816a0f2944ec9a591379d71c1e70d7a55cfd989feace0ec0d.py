code = """import json, re

# Load project_info from storage file
with open(var_call_F1Cr1axxD8GaZB9t17l1WRvC, 'r') as f:
    data = json.load(f)

repos = []
pattern_repo = re.compile(r"project\s+([A-Za-z0-9_.\-]+\/[A-Za-z0-9_.\-]+)")
pattern_stars = re.compile(r"([0-9,]+)\s+stars")

for entry in data:
    pi = entry.get('Project_Information') or ''
    if 'star' in pi.lower():
        mrepo = pattern_repo.search(pi)
        mstars = pattern_stars.search(pi)
        if mrepo and mstars:
            repo = mrepo.group(1)
            stars = int(mstars.group(1).replace(',', ''))
            repos.append((repo, stars))

# Sort by stars desc and take top 500
repos_sorted = sorted(repos, key=lambda x: x[1], reverse=True)[:500]
# Prepare output list of repo names
top_repos = [{'ProjectName': r, 'Stars': s} for r,s in repos_sorted]

import json
print("__RESULT__:")
print(json.dumps(top_repos))"""

env_args = {'var_call_vEKisZqJWopddbWQzMRd4RTg': ['packageinfo'], 'var_call_eYZ4JKovm4apy0FR8ztQOSAQ': ['project_info', 'project_packageversion'], 'var_call_zrluJU3ZETPcFFrWrV6bwh6x': 'file_storage/call_zrluJU3ZETPcFFrWrV6bwh6x.json', 'var_call_ZpPIHO070TBScmHqfH3e0QiQ': 'file_storage/call_ZpPIHO070TBScmHqfH3e0QiQ.json', 'var_call_F1Cr1axxD8GaZB9t17l1WRvC': 'file_storage/call_F1Cr1axxD8GaZB9t17l1WRvC.json'}

exec(code, env_args)
