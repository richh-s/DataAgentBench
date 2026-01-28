code = """import json
import re

# Load data from previous tool results
with open(var_call_TWSODwC5rKyketYdEYUZZUzs, 'r') as f:
    funding_data = json.load(f)

with open(var_call_j74lAwmE8ofiz9Y8U0ygMnfC, 'r') as f:
    civic_docs = json.load(f)

# Build set of funding project names with Amount > 50000
funded_projects = set()
for rec in funding_data:
    try:
        amt = float(rec.get('Amount', 0))
    except:
        try:
            amt = float(str(rec.get('Amount','')).replace(',',''))
        except:
            amt = 0
    if amt > 50000:
        funded_projects.add(rec.get('Project_Name','').strip())

# Helper to extract design capital projects from a document text
def extract_design_projects(text):
    projects = []
    txt = text
    header_patterns = [r"Capital Improvement Projects \(Design\)", r"Capital Improvement Projects \(Design\):"]
    start = None
    for pat in header_patterns:
        m = re.search(pat, txt, flags=re.IGNORECASE)
        if m:
            start = m.end()
            break
    if start is None:
        return projects
    # find end by looking for typical next headers
    end_markers = [r"Capital Improvement Projects \(Construction\)", r"Capital Improvement Projects \(Not Started\)", r"Capital Improvement Projects \(Construction\)", r"Capital Improvement Projects \(Not Started\)", r"Capital Improvement Projects \(Construction\)"]
    end = None
    for em in end_markers:
        m2 = re.search(em, txt[start:], flags=re.IGNORECASE)
        if m2:
            cand = start + m2.start()
            if end is None or cand < end:
                end = cand
    snippet = txt[start:end] if end else txt[start: start+5000]  # limit if no end

    # Split into lines and apply heuristics
    lines = [ln.strip() for ln in snippet.splitlines()]

    skip_keywords = ['updates', 'project schedule', 'project description', 'page', 'agenda', 'recommended action', 'discussion', 'item', 'estimated schedule', 'project is', 'updates:', 'project updates']
    for i, line in enumerate(lines):
        if not line:
            continue
        low = line.lower()
        if line.startswith('(cid'):
            continue
        if ':' in line and len(line) < 60:
            # likely a label like 'Updates:' or 'Project Schedule:'
            # but avoid skipping titles containing ':' rarely
            if any(k in low for k in skip_keywords):
                continue
        if any(k in low for k in skip_keywords):
            continue
        # exclude lines that are all uppercase and short (like headers)
        if line.isupper() and len(line.split()) < 6:
            continue
        # exclude lines that look like sentences (contain verbs 'is', 'will', 'are')
        if re.search(r"\b(is|will|are|has|have|awaiting|working|plans|submitted|complete|begin|advertise)\b", low):
            continue
        # Exclude lines that start with digits and are just numbering
        if re.match(r'^\d+$', line):
            continue
        # Likely project title
        # Further trim trailing punctuation
        title = re.sub(r'\s+', ' ', line).strip()
        # Avoid capturing lines like 'Page 1 of 6'
        if re.match(r'page \d+ of', low):
            continue
        # Exclude short non-descriptive words
        if len(title) < 5:
            continue
        projects.append(title)
    # Deduplicate preserving order
    seen = set()
    out = []
    for p in projects:
        if p not in seen:
            seen.add(p)
            out.append(p)
    return out

# Aggregate design capital projects from all civic docs
design_projects = []
for doc in civic_docs:
    text = doc.get('text','')
    extracted = extract_design_projects(text)
    for p in extracted:
        design_projects.append(p)

# Deduplicate
design_projects_unique = []
seen = set()
for p in design_projects:
    if p not in seen:
        seen.add(p)
        design_projects_unique.append(p)

# Now find intersection with funded_projects
matched = []
for p in design_projects_unique:
    # match exact or with minor normalization: strip, collapse spaces
    if p in funded_projects:
        matched.append(p)
    else:
        # try more flexible matching: case-insensitive and remove project suffixes like '(FEMA Project)'
        p_norm = re.sub(r"\s+\(.*?\)$", '', p).strip().lower()
        for fp in funded_projects:
            fp_norm = re.sub(r"\s+\(.*?\)$", '', fp).strip().lower()
            if p_norm == fp_norm:
                matched.append(fp)
                break

# Prepare result
result = {
    'design_projects_extracted': design_projects_unique,
    'funded_projects_count_over_50k': len(funded_projects),
    'matched_projects': matched,
    'matched_count': len(matched)
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_TWSODwC5rKyketYdEYUZZUzs': 'file_storage/call_TWSODwC5rKyketYdEYUZZUzs.json', 'var_call_k7B0exd6Wt1c6Oh0vLH2K3QN': ['civic_docs'], 'var_call_j74lAwmE8ofiz9Y8U0ygMnfC': 'file_storage/call_j74lAwmE8ofiz9Y8U0ygMnfC.json'}

exec(code, env_args)
