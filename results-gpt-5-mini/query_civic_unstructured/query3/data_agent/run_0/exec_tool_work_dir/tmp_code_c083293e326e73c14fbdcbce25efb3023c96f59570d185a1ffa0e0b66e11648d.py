code = """import json
import re
# Load data from storage-provided variables (file paths)
with open(var_call_O8fNiGy0hYX2JWmSnRw9hiIg, 'r') as f:
    funding = json.load(f)
with open(var_call_RDTPadJ0MEdOGRSFv71OoRd6, 'r') as f:
    civic_docs = json.load(f)

# Combine all civic texts into one string
all_text = "\n".join([doc.get('text','') for doc in civic_docs])
all_text_l = all_text.lower()

results = []

def find_status_around(idx):
    # Look backwards up to 2000 chars for section headers or status phrases
    start = max(0, idx-2000)
    context = all_text[start:idx+2000].lower()
    # Check for section headers with Design/Construction/Not Started
    m = re.search(r'capital improvement projects \(([^)]+)\)', context)
    if m:
        sec = m.group(1).strip()
        return sec
    m2 = re.search(r'capital improvement projects \- ([^\n]+)', context)
    if m2:
        return m2.group(1).strip()
    # Look for explicit phrases
    if re.search(r'preliminary design|in the preliminary design phase|finalizing the design|complete design|final design', context):
        return 'Design'
    if re.search(r'construction was completed|complete construction|complete construction:|notice of completion|was completed', context):
        return 'Completed'
    if re.search(r'not started|identified but not begun|not begun', context):
        return 'Not Started'
    if re.search(r'currently under construction|begin construction|begin construction:|begin construction', context):
        return 'Construction'
    # If nothing found, return Unknown
    return 'Unknown'

# Normalize funding entries to dicts
for row in funding:
    proj = row.get('Project_Name','')
    proj_l = proj.lower()
    funding_source = row.get('Funding_Source')
    amount = row.get('Amount')
    matched = False
    status = None
    # If project name explicitly mentions FEMA or emergency, include it
    if 'fema' in proj_l or 'emergency' in proj_l:
        # Try to find occurrence of project base name in text
        # Remove parentheses suffixes for searching
        base = re.sub(r"\s*\([^)]*\)", '', proj).strip()
        idx = all_text_l.find(base.lower())
        if idx!=-1:
            status = find_status_around(idx)
        else:
            status = 'Unknown'
        matched = True
    else:
        # Search for the project name in civic text
        idx = all_text_l.find(proj_l)
        if idx!=-1:
            # Check context for fema or emergency
            ctx = all_text_l[max(0, idx-200): idx+len(proj_l)+200]
            if 'fema' in ctx or 'emergency' in ctx:
                status = find_status_around(idx)
                matched = True
        # Also search for base name without suffixes
        if not matched:
            base = re.sub(r"\s*\([^)]*\)", '', proj).strip()
            if base and base.lower() != proj_l:
                idx2 = all_text_l.find(base.lower())
                if idx2!=-1:
                    ctx2 = all_text_l[max(0, idx2-200): idx2+len(base)+200]
                    if 'fema' in ctx2 or 'emergency' in ctx2:
                        status = find_status_around(idx2)
                        matched = True
    if matched:
        results.append({
            'Project_Name': proj,
            'Funding_Source': funding_source,
            'Amount': int(amount) if amount not in (None, '') and str(amount).isdigit() else amount,
            'Status': status
        })

# Additionally, search civic docs for projects mentioning 'emergency' that might not be in funding table
# Find occurrences of lines with 'emergency' or 'fema' and attempt to extract a nearby project title
pattern = re.compile(r"([A-Z][A-Za-z0-9 &'\-/,.()]{3,80}?)(?:Project|Repairs|Improvements|Repairs Project|Facility|Project)\b", re.IGNORECASE)
for m in re.finditer(pattern, all_text):
    span = m.span()
    ctx = all_text_l[max(0, span[0]-200): span[1]+200]
    if 'fema' in ctx.lower() or 'emergency' in ctx.lower():
        title = m.group(0).strip()
        # Check if already in results
        if any(r['Project_Name'].lower() == title.lower() for r in results):
            continue
        # Try to find funding record
        fund_match = None
        for row in funding:
            if row.get('Project_Name','').lower() == title.lower() or re.sub(r"\s*\([^)]*\)", '', row.get('Project_Name','')).strip().lower() == title.lower():
                fund_match = row
                break
        status = find_status_around(span[0])
        results.append({
            'Project_Name': fund_match.get('Project_Name') if fund_match else title,
            'Funding_Source': fund_match.get('Funding_Source') if fund_match else None,
            'Amount': int(fund_match.get('Amount')) if fund_match and str(fund_match.get('Amount')).isdigit() else (fund_match.get('Amount') if fund_match else None),
            'Status': status
        })

# Deduplicate results by Project_Name
seen = set()
unique_results = []
for r in results:
    key = r['Project_Name']
    if key.lower() in seen:
        continue
    seen.add(key.lower())
    unique_results.append(r)

import json
print("__RESULT__:")
print(json.dumps(unique_results))"""

env_args = {'var_call_RDTPadJ0MEdOGRSFv71OoRd6': 'file_storage/call_RDTPadJ0MEdOGRSFv71OoRd6.json', 'var_call_HpgQvXmAaa9rS2LPuJKiZVjk': ['Funding'], 'var_call_O8fNiGy0hYX2JWmSnRw9hiIg': 'file_storage/call_O8fNiGy0hYX2JWmSnRw9hiIg.json'}

exec(code, env_args)
