code = """import json, re
# Load data from storage variables
with open(var_call_M8qlZNqVuIKl29NBwoSsNyQo, 'r') as f:
    funding_records = json.load(f)
with open(var_call_OpyqoHYzXydQ2FBkZLINPRNp, 'r') as f:
    civic_docs = json.load(f)

# Helper to normalize names for fuzzy matching
import unicodedata
import re

def normalize(s):
    if s is None:
        return ""
    s = str(s).lower()
    s = unicodedata.normalize('NFKD', s)
    s = re.sub(r"[^a-z0-9]+", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

# Extract project names under Capital Improvement Projects (Design)
design_projects = []
for doc in civic_docs:
    text = doc.get('text','')
    if not text:
        continue
    # Find the design section
    m = re.search(r'Capital Improvement Projects\s*\(Design\)(.*?)(Capital Improvement Projects\s*\(Construction\)|Capital Improvement Projects\s*\(Not Started\)|Capital Improvement Projects\s*\(\w+\)|$)', text, flags=re.IGNORECASE|re.DOTALL)
    section = None
    if m:
        section = m.group(1)
    else:
        # fallback: find 'Capital Improvement Projects (Design)' and take next 1000 chars
        m2 = re.search(r'Capital Improvement Projects\s*\(Design\)', text, flags=re.IGNORECASE)
        if m2:
            start = m2.end()
            section = text[start:start+2000]
    if not section:
        continue
    # Find candidate project names: lines followed by double newline and '(cid' or 'Updates' or 'Project Schedule' etc
    # We'll split by double newlines and take segments where first line looks like a title
    parts = re.split(r"\n\s*\n", section)
    for i in range(len(parts)):
        part = parts[i].strip()
        if not part:
            continue
        # Exclude sections that start with words like 'Updates', 'Project Schedule', 'Page', 'RECOMMENDED', 'DISCUSSION'
        if re.match(r'^(updates|project schedule|page|recommended|discussion|agenda|begin construction|advertise)', part, flags=re.IGNORECASE):
            continue
        # Consider first line as project name candidate
        first_line = part.splitlines()[0].strip()
        # Heuristic: valid project name is 3-120 chars and contains letters and not too many lowercase words only
        if 3 <= len(first_line) <= 120 and re.search('[A-Za-z]', first_line):
            # Avoid generic headings
            if re.search(r'(capital improvement|projects status|agenda|item|prepared by|meeting date)', first_line, flags=re.IGNORECASE):
                continue
            # Further filter out lines that are sentences (contain periods) or start with lowercase
            if first_line.endswith(':'):
                first_line = first_line[:-1].strip()
            if re.match(r'^[A-Z0-9][A-Za-z0-9 &\-\'/(),.#]+$', first_line):
                design_projects.append(first_line)

# Deduplicate while preserving order
seen = set()
design_projects_unique = []
for p in design_projects:
    pn = p.strip()
    if pn.lower() not in seen:
        seen.add(pn.lower())
        design_projects_unique.append(pn)

# Prepare funding lookup
funding_list = funding_records
# Normalize funding names
for fr in funding_list:
    fr['norm_name'] = normalize(fr.get('Project_Name'))
    try:
        fr['Amount'] = int(fr.get('Amount'))
    except:
        try:
            fr['Amount'] = int(str(fr.get('Amount')).replace(',',''))
        except:
            fr['Amount'] = 0

# For each design project, see if there's funding > 50000
matched_projects = []
matched_funding_records = []
for dp in design_projects_unique:
    n_dp = normalize(dp)
    matched = False
    for fr in funding_list:
        nf = fr['norm_name']
        # match if one contains the other and amount>50000
        if fr['Amount'] > 50000 and (n_dp == nf or n_dp in nf or nf in n_dp):
            matched = True
            matched_funding_records.append({'Project_Name': fr.get('Project_Name'), 'Amount': fr.get('Amount')})
    if matched:
        matched_projects.append(dp)

# Unique matched project names and count
matched_projects_unique = []
mp_seen = set()
for p in matched_projects:
    npn = normalize(p)
    if npn not in mp_seen:
        mp_seen.add(npn)
        matched_projects_unique.append(p)

result = {'count': len(matched_projects_unique), 'projects': matched_projects_unique, 'matched_funding_records_count': len(matched_funding_records)}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_M8qlZNqVuIKl29NBwoSsNyQo': 'file_storage/call_M8qlZNqVuIKl29NBwoSsNyQo.json', 'var_call_OpyqoHYzXydQ2FBkZLINPRNp': 'file_storage/call_OpyqoHYzXydQ2FBkZLINPRNp.json'}

exec(code, env_args)
