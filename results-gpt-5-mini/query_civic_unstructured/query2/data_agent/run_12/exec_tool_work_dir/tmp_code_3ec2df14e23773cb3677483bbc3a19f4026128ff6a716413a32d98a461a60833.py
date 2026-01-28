code = """import json
import re

# Load data from storage-provided file paths
with open(var_call_s3s9kMHqzePGSEzEZp7cikyi, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_y31CKagxiG5kZ38LxNmcdJ1z, 'r') as f:
    funding = json.load(f)

# Normalize funding amounts
for r in funding:
    try:
        r['Amount'] = int(r['Amount'])
    except:
        # fallback if missing or malformed
        r['Amount'] = 0

# Keywords to identify park-related projects
keywords = ['park', 'playground', 'walkway', 'bluffs', 'trail']

# Build list of candidate funding project names that are park-related
candidate_funding = [r for r in funding if any(k in r['Project_Name'].lower() for k in keywords)]

matched = []

# For each candidate, search civic documents for evidence of completion in 2022 near the project name
for fr in candidate_funding:
    pname = fr['Project_Name']
    pname_lower = pname.lower()
    found = False
    for doc in civic_docs:
        text = doc.get('text','').lower()
        # find occurrences of project name in text
        idx = text.find(pname_lower)
        if idx != -1:
            # Define window of context
            start = max(0, idx-500)
            end = min(len(text), idx+500)
            window = text[start:end]
            if 'completed' in window and '2022' in window:
                found = True
                break
        else:
            # If exact project name not found, check if significant portion of name appears (e.g., "bluffs park" finds "bluffs park shade structure")
            # Check for all words of short name parts
            parts = re.findall(r"[a-z0-9]+", pname_lower)
            # take up to first 4 meaningful words
            parts = [p for p in parts if p not in ('the','and','of','project','repairs','repair','improvements','improvement')]
            if len(parts) >= 2:
                # check if at least two of the parts appear near a 'completed'+'2022'
                # find positions of parts occurrences
                positions = [m.start() for m in re.finditer(re.escape(parts[0]), text)]
                for pos in positions:
                    start = max(0, pos-500)
                    end = min(len(text), pos+500)
                    window = text[start:end]
                    # require at least one other part in the window
                    if any(p in window for p in parts[1:]) and 'completed' in window and '2022' in window:
                        found = True
                        break
            if found:
                break
    if found:
        matched.append({'Project_Name': fr['Project_Name'], 'Amount': fr['Amount']})

# Also consider funding entries that may match park projects mentioned in civic docs but whose funding names don't contain the keywords
# So scan civic docs for project names that include words like 'park' and 'completed' and '2022', then try to match funding rows by fuzzy substring
extracted_projects = set()
for doc in civic_docs:
    text = doc.get('text','')
    # find lines or headers that look like project titles followed by Updates or Project Schedule
    # A simple heuristic: find phrases that contain 'park' within 80 chars and capture surrounding 100 chars to the left to get the project name
    for m in re.finditer(r"([A-Za-z0-9\-\'\(\)\,\&\s]{0,80}park[A-Za-z0-9\-\'\(\)\,\&\s]{0,80})", text, flags=re.IGNORECASE):
        snippet = m.group(1)
        # now check if within 200 chars after snippet there's 'completed' and '2022'
        start = max(0, m.start()-10)
        end = min(len(text), m.end()+200)
        window = text[start:end].lower()
        if 'completed' in window and '2022' in window:
            # clean snippet to form a probable project name
            cleaned = re.sub(r"\s+"," ", snippet).strip()
            cleaned = re.sub(r"[:\n\r]"," ", cleaned)
            extracted_projects.add(cleaned)

# Try to match extracted_projects to funding entries by simple substring inclusion
for ep in extracted_projects:
    ep_lower = ep.lower()
    for fr in funding:
        if fr['Project_Name'].lower() in ep_lower or ep_lower in fr['Project_Name'].lower():
            # ensure not already added
            if not any(m['Project_Name']==fr['Project_Name'] for m in matched):
                matched.append({'Project_Name': fr['Project_Name'], 'Amount': fr['Amount']})

# Compute total
total = sum(m['Amount'] for m in matched)

result = {'matched_projects': matched, 'total_funding': total}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_s3s9kMHqzePGSEzEZp7cikyi': 'file_storage/call_s3s9kMHqzePGSEzEZp7cikyi.json', 'var_call_y31CKagxiG5kZ38LxNmcdJ1z': 'file_storage/call_y31CKagxiG5kZ38LxNmcdJ1z.json'}

exec(code, env_args)
