code = """import json, re
# Load files from storage paths
pkg_path = var_call_VjfWGqbT4O4J9Z3nOXU8Ab5K
ppv_path = var_call_PkOqmdeUT7VwIzFiO0NVR4nA
pinfo_path = var_call_bz8cq4VjmBoy2JJ39MAi4yUg
with open(pkg_path, 'r', encoding='utf-8') as f:
    pkg_data = json.load(f)
with open(ppv_path, 'r', encoding='utf-8') as f:
    ppv_data = json.load(f)
with open(pinfo_path, 'r', encoding='utf-8') as f:
    pinfo_data = json.load(f)

# Build set of (Name,Version) from package pairs
pairs = {(p['Name'], p['Version']) for p in pkg_data.get('pairs', [])}
# Filter project_packageversion entries matching those pairs
matched_projects = set()
for rec in ppv_data:
    if rec.get('System') == 'NPM' and (rec.get('Name'), rec.get('Version')) in pairs:
        proj = rec.get('ProjectName')
        if proj:
            matched_projects.add(proj)
matched_projects = sorted(matched_projects)

# Helper to extract forks count from Project_Information text
number_re = re.compile(r"([0-9]{1,3}(?:,[0-9]{3})*|[0-9]+)")
fork_patterns = [re.compile(r'([0-9,]+)\s*(?:forks|fork)\b', re.IGNORECASE),
                 re.compile(r'forked\s*([0-9,]+)', re.IGNORECASE),
                 re.compile(r'been forked\s*([0-9,]+)', re.IGNORECASE),
                 re.compile(r'forks count of\s*([0-9,]+)', re.IGNORECASE)]

def extract_forks(s):
    if not s:
        return None
    for pat in fork_patterns:
        m = pat.search(s)
        if m:
            num = m.group(1)
            try:
                return int(num.replace(',', ''))
            except:
                pass
    # fallback: find 'fork' and nearest number before it
    sl = s.lower()
    idx = sl.find('fork')
    if idx != -1:
        # find all numbers with spans
        for m in number_re.finditer(s):
            start, end = m.span()
            if end <= idx + 20:  # allow numbers up to 20 chars before 'fork'
                last_num = m.group(1)
        try:
            return int(last_num.replace(',', ''))
        except:
            return None
    return None

# For each matched project name, find project_info entries containing it
results = []
for proj in matched_projects:
    found = False
    for rec in pinfo_data:
        pi = rec.get('Project_Information') or ''
        if proj in pi:
            forks = extract_forks(pi)
            results.append({'ProjectName': proj, 'Forks': forks, 'Project_Information': pi})
            found = True
            break
    if not found:
        # no project_info match; include with forks = None
        results.append({'ProjectName': proj, 'Forks': None, 'Project_Information': None})

# Keep only those with forks not None, sort by forks desc
with_forks = [r for r in results if r['Forks'] is not None]
with_forks.sort(key=lambda x: x['Forks'], reverse=True)
# take top 5
top5 = with_forks[:5]
# If fewer than 5, include entries with None forks until 5
if len(top5) < 5:
    others = [r for r in results if r['Forks'] is None]
    top5.extend(others[:5-len(top5)])

# Prepare output
out = top5
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_9WXql6CNrMRLYiHsQOH17uQs': 'file_storage/call_9WXql6CNrMRLYiHsQOH17uQs.json', 'var_call_VjfWGqbT4O4J9Z3nOXU8Ab5K': 'file_storage/call_VjfWGqbT4O4J9Z3nOXU8Ab5K.json', 'var_call_PkOqmdeUT7VwIzFiO0NVR4nA': 'file_storage/call_PkOqmdeUT7VwIzFiO0NVR4nA.json', 'var_call_bz8cq4VjmBoy2JJ39MAi4yUg': 'file_storage/call_bz8cq4VjmBoy2JJ39MAi4yUg.json'}

exec(code, env_args)
