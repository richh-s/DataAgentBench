code = """import json
from pathlib import Path
import re

# Load files
civic_path = Path(var_call_x5yXZsAAfqzLymT3gHILyQpc)
with civic_path.open('r', encoding='utf-8') as f:
    civic_docs = json.load(f)
funding_path = Path(var_call_zuIL1ZirMabii4vC6dEGiW4a)
with funding_path.open('r', encoding='utf-8') as f:
    funding = json.load(f)

# normalize helper
import string
trans_table = str.maketrans('', '', string.punctuation)
def normalize(s):
    if s is None:
        return ''
    s2 = s.lower()
    s2 = s2.replace('\n',' ').replace('\r',' ')
    s2 = re.sub(r"\s+", ' ', s2).strip()
    s2 = s2.translate(trans_table)
    return s2

# extract design projects
design_projects = set()
for doc in civic_docs:
    text = doc.get('text','')
    lower = text.lower()
    key = 'capital improvement projects (design)'
    idx = lower.find(key)
    if idx == -1:
        continue
    # slice from idx to next major header
    # find next occurrence of 'capital improvement projects (' after idx+1
    next_idx = lower.find('capital improvement projects (', idx+1)
    if next_idx == -1:
        section = text[idx:]
    else:
        section = text[idx:next_idx]
    # split into lines and look for project title heuristically
    lines = [ln.strip() for ln in section.splitlines()]
    for i, ln in enumerate(lines):
        if not ln:
            continue
        low = ln.lower()
        # skip lines that are clearly not titles
        if low.startswith('(') or low.startswith('cid:'):
            continue
        if any(tok in low for tok in ['updates', 'project schedule', 'project description', 'agenda', 'estimated schedule', 'page']):
            continue
        if len(ln) < 4:
            continue
        # heuristic: if next non-empty line contains 'updates' or '(cid' then this is a title
        next_nonempty = ''
        for j in range(i+1, min(i+6, len(lines))):
            if lines[j]:
                next_nonempty = lines[j].lower()
                break
        if 'update' in next_nonempty or next_nonempty.startswith('(cid') or 'project schedule' in next_nonempty or 'project description' in next_nonempty:
            design_projects.add(ln)
        else:
            # accept if contains keywords
            if any(k in low for k in ['park','road','drain','storm','civic center','skate','pch','malibu','trancas','clover','latigo','retaining','slope','water','traffic','walkway']):
                design_projects.add(ln)

# normalize mapping
norm_design = {normalize(p): p for p in design_projects}

# find funding records with amount > 50000 that match design projects
matching_projects = set()
for rec in funding:
    pname = rec.get('Project_Name')
    if pname is None:
        continue
    # parse amount
    amt_raw = rec.get('Amount', 0)
    try:
        amt = int(str(amt_raw))
    except:
        try:
            amt = int(float(str(amt_raw)))
        except:
            amt = 0
    if amt <= 50000:
        continue
    np = normalize(pname)
    if np in norm_design:
        matching_projects.add(norm_design[np])
        continue
    # substring match
    found = False
    for nd, orig in norm_design.items():
        if nd and (nd in np or np in nd):
            matching_projects.add(orig)
            found = True
            break
    if found:
        continue
    # token overlap
    tokens_p = set(np.split())
    for nd, orig in norm_design.items():
        tokens_d = set(nd.split())
        if len(tokens_p & tokens_d) >= 2:
            matching_projects.add(orig)
            break

result = {'count': len(matching_projects), 'projects': sorted(list(matching_projects))}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_PvP9ggpoXdIFKvf81tjWJq4X': ['civic_docs'], 'var_call_ReFFgmHoistAkOtfwguJGOQC': ['Funding'], 'var_call_x5yXZsAAfqzLymT3gHILyQpc': 'file_storage/call_x5yXZsAAfqzLymT3gHILyQpc.json', 'var_call_zuIL1ZirMabii4vC6dEGiW4a': 'file_storage/call_zuIL1ZirMabii4vC6dEGiW4a.json'}

exec(code, env_args)
