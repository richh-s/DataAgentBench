code = """import json, re

# Load the results from the previous query_db calls
with open(var_call_PKlwf4Qk93xrFly3pK1f1W1I, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_UhGNs1Y0qDSFpmbp65i5E0oC, 'r') as f:
    funding = json.load(f)

# Normalize funding amounts and prepare lookup
for rec in funding:
    # ensure Amount is int
    rec['Amount'] = int(rec['Amount'])
    rec['Project_Name_norm'] = rec['Project_Name'].strip().lower()

# Extract project names from civic docs where 'completed' and '2022' appear
completed_2022_projects = set()
pattern_completed_2022 = re.compile(r'completed[^\n]{0,100}?2022|completed[, ]+2022|completed.*2022', re.IGNORECASE)
park_keywords = ['park', 'playground']

for doc in civic_docs:
    text = doc.get('text','')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if 'completed' in line.lower() and '2022' in line:
            # search backwards for a candidate project title
            for j in range(max(0, i-6), i):
                cand = lines[j].strip()
                if not cand:
                    continue
                low = cand.lower()
                # skip lines that are clearly not titles
                if any(x in low for x in ['updates', 'project schedule', 'page', 'agenda', 'item', 'meeting', 'subject', 'approved', '(cid:', 'date prepared']):
                    continue
                # If candidate contains park-related keywords, record it
                if any(k in low for k in park_keywords):
                    # clean candidate: remove trailing colons
                    cand_clean = cand.rstrip(':').strip()
                    completed_2022_projects.add(cand_clean)
                    break
            else:
                # fallback: try to extract inline project name via preceding punctuation or heading patterns
                # e.g., lines like 'Bluffs Park Shade Structure\n\n(cid:190) Updates: Construction was completed November 2022.'
                # try to find a title pattern earlier in the document using regex: look for lines with Park words
                for j in range(0, i):
                    cand = lines[j].strip()
                    if cand and any(k in cand.lower() for k in park_keywords):
                        completed_2022_projects.add(cand.rstrip(':').strip())
                        break

# Now match these project names to funding records using case-insensitive matching (exact or substring)
matched_projects = []
matched_funding_total = 0
matched_funding_names = set()

for proj in completed_2022_projects:
    low_proj = proj.lower()
    found = False
    for rec in funding:
        if low_proj == rec['Project_Name_norm']:
            matched_projects.append({'name': rec['Project_Name'], 'amount': rec['Amount']})
            matched_funding_total += rec['Amount']
            matched_funding_names.add(rec['Project_Name'])
            found = True
        elif low_proj in rec['Project_Name_norm'] or rec['Project_Name_norm'] in low_proj:
            matched_projects.append({'name': rec['Project_Name'], 'amount': rec['Amount']})
            matched_funding_total += rec['Amount']
            matched_funding_names.add(rec['Project_Name'])
            found = True
    # no direct funding match found; continue

# Additionally, consider any funding projects that explicitly mention 'Park' and have a completion mention in any civic doc for 2022 even if extraction missed
# We'll check funding projects with 'park' in name and see if their names appear near 'completed' and '2022' in any civic doc text
for rec in funding:
    if 'park' in rec['Project_Name'].lower():
        name_low = rec['Project_Name'].lower()
        if rec['Project_Name'] in matched_funding_names:
            continue
        # search in civic docs text for patterns like '<Project_Name>' followed by 'completed' and '2022' within 200 chars
        for doc in civic_docs:
            txt = doc.get('text','')
            idx = txt.lower().find(name_low)
            if idx != -1:
                # search nearby for completed and 2022
                window = txt[max(0, idx-200): idx+len(name_low)+200].lower()
                if 'completed' in window and '2022' in window:
                    matched_projects.append({'name': rec['Project_Name'], 'amount': rec['Amount']})
                    matched_funding_total += rec['Amount']
                    matched_funding_names.add(rec['Project_Name'])
                    break

# Prepare result
result = {
    'completed_2022_park_projects_found_in_docs': sorted(list(completed_2022_projects)),
    'matched_funding_records': matched_projects,
    'total_funding_for_park_projects_completed_in_2022': matched_funding_total
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_PKlwf4Qk93xrFly3pK1f1W1I': 'file_storage/call_PKlwf4Qk93xrFly3pK1f1W1I.json', 'var_call_UhGNs1Y0qDSFpmbp65i5E0oC': 'file_storage/call_UhGNs1Y0qDSFpmbp65i5E0oC.json'}

exec(code, env_args)
