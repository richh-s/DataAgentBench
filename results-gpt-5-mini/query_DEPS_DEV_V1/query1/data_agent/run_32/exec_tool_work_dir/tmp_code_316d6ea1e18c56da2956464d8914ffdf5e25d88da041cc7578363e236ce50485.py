code = """import json, re

# Load the data from previous query_db calls which are stored as file paths in the provided variables
# Variables available in this environment (provided by the system):
# var_call_MMzt9waUuV2iz8lNO0MjwGpc, var_call_CLrkvr1Bnp4cScIBWrvl1e1q, var_call_UNlvHcfyNgy88rfLUnKe2473

def load_maybe_json(var):
    if isinstance(var, str) and var.endswith('.json'):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

pkgs = load_maybe_json(var_call_MMzt9waUuV2iz8lNO0MjwGpc)
ppv = load_maybe_json(var_call_CLrkvr1Bnp4cScIBWrvl1e1q)
pinfo = load_maybe_json(var_call_UNlvHcfyNgy88rfLUnKe2473)

# Build project_info mapping from repo -> stars
repo_stars = {}
repo_info_map = {}
repo_pattern = re.compile(r'([A-Za-z0-9_.\-]+/[A-Za-z0-9_.\-]+)')
stars_patterns = [re.compile(r'([\d,]+)\s+stars', re.IGNORECASE),
                  re.compile(r'stars count of\s*([\d,]+)', re.IGNORECASE),
                  re.compile(r'has garnered a total of\s*([\d,]+)\s+stars', re.IGNORECASE),
                  re.compile(r'has a total of\s*([\d,]+)\s+stars', re.IGNORECASE)]

for entry in pinfo:
    pi = entry.get('Project_Information') if isinstance(entry, dict) else None
    if not pi:
        continue
    # find repo
    repo_match = repo_pattern.search(pi)
    if not repo_match:
        continue
    repo = repo_match.group(1)
    # find stars
    stars = None
    for pat in stars_patterns:
        m = pat.search(pi)
        if m:
            try:
                stars = int(m.group(1).replace(',', ''))
            except:
                stars = 0
            break
    if stars is None:
        # try a generic fallback: look for 'star' and parse nearby numbers
        m = re.search(r'([\d,]+)\s*(?:open issues|issues|forks|stars)', pi)
        if m:
            try:
                stars = int(m.group(1).replace(',', ''))
            except:
                stars = 0
        else:
            stars = 0
    # store max if multiple entries
    if repo in repo_stars:
        if stars > repo_stars[repo]:
            repo_stars[repo] = stars
            repo_info_map[repo] = entry
    else:
        repo_stars[repo] = stars
        repo_info_map[repo] = entry

# Index project_packageversion by (System,Name,Version) -> list of ProjectName
ppv_index = {}
for r in ppv:
    key = (r.get('System'), r.get('Name'), r.get('Version'))
    ppv_index.setdefault(key, []).append(r.get('ProjectName'))

# For each latest package, find corresponding project(s) and their stars
results = []
for p in pkgs:
    key = (p.get('System'), p.get('Name'), p.get('Version'))
    project_names = ppv_index.get(key, [])
    best_stars = 0
    best_repo = None
    for proj in project_names:
        if proj in repo_stars:
            if repo_stars[proj] > best_stars:
                best_stars = repo_stars[proj]
                best_repo = proj
    results.append({
        'Name': p.get('Name'),
        'Version': p.get('Version'),
        'ProjectName': best_repo,
        'Stars': best_stars
    })

# Sort by Stars desc and take top 5
results_sorted = sorted(results, key=lambda x: x['Stars'], reverse=True)
top5 = results_sorted[:5]

# Ensure JSON serializable
out = json.dumps(top5)

print("__RESULT__:")
print(out)"""

env_args = {'var_call_MMzt9waUuV2iz8lNO0MjwGpc': 'file_storage/call_MMzt9waUuV2iz8lNO0MjwGpc.json', 'var_call_CLrkvr1Bnp4cScIBWrvl1e1q': 'file_storage/call_CLrkvr1Bnp4cScIBWrvl1e1q.json', 'var_call_UNlvHcfyNgy88rfLUnKe2473': 'file_storage/call_UNlvHcfyNgy88rfLUnKe2473.json'}

exec(code, env_args)
