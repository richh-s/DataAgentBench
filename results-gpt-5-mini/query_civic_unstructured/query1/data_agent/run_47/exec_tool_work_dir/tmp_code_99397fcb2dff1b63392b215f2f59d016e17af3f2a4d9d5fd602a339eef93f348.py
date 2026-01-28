code = """import json

# Load data from storage variables (file paths)
with open(var_call_M8qlZNqVuIKl29NBwoSsNyQo, 'r') as f:
    funding_records = json.load(f)
with open(var_call_OpyqoHYzXydQ2FBkZLINPRNp, 'r') as f:
    civic_docs = json.load(f)

# Normalization helper
import unicodedata, re

def normalize(s):
    if s is None:
        return ""
    s = str(s).lower()
    s = unicodedata.normalize('NFKD', s)
    s = re.sub(r'[^a-z0-9]+', ' ', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

# Extract project titles from the 'Design' section
design_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    low = text
    start_tag = 'Capital Improvement Projects (Design)'
    if start_tag.lower() in low.lower():
        # find start index case-insensitive
        li = low.lower().find(start_tag.lower())
        start = li + len(start_tag)
        # find end - next section markers
        end_markers = ['Capital Improvement Projects (Construction)'.lower(), 'Capital Improvement Projects (Not Started)'.lower(), 'Capital Improvement Projects ('.lower()]
        end = None
        tail = low[start:]
        for em in end_markers:
            idx = tail.lower().find(em)
            if idx != -1:
                end = start + idx
                break
        if end is None:
            end = start + 2000
        section = low[start:end]
        # split into lines and choose candidate titles as lines with length and with letters
        lines = [ln.strip() for ln in section.splitlines()]
        for ln in lines:
            if not ln:
                continue
            # skip obvious non-title lines
            if any(ln.lower().startswith(x) for x in ['updates', 'project schedule', 'page', 'recommended', 'discussion', '(cid']):
                continue
            if 3 <= len(ln) <= 120 and re.search('[A-Za-z]', ln):
                # avoid lines that are sentences (contain period) or very long phrases with multiple clauses
                if '.' in ln and len(ln) < 50:
                    continue
                # Take lines that start with uppercase letter or all caps or contain keywords
                if ln[0].isupper() or ln.isupper() or any(k in ln.lower() for k in ['project','park','road','repair','improvements','walkway','playground','median','biofilter','drain']):
                    # cleanup
                    title = ln.rstrip(':').strip()
                    # avoid generic headings
                    if any(g in title.lower() for g in ['agenda','item','to:','prepared by','approved by','date prepared']):
                        continue
                    design_projects.append(title)

# deduplicate preserving order
seen = set()
design_projects_unique = []
for p in design_projects:
    np = p.strip()
    if np.lower() not in seen:
        seen.add(np.lower())
        design_projects_unique.append(np)

# Normalize funding records and convert Amount
for fr in funding_records:
    fr['norm_name'] = normalize(fr.get('Project_Name'))
    try:
        fr['Amount'] = int(fr.get('Amount'))
    except:
        try:
            fr['Amount'] = int(str(fr.get('Amount')).replace(',',''))
        except:
            fr['Amount'] = 0

# Match design projects to funding >50000
matched_projects = []
matched_funding_records = []
for dp in design_projects_unique:
    n_dp = normalize(dp)
    matched = False
    for fr in funding_records:
        if fr['Amount'] > 50000:
            nf = fr['norm_name']
            if n_dp == nf or n_dp in nf or nf in n_dp:
                matched = True
                matched_funding_records.append({'Project_Name': fr.get('Project_Name'), 'Amount': fr.get('Amount')})
    if matched:
        matched_projects.append(dp)

# unique matched projects
mp_seen = set()
matched_projects_unique = []
for p in matched_projects:
    np = normalize(p)
    if np not in mp_seen:
        mp_seen.add(np)
        matched_projects_unique.append(p)

result = {'count': len(matched_projects_unique), 'projects': matched_projects_unique, 'matched_funding_records_count': len(matched_funding_records)}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_M8qlZNqVuIKl29NBwoSsNyQo': 'file_storage/call_M8qlZNqVuIKl29NBwoSsNyQo.json', 'var_call_OpyqoHYzXydQ2FBkZLINPRNp': 'file_storage/call_OpyqoHYzXydQ2FBkZLINPRNp.json'}

exec(code, env_args)
