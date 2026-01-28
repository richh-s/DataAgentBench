code = """import json, re

# Load data from storage-provided file paths
with open(var_call_1WNMnXzLqRr9u8gix6ncsCDL, 'r') as f:
    funding = json.load(f)
with open(var_call_wWPlT1QfVgACpt3TGPAyJdfb, 'r') as f:
    civic_docs = json.load(f)

# Normalize funding records
for r in funding:
    # Ensure Amount is int
    try:
        r['Amount'] = int(r['Amount'])
    except:
        # remove non-digits
        nums = re.findall(r"\d+", str(r.get('Amount','0')))
        r['Amount'] = int(nums[0]) if nums else 0
    r['Project_Name_lc'] = r['Project_Name'].lower()

# Function to find project heading near a line index
def find_heading(lines, idx):
    # look up to 8 previous lines for a candidate containing 'park' or capitalized words
    for i in range(idx-1, max(idx-9, -1), -1):
        line = lines[i].strip()
        if not line:
            continue
        low = line.lower()
        if 'updates' in low or 'project schedule' in low or 'agenda' in low or 'item' in low or 'meeting' in low:
            continue
        # If line contains 'park' return it
        if 'park' in low:
            return line
        # If line looks like a project title (few words, each capitalized or contains words like 'Project','Repairs','Repair','Walkway','Playground','Shade')
        if re.search(r"\b(Project|Repairs|Repair|Walkway|Playground|Shade|Renovation|Structure|Playground|Slopes|Benches|Park|Walkway)\b", line, re.IGNORECASE):
            return line
    # As fallback, search next few lines (some docs put title after)
    for i in range(idx+1, min(idx+6, len(lines))):
        line = lines[i].strip()
        if not line:
            continue
        if 'updates' in line.lower():
            continue
        if 'park' in line.lower() or re.search(r"\b(Project|Repairs|Repair|Walkway|Playground|Shade|Renovation|Structure)\b", line, re.IGNORECASE):
            return line
    return None

found_projects = set()

for doc in civic_docs:
    text = doc.get('text','')
    if not text:
        continue
    # Normalize punctuation
    text_clean = text.replace('\r', '\n')
    lines = [l for l in text_clean.split('\n')]
    for i, line in enumerate(lines):
        low = line.lower()
        # Look for lines indicating completion in 2022
        if 'completed' in low and '2022' in low:
            heading = find_heading(lines, i)
            if heading:
                # Clean heading
                h = re.sub(r"\s+", ' ', heading).strip()
                # remove leading numbering like '1.' or 'Item'
                h = re.sub(r"^\W+", '', h)
                found_projects.add(h)
        # Also look for patterns like 'Complete Construction: April 2023' so skip; only 2022
        # Also consider lines like 'Complete Construction: November 2022'
        if ('complete construction' in low or 'complete construction:' in low or 'complete design' in low) and '2022' in low:
            heading = find_heading(lines, i)
            if heading:
                h = re.sub(r"\s+", ' ', heading).strip()
                found_projects.add(h)
        # Also look for 'Notice of completion filed' lines mentioning 2023 but that implies completion in 2022 sometimes; skip complexity

# Filter found projects to those containing 'park'
park_projects = [p for p in found_projects if 'park' in p.lower()]
# Deduplicate and sort
park_projects = sorted(set(park_projects))

# Now match these to funding table using case-insensitive substring matching
matched_records = []
matched_project_names = set()
for p in park_projects:
    pl = p.lower()
    for r in funding:
        if pl in r['Project_Name_lc'] or r['Project_Name_lc'] in pl:
            matched_records.append({'Project_Name': r['Project_Name'], 'Amount': r['Amount'], 'Funding_ID': r['Funding_ID']})
            matched_project_names.add(r['Project_Name'])
# Also try fuzzy containment: if project words intersect
if not matched_records and park_projects:
    for p in park_projects:
        words = [w for w in re.findall(r"[a-zA-Z0-9]+", p.lower()) if len(w)>3]
        for r in funding:
            if all(any(w in rn for rn in [r['Project_Name_lc']]) for w in words):
                matched_records.append({'Project_Name': r['Project_Name'], 'Amount': r['Amount'], 'Funding_ID': r['Funding_ID']})
                matched_project_names.add(r['Project_Name'])

# Additionally, sometimes funding table has park projects not detected due to heading extraction; look for funding records with 'park' and check civic docs if they were completed in 2022 by searching text
# Find funding records with 'park' in name
for r in funding:
    if 'park' in r['Project_Name_lc'] and r['Project_Name'] not in matched_project_names:
        # search civic docs for project name and 'completed' and '2022'
        name_lc = r['Project_Name'].lower()
        done = False
        for doc in civic_docs:
            if name_lc.split()[0] in doc.get('text','').lower():
                if 'completed' in doc.get('text','').lower() and '2022' in doc.get('text','').lower():
                    # crude check: presence of both anywhere in doc
                    matched_records.append({'Project_Name': r['Project_Name'], 'Amount': r['Amount'], 'Funding_ID': r['Funding_ID']})
                    matched_project_names.add(r['Project_Name'])
                    break

# Compute total funding
total = sum(r['Amount'] for r in matched_records)

# Prepare result
result = {'park_projects_completed_2022': sorted(list(matched_project_names)), 'total_funding': total}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_CeyxRynO2d9ptMHB9H0F39vr': ['civic_docs'], 'var_call_1WNMnXzLqRr9u8gix6ncsCDL': 'file_storage/call_1WNMnXzLqRr9u8gix6ncsCDL.json', 'var_call_wWPlT1QfVgACpt3TGPAyJdfb': 'file_storage/call_wWPlT1QfVgACpt3TGPAyJdfb.json'}

exec(code, env_args)
