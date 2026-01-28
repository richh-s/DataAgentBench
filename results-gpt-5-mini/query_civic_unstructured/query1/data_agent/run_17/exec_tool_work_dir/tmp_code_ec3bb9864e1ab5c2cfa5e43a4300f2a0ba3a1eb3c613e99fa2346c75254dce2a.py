code = """import json
import re

# Load data from storage-provided file paths
funding_path = var_call_cYygX3IxyHQLhoX8Hef7wm3K
civic_docs_path = var_call_Ryd0TqUVXbPge07OF0RDcwpa

with open(funding_path, 'r', encoding='utf-8') as f:
    funding_list = json.load(f)

with open(civic_docs_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Normalize funding records: ensure Amount is int and Project_Name is str
for rec in funding_list:
    try:
        rec['Amount'] = int(rec.get('Amount'))
    except:
        # if conversion fails, try to remove non-digits
        s = str(rec.get('Amount'))
        digits = re.sub(r"[^0-9]", "", s)
        rec['Amount'] = int(digits) if digits else 0
    rec['Project_Name'] = str(rec.get('Project_Name','')).strip()

# Extract project names from civic docs under the "Capital Improvement Projects (Design)" section
projects_found = []
pattern = re.compile(r"Capital Improvement Projects \(Design\)(.*?)(Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Capital Improvement Projects \(Construction\))", re.S|re.I)

for doc in civic_docs:
    text = doc.get('text','')
    m = pattern.search(text)
    seg = None
    if m:
        seg = m.group(1)
    else:
        # Fallback: find start and take some lines after
        start = re.search(r"Capital Improvement Projects \(Design\)", text, re.I)
        if start:
            seg = text[start.end(): start.end()+4000]  # take a chunk
    if not seg:
        continue
    # Split into lines and heuristically extract project title lines
    lines = [ln.strip() for ln in seg.splitlines()]
    for i, ln in enumerate(lines):
        if not ln:
            continue
        low = ln.lower()
        # Exclude metadata lines
        if low.startswith('(') or low.startswith('cid:'):
            continue
        if low.startswith('updates') or low.startswith('project schedule') or low.startswith('page'):
            continue
        if ':' in ln and len(ln.split(':')[0])<20 and not ln.lower().endswith('project'):
            # probably a label like "Updates:" or "Project Description:" skip
            continue
        # Exclude lines that are clearly not titles
        if re.match(r'^[0-9]+\.', ln):
            continue
        # Remove stray bulletin markers
        if ln.lower().startswith('recommend') or ln.lower().startswith('discussion'):
            continue
        # Simple heuristic: titles are often in Title Case and not full sentences; allow long ones too
        # Also avoid lines that contain words like 'page' or 'agenda' which we already filtered
        # Clean leading/trailing punctuation
        cleaned = ln.strip(' -\u2022')
        # Remove trailing words like "Project" repeated on next line? keep as is
        if len(cleaned) > 3:
            projects_found.append(cleaned)

# Deduplicate while preserving order
seen = set()
projects = []
for p in projects_found:
    if p not in seen:
        seen.add(p)
        projects.append(p)

# Now match with funding_list (which already contains only Amount > 50000 from earlier query)
matched_projects = {}
for proj in projects:
    pl = proj.lower()
    for rec in funding_list:
        fn = rec['Project_Name']
        fl = fn.lower()
        if pl in fl or fl in pl:
            # record match
            matched_projects[proj] = matched_projects.get(proj, []) + [ {'Funding_Project_Name': fn, 'Amount': rec['Amount']} ]

count = len(matched_projects)

# Prepare result
result = {
    'design_capital_projects_extracted_count': len(projects),
    'design_capital_projects_extracted_sample': projects[:50],
    'matched_count': count,
    'matched_projects': matched_projects
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_cYygX3IxyHQLhoX8Hef7wm3K': 'file_storage/call_cYygX3IxyHQLhoX8Hef7wm3K.json', 'var_call_3DeNmZ7TczDSNBr4GLPgKgAb': ['civic_docs'], 'var_call_Ryd0TqUVXbPge07OF0RDcwpa': 'file_storage/call_Ryd0TqUVXbPge07OF0RDcwpa.json'}

exec(code, env_args)
