code = """import json, re

# Load data from storage file paths
funding_path = var_call_ATm3CpOdIAXM5mLPJXpp6T1q
civic_path = var_call_RbLnR9lPViXAjmDMgVmuuyTJ

with open(funding_path, 'r') as f:
    funding = json.load(f)
with open(civic_path, 'r') as f:
    civic = json.load(f)

# Normalize funding records
for r in funding:
    # Ensure Amount is integer
    try:
        r['Amount'] = int(r.get('Amount') or 0)
    except:
        # remove non-digits
        nums = re.sub(r"[^0-9]", "", str(r.get('Amount') or '0'))
        r['Amount'] = int(nums) if nums else 0

# Build a map of funding records by project name
# We'll focus on funding records that mention 'park' in their name
park_funding = [r for r in funding if 'park' in r['Project_Name'].lower()]

# Prepare civic texts combined
civic_texts = [doc['text'] for doc in civic]

# Function to test if a project is marked completed in 2022 in any civic doc
def project_completed_in_2022(project_name):
    pn = project_name.lower()
    pn_tokens = [t for t in re.split(r"\W+", pn) if t]
    for text in civic_texts:
        tlower = text.lower()
        # Try exact substring match first
        idx = tlower.find(pn)
        if idx != -1:
            # search window after occurrence for 'completed' and '2022'
            window = tlower[idx: idx + 2000]
            if re.search(r"completed", window) and re.search(r"2022", window):
                return True
            # also check before occurrence
            window2 = tlower[max(0, idx-200): idx+200]
            if re.search(r"completed", window2) and re.search(r"2022", window2):
                return True
        # If exact not found, try token overlap: require at least 2 tokens match near each other
        # find occurrences of first two significant tokens
        if len(pn_tokens) >= 2:
            # build regex that allows up to 10 words between tokens
            token_regex = r"\\b" + re.escape(pn_tokens[0]) + r"\\b.*?\\b" + re.escape(pn_tokens[1]) + r"\\b"
            if re.search(token_regex, tlower, flags=re.DOTALL):
                # find match and check for completed and 2022 nearby
                m = re.search(token_regex, tlower, flags=re.DOTALL)
                idx2 = m.start()
                window = tlower[idx2: idx2+2000]
                if re.search(r"completed", window) and re.search(r"2022", window):
                    return True
        # Also check if the text contains 'park' and project-specific unique token and completed+2022
        if 'park' in pn_tokens:
            # find any occurrence of 'park' in text
            all_idxs = [m.start() for m in re.finditer(r"park", tlower)]
            for pi in all_idxs:
                window = tlower[max(0, pi-200): pi+200]
                # check for any overlap with project tokens
                token_match = any(tok in window for tok in pn_tokens if len(tok) > 3)
                if token_match and re.search(r"completed", window) and re.search(r"2022", window):
                    return True
    return False

# Now check each park funding record if completed in 2022
matched_records = []
for r in park_funding:
    name = r['Project_Name']
    if project_completed_in_2022(name):
        matched_records.append(r)

# Additionally, some park projects might be referred in civic docs but funding table name differs (e.g., 'Legacy Park Benches and Arbors Renovation' etc.)
# We already considered all funding rows with 'park' in name. We'll also check for other funding rows whose names might match civic docs park projects via partial token overlap
# Find civic doc park project headings by scanning for lines with 'park' and taking the line as project name candidate
park_candidates = set()
for text in civic_texts:
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if 'park' in line.lower():
            ln = line.strip()
            # clean lines that are too short or contain 'updates' etc
            if len(ln) > 3 and not re.search(r'updates|project|page|item|agenda', ln.lower()):
                park_candidates.add(ln)

# For each funding record not already matched but with tokens overlapping park candidate, check completion
for r in funding:
    if r in matched_records:
        continue
    name = r['Project_Name']
    lname = name.lower()
    if 'park' in lname:
        # already in park_funding but maybe not matched earlier due to search; recheck with more relaxed match
        if project_completed_in_2022(name):
            matched_records.append(r)

# Sum amounts from matched_records
total = sum(r['Amount'] for r in matched_records)

# For transparency in output, also list matched project names and amounts
output = {
    'total_funding_completed_parks_2022': total,
    'matched_projects': [{ 'Project_Name': r['Project_Name'], 'Amount': r['Amount'] } for r in matched_records]
}

import json
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_ATm3CpOdIAXM5mLPJXpp6T1q': 'file_storage/call_ATm3CpOdIAXM5mLPJXpp6T1q.json', 'var_call_4Gmfh6nK9VlLkgS6gVcK8nr7': ['civic_docs'], 'var_call_RbLnR9lPViXAjmDMgVmuuyTJ': 'file_storage/call_RbLnR9lPViXAjmDMgVmuuyTJ.json'}

exec(code, env_args)
