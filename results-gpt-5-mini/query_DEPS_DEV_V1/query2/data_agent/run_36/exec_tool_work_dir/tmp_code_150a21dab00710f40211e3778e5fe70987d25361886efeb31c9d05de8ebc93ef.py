code = """import json, re
# Load files
pck_path = var_call_w7ZuVRkYUn4Gu7SpWccSzHVL
ppv_path = var_call_M6Q0rrpmAJZ6OZfdr1nqHru3
pinfo_path = var_call_ukDcz9BPczGPF2UTPdFHqhF0
with open(pck_path, 'r', encoding='utf-8') as f:
    pcks = json.load(f)
with open(ppv_path, 'r', encoding='utf-8') as f:
    ppvs = json.load(f)
with open(pinfo_path, 'r', encoding='utf-8') as f:
    pinfos = json.load(f)
# Build set of (Name,Version) from packageinfo records (System should be NPM already)
pkg_set = set((r['Name'], r['Version']) for r in pcks if r.get('Name') and r.get('Version'))
# Map project_packageversion entries to project names if they match
proj_names = {}
for r in ppvs:
    if r.get('System')!='NPM':
        continue
    key = (r.get('Name'), r.get('Version'))
    if key in pkg_set:
        proj = r.get('ProjectName')
        if proj:
            proj_names.setdefault(proj, []).append(key)
# Build mapping from project_info Project_Information to forks count
# Also create a mapping from repo name to fork counts by searching Project_Information text for repo
# We'll attempt to match each proj_name by substring in Project_Information
# Preprocess project_info entries into list
pinfo_texts = [entry.get('Project_Information','') for entry in pinfos]
# function to extract forks
def extract_forks(text):
    # try patterns: 'X forks', 'forks count of X', 'been forked X times', 'forks count of X'
    patterns = [r'([0-9,]+)\s+forks', r'forked\s+([0-9,]+)\s+times', r'forks count of\s*([0-9,]+)', r'forks: ([0-9,]+)']
    for pat in patterns:
        m = re.search(pat, text, flags=re.IGNORECASE)
        if m:
            num = m.group(1)
            num = int(num.replace(',',''))
            return num
    # fallback: try to find 'fork' and nearby number
    m = re.search(r'([0-9,]+)\s+(?:stars,?\s+and\s+)?[0-9,]+\s+forks', text, flags=re.IGNORECASE)
    if m:
        return int(m.group(1).replace(',',''))
    return None
# For each proj in proj_names, search pinfo_texts to find a matching Project_Information that contains the proj (owner/repo)
results = []
for proj in proj_names.keys():
    matched_forks = None
    # search for exact proj substring
    for txt in pinfo_texts:
        if proj in txt:
            f = extract_forks(txt)
            if f is not None:
                matched_forks = f
                break
    # if not found, try splitting proj into repo (after /) and search for repo name with owner
    if matched_forks is None:
        owner_repo = proj
        parts = proj.split('/')
        if len(parts)==2:
            owner, repo = parts
            for txt in pinfo_texts:
                if f'{owner}/{repo}' in txt or repo in txt:
                    f = extract_forks(txt)
                    if f is not None:
                        matched_forks = f
                        break
    if matched_forks is not None:
        results.append({'project': proj, 'forks': matched_forks, 'packages': proj_names[proj]})
# If no results found, return empty
# Sort by forks desc and take top 5
results_sorted = sorted(results, key=lambda x: x['forks'], reverse=True)[:5]
# Prepare output: list of dicts with project and forks
out = [{'project': r['project'], 'forks': r['forks']} for r in results_sorted]
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_w7ZuVRkYUn4Gu7SpWccSzHVL': 'file_storage/call_w7ZuVRkYUn4Gu7SpWccSzHVL.json', 'var_call_IxA7XUhlcREjW05n5cTzF5ho': 'file_storage/call_IxA7XUhlcREjW05n5cTzF5ho.json', 'var_call_M6Q0rrpmAJZ6OZfdr1nqHru3': 'file_storage/call_M6Q0rrpmAJZ6OZfdr1nqHru3.json', 'var_call_ukDcz9BPczGPF2UTPdFHqhF0': 'file_storage/call_ukDcz9BPczGPF2UTPdFHqhF0.json'}

exec(code, env_args)
