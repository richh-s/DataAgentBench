code = """import json
import pandas as pd
import re

# Load results from storage variables (they may be file paths or already lists)

def load_var(v):
    if isinstance(v, str):
        # assume it's a file path to JSON
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg_records = load_var(var_call_am6hhnfUfw7SPCRyAcX9tV0g)
map_records = load_var(var_call_bjkfRhdFgTmEeRzJFIXMqhdP)
proj_records = load_var(var_call_KtGXEIxsWbYECa7wpbwgg3KS)

# DataFrames
df_pkg = pd.DataFrame(pkg_records)
df_map = pd.DataFrame(map_records)
df_proj = pd.DataFrame(proj_records)

# Merge package releases with project mapping
if not df_pkg.empty and not df_map.empty:
    df_merged = pd.merge(df_pkg, df_map, on=["System", "Name", "Version"], how='inner')
else:
    df_merged = pd.DataFrame(columns=["System","Name","Version","ProjectName"]) 

# Get unique project names from merged
project_names = df_merged['ProjectName'].dropna().unique().tolist()
project_names_lower = {p.lower(): p for p in project_names}

# Helper to parse licenses field into list
def parse_licenses(s):
    if s is None:
        return []
    if isinstance(s, list):
        return s
    try:
        parsed = json.loads(s)
        if isinstance(parsed, list):
            return parsed
    except Exception:
        pass
    # fallback: check for "MIT" substring
    if 'MIT' in str(s):
        return ['MIT']
    return []

# Extract repo and forks from Project_Information
repo_pattern = re.compile(r'([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)')
# Several patterns for forks
fork_patterns = [
    re.compile(r'forks?[,\s\w]{0,20}?([0-9,]+)', re.IGNORECASE),
    re.compile(r'forked\s+([0-9,]+)\s+times', re.IGNORECASE),
    re.compile(r'forks count of\s*([0-9,]+)', re.IGNORECASE),
    re.compile(r'forks count[:\s]*([0-9,]+)', re.IGNORECASE),
]

proj_infos = []
for rec in proj_records:
    pi = rec.get('Project_Information') if isinstance(rec, dict) else None
    lic = rec.get('Licenses') if isinstance(rec, dict) else None
    licenses = parse_licenses(lic)
    if 'MIT' not in licenses:
        continue
    if not pi:
        continue
    # find repo - choose first repo-like token after 'project' or 'GitHub project' if possible
    repo_match = None
    # try to find patterns like 'The project owner/repo' or 'The GitHub project owner/repo'
    m = re.search(r'(?:The project|The GitHub project|The project on GitHub|The GitHub repository|The project named)\s+([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)', pi)
    if m:
        repo_match = m.group(1)
    else:
        # fallback to any owner/repo
        m2 = repo_pattern.search(pi)
        if m2:
            repo_match = m2.group(1)
    # extract forks
    forks = None
    for fp in fork_patterns:
        m = fp.search(pi)
        if m:
            num = m.group(1)
            try:
                forks = int(num.replace(',', ''))
                break
            except:
                pass
    # sometimes project info says 'has been forked X times' or 'has X forks, and Y stars' etc
    if forks is None:
        m = re.search(r'has\s+([0-9,]+)\s+forks', pi, re.IGNORECASE)
        if m:
            try:
                forks = int(m.group(1).replace(',', ''))
            except:
                forks = None

    # if still None, try to find the last number after 'fork' word
    if forks is None and repo_match:
        # find all numbers and take one near 'fork'
        all_nums = [(mo.group(0), mo.start()) for mo in re.finditer(r'[0-9,]+', pi)]
        fork_word_pos = pi.lower().find('fork')
        if fork_word_pos != -1 and all_nums:
            # choose the number with minimum distance to fork_word_pos
            best = None
            best_dist = None
            for num, pos in all_nums:
                dist = abs(pos - fork_word_pos)
                if best is None or dist < best_dist:
                    try:
                        val = int(num.replace(',', ''))
                        best = val
                        best_dist = dist
                    except:
                        continue
            forks = best

    if repo_match and forks is not None:
        proj_infos.append({'repo': repo_match, 'forks': forks, 'Project_Information': pi})

# Build lookup from repo lower -> info (if multiple, keep max forks)
repo_info = {}
for p in proj_infos:
    k = p['repo'].lower()
    if k in repo_info:
        if p['forks'] > repo_info[k]['forks']:
            repo_info[k] = p
    else:
        repo_info[k] = p

# Now, for each project name from merged mapping, find forks if license MIT
results = []
for pn in project_names:
    key = pn.lower()
    if key in repo_info:
        results.append({'ProjectName': pn, 'Forks': repo_info[key]['forks'], 'Project_Information': repo_info[key]['Project_Information']})

# If some project_names are in different format (like owner/repo vs owner/repo.git), normalize
# Also, try matching by ignoring .git suffix or case
if not results:
    # attempt matching by trimming possible '.git' suffix and matching prefixes
    for pn in project_names:
        k = pn.lower().rstrip('.git')
        for repo_k, info in repo_info.items():
            if repo_k.rstrip('.git') == k:
                results.append({'ProjectName': pn, 'Forks': info['forks'], 'Project_Information': info['Project_Information']})

# Sort results by forks desc and take top 5
results_sorted = sorted(results, key=lambda x: x['Forks'], reverse=True)[:5]

# Prepare final output list
final = []
for r in results_sorted:
    final.append({'ProjectName': r['ProjectName'], 'Forks': r['Forks'], 'Project_Information': r['Project_Information']})

import json
print("__RESULT__:")
print(json.dumps(final))"""

env_args = {'var_call_am6hhnfUfw7SPCRyAcX9tV0g': 'file_storage/call_am6hhnfUfw7SPCRyAcX9tV0g.json', 'var_call_bjkfRhdFgTmEeRzJFIXMqhdP': 'file_storage/call_bjkfRhdFgTmEeRzJFIXMqhdP.json', 'var_call_KtGXEIxsWbYECa7wpbwgg3KS': 'file_storage/call_KtGXEIxsWbYECa7wpbwgg3KS.json'}

exec(code, env_args)
