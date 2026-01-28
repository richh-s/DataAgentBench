code = """import json
import re

# Load the data files from previous tool calls
with open(var_call_BlrHgWqyl55XUVYLjxmR5g0W, 'r') as f:
    packages = json.load(f)
with open(var_call_3FONgrMOrEeljYTn8rABMdeD, 'r') as f:
    proj_pkg = json.load(f)
with open(var_call_75162DN7WTh495bZ9jZviXBw, 'r') as f:
    proj_info = json.load(f)

# Helper to safely parse JSON-like strings
def try_load(s):
    if s is None:
        return None
    s = s.strip()
    try:
        return json.loads(s)
    except Exception:
        # fallback: try to fix common issues
        try:
            return json.loads(s.replace("\'", '"'))
        except Exception:
            return None

# Filter packages: NPM, Licenses contains MIT, VersionInfo.IsRelease == true
mit_release_keys = set()
for p in packages:
    try:
        if p.get('System') != 'NPM':
            continue
        lic = try_load(p.get('Licenses', '[]'))
        if not lic or 'MIT' not in lic:
            continue
        vinfo = try_load(p.get('VersionInfo', '{}'))
        if not vinfo or not vinfo.get('IsRelease'):
            continue
        key = (p.get('System'), p.get('Name'), p.get('Version'))
        mit_release_keys.add(key)
    except Exception:
        continue

# Map matching project_packageversion entries
project_names = set()
for r in proj_pkg:
    key = (r.get('System'), r.get('Name'), r.get('Version'))
    if key in mit_release_keys:
        pn = r.get('ProjectName')
        if pn:
            project_names.add(pn)

# Build a mapping from project_info Project_Information to its record for faster search
# We'll search Project_Information text to find occurrence of project_name
proj_info_texts = [rec.get('Project_Information','') for rec in proj_info]

# Function to extract forks from a text
num_re = re.compile(r"([0-9][0-9,]*)\s*(?:forks|fork)\b", re.IGNORECASE)

def extract_forks(text):
    matches = num_re.findall(text or '')
    if not matches:
        # also try patterns like 'been forked 12 times'
        m2 = re.search(r"been forked\s*([0-9][0-9,]*)", text or '', re.IGNORECASE)
        if m2:
            return int(m2.group(1).replace(',',''))
        return 0
    # pick the largest numeric match
    nums = [int(m.replace(',','')) for m in matches]
    return max(nums)

# For each project_name, find best matching project_info entry (first that contains it)
results = []
for pn in project_names:
    # search
    matched = None
    for rec in proj_info:
        pi = rec.get('Project_Information','')
        if pn in pi:
            matched = rec
            break
    forks = 0
    if matched:
        forks = extract_forks(matched.get('Project_Information',''))
    else:
        # try a looser match using only repo name part after '/'
        repo_part = pn.split('/')[-1]
        for rec in proj_info:
            pi = rec.get('Project_Information','')
            if repo_part in pi:
                matched = rec
                forks = extract_forks(pi)
                break
    results.append({'ProjectName': pn, 'Forks': forks})

# Deduplicate by ProjectName (already set), sort by forks desc
results_sorted = sorted(results, key=lambda x: x['Forks'], reverse=True)
top5 = results_sorted[:5]

import json
print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_call_BlrHgWqyl55XUVYLjxmR5g0W': 'file_storage/call_BlrHgWqyl55XUVYLjxmR5g0W.json', 'var_call_JMR1M6fIMwN2XrDDQM2bacgy': ['project_info', 'project_packageversion'], 'var_call_75162DN7WTh495bZ9jZviXBw': 'file_storage/call_75162DN7WTh495bZ9jZviXBw.json', 'var_call_3FONgrMOrEeljYTn8rABMdeD': 'file_storage/call_3FONgrMOrEeljYTn8rABMdeD.json'}

exec(code, env_args)
