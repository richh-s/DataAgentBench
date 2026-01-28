code = """import json, re

# Load results from previous tool calls (file paths provided in storage variables)
with open(var_call_i7pIUn02ScRKLaKBgJHjsfpF, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_yGOk2ofuIXBkXuO9xfTzY1aP, 'r', encoding='utf-8') as f:
    funding_rows = json.load(f)

# Helper normalize
def norm(s):
    return re.sub(r"\s+", " ", s.lower().strip())

# Extract project names listed under the "Capital Improvement Projects (Design)" sections
design_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    key = 'Capital Improvement Projects (Design)'
    start_idx = text.find(key)
    if start_idx == -1:
        # try lowercase variant
        start_idx = text.lower().find(key.lower())
        if start_idx == -1:
            continue
        else:
            start_idx = start_idx
    else:
        start_idx = start_idx
    start = start_idx + len(key)
    # Find end of the Design section by looking for common next headings
    end = len(text)
    next_heads = [
        'Capital Improvement Projects (Construction)',
        'Capital Improvement Projects (Not Started)',
        'Capital Improvement Projects (Construction)',
        'Capital Improvement Projects (Not Started)',
        '\n\nCapital Improvement Projects (Construction)',
        '\n\nCapital Improvement Projects (Not Started)'
    ]
    for nh in next_heads:
        j = text.find(nh, start)
        if j != -1 and j < end:
            end = j
    block = text[start:end]
    # Split into lines and apply heuristics to detect project title lines
    lines = [ln.strip() for ln in block.splitlines()]
    for ln in lines:
        if not ln:
            continue
        low = ln.lower()
        # Skip obvious non-title lines
        if ':' in ln:
            continue
        if low.startswith('updates') or low.startswith('(cid') or low.startswith('page') or low.startswith('agenda'):
            continue
        if 'project schedule' in low or 'project description' in low or 'estimated schedule' in low or 'project updates' in low:
            continue
        if low.startswith('recommended action') or low.startswith('discussion'):
            continue
        # Skip very short lines
        if len(ln) < 6:
            continue
        # Lines that are likely sentences rather than titles often end with a period; skip those
        if ln.endswith('.'):
            continue
        # Avoid lines that are all uppercase words like headers (but some project names may be title case)
        # If passes heuristics, add
        design_projects.add(ln)

# Normalize and prepare mapping
design_norm_map = {norm(s): s for s in design_projects}

# Prepare funding set (already filtered to Amount > 50000 by previous query)
funding_set = set()
for r in funding_rows:
    pname = r.get('Project_Name') or ''
    # Normalize amount to int
    amt_raw = r.get('Amount', 0)
    try:
        amt = int(float(amt_raw))
    except:
        try:
            amt = int(str(amt_raw).replace(',',''))
        except:
            amt = 0
    if amt > 50000:
        funding_set.add(pname)
fund_norm_map = {norm(s): s for s in funding_set}

# Match design projects to funded projects using normalized forms and substring checks
matched_design_projects = set()
for dnorm, dorig in design_norm_map.items():
    for fnorm, forig in fund_norm_map.items():
        if dnorm == fnorm or dnorm in fnorm or fnorm in dnorm:
            matched_design_projects.add(dorig)
            break

count = len(matched_design_projects)
result = {"count": count, "matched_projects": sorted(list(matched_design_projects))}

import json
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_niYonW9IOdRbZkwnICOKFidL': ['civic_docs'], 'var_call_RDD7R3XhMlU6f4fAerIDHaAH': ['Funding'], 'var_call_yGOk2ofuIXBkXuO9xfTzY1aP': 'file_storage/call_yGOk2ofuIXBkXuO9xfTzY1aP.json', 'var_call_i7pIUn02ScRKLaKBgJHjsfpF': 'file_storage/call_i7pIUn02ScRKLaKBgJHjsfpF.json'}

exec(code, env_args)
