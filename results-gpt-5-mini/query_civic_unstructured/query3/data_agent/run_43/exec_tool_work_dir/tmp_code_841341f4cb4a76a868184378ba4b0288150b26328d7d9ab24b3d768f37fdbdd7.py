code = """import json
import re
from pathlib import Path

# Load data from storage-provided file paths
civic_docs_path = Path(var_call_owt1CJlXOW5XHdAgyXm7RWEF)
funding_path = Path(var_call_nGx2atNIB0SdTXF5VUqvFXNi)

with open(civic_docs_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Normalize funding records into list of dicts
funding_records = funding

# Identify candidate funding projects related to 'FEMA' or 'emergency'
keywords = ['fema', 'emergency', 'outdoor warning', 'warning', 'emergency warning']

candidates = []
for rec in funding_records:
    name = rec.get('Project_Name','') or ''
    source = rec.get('Funding_Source','') or ''
    lname = name.lower()
    lsource = source.lower()
    if any(k in lname for k in keywords) or any(k in lsource for k in ['federal assistance','fema']):
        candidates.append(rec)

# Also include records whose Project_Name contains '(FEMA' or 'FEMA/'
for rec in funding_records:
    name = rec.get('Project_Name','') or ''
    if '(fema' in name.lower() or 'fema/' in name.lower() or 'fema' in name.lower() and rec not in candidates:
        candidates.append(rec)

# Deduplicate by Project_Name
unique = {}
for rec in candidates:
    unique[rec['Project_Name']] = rec
candidates = list(unique.values())

# Prepare function to infer status from civic docs text
section_headers = ['capital improvement projects (design)', 'capital improvement projects (construction)',
                   'capital improvement projects (not started)', 'capital improvement projects (design)',
                   'disaster recovery projects', 'disaster recovery projects status', 'capital improvement projects']

def infer_status_from_context(text, idx_start, project_name):
    window_start = max(0, idx_start - 2000)
    context = text[window_start: idx_start + 2000].lower()
    # Check for explicit headers near context
    if 'design' in context and 'construction' not in context:
        return 'design'
    if 'construction' in context:
        # if mentions completed
        if 'construction was completed' in context or 'notice of completion' in context or 'complete construction' in context:
            return 'completed'
        # if mentions currently under construction -> treat as completed (in-progress)
        if 'currently under construction' in context or 'begin construction' in context or 'begin construction:' in context:
            # If there is a future-sounding schedule (e.g., Begin Construction: Fall 2023) -> not started
            # simple heuristic: if 'begin construction:' exists and words like 'fall' or months follow, assume not started
            if 'begin construction:' in context:
                return 'not started'
            return 'completed'
    if 'not started' in context or 'will be' in context or 'identified' in context or 'waiting' in context or 'awaiting' in context:
        return 'not started'
    # specific phrases
    if 'working with the consultant' in context or 'finalize the design' in context or 'finalizing the design' in context or 'final design' in context or 'preliminary design' in context:
        return 'design'
    if 'completed' in context or 'notice of completion' in context:
        return 'completed'
    return None

# For each candidate, search civic docs for project name and infer status
results = []
all_texts = "\n\n".join(d.get('text','') for d in civic_docs)
lower_text = all_texts.lower()

for rec in candidates:
    pname = rec['Project_Name']
    lname = pname.lower()
    status = None
    # try exact match
    idx = lower_text.find(lname)
    if idx != -1:
        status = infer_status_from_context(lower_text, idx, pname)
    else:
        # try partial matching by stripping parenthetical tags and variants
        simple = re.sub(r"\(.*?\)", "", lname).strip()
        if simple and simple in lower_text:
            idx = lower_text.find(simple)
            status = infer_status_from_context(lower_text, idx, pname)
        else:
            # try matching by key tokens
            tokens = [t for t in ['outdoor warning','warning','emergency','latigo canyon','clover heights','encinal canyon','guardrail'] if t in lname]
            found = False
            for t in tokens:
                idx = lower_text.find(t)
                if idx!=-1:
                    status = infer_status_from_context(lower_text, idx, pname)
                    found = True
                    break
    # Normalize amount to int if possible
    amt = rec.get('Amount')
    try:
        amount = int(str(amt))
    except:
        try:
            amount = int(float(str(amt)))
        except:
            amount = None
    results.append({'Project_Name': rec.get('Project_Name'), 'Funding_Source': rec.get('Funding_Source'), 'Amount': amount, 'Status': status})

# Sort results by Project_Name
results = sorted(results, key=lambda x: x['Project_Name'] or '')

import json
print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_owt1CJlXOW5XHdAgyXm7RWEF': 'file_storage/call_owt1CJlXOW5XHdAgyXm7RWEF.json', 'var_call_nGx2atNIB0SdTXF5VUqvFXNi': 'file_storage/call_nGx2atNIB0SdTXF5VUqvFXNi.json'}

exec(code, env_args)
