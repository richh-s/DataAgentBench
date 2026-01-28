code = """import json
import re

# Load funding data from storage variable (file path or list)
funding_var = var_call_HhaxClLn5rXkeecfvhdgCo2s
if isinstance(funding_var, str) and funding_var.endswith('.json'):
    with open(funding_var, 'r') as f:
        funding_records = json.load(f)
else:
    funding_records = funding_var

# Convert funding records to normalized list of dicts with name and amount (int)
funds = []
for r in funding_records:
    name = r.get('Project_Name') or r.get('project_name')
    amount = r.get('Amount')
    try:
        amount = int(amount)
    except:
        try:
            amount = int(str(amount).replace('$','').replace(',',''))
        except:
            amount = None
    funds.append({'name': name.strip() if isinstance(name, str) else name, 'amount': amount})

# Load civic docs results
civic_var = var_call_xHC5GICLu8eEJRoCxkvhkNRK
if isinstance(civic_var, str) and civic_var.endswith('.json'):
    with open(civic_var, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_var

# Extract project names from 'Capital Improvement Projects (Design)' sections
design_project_candidates = []
start_markers = [r'Capital Improvement Projects (Design)', r'Capital Improvement Projects \(Design\)']
end_markers = [r'Capital Improvement Projects (Construction)', r'Capital Improvement Projects \(Construction\)',
               r'Capital Improvement Projects (Not Started)', r'Capital Improvement Projects \(Not Started\)',
               r'Capital Improvement Projects \(Construction\)', r'Capital Improvement Projects (Not Started)']

for doc in civic_docs:
    text = doc.get('text', '')
    # Find start index
    si = None
    for sm in start_markers:
        m = re.search(sm, text, flags=re.IGNORECASE)
        if m:
            si = m.end()
            break
    if si is None:
        continue
    # Find end index after si
    ei = None
    for em in end_markers:
        m = re.search(em, text[si:], flags=re.IGNORECASE)
        if m:
            ei = si + m.start()
            break
    section = text[si:ei] if ei else text[si:si+5000]  # limit if no explicit end
    # Split lines and extract likely project titles
    lines = [ln.strip() for ln in section.splitlines()]
    for i, ln in enumerate(lines):
        if not ln:
            continue
        low = ln.lower()
        # filter out lines that are clearly not titles
        if low.startswith('(cid') or low.startswith('updates:') or low.startswith('project schedule') or low.startswith('page'):
            continue
        if ':' in ln and len(ln.split(':')[0].split())<4 and ln.endswith(':'):
            continue
        # Reject lines that are headings like 'RECOMMENDED ACTION' or 'DISCUSSION'
        if ln.isupper() and len(ln.split())<6:
            continue
        # Very short
        if len(ln) < 4:
            continue
        # Lines that contain words indicating they are project titles
        keywords = ['project', 'repair', 'improvements', 'walkway', 'park', 'road', 'study', 'skate', 'treatment', 'drain', 'median', 'culvert', 'retaining', 'traffic', 'signals', 'water']
        if any(k in low for k in keywords):
            # Clean numeric prefixes like item numbers
            cleaned = re.sub(r'^[0-9\.\)\s-]+', '', ln)
            # Remove duplicate whitespace
            cleaned = re.sub(r'\s+', ' ', cleaned).strip()
            design_project_candidates.append(cleaned)

# Deduplicate while preserving order
seen = set()
design_projects = []
for p in design_project_candidates:
    key = p.lower()
    if key not in seen:
        seen.add(key)
        design_projects.append(p)

# Now match design_projects to funding records (funds contains amounts >50000 already)
matched = []
for dp in design_projects:
    dp_low = re.sub(r'[^a-z0-9 ]','', dp.lower())
    for f in funds:
        fname = f['name'] or ''
        fname_low = re.sub(r'[^a-z0-9 ]','', fname.lower())
        if not fname_low or f['amount'] is None:
            continue
        # consider a match if one name is substring of the other (word boundaries)
        if dp_low in fname_low or fname_low in dp_low:
            # ensure amount > 50000
            if f['amount'] > 50000:
                matched.append({'design_project': dp, 'funding_project': fname, 'amount': f['amount']})

# Also attempt fuzzy matching by partial token overlap (>=3 token common)
if not matched:
    for dp in design_projects:
        dp_tokens = set([t for t in re.split(r'\s+', re.sub(r'[^a-z0-9 ]','', dp.lower())) if t])
        for f in funds:
            fname = f['name'] or ''
            fname_tokens = set([t for t in re.split(r'\s+', re.sub(r'[^a-z0-9 ]','', fname.lower())) if t])
            if len(dp_tokens & fname_tokens) >= 3 and f['amount'] and f['amount']>50000:
                matched.append({'design_project': dp, 'funding_project': fname, 'amount': f['amount']})

# Build unique set of design projects that have funding > 50k
matched_design_projects = {}
for m in matched:
    key = m['design_project']
    if key not in matched_design_projects:
        matched_design_projects[key] = []
    matched_design_projects[key].append({'funding_project': m['funding_project'], 'amount': m['amount']})

result = {
    'design_projects_extracted_count': len(design_projects),
    'design_projects_extracted': design_projects,
    'matched_design_projects_count': len(matched_design_projects),
    'matched_design_projects': matched_design_projects,
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_HhaxClLn5rXkeecfvhdgCo2s': 'file_storage/call_HhaxClLn5rXkeecfvhdgCo2s.json', 'var_call_gxQ31uzAyHYmY5zFFEy0onVA': ['civic_docs'], 'var_call_xHC5GICLu8eEJRoCxkvhkNRK': 'file_storage/call_xHC5GICLu8eEJRoCxkvhkNRK.json'}

exec(code, env_args)
