code = """import json
import re

# Load data from storage-provided file paths
with open(var_call_xYjO3mcSeBIt97sirYJWD4aI, 'r', encoding='utf-8') as f:
    docs = json.load(f)
with open(var_call_XqQKXQCbSVgZ3PMW0v33W6G7, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Normalize funding records and keep those >50000
funding_records = []
for r in funding:
    name = r.get('Project_Name', '').strip()
    amt = r.get('Amount')
    try:
        amt_val = int(str(amt).replace(',', '').strip())
    except:
        try:
            amt_val = int(float(str(amt)))
        except:
            amt_val = 0
    if amt_val > 50000:
        funding_records.append({'Project_Name': name, 'Amount': amt_val})

# Extract design capital project names from civic docs
design_projects = set()
for doc in docs:
    text = doc.get('text', '')
    if not text:
        continue
    # Find the Design section
    m = re.search(r'Capital Improvement Projects \(Design\)', text, flags=re.IGNORECASE)
    if not m:
        continue
    start = m.end()
    # Find end marker for the design section
    end_markers = [
        'Capital Improvement Projects (Construction)',
        'Capital Improvement Projects (Not Started)',
        'Capital Improvement Projects (Construction)',
        'Capital Improvement Projects (Not Started)',
        'Capital Improvement Projects (Construction)'
    ]
    end = len(text)
    for em in end_markers:
        i = text.find(em, start)
        if i != -1:
            end = min(end, i)
    block = text[start:end]
    # Find project titles in the block. Projects often are followed by a blank line and "(cid:... ) Updates" or "(cid:... ) Updates:"
    pattern = re.compile(r'(?:\n\n|^)([^\n]{3,200}?)\n\n\(cid:', flags=re.IGNORECASE)
    found = pattern.findall(block)
    for fproj in found:
        name = fproj.strip()
        # Filter out lines that are clearly not project names
        if len(name) < 3:
            continue
        # Exclude lines that look like headings or page markers
        if re.search(r'page \d+ of', name, flags=re.IGNORECASE):
            continue
        # Exclude common words
        if name.lower() in ('discussion', 'recommended action', 'discussion:'):
            continue
        design_projects.add(name)

# As a fallback, also try to capture lines that appear as headings followed by "Updates:" with or without the (cid) markers
for doc in docs:
    text = doc.get('text','')
    matches = re.findall(r'\n\n([^\n]{3,200}?)\n\nUpdates:', text, flags=re.IGNORECASE)
    for m in matches:
        design_projects.add(m.strip())

# Now match funding projects to design projects using case-insensitive substring matching
matched_design_projects = set()
for fr in funding_records:
    fname = fr['Project_Name'].strip()
    if not fname:
        continue
    lname = fname.lower()
    for d in design_projects:
        ld = d.lower()
        # consider a match if one contains the other and the shorter is at least 4 chars
        if (ld in lname or lname in ld) and (len(ld) >= 4 and len(lname) >= 4):
            matched_design_projects.add(d)
            break

# Prepare result
result = {
    'design_projects_extracted_count': len(design_projects),
    'design_projects_sample': sorted(list(design_projects))[:50],
    'funding_records_over_50000_count': len(funding_records),
    'matched_design_projects_count': len(matched_design_projects),
    'matched_design_projects': sorted(list(matched_design_projects))
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_cPoQSPGxNvpW6SvSA53ZT9xM': ['civic_docs'], 'var_call_Ma8oIGUwnH0j9CZPgDDpHk8d': ['Funding'], 'var_call_XqQKXQCbSVgZ3PMW0v33W6G7': 'file_storage/call_XqQKXQCbSVgZ3PMW0v33W6G7.json', 'var_call_xYjO3mcSeBIt97sirYJWD4aI': 'file_storage/call_xYjO3mcSeBIt97sirYJWD4aI.json'}

exec(code, env_args)
