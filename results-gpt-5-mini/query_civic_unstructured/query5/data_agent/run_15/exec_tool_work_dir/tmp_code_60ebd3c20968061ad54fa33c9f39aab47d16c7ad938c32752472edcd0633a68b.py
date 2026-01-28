code = """import json, re
# Load the large results from the provided storage file paths
with open(var_call_LI9QaoTR0VnE2QJsd1lU8YiW, 'r') as f:
    funding_records = json.load(f)
with open(var_call_FIuWCg0txJD8m6iJmSv8qz72, 'r') as f:
    civic_docs = json.load(f)

# Normalize funding amounts and prepare list
for r in funding_records:
    try:
        r['Amount'] = int(r.get('Amount') or 0)
    except:
        # remove non-digit characters
        s = re.sub(r"[^0-9]", "", str(r.get('Amount') or '0'))
        r['Amount'] = int(s) if s else 0

# Disaster-related keyword pattern
disaster_kw = re.compile(r'FEMA|CalOES|CalJPIA|\bdisaster\b|\bfire\b|Woolsey|Recovery|FEMA/CalOES', re.I)

matched_projects = []

# Pre-concatenate all civic texts for easier searching
all_texts = [(doc.get('filename',''), doc.get('text','')) for doc in civic_docs]

for rec in funding_records:
    pname = rec.get('Project_Name','')
    base_name = re.sub(r'\s*\(.*?\)\s*', ' ', pname).strip()
    is_disaster = bool(disaster_kw.search(pname))
    if not is_disaster:
        # also check if base_name contains typical disaster words
        if disaster_kw.search(base_name):
            is_disaster = True
    if not is_disaster:
        continue
    # Search civic docs for project mentions and look for '2022' in nearby context
    found_2022 = False
    matched_filenames = []
    lname = pname.lower()
    lbase = base_name.lower()
    for filename, text in all_texts:
        lt = text.lower()
        # try exact name first
        idx = lt.find(lname)
        if idx == -1 and lbase:
            idx = lt.find(lbase)
        if idx != -1:
            start = max(0, idx-300)
            end = min(len(lt), idx+len(lname)+300)
            window = lt[start:end]
            if '2022' in window:
                found_2022 = True
                matched_filenames.append(filename)
    if found_2022:
        matched_projects.append({
            'Project_Name': pname,
            'Base_Name': base_name,
            'Amount': rec['Amount'],
            'Matched_Files': matched_filenames
        })

# Sum amounts
total = sum(p['Amount'] for p in matched_projects)

# Prepare output
out = {
    'total_funding': total,
    'projects': matched_projects
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_FIuWCg0txJD8m6iJmSv8qz72': 'file_storage/call_FIuWCg0txJD8m6iJmSv8qz72.json', 'var_call_LI9QaoTR0VnE2QJsd1lU8YiW': 'file_storage/call_LI9QaoTR0VnE2QJsd1lU8YiW.json'}

exec(code, env_args)
