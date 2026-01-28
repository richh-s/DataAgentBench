code = """import json
import re
from pathlib import Path

# Load tool results from storage file paths
funding_path = Path(var_call_6sPeBNDTHNtwmBHnnW5cL0Lo)
civic_path = Path(var_call_uIW8AEKnifZF8TLcNMhOHUny)

funding = json.load(open(funding_path, 'r'))
civic_docs = json.load(open(civic_path, 'r'))

# Helper to clean project names: remove parenthetical suffixes and normalize spaces and lower
def clean_name(s):
    if s is None:
        return ''
    s = re.sub(r"\(.*?\)", "", s)  # remove parentheses content
    s = re.sub(r"[^0-9a-zA-Z &,-]", " ", s)  # replace punctuation with space
    s = re.sub(r"\s+", " ", s).strip().lower()
    return s

# Extract Capital Improvement Projects (Design) project names from civic docs
design_projects = set()
for doc in civic_docs:
    text = doc.get('text','')
    lower = text.lower()
    header = 'capital improvement projects (design)'
    if header in lower:
        start = lower.find(header)
        # take substring starting after header
        sub = text[start+len(header):]
        # stop at next 'capital improvement projects (' occurrence if present
        m = re.search(r'capital improvement projects \((construction|not started|design)\)', sub, flags=re.IGNORECASE)
        if m:
            sub = sub[:m.start()]
        # also stop at 'capital improvement projects (construction)' exact
        stop_tokens = ['capital improvement projects (construction)', 'capital improvement projects (not started)', 'capital improvement projects (design)', '\n\ncapital improvement projects']
        stop_index = None
        for tok in stop_tokens:
            idx = sub.lower().find(tok)
            if idx != -1:
                if stop_index is None or idx < stop_index:
                    stop_index = idx
        if stop_index is not None:
            sub = sub[:stop_index]
        # Now parse lines to find project titles. Heuristic: project title line is followed by a line containing '(cid' or 'updates' or 'project schedule' or 'project description'
        lines = sub.splitlines()
        # find indices of non-empty lines
        for i, line in enumerate(lines):
            line_stripped = line.strip()
            if not line_stripped:
                continue
            # lookahead for next non-empty line
            lookahead = None
            for j in range(i+1, min(i+6, len(lines))):
                if lines[j].strip():
                    lookahead = lines[j].strip().lower()
                    break
            if lookahead and (lookahead.startswith('(cid:') or 'updates' in lookahead or 'project schedule' in lookahead or 'project description' in lookahead or lookahead.startswith('project updates') or 'estimated schedule' in lookahead):
                # this line is likely a project title
                # ignore lines that are clearly headings
                if len(line_stripped) > 3 and not line_stripped.lower().startswith('page') and not line_stripped.isupper():
                    design_projects.add(line_stripped)

# fallback: if none found, try extracting known patterns: lines between header and updates markers that are title-like
if not design_projects:
    for doc in civic_docs:
        text = doc.get('text','')
        parts = re.split(r'Capital Improvement Projects \(Design\)', text, flags=re.IGNORECASE)
        if len(parts) > 1:
            sub = parts[1]
            # split by double newlines and take segments that look like titles
            segs = re.split(r"\n\n+", sub)
            for seg in segs[:30]:
                s = seg.strip().split('\n')[0].strip()
                if 3 < len(s) < 150 and not s.lower().startswith('page'):
                    design_projects.add(s)

# Normalize design project names
cleaned_design = {p: clean_name(p) for p in design_projects}

# Prepare funding records mapping and clean names
for r in funding:
    # convert Amount to int
    try:
        r['Amount'] = int(r['Amount'])
    except:
        try:
            r['Amount'] = int(float(r['Amount']))
        except:
            r['Amount'] = 0
    r['clean_name'] = clean_name(r.get('Project_Name',''))

# For each design project, check if there's a funding record with Amount > 50000 and name match
matched_projects = []
for orig_name, cname in cleaned_design.items():
    found = False
    matched_records = []
    for r in funding:
        fn = r['clean_name']
        # match if one contains the other and words overlap
        if (cname and fn and (cname in fn or fn in cname)):
            if r['Amount'] > 50000:
                found = True
                matched_records.append({'Funding_ID': r.get('Funding_ID'), 'Funding_Project_Name': r.get('Project_Name'), 'Amount': r.get('Amount')})
    if found:
        matched_projects.append({'Project_Name': orig_name, 'clean_name': cname, 'funding_matches': matched_records})

# Count unique projects
count = len(matched_projects)

# Prepare result
result = {'count': count, 'projects': [p['Project_Name'] for p in matched_projects]}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_6sPeBNDTHNtwmBHnnW5cL0Lo': 'file_storage/call_6sPeBNDTHNtwmBHnnW5cL0Lo.json', 'var_call_uIW8AEKnifZF8TLcNMhOHUny': 'file_storage/call_uIW8AEKnifZF8TLcNMhOHUny.json'}

exec(code, env_args)
