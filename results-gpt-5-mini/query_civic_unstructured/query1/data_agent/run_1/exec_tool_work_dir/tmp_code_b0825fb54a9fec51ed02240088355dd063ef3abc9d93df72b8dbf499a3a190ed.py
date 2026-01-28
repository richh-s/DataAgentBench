code = """import json, re

# Load data from storage variables (file paths or direct lists)
civic_docs_path = var_call_QCpzQiWWNyhvMPkrhyhkgvPY
funding_path = var_call_qiXNGGtDuFZVtAvMjVEdUaQz

def load_json_var(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return v

civic_docs = load_json_var(civic_docs_path)
funding_records = load_json_var(funding_path)

# Helper to normalize names by lowercasing, trimming, and removing parenthetical suffixes
paren_re = re.compile(r"\s*\([^)]*\)\s*$")

def normalize(name):
    if name is None:
        return ""
    s = name.strip()
    s = paren_re.sub('', s)
    s = re.sub(r"[^0-9a-zA-Z &,-]", ' ', s)  # keep common chars, replace others with space
    s = re.sub(r"\s+", ' ', s)
    return s.lower()

# Extract project names from 'Capital Improvement Projects (Design)' sections
design_projects = set()
headers_end = [
    'capital improvement projects (construction)',
    'capital improvement projects (not started)',
    'capital improvement projects (construction)',
    'capital improvement projects (not started)'
]

for doc in civic_docs:
    text = doc.get('text', '')
    low = text.lower()
    key = 'capital improvement projects (design)'
    idx = low.find(key)
    if idx == -1:
        # Try alternative header variants
        idx = low.find('capital improvement projects – design')
    if idx == -1:
        continue
    # find end of section
    end_idx = len(text)
    for endh in headers_end:
        j = low.find(endh, idx+len(key))
        if j != -1:
            end_idx = min(end_idx, j)
    section = text[idx:end_idx]
    lines = section.splitlines()
    # iterate lines to find titles
    for i, line in enumerate(lines):
        s = line.strip()
        if not s:
            continue
        s_low = s.lower()
        # skip obvious non-title lines
        if s_low.endswith(':'):
            continue
        if s_low.startswith('(cid'):
            continue
        if s_low in ('updates', 'discussion', 'project description', 'project updates', 'recommended action'):
            continue
        # look ahead for next non-empty line
        next_line = None
        for j in range(i+1, len(lines)):
            if lines[j].strip():
                next_line = lines[j].strip()
                break
        if next_line is None:
            # last non-empty line in section, consider as project
            candidate = s
            # avoid capturing header itself
            if candidate.lower().startswith(key):
                continue
            design_projects.add(candidate)
            continue
        nl = next_line.lower()
        if ('update' in nl) or nl.startswith('(cid') or 'project schedule' in nl or 'estimated schedule' in nl or nl.endswith(':') or 'project description' in nl:
            # likely title
            if not s.lower().startswith(key):
                design_projects.add(s)
        else:
            # sometimes titles are multi-line: if current line capitalized and next line lowercase starting with '(' then ok
            # otherwise skip
            # Heuristic: if line contains year or digits or length>30 treat as title
            if len(s) > 20 or re.search(r"\d", s):
                design_projects.add(s)

# Normalize design project names
norm_design = {normalize(n): n for n in design_projects}

# Process funding records (they are already filtered to Amount > 50000)
matched = set()
for rec in funding_records:
    pname = rec.get('Project_Name') or rec.get('ProjectName') or ''
    amt = rec.get('Amount')
    try:
        amt_val = int(str(amt))
    except:
        try:
            amt_val = int(float(str(amt)))
        except:
            amt_val = 0
    if amt_val <= 50000:
        continue
    norm_f = normalize(pname)
    # try exact match or substring match
    for nd, orig in norm_design.items():
        if nd == '':
            continue
        if nd == norm_f or nd in norm_f or norm_f in nd:
            matched.add(orig)

result = {
    'count': len(matched),
    'matched_projects': sorted(list(matched))
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_qiXNGGtDuFZVtAvMjVEdUaQz': 'file_storage/call_qiXNGGtDuFZVtAvMjVEdUaQz.json', 'var_call_QCpzQiWWNyhvMPkrhyhkgvPY': 'file_storage/call_QCpzQiWWNyhvMPkrhyhkgvPY.json'}

exec(code, env_args)
