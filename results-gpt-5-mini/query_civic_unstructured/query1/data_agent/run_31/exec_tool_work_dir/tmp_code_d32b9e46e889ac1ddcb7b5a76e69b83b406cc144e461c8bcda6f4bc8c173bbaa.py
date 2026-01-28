code = """import json
import re
from pathlib import Path

# Load data from storage-provided variables

# var_call_x5yXZsAAfqzLymT3gHILyQpc and var_call_zuIL1ZirMabii4vC6dEGiW4a are available

# Read the civic docs JSON file
civic_path = Path(var_call_x5yXZsAAfqzLymT3gHILyQpc)
with civic_path.open('r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Read the funding JSON file
funding_path = Path(var_call_zuIL1ZirMabii4vC6dEGiW4a)
with funding_path.open('r', encoding='utf-8') as f:
    funding = json.load(f)

# Helper to normalize names
import string
trans_table = str.maketrans('', '', string.punctuation)

def normalize(s):
    if s is None:
        return ''
    s2 = s.lower()
    s2 = s2.replace('\n', ' ').replace('\r', ' ')
    s2 = re.sub(r"\s+", ' ', s2).strip()
    s2 = s2.translate(trans_table)
    return s2

# Extract design projects from civic documents
design_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    # Find Capital Improvement Projects (Design) section
    m = re.search(r'Capital Improvement Projects \(Design\)(.*?)(Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Capital Improvement Projects \(Construction\)|$)', text, re.S|re.I)
    if not m:
        # try alternative header spacing/case
        m = re.search(r'Capital Improvement Projects\s*\(Design\)(.*?)(Capital Improvement Projects\s*\(|$)', text, re.S|re.I)
    if not m:
        continue
    section = m.group(1)
    # Split into lines and pick likely project title lines
    lines = [ln.strip() for ln in section.splitlines()]
    for i, ln in enumerate(lines):
        if not ln:
            continue
        # skip lines that look like notes or markers
        if ln.startswith('(') or ln.lower().startswith('cid:'):
            continue
        low = ln.lower()
        skip_tokens = ['updates', 'project schedule', 'project description', 'page', 'agenda', 'estimated schedule', 'project is', 'project updates']
        if any(tok in low for tok in skip_tokens):
            continue
        # also skip lines that are short like headings
        if len(ln) < 4:
            continue
        # Exclude lines that are all uppercase 'ITEM' etc
        if ln.isupper() and len(ln.split())<6:
            continue
        # Heuristic: if next non-empty line contains 'Updates' or '(cid', then current line is a project title
        next_nonempty = ''
        for j in range(i+1, min(i+6, len(lines))):
            if lines[j]:
                next_nonempty = lines[j].lower()
                break
        if 'update' in next_nonempty or 'updates' in next_nonempty or next_nonempty.startswith('(cid') or 'project schedule' in next_nonempty or 'project description' in next_nonempty:
            design_projects.add(ln)
        else:
            # also accept some obvious project patterns containing keywords
            keywords = ['park','road','drain','storm','civic center','skate','pch','malibu','trancas','clover','latigo','retaining','slope','water','traffic','walkway']
            if any(k in low for k in keywords):
                design_projects.add(ln)

# Normalize design project names for matching
norm_design = {normalize(p): p for p in design_projects}

# Process funding records, find matches where amount > 50000
matching_projects = set()
for rec in funding:
    fname = rec.get('Project_Name')
    if fname is None:
        continue
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
    nfname = normalize(fname)
    # direct match
    if nfname in norm_design:
        matching_projects.add(norm_design[nfname])
        continue
    # substring matches
    matched = False
    for nd, orig in norm_design.items():
        if nd and (nd in nfname or nfname in nd):
            matching_projects.add(orig)
            matched = True
            break
    if matched:
        continue
    # token overlap match: at least two shared tokens
    f_tokens = set(nfname.split())
    for nd, orig in norm_design.items():
        d_tokens = set(nd.split())
        if len(f_tokens & d_tokens) >= 2:
            matching_projects.add(orig)
            break

# Prepare result
result = {
    'count': len(matching_projects),
    'projects': sorted(list(matching_projects))
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_PvP9ggpoXdIFKvf81tjWJq4X': ['civic_docs'], 'var_call_ReFFgmHoistAkOtfwguJGOQC': ['Funding'], 'var_call_x5yXZsAAfqzLymT3gHILyQpc': 'file_storage/call_x5yXZsAAfqzLymT3gHILyQpc.json', 'var_call_zuIL1ZirMabii4vC6dEGiW4a': 'file_storage/call_zuIL1ZirMabii4vC6dEGiW4a.json'}

exec(code, env_args)
