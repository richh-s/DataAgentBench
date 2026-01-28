code = """import json
from pathlib import Path

# Load tool results stored in files
with open(var_call_GJgKFWFoYXX9ZQ06amDIgLQs, 'r', encoding='utf-8') as f:
    funding_records = json.load(f)
with open(var_call_70j7EIEoi4BAitiidmGSdKTA, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Normalize funding records: convert Amount to int, strip Project_Name
funding = []
for r in funding_records:
    try:
        amt = int(r.get('Amount'))
    except:
        try:
            amt = int(float(r.get('Amount')))
        except:
            continue
    name = r.get('Project_Name','').strip()
    funding.append({'Project_Name': name, 'Amount': amt})

# Build set of funded project names with Amount > 50000
funded_gt50k = {r['Project_Name'] for r in funding if r['Amount'] > 50000}

# Function to extract project names from 'Capital Improvement Projects (Design)' sections
import re

def extract_design_projects(text):
    projects = []
    header = 'Capital Improvement Projects (Design)'
    idx = text.find(header)
    if idx == -1:
        return projects
    # find end by next major header
    end_tokens = ['Capital Improvement Projects (Construction)',
                  'Capital Improvement Projects (Not Started)',
                  'Capital Improvement Projects (Design)',
                  '\n\nCapital Improvement Projects',
                  '\n\nCapital Improvement Projects']
    end_idx = len(text)
    for tok in end_tokens:
        j = text.find(tok, idx + len(header))
        if j != -1:
            end_idx = min(end_idx, j)
    section = text[idx + len(header):end_idx]
    # Split into lines and filter
    lines = [ln.strip() for ln in section.splitlines()]
    for ln in lines:
        if not ln:
            continue
        low = ln.lower()
        # Exclude meta lines
        if any(x in low for x in ['updates', 'project schedule', 'project description', 'estimated schedule', 'complete design', 'advertise', 'begin construction', '(cid:', 'page', 'agenda', 'recommended action', 'discussion', 'to:', 'prepared by']):
            continue
        # Exclude lines that end with ':' or are short labels
        if ln.endswith(':'):
            continue
        # Exclude lines that are clearly sentences (contain more than 20 words)
        if len(ln.split()) > 20:
            continue
        # Exclude lines that are all uppercase words and short (likely headers)
        if re.fullmatch(r'[A-Z0-9\W\s]+', ln) and len(ln.split()) <= 5 and ln.isupper():
            continue
        # Exclude lines that start with digits and are not project-like (like dates but probably safe)
        # Accept lines that contain letters and are not metadata
        if re.search('[A-Za-z]', ln):
            # Clean trailing punctuation
            cleaned = ln.strip(' -\u2013\u2014')
            projects.append(cleaned)
    # Heuristic dedup while preserving order
    seen = set()
    out = []
    for p in projects:
        if p not in seen:
            seen.add(p)
            out.append(p)
    return out

# Extract from all civic documents
design_projects = []
for doc in civic_docs:
    txt = doc.get('text','')
    ps = extract_design_projects(txt)
    design_projects.extend(ps)

# Deduplicate
seen = set()
design_projects_unique = []
for p in design_projects:
    if p not in seen:
        seen.add(p)
        design_projects_unique.append(p)

# Now find intersection with funded_gt50k (use exact match and also try case-insensitive)
funded_matches = []
funded_lower = {n.lower(): n for n in funded_gt50k}
for proj in design_projects_unique:
    if proj in funded_gt50k:
        # exact match
        # find amount
        amt = next((r['Amount'] for r in funding if r['Project_Name']==proj), None)
        funded_matches.append({'Project_Name': proj, 'Amount': amt})
    else:
        # try case-insensitive match
        key = proj.lower()
        if key in funded_lower:
            matched_name = funded_lower[key]
            amt = next((r['Amount'] for r in funding if r['Project_Name']==matched_name), None)
            funded_matches.append({'Project_Name': matched_name, 'Amount': amt})

# Prepare result
result = {
    'design_capital_projects_extracted_count': len(design_projects_unique),
    'design_capital_projects_extracted': design_projects_unique,
    'funded_projects_over_50k_count': len(funded_matches),
    'funded_projects_over_50k': funded_matches
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_GJgKFWFoYXX9ZQ06amDIgLQs': 'file_storage/call_GJgKFWFoYXX9ZQ06amDIgLQs.json', 'var_call_VxneExt2hKcFVVPOdTv38nAJ': ['civic_docs'], 'var_call_70j7EIEoi4BAitiidmGSdKTA': 'file_storage/call_70j7EIEoi4BAitiidmGSdKTA.json'}

exec(code, env_args)
