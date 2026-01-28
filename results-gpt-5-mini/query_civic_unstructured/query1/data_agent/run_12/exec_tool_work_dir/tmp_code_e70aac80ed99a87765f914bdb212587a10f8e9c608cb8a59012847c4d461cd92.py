code = """import json
import re

# Load civic docs
civic_path = var_call_ZEagpG3qicTk8xDnkvuXEAoZ
if isinstance(civic_path, str):
    with open(civic_path, 'r', encoding='utf-8') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_path

# Load funding data
funding_path = var_call_zb5hL7XuNPEyB7pXOtEhCvU5
if isinstance(funding_path, str):
    with open(funding_path, 'r', encoding='utf-8') as f:
        funding = json.load(f)
else:
    funding = funding_path

# Normalize funding amounts and prepare list
for row in funding:
    try:
        row['Amount'] = int(row.get('Amount', 0))
    except:
        # remove non-digits
        s = re.sub(r"[^0-9]", "", str(row.get('Amount', '0')))
        row['Amount'] = int(s) if s else 0

# Function to extract design project names from a document text
def extract_design_projects(text):
    names = []
    # find the Design section
    m = re.search(r'Capital Improvement Projects \(Design\)', text, flags=re.IGNORECASE)
    if not m:
        return names
    start = m.end()
    # find next section marker
    end_markers = [r'Capital Improvement Projects \(Construction\)',
                   r'Capital Improvement Projects \(Not Started\)',
                   r'Capital Improvement Projects \(Completed\)',
                   r'Capital Improvement Projects']
    end = None
    for em in end_markers:
        me = re.search(em, text[start:], flags=re.IGNORECASE)
        if me:
            pos = start + me.start()
            if end is None or pos < end:
                end = pos
    section = text[start:end] if end else text[start: start+10000]

    # heuristic regex patterns to capture project title lines followed by updates or Project Description
    patterns = [r'\n([^\n]{5,200}?)\n\n\(cid:',
                r'\n([^\n]{5,200}?)\n\nUpdates:',
                r'\n([^\n]{5,200}?)\n\nProject Description:',
                r'\n([^\n]{5,200}?)\n\nProject Updates:',
                r'\n([^\n]{5,200}?)\n\nEstimated Schedule:',
                r'\n([^\n]{5,200}?)\n\nProject Schedule:']
    for pat in patterns:
        for match in re.findall(pat, section, flags=re.IGNORECASE):
            name = match.strip()
            # filter out lines that are too generic
            if len(name) > 3 and 'Page' not in name and 'Agenda Item' not in name:
                names.append(name)
    # As a fallback, also look for lines in the section that are title-cased and not lines starting with '(' or lower-case
    if not names:
        lines = [ln.strip() for ln in section.splitlines() if ln.strip()]
        for i, ln in enumerate(lines):
            if len(ln) > 5 and not ln.endswith(':') and not ln.startswith('(') and not ln.lower().startswith('page'):
                # avoid lines that are likely sentences
                if ln[0].isupper():
                    names.append(ln)
    # deduplicate while preserving order
    seen = set()
    uniq = []
    for n in names:
        if n.lower() not in seen:
            seen.add(n.lower())
            uniq.append(n)
    return uniq

# Extract project names across all civic docs
design_projects = []
for doc in civic_docs:
    text = doc.get('text','')
    ps = extract_design_projects(text)
    for p in ps:
        if p not in design_projects:
            design_projects.append(p)

# Now, for each design project, find matching funding rows and sum amounts
results = []
for proj in design_projects:
    proj_l = proj.lower()
    matching_rows = []
    total_amount = 0
    for row in funding:
        fn = str(row.get('Project_Name','')).lower()
        if not fn:
            continue
        # match if exact or substring either way
        if proj_l == fn or proj_l in fn or fn in proj_l:
            matching_rows.append({'Project_Name': row.get('Project_Name'), 'Amount': row.get('Amount')})
            total_amount += row.get('Amount', 0)
    results.append({'project': proj, 'matched_funding_rows': matching_rows, 'total_amount': total_amount})

# Count design capital projects with funding > 50000
count = sum(1 for r in results if r['total_amount'] > 50000)

output = {'count': count, 'details': results}

import json
print("----BEGIN PRINT FORMAT----")
print('__RESULT__:')
print(json.dumps(output))
print("----END PRINT FORMAT----")"""

env_args = {'var_call_ZEagpG3qicTk8xDnkvuXEAoZ': 'file_storage/call_ZEagpG3qicTk8xDnkvuXEAoZ.json', 'var_call_zb5hL7XuNPEyB7pXOtEhCvU5': 'file_storage/call_zb5hL7XuNPEyB7pXOtEhCvU5.json'}

exec(code, env_args)
