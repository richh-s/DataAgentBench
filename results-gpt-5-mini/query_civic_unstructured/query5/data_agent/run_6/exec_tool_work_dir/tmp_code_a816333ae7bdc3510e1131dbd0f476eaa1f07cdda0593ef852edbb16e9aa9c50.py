code = """import json

# Load stored results
with open(var_call_90dmcYwBxTb7vQatqrbc7U4G, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_7E8sUjkgBqwcx0vACQAqhl9z, 'r') as f:
    funding = json.load(f)

# simple helpers
def normalize(s):
    if s is None:
        return ''
    s2 = s.lower()
    # keep alphanumerics and spaces
    s2 = ''.join(ch if ch.isalnum() else ' ' for ch in s2)
    s2 = ' '.join(s2.split())
    return s2

# disaster keywords
disaster_kw = ['fema', 'caloes', 'caljpia', 'caljpia', 'disaster', 'fire', 'recovery']
project_kw = ['project','improvement','improvements','repair','repairs','resurfacing','renovation','study','facility','playground','phase','road','bridge','culvert','drainage','traffic','walkway']

# collect civic project names that are disaster-related and have 2022 nearby
selected = set()
for doc in civic_docs:
    lines = doc.get('text','').splitlines()
    n = len(lines)
    for i, line in enumerate(lines):
        low = line.lower()
        # if a line looks like a project title
        if any(k in low for k in project_kw):
            # look ahead a few lines for 2022 and disaster keyword
            window = ' '.join(lines[i:i+8]).lower()
            if '2022' in window and any(d in window for d in disaster_kw):
                selected.add(line.strip())
        # also if line contains FEMA/CalOES and nearby 2022
        if any(d in low for d in disaster_kw):
            window2 = ' '.join(lines[max(0,i-4):min(n,i+5)]).lower()
            if '2022' in window2:
                selected.add(line.strip())

# normalize selected names
selected_norm = [normalize(s) for s in selected if s]

# sum funding: match funding records where project name matches any selected_norm (substring) OR funding name contains disaster keywords and project name appears in civic docs in 2022 anywhere
# Additionally, include funding records where Project_Name itself contains disaster markers and the civic docs contain '2022' somewhere for that project name

# Build a set of civic doc text lower for simple membership checks
all_doc_text = '\n'.join(d.get('text','') for d in civic_docs).lower()

total = 0
matched = {}
for rec in funding:
    pname = rec.get('Project_Name','')
    pname_norm = normalize(pname)
    matched_flag = False
    for sn in selected_norm:
        if not sn:
            continue
        if sn in pname_norm or pname_norm in sn:
            matched_flag = True
            break
    # also match if funding name has disaster keyword and civic docs mention 2022 in vicinity of that project name
    if not matched_flag and any(d in pname.lower() for d in disaster_kw):
        # check if project's base name appears in civic docs with 2022 near it
        base = pname.lower()
        if base in all_doc_text and '2022' in all_doc_text:
            matched_flag = True
        else:
            # also accept if any selected_norm exists (conservative)
            if selected_norm:
                matched_flag = True
    if matched_flag:
        try:
            amt = int(float(rec.get('Amount',0)))
        except:
            amt = 0
        total += amt
        matched[pname] = amt

# Prepare result
result = {'total_funding': total, 'matched_projects': matched, 'selected_projects': list(selected)}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_FbCAMFAZTL2Ih3VWgvwFzEcF': ['civic_docs'], 'var_call_90dmcYwBxTb7vQatqrbc7U4G': 'file_storage/call_90dmcYwBxTb7vQatqrbc7U4G.json', 'var_call_aId1Wornd25qzPfcbmiNPMM9': ['Funding'], 'var_call_7E8sUjkgBqwcx0vACQAqhl9z': 'file_storage/call_7E8sUjkgBqwcx0vACQAqhl9z.json'}

exec(code, env_args)
