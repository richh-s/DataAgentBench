code = """import json
import re

# Load the stored query results from files
with open(var_call_cw1ExblnS6q3arcB6rY11l2F, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_xuXPISfPelohqatkiXoesOCZ, 'r') as f:
    funding_records = json.load(f)

# Extract 'Capital Improvement Projects (Design)' blocks from civic documents
design_projects = []
for doc in civic_docs:
    text = doc.get('text','')
    # find start of design section
    m = re.search(r'Capital Improvement Projects \(Design\)', text, re.I)
    if not m:
        # try simpler phrase
        m = re.search(r'Capital Improvement Projects\s*\(Design\)', text, re.I)
    if not m:
        continue
    start = m.end()
    # find end: look for common following headers
    end_match = re.search(r'Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)', text[start:], re.I)
    if end_match:
        end = start + end_match.start()
    else:
        # fallback: try to find 'Capital Improvement Projects (Construction)' anywhere after
        em = re.search(r'Capital Improvement Projects \(Construction\)', text[start:], re.I)
        if em:
            end = start + em.start()
        else:
            end = len(text)
    block = text[start:end]
    # split block into segments separated by 2+ newlines
    segments = re.split(r'\n\s*\n', block)
    for seg in segments:
        first_line = seg.strip().split('\n')[0].strip()
        if not first_line:
            continue
        # filter out lines that are clearly not project titles
        if re.search(r'Updates:|Project Schedule|Estimated Schedule|Project Description|RECOMMENDED ACTION|DISCUSSION|Page \d+|Agenda Item|Agenda', first_line, re.I):
            continue
        if first_line.lower().startswith('(cid'):
            continue
        # Additional filter: ignore lines that are short and look like headers
        if len(first_line) < 4:
            continue
        # add as project name
        design_projects.append(first_line)

# Deduplicate while preserving order
seen = set()
unique_design_projects = []
for p in design_projects:
    if p not in seen:
        seen.add(p)
        unique_design_projects.append(p)

# Normalize function to compare names
def normalize(name):
    name = re.sub(r"\(.*?\)", "", name)  # remove parenthetical parts
    name = name.lower()
    name = re.sub(r"[^a-z0-9\s]", " ", name)
    name = re.sub(r"\s+", " ", name).strip()
    return name

funding_norms = []
for r in funding_records:
    pname = r.get('Project_Name','')
    amt = r.get('Amount')
    try:
        amt_int = int(amt)
    except:
        try:
            amt_int = int(float(amt))
        except:
            amt_int = 0
    funding_norms.append({'orig': pname, 'norm': normalize(pname), 'amount': amt_int})

# Match design projects (capital) to funding > 50k
matched_projects = []
for p in unique_design_projects:
    p_norm = normalize(p)
    if len(p_norm) < 3:
        continue
    for fr in funding_norms:
        if fr['amount'] <= 50000:
            continue
        fn = fr['norm']
        # match if exact norm equality or one contains the other
        if p_norm == fn or p_norm in fn or fn in p_norm:
            matched_projects.append({'project_name': p, 'funding_record': fr})
            break

# Prepare result: count unique matched capital design projects
matched_names = [m['project_name'] for m in matched_projects]
count = len(matched_names)

import json
result = {'count': count, 'matched_projects': matched_names}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_7N3Y42AyKSQv4OAbqJJcpBzF': ['civic_docs'], 'var_call_cw1ExblnS6q3arcB6rY11l2F': 'file_storage/call_cw1ExblnS6q3arcB6rY11l2F.json', 'var_call_xuXPISfPelohqatkiXoesOCZ': 'file_storage/call_xuXPISfPelohqatkiXoesOCZ.json'}

exec(code, env_args)
