code = """import json,re

# Load previous tool results from storage file paths
with open(var_call_FrBndGx95lvLCMT0CPcB2JYt, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_p9bRrpvoVxd61gmQLKu2Xy6l, 'r', encoding='utf-8') as f:
    funding_rows = json.load(f)

# Extract design projects from civic_docs by finding the 'Capital Improvement Projects (Design)' section
design_projects = set()
for doc in civic_docs:
    text = doc.get('text','')
    if not text:
        continue
    start_marker = 'Capital Improvement Projects (Design)'
    start_idx = text.find(start_marker)
    if start_idx == -1:
        continue
    section = text[start_idx+len(start_marker):]
    # Determine end of this section by common next-section headers
    end_markers = ['Capital Improvement Projects (Construction)',
                   'Capital Improvement Projects (Not Started)',
                   'Capital Improvement Projects (Construction)',
                   'Capital Improvement Projects (Not Started)',
                   'Capital Improvement Projects (Construction)']
    end_idx = None
    for m in end_markers:
        i = section.find(m)
        if i != -1:
            if end_idx is None or i < end_idx:
                end_idx = i
    if end_idx is not None:
        section = section[:end_idx]
    # Split into lines and heuristically pick project title lines
    lines = section.splitlines()
    for line in lines:
        s = line.strip()
        if not s:
            continue
        # skip lines that are clearly not project titles
        skip_keywords = ['updates', 'project schedule', 'estimated schedule', 'project description', 'agenda', 'page', 'cid:', 'recommend', 'discussion', 'updates:']
        low = s.lower()
        if any(k in low for k in skip_keywords):
            continue
        if low.startswith('(') or low.startswith('cid:'):
            continue
        # skip lines with many words that look like sentences (contain verbs)
        if len(s) > 140:
            continue
        # avoid lines that end with ':' which are headers
        if s.endswith(':'):
            continue
        # Heuristic: must contain at least one lowercase or uppercase letter and at least two words
        if len(re.findall(r"[A-Za-z]", s)) == 0:
            continue
        if len(s.split()) < 2:
            continue
        # Remove leading bullets or weird chars
        s_clean = re.sub(r'^[^A-Za-z0-9]+', '', s)
        s_clean = s_clean.strip()
        # Avoid lines that are just single words like 'Discussion'
        if s_clean.lower() in ['discussion', 'recommended action']:
            continue
        design_projects.add(s_clean)

# Normalize function for matching
def normalize(name):
    if not name:
        return ''
    s = name.lower()
    s = re.sub(r"\(.*?\)", '', s)  # remove parenthetical
    s = re.sub(r'[^a-z0-9\s]', ' ', s)
    s = re.sub(r'\bproject\b', '', s)
    s = re.sub(r'\bthe\b', '', s)
    s = re.sub(r'\bphase\b', '', s)
    s = re.sub(r'\s+', ' ', s)
    return s.strip()

norm_design = {normalize(x): x for x in design_projects}

# Process funding rows (already filtered >50000 by the earlier query)
matches = set()
matched_funding_records = []
for fr in funding_rows:
    pname = fr.get('Project_Name') or fr.get('ProjectName') or ''
    norm_f = normalize(pname)
    # direct match
    if norm_f in norm_design:
        matches.add(norm_design[norm_f])
        matched_funding_records.append({'Funding_ID': fr.get('Funding_ID'), 'Project_Name': fr.get('Project_Name'), 'Amount': fr.get('Amount')})
        continue
    # substring match either way
    for nd_norm, orig in norm_design.items():
        if nd_norm and (nd_norm in norm_f or norm_f in nd_norm):
            matches.add(orig)
            matched_funding_records.append({'Funding_ID': fr.get('Funding_ID'), 'Project_Name': fr.get('Project_Name'), 'Amount': fr.get('Amount')})
            break

# Prepare result
result = {
    'design_projects_extracted_count': len(design_projects),
    'matched_design_projects_count': len(matches),
    'matched_projects': sorted(list(matches)),
    'matched_funding_records_count': len(matched_funding_records),
    'matched_funding_records_sample': matched_funding_records[:50]
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_jgOIUDzVq19K2SZ4sahlMvss': ['civic_docs'], 'var_call_53PVcTv8dNJe04wWl0gFcGFH': ['Funding'], 'var_call_FrBndGx95lvLCMT0CPcB2JYt': 'file_storage/call_FrBndGx95lvLCMT0CPcB2JYt.json', 'var_call_p9bRrpvoVxd61gmQLKu2Xy6l': 'file_storage/call_p9bRrpvoVxd61gmQLKu2Xy6l.json'}

exec(code, env_args)
