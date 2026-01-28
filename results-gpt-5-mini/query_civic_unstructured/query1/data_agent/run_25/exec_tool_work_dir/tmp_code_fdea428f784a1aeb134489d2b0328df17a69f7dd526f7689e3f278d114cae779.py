code = """import json, re

# Load data from storage file paths provided by previous tool calls
with open(var_call_fNDIQg0o0VoydorlD2pQQCGn, 'r', encoding='utf-8') as f:
    docs = json.load(f)
with open(var_call_YrZ6gGIqZD0ctoUa5lEpkZKS, 'r', encoding='utf-8') as f:
    funding_rows = json.load(f)

# Helper to normalize project names
def normalize(name):
    if not name:
        return ''
    s = name
    # remove parenthetical content
    s = re.sub(r"\(.*?\)", "", s)
    # replace ampersand with and
    s = s.replace('&', ' and ')
    # remove non-alphanumeric characters except spaces
    s = re.sub(r'[^0-9a-zA-Z ]+', ' ', s)
    # collapse spaces and lowercase
    s = re.sub(r'\s+', ' ', s).strip().lower()
    return s

# Extract project names under Capital Improvement Projects (Design)
design_projects = set()
section_heading_re = re.compile(r'Capital Improvement Projects\s*\(Design\)', flags=re.IGNORECASE)
end_section_re = re.compile(r'Capital Improvement Projects\s*\(Construction\)|Capital Improvement Projects\s*\(Not Started\)', flags=re.IGNORECASE)
for doc in docs:
    text = doc.get('text','')
    m = section_heading_re.search(text)
    if not m:
        continue
    start = m.end()
    em = end_section_re.search(text[start:])
    if em:
        section = text[start:start+em.start()]
    else:
        section = text[start:]
    lines = [ln.strip() for ln in section.splitlines()]
    # iterate lines and pick lines that look like project names
    for i, line in enumerate(lines):
        if not line:
            continue
        # skip lines that are clearly not project names
        if len(line) < 3:
            continue
        low = line.lower()
        # Skip headings or lines like 'updates:' etc
        if 'updates:' in low or 'project schedule' in low or 'page'==low or low.startswith('agenda'):
            continue
        # find next non-empty line
        next_nonempty = ''
        for j in range(i+1, len(lines)):
            if lines[j]:
                next_nonempty = lines[j]
                break
        nn = next_nonempty.lower()
        # If the next non-empty line indicates details about a project, current line is likely a project name
        if any(k in nn for k in ['updates', '(cid:', 'project description', 'project schedule', 'estimated schedule', 'project updates']):
            design_projects.add(line.strip())
        else:
            # Also consider lines that end with 'Project' or contain 'Park' or 'Road' or 'Repair' etc as potential project names
            if re.search(r'\b(project|park|road|repairs|repair|study|improvements|walkway|playground|facility)\b', low):
                design_projects.add(line.strip())

# Normalize funding project names for quick matching
funding_norms = []
for r in funding_rows:
    pname = r.get('Project_Name') or r.get('Project_Name')
    amt = r.get('Amount')
    try:
        amt_val = float(amt)
    except:
        try:
            amt_val = float(str(amt).replace(',',''))
        except:
            amt_val = 0
    funding_norms.append({'orig': pname, 'norm': normalize(pname), 'amount': amt_val})

# Match design capital projects to funding records with amount > 50000
matched = []
for proj in sorted(design_projects):
    norm_proj = normalize(proj)
    if not norm_proj:
        continue
    for fr in funding_norms:
        if fr['amount'] <= 50000:
            continue
        fn = fr['norm']
        if not fn:
            continue
        # match if one name is substring of the other
        if norm_proj in fn or fn in norm_proj:
            matched.append({'project_name': proj, 'funding_record': fr['orig'], 'amount': fr['amount']})
            break

# Unique matched project names
unique_matched_projects = sorted({m['project_name'] for m in matched})
count = len(unique_matched_projects)

# Prepare result
result = {'count': count, 'matched_projects': unique_matched_projects}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_YrZ6gGIqZD0ctoUa5lEpkZKS': 'file_storage/call_YrZ6gGIqZD0ctoUa5lEpkZKS.json', 'var_call_fNDIQg0o0VoydorlD2pQQCGn': 'file_storage/call_fNDIQg0o0VoydorlD2pQQCGn.json'}

exec(code, env_args)
