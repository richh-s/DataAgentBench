code = """import json, re

# Load funding and civic docs from storage file paths
with open(var_call_pSrNmu38G145Fy0MAdlanHwu, 'r', encoding='utf-8') as f:
    funding = json.load(f)
with open(var_call_Ag1Nv9ECG7ZO4PrsZpGxuiUV, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Helper to strip parenthetical suffix
def strip_paren(name):
    return re.sub(r"\s*\([^)]*\)", "", name).strip()

# Identify candidate funding entries related to FEMA or emergency or warning
candidates = []
for rec in funding:
    pn = rec.get('Project_Name','')
    if re.search(r'FEMA', pn, re.I) or re.search(r'emergency', pn, re.I) or re.search(r'warning', pn, re.I):
        candidates.append(rec)

# Also include funding entries whose base name appears in any civic doc near 'emergency' or 'FEMA'
for rec in funding:
    base = strip_paren(rec.get('Project_Name',''))
    if any(re.search(re.escape(base), doc.get('text',''), re.I) and re.search(r'FEMA|emergency|warning', doc.get('text',''), re.I) for doc in civic_docs):
        if rec not in candidates:
            candidates.append(rec)

results = []

for rec in candidates:
    pn = rec.get('Project_Name','')
    base = strip_paren(pn)
    found_status = None
    # Search civic docs for the project name or base name
    for doc in civic_docs:
        txt = doc.get('text','')
        m = re.search(re.escape(pn), txt, re.I)
        if not m:
            m = re.search(re.escape(base), txt, re.I)
        if not m:
            continue
        idx = m.start()
        window_start = max(0, idx-1000)
        window = txt[window_start: idx+500]
        wlow = window.lower()
        # Priority checks
        if re.search(r'currently under construction', wlow) or re.search(r'complete construction', wlow) or re.search(r'construction was completed', wlow) or re.search(r'complete construction:', wlow):
            found_status = 'completed'
        elif re.search(r'complete design|preliminary design|design plans|working with the consultant|plans and specifications have been completed|staff is working with the consultant|project is in the preliminary design', wlow):
            found_status = 'design'
        elif re.search(r'not started|identified in|waiting for|waiting for the agreement|waiting for the agreement|rejected all bids due to a budget shortfall', wlow):
            # treat waiting or identified as not started
            found_status = 'not started'
        else:
            # look for section headers before idx
            prior = txt[max(0, idx-2000): idx]
            # find last occurrence of Capital Improvement Projects and capture the subheader line if present
            si = prior.rfind('Capital Improvement Projects')
            if si!=-1:
                header_fragment = prior[si: si+200]
                if 'Design' in header_fragment:
                    found_status = 'design'
                elif 'Construction' in header_fragment:
                    found_status = 'completed'
                elif 'Not Started' in header_fragment:
                    found_status = 'not started'
        if not found_status:
            # final fallback: search nearby 500 chars for keywords
            if re.search(r'caloes|fema', wlow):
                # if FEMA/CalOES mentioned near, probably design/awaiting approval -> design
                found_status = 'design'
            else:
                found_status = 'unknown'
        break
    # If not found in any doc, status unknown
    if not found_status:
        found_status = 'unknown'
    # Normalize amount to integer if possible
    amount = rec.get('Amount')
    try:
        amount_val = int(amount)
    except:
        try:
            amount_val = int(float(amount))
        except:
            amount_val = None
    results.append({
        'Project_Name': pn,
        'Funding_Source': rec.get('Funding_Source'),
        'Amount': amount_val,
        'Status': found_status
    })

# Deduplicate by Project_Name keeping first
seen = set()
unique_results = []
for r in results:
    if r['Project_Name'] not in seen:
        unique_results.append(r)
        seen.add(r['Project_Name'])

import json
print("__RESULT__:")
print(json.dumps(unique_results))"""

env_args = {'var_call_Ag1Nv9ECG7ZO4PrsZpGxuiUV': 'file_storage/call_Ag1Nv9ECG7ZO4PrsZpGxuiUV.json', 'var_call_pSrNmu38G145Fy0MAdlanHwu': 'file_storage/call_pSrNmu38G145Fy0MAdlanHwu.json'}

exec(code, env_args)
