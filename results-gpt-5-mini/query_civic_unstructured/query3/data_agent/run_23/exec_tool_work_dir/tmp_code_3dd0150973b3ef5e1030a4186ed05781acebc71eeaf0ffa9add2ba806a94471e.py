code = """import json, re

# Load tool results from storage variables
civic_docs_path = var_call_4mLAARyPY98ipz6fdcJufYyy
funding_path = var_call_5ZTqNs3HVZYVKoxQ2862Me1r

with open(funding_path, 'r') as f:
    funding = json.load(f)

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Normalize funding records
for rec in funding:
    # Ensure Amount is int
    try:
        rec['Amount'] = int(rec.get('Amount') if rec.get('Amount') is not None else 0)
    except:
        try:
            rec['Amount'] = int(float(rec.get('Amount')))
        except:
            rec['Amount'] = None
    rec['Project_Name_raw'] = rec.get('Project_Name', '')
    rec['Project_Name_low'] = rec.get('Project_Name', '').lower()

# Prepare civic docs texts lowercased for searching and header positions
docs = []
for d in civic_docs:
    text = d.get('text','')
    low = text.lower()
    docs.append({'filename': d.get('filename',''), 'text': text, 'low': low})

# Headers to detect and map to statuses
header_status_map = [
    ("capital improvement projects (design)", 'design'),
    ("capital improvement projects (construction)", 'completed'),
    ("capital improvement projects (not started)", 'not started'),
    ("capital improvement projects (design)", 'design'),
    ("capital improvement projects (construction)", 'completed'),
    ("capital improvement projects (not started)", 'not started'),
    ("disaster recovery projects", 'design'),
    ("disaster recovery projects status", 'design')
]

results = []

# Helper to find status for a project by looking at the civic docs where it appears
def find_status_for_project(project_low):
    # Return first status found or None
    for doc in docs:
        idx = doc['low'].find(project_low)
        if idx != -1:
            # collect header positions
            header_positions = []
            for hdr, st in header_status_map:
                hidx = doc['low'].find(hdr)
                if hidx != -1:
                    header_positions.append((hidx, st))
            if header_positions:
                # find the header with largest position less than idx
                preceding = [(p,s) for (p,s) in header_positions if p < idx]
                if preceding:
                    chosen = max(preceding, key=lambda x: x[0])
                    return chosen[1]
            # If no header found, attempt to infer from nearby phrases within +/-300 chars
            window = doc['low'][max(0, idx-300): idx+300]
            if 'construction was completed' in window or 'notice of completion' in window or 'complete construction' in window:
                return 'completed'
            if 'preliminary design' in window or 'complete design' in window or 'design plans' in window or 'final design' in window:
                return 'design'
            if 'project is not started' in window or 'not started' in window or 'identified' in window:
                return 'not started'
            # Fallback: if doc contains 'construction' near
            if 'construction' in window:
                return 'completed'
            if 'design' in window:
                return 'design'
    return None

# Build set of funding records to include
included = []
for rec in funding:
    pname_low = rec['Project_Name_low']
    include = False
    status = None
    # include if project name contains fema or emergency
    if 'fema' in pname_low or 'emergency' in pname_low:
        include = True
    else:
        # check if project name appears in any civic doc that contains fema or emergency
        for doc in docs:
            if pname_low in doc['low']:
                if ('fema' in doc['low']) or ('emergency' in doc['low']):
                    include = True
                    status = find_status_for_project(pname_low)
                    break
        # Also include if project name appears and doc contains word 'warning' (for outdoor warning signs/sirens)
            # (only if previously not included)
            # Note: we don't double-add
    # Additionally, if not included, check if any civic doc contains 'emergency' or 'fema' and the project name appears anywhere in that doc
    if not include:
        for doc in docs:
            if ('fema' in doc['low'] or 'emergency' in doc['low']) and pname_low in doc['low']:
                include = True
                status = find_status_for_project(pname_low)
                break
    if include:
        if status is None:
            status = find_status_for_project(pname_low)
        included.append({'Project_Name': rec['Project_Name_raw'], 'Funding_Source': rec.get('Funding_Source'), 'Amount': rec.get('Amount'), 'Status': status})

# Additionally, find projects mentioned in civic docs that include the keywords 'fema' or 'emergency' even if not in funding table
# But the instruction expects joining funding data; skip those without funding

# Remove duplicates by Project_Name keeping first
seen = set()
final = []
for r in included:
    key = r['Project_Name']
    if key not in seen:
        seen.add(key)
        final.append(r)

# Sort final by Project_Name
final_sorted = sorted(final, key=lambda x: x['Project_Name'].lower())

# Output as JSON string
out = json.dumps(final_sorted)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_4mLAARyPY98ipz6fdcJufYyy': 'file_storage/call_4mLAARyPY98ipz6fdcJufYyy.json', 'var_call_5ZTqNs3HVZYVKoxQ2862Me1r': 'file_storage/call_5ZTqNs3HVZYVKoxQ2862Me1r.json'}

exec(code, env_args)
