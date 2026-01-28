code = """import json
from pathlib import Path

# Load the stored query results from the provided storage keys
with open(var_call_llv73ggBnMMKgowx3DFgb5tX, 'r') as f:
    funding = json.load(f)
with open(var_call_53aW8AfzerFmNtvvoo5BLQJe, 'r') as f:
    civic_docs = json.load(f)

# Normalize funding amounts and prepare records
for r in funding:
    # Ensure Amount is int
    try:
        r['Amount'] = int(r.get('Amount') if r.get('Amount') is not None else 0)
    except:
        # strip non-digits
        s = ''.join(ch for ch in str(r.get('Amount','0')) if ch.isdigit())
        r['Amount'] = int(s) if s else 0
    r['Project_Name_norm'] = r['Project_Name'].lower()

# Build a combined text corpus from civic documents
texts = [d.get('text','') for d in civic_docs]

# Function to check if a project appears as completed in 2022 in any document
import re

def project_completed_2022(project_name, texts):
    pname = project_name.lower()
    for doc in texts:
        doc_low = doc.lower()
        # find positions where project name occurs
        start = 0
        while True:
            idx = doc_low.find(pname, start)
            if idx == -1:
                break
            # define window around occurrence
            win_start = max(0, idx-200)
            win_end = min(len(doc_low), idx+len(pname)+200)
            window = doc_low[win_start:win_end]
            # check for 'completed' and '2022' in window
            if ('completed' in window or 'completion' in window or 'complete construction' in window) and '2022' in window:
                return True, window
            start = idx + 1
    return False, None

# Find park-related funding records: those with 'park' in Project_Name
park_fundings = [r for r in funding if 'park' in r['Project_Name_norm']]

matched = []
for r in park_fundings:
    pname = r['Project_Name']
    is_completed, window = project_completed_2022(pname, texts)
    if is_completed:
        matched.append({'Project_Name': r['Project_Name'], 'Amount': r['Amount']})

# Additionally, check for other park-related keywords in funding (playground, walkway, bluffs, bluffs park, 'playground', 'walkway', 'shade structure')
extra_keywords = ['playground', 'walkway', 'shade structure', 'bluffs', 'playground']
for r in funding:
    if any(k in r['Project_Name'].lower() for k in extra_keywords) and 'park' not in r['Project_Name'].lower():
        is_completed, window = project_completed_2022(r['Project_Name'], texts)
        if is_completed:
            # avoid duplicates
            if not any(m['Project_Name']==r['Project_Name'] for m in matched):
                matched.append({'Project_Name': r['Project_Name'], 'Amount': r['Amount']})

# Sum amounts
total = sum(m['Amount'] for m in matched)

# Prepare result JSON-serializable
result = {'total_funding': total, 'matched_projects': matched}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_53aW8AfzerFmNtvvoo5BLQJe': 'file_storage/call_53aW8AfzerFmNtvvoo5BLQJe.json', 'var_call_llv73ggBnMMKgowx3DFgb5tX': 'file_storage/call_llv73ggBnMMKgowx3DFgb5tX.json'}

exec(code, env_args)
