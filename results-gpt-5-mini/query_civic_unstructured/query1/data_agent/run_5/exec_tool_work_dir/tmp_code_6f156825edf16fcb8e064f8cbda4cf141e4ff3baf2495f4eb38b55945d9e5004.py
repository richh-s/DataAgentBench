code = """import json

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

# Extract design capital project names from civic docs using simpler heuristics
design_projects = set()
for doc in docs:
    text = doc.get('text', '')
    if not text:
        continue
    lower = text.lower()
    header = 'capital improvement projects (design)'
    if header not in lower:
        continue
    start = lower.find(header)
    # find end markers
    end_markers = ['capital improvement projects (construction)', 'capital improvement projects (not started)']
    end = len(text)
    for em in end_markers:
        idx = lower.find(em, start+1)
        if idx != -1:
            end = min(end, idx)
    block = text[start:end]
    # split into lines
    lines = block.splitlines()
    # look for lines that are likely project titles: a line followed within next 4 lines by a line containing 'updates' or 'project schedule' or '(cid:'
    for i, line in enumerate(lines):
        s = line.strip()
        if not s:
            continue
        # skip lines that look like headings or page markers
        low = s.lower()
        if any(k in low for k in ['agenda', 'page', 'recommended action', 'discussion', 'item', 'public works commission']):
            continue
        # check next few lines
        following = ' '.join(lines[i+1:i+5]).lower()
        if ('updates' in following) or ('project schedule' in following) or ('(cid:' in following) or ('updates:' in following):
            # filter out short or numeric lines
            if len(s) >= 4:
                # remove leading bullets or markers
                s_clean = s.lstrip('\uf0b7•- ').strip()
                design_projects.add(s_clean)

# Also as fallback get any bold-like headings that include word 'Project' within the design block
for doc in docs:
    text = doc.get('text','')
    if not text:
        continue
    lower = text.lower()
    header = 'capital improvement projects (design)'
    if header not in lower:
        continue
    start = lower.find(header)
    end_markers = ['capital improvement projects (construction)', 'capital improvement projects (not started)']
    end = len(text)
    for em in end_markers:
        idx = lower.find(em, start+1)
        if idx != -1:
            end = min(end, idx)
    block = text[start:end]
    for line in block.splitlines():
        s = line.strip()
        if 'project' in s.lower() and len(s) > 10 and not s.lower().startswith('(cid:'):
            design_projects.add(s)

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

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_cPoQSPGxNvpW6SvSA53ZT9xM': ['civic_docs'], 'var_call_Ma8oIGUwnH0j9CZPgDDpHk8d': ['Funding'], 'var_call_XqQKXQCbSVgZ3PMW0v33W6G7': 'file_storage/call_XqQKXQCbSVgZ3PMW0v33W6G7.json', 'var_call_xYjO3mcSeBIt97sirYJWD4aI': 'file_storage/call_xYjO3mcSeBIt97sirYJWD4aI.json'}

exec(code, env_args)
