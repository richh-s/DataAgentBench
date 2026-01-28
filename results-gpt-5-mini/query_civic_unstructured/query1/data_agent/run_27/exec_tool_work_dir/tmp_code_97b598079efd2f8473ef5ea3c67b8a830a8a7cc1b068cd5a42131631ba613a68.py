code = """import json
import re
from pathlib import Path

# Load files from storage variables
funding_path = Path(var_call_6sPeBNDTHNtwmBHnnW5cL0Lo)
civic_path = Path(var_call_uIW8AEKnifZF8TLcNMhOHUny)

funding = json.load(open(funding_path, 'r'))
civic_docs = json.load(open(civic_path, 'r'))

def clean_name(s):
    if s is None:
        return ''
    s = re.sub(r"\(.*?\)", "", s)  # remove parentheses content
    s = re.sub(r"[^0-9a-zA-Z &,-]", " ", s)
    s = re.sub(r"\s+", " ", s).strip().lower()
    return s

# Normalize funding amounts and names
for r in funding:
    try:
        r['Amount'] = int(r.get('Amount', 0))
    except:
        try:
            r['Amount'] = int(float(r.get('Amount', 0)))
        except:
            r['Amount'] = 0
    r['clean_name'] = clean_name(r.get('Project_Name',''))

# Extract design projects
design_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    lower = text.lower()
    key = 'capital improvement projects (design)'
    if key in lower:
        idx = lower.find(key)
        sub = text[idx + len(key):]
        # stop at next header occurrence
        stop_tokens = ['capital improvement projects (construction)', 'capital improvement projects (not started)', 'capital improvement projects (design)']
        stop_idx = None
        for tok in stop_tokens:
            i = sub.lower().find(tok)
            if i != -1:
                if stop_idx is None or i < stop_idx:
                    stop_idx = i
        if stop_idx is not None:
            sub = sub[:stop_idx]
        # split into lines
        lines = sub.splitlines()
        for i, line in enumerate(lines):
            line_str = line.strip()
            if not line_str:
                continue
            # ignore headings like 'updates' etc
            if line_str.lower().startswith('updates') or line_str.lower().startswith('project schedule') or line_str.lower().startswith('project description'):
                continue
            # lookahead for indicator lines
            lookahead = None
            for j in range(i+1, min(i+6, len(lines))):
                nxt = lines[j].strip()
                if nxt:
                    lookahead = nxt.lower()
                    break
            if lookahead and (lookahead.startswith('(cid:') or 'updates' in lookahead or 'project schedule' in lookahead or 'project description' in lookahead or 'estimated schedule' in lookahead):
                # consider this a title
                # filter out short or irrelevant lines
                if 4 < len(line_str) < 200 and not line_str.lower().startswith('page'):
                    design_projects.add(line_str)

# As a fallback, also collect some capital lines that look like titles within first 3000 chars after key
if not design_projects:
    for doc in civic_docs:
        text = doc.get('text','')
        parts = re.split(r'Capital Improvement Projects \(Design\)', text, flags=re.IGNORECASE)
        if len(parts) > 1:
            sub = parts[1][:3000]
            segs = re.split(r"\n\n+", sub)
            for seg in segs[:40]:
                s = seg.strip().split('\n')[0].strip()
                if 4 < len(s) < 200 and not s.lower().startswith('page'):
                    design_projects.add(s)

# Clean design names
cleaned_design = {p: clean_name(p) for p in design_projects}

# Match with funding records where Amount > 50000
matched = []
for orig, cname in cleaned_design.items():
    matches = []
    for r in funding:
        if r['Amount'] > 50000:
            fn = r['clean_name']
            if cname and fn and (cname in fn or fn in cname):
                matches.append({'Funding_ID': r.get('Funding_ID'), 'Funding_Project_Name': r.get('Project_Name'), 'Amount': r.get('Amount')})
    if matches:
        matched.append({'Project_Name': orig, 'clean_name': cname, 'funding_matches': matches})

count = len(matched)

out = {'count': count, 'projects': [m['Project_Name'] for m in matched]}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_6sPeBNDTHNtwmBHnnW5cL0Lo': 'file_storage/call_6sPeBNDTHNtwmBHnnW5cL0Lo.json', 'var_call_uIW8AEKnifZF8TLcNMhOHUny': 'file_storage/call_uIW8AEKnifZF8TLcNMhOHUny.json'}

exec(code, env_args)
