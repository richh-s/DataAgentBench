code = """import json
import re

# Load funding data from storage variable
funding_var = var_call_uyoeMFT0noZzzIlkP64WP5ai
civic_var = var_call_Eje7Rsgk3iEWnXiMG5xwnCE1

def load_var(v):
    if isinstance(v, str):
        # assume it's a path to a json file
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return v

funding = load_var(funding_var)
civic_docs = load_var(civic_var)

# Normalize function: remove parenthetical suffixes, punctuation, lowercase, collapse spaces
def normalize(name):
    if name is None:
        return ''
    # remove parenthetical content
    name = re.sub(r"\([^)]*\)", "", name)
    # remove non-alphanumeric characters except spaces
    name = re.sub(r"[^0-9a-zA-Z ]+", " ", name)
    name = re.sub(r"\s+", " ", name).strip().lower()
    return name

# Filter funding > 50000
funded_projects = []
for r in funding:
    try:
        amt = int(r.get('Amount', 0))
    except:
        try:
            amt = int(str(r.get('Amount','0')).replace(',',''))
        except:
            amt = 0
    if amt > 50000:
        funded_projects.append(r.get('Project_Name',''))

# Build normalized set for funded projects
funded_norms = {normalize(p): p for p in funded_projects}

# Extract design projects from civic docs
design_projects = []
for doc in civic_docs:
    text = doc.get('text','')
    if not text:
        continue
    # find design section
    start_idx = -1
    for header in ["Capital Improvement Projects (Design)", "Capital Improvement Projects - Design", "Capital Improvement Projects (Design):"]:
        start_idx = text.find(header)
        if start_idx != -1:
            start_idx += len(header)
            break
    if start_idx == -1:
        continue
    # find end of section
    end_idx = -1
    for end_header in ["Capital Improvement Projects (Construction)", "Capital Improvement Projects (Not Started)", "Capital Improvement Projects (Construction)", "Capital Improvement Projects (Not Started)", "Capital Improvement Projects (Construction)"]:
        end_idx = text.find(end_header, start_idx)
        if end_idx != -1:
            break
    section = text[start_idx:end_idx] if end_idx != -1 else text[start_idx:]
    # split lines and pick candidate project name lines
    lines = section.splitlines()
    for ln in lines:
        s = ln.strip()
        if not s:
            continue
        # skip lines that are headings or metadata
        low = s.lower()
        if low.startswith('(cid') or low.startswith('updates:') or low.startswith('project schedule') or low.startswith('est') or low.startswith('page') or low.startswith('agenda'):
            continue
        if ':' in s and len(s.split(':')[0].split())<5:
            # likely a label like "Updates:" or "Project Schedule:"; skip
            if s.endswith(':') or low.startswith('updates') or low.startswith('project schedule'):
                continue
        # skip lines that are clearly sentences (contain verbs like is, will, has)
        if re.search(r"\b(is|will|has|are|were|was|working|submitted|complete|begin|advertise)\b", low):
            continue
        # skip lines that are short
        if len(s) < 4:
            continue
        # avoid lines that look like plain text comments
        # Heuristic: treat lines with Title Case or containing key words as project names
        design_projects.append(s)

# Deduplicate while preserving order
seen = set()
design_unique = []
for p in design_projects:
    if p not in seen:
        seen.add(p)
        design_unique.append(p)

# Normalize design project names
design_norm_map = {normalize(p): p for p in design_unique}

# Match normalized names using substring matching
matched_designs = set()
for d_norm, d_orig in design_norm_map.items():
    for f_norm, f_orig in funded_norms.items():
        if not d_norm or not f_norm:
            continue
        if d_norm == f_norm or d_norm in f_norm or f_norm in d_norm:
            matched_designs.add(d_orig)

# Prepare result
result = {
    'count': len(matched_designs),
    'matched_projects': sorted(list(matched_designs))
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_uyoeMFT0noZzzIlkP64WP5ai': 'file_storage/call_uyoeMFT0noZzzIlkP64WP5ai.json', 'var_call_Eje7Rsgk3iEWnXiMG5xwnCE1': 'file_storage/call_Eje7Rsgk3iEWnXiMG5xwnCE1.json'}

exec(code, env_args)
