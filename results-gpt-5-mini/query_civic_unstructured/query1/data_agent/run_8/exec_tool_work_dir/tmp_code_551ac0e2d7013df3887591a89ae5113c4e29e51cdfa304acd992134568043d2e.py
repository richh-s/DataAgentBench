code = """import json, re, string

docs_path = var_call_AvuBLWcpqQ0SJshtO6YsIDvN
fund_path = var_call_s1fX0ebjWAdtFmejFM65oemZ

with open(docs_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)
with open(fund_path, 'r', encoding='utf-8') as f:
    funds = json.load(f)

def normalize(s):
    if s is None:
        return ""
    s = str(s).lower()
    s = s.translate(str.maketrans('', '', string.punctuation))
    s = re.sub(r'\s+', ' ', s).strip()
    return s

design_projects = set()
for doc in docs:
    text = doc.get('text','')
    # heuristic 1: previous line before 'Updates:'
    lines = text.splitlines()
    for i,l in enumerate(lines):
        if 'updates' in l.lower():
            k = i-1
            while k>=0 and (not lines[k].strip() or lines[k].strip().lower().startswith('page') or 'agenda' in lines[k].lower()):
                k -= 1
            if k>=0:
                candidate = lines[k].strip()
                if len(candidate) > 2:
                    design_projects.add(candidate)
    # heuristic 2: explicit Design block
    m = re.search(r'Capital Improvement Projects\s*\(Design\)(.*?)(Capital Improvement Projects\s*\(Construction\)|Capital Improvement Projects\s*\(Not Started\)|$)', text, flags=re.S|re.I)
    if m:
        block = m.group(1)
        blines = block.splitlines()
        for l in blines:
            s = l.strip()
            if not s:
                continue
            low = s.lower()
            if any(x in low for x in ['updates','project schedule','(','cid','page','agenda','item']):
                continue
            if ':' in s or '.' in s:
                continue
            words = s.split()
            if len(words) >= 2 and len(words) <= 12:
                # likely a project title
                design_projects.add(s)
            else:
                # also accept if ends with 'Project' or contains 'improvements' or 'repairs' or 'resurfacing' or 'repair'
                if s.lower().endswith('project') or any(k in s.lower() for k in ['improvements','repairs','resurfacing','repair','study','plan','facility','park','road','drain']):
                    design_projects.add(s)

# Normalize set
candidate_projects = sorted(list(design_projects))

# Prepare funding lookup
fund_records = funds

matching_projects = []
for proj in candidate_projects:
    nproj = normalize(proj)
    if not nproj:
        continue
    matched = False
    for rec in fund_records:
        fpn = rec.get('Project_Name','')
        if fpn is None:
            continue
        nfpn = normalize(fpn)
        if not nfpn:
            continue
        if nproj in nfpn or nfpn in nproj:
            # parse amount
            amt_raw = rec.get('Amount', 0)
            try:
                amt = int(str(amt_raw).replace(',',''))
            except:
                try:
                    amt = int(float(amt_raw))
                except:
                    amt = 0
            if amt > 50000:
                matched = True
                break
    if matched:
        matching_projects.append(proj)

matching_projects = sorted(list(set(matching_projects)))
count = len(matching_projects)

out = {'count': count, 'projects': matching_projects}
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_AvuBLWcpqQ0SJshtO6YsIDvN': 'file_storage/call_AvuBLWcpqQ0SJshtO6YsIDvN.json', 'var_call_s1fX0ebjWAdtFmejFM65oemZ': 'file_storage/call_s1fX0ebjWAdtFmejFM65oemZ.json'}

exec(code, env_args)
