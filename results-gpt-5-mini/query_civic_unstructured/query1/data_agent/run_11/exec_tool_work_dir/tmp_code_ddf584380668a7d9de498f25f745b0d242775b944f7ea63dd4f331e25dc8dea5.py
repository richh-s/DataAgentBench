code = """import json
import re

# Load tool results from storage files
with open(var_call_ix0eo19rhuYMXCVB7NWYe7Bw, 'r') as f:
    funding_records = json.load(f)
with open(var_call_F5LLyuXJFu5iKRtBhKU2o7T2, 'r') as f:
    civic_docs = json.load(f)

# Extract funding project names and amounts
funding_list = []
for r in funding_records:
    name = r.get('Project_Name')
    amt = r.get('Amount')
    try:
        amt_int = int(str(amt).replace(',', '').strip())
    except:
        try:
            amt_int = int(float(amt))
        except:
            amt_int = None
    funding_list.append({'Project_Name': name, 'Amount': amt_int})

# Function to extract design project names from a civic doc text
def extract_design_projects(text):
    projects = []
    lower = text.lower()
    # look for section header
    headers = ['capital improvement projects (design)', 'capital improvement projects ( design )', 'capital improvement projects (design)']
    idx = -1
    for h in headers:
        idx = lower.find(h)
        if idx != -1:
            header = h
            break
    if idx == -1:
        # try a more general find
        m = re.search(r'capital improvement projects\s*\(design\)', lower)
        if m:
            idx = m.start()
    if idx == -1:
        return projects
    # find end of section: look for common next sections
    end_markers = ['capital improvement projects (construction)', 'capital improvement projects (not started)', 'capital improvement projects (construction)', 'capital improvement projects (not started)', '\n\ncapital improvement projects', '\n\ncapital improvement projects (construction)']
    end_idx = len(text)
    for em in end_markers:
        pos = lower.find(em, idx+1)
        if pos != -1:
            end_idx = min(end_idx, pos)
    section = text[idx:end_idx]
    lines = section.splitlines()
    # helper to find next non-empty line index
    def next_non_empty(i):
        j = i+1
        while j < len(lines):
            if lines[j].strip():
                return j
            j += 1
        return None
    # Keywords indicating project lines
    keywords = ['project','repairs','improvements','study','plan','playground','walkway','resurfacing','traffic','park','skate','walkway','hvac','roof','crosswalk','median','signs','biofilter','storm','drain','culvert','retaining wall','slope','treatment','water']
    for i, line in enumerate(lines):
        s = line.strip()
        if not s:
            continue
        # skip lines that are headings or table of contents
        low = s.lower()
        if low.startswith('item') or low.startswith('to:') or low.startswith('prepared by') or low.startswith('approved by') or low.startswith('date prepared') or low.startswith('meeting date') or low.startswith('subject') or low.startswith('recommended action') or low.startswith('discussion'):
            continue
        # look at next non-empty line
        ni = next_non_empty(i)
        next_line = lines[ni].strip() if ni is not None else ''
        if next_line.startswith('(cid:') or next_line.lower().startswith('updates') or 'updates:' in next_line.lower() or next_line.lower().startswith('project schedule') or next_line.lower().startswith('project description') or next_line.lower().startswith('('):
            projects.append(s)
            continue
        # or if current line contains keywords
        for kw in keywords:
            if kw in low:
                projects.append(s)
                break
    # clean projects
    cleaned = []
    for p in projects:
        cp = re.sub(r'\s+', ' ', p).strip()
        if cp and cp not in cleaned:
            cleaned.append(cp)
    return cleaned

# Aggregate design projects from all docs
design_projects = []
for doc in civic_docs:
    text = doc.get('text','')
    pd = extract_design_projects(text)
    for p in pd:
        if p not in design_projects:
            design_projects.append(p)

# Normalize helper
def norm(s):
    return re.sub(r'[^a-z0-9]', ' ', s.lower()).strip()

# Build normalized maps
norm_design = {norm(p): p for p in design_projects}
# For funding, keep list
funding_by_norm = {}
for f in funding_list:
    n = norm(f['Project_Name'] or '')
    funding_by_norm.setdefault(n, []).append(f)

# Matching: if exact norm matches or one contains the other
matched = {}
for d_norm, d_orig in norm_design.items():
    matches = []
    for f_norm, f_records in funding_by_norm.items():
        if not f_norm or not d_norm:
            continue
        if d_norm == f_norm or d_norm in f_norm or f_norm in d_norm:
            # include records with amount > 50000
            for rec in f_records:
                if rec['Amount'] is not None and rec['Amount'] > 50000:
                    matches.append(rec)
    if matches:
        # dedupe by Project_Name
        unique = {m['Project_Name']: m for m in matches}
        matched[d_orig] = list(unique.values())

# Count unique design projects matched
count = len(matched)

# Prepare result
result = {
    'count': count,
    'matched_projects': []
}
for d, recs in matched.items():
    result['matched_projects'].append({'design_project_name': d, 'funding_records': recs})

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_vEj1i90GOr4rti3UfgFRVXSF': ['civic_docs'], 'var_call_I4QKKhsbpH5JYKZMz2RDAT9S': ['Funding'], 'var_call_ix0eo19rhuYMXCVB7NWYe7Bw': 'file_storage/call_ix0eo19rhuYMXCVB7NWYe7Bw.json', 'var_call_F5LLyuXJFu5iKRtBhKU2o7T2': 'file_storage/call_F5LLyuXJFu5iKRtBhKU2o7T2.json'}

exec(code, env_args)
