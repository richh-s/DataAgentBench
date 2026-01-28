code = """import json
import re
from pathlib import Path

# Load the query results from the storage file paths provided by prior tool calls
civic_path = Path(var_call_bu8LPbUHDRNIbQ84TXKpVe55)
funding_path = Path(var_call_O0tyg822jhfLZAIPR1IgNBpH)

with open(civic_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r', encoding='utf-8') as f:
    funding_rows = json.load(f)

# Normalize funding into list of dicts
funding = []
for r in funding_rows:
    # Ensure proper types
    try:
        amount = int(r.get('Amount'))
    except:
        try:
            amount = int(float(r.get('Amount')))
        except:
            amount = None
    funding.append({
        'Funding_ID': r.get('Funding_ID'),
        'Project_Name': r.get('Project_Name'),
        'Funding_Source': r.get('Funding_Source'),
        'Amount': amount
    })

# Pre-lowercase civic texts for searching
civic_texts = []
for doc in civic_docs:
    txt = doc.get('text','')
    civic_texts.append({'filename': doc.get('filename'), 'text': txt, 'ltext': txt.lower()})

# Helper to strip parenthetical suffixes for matching base project names
def base_name(pname):
    # remove trailing parenthetical like " (FEMA Project)"
    return re.sub(r"\s*\([^)]*\)\s*$", "", pname).strip()

candidates = []

for row in funding:
    pname = row['Project_Name'] or ''
    lp = pname.lower()
    included = False
    # Criterion 1: project name contains 'fema' or 'emergency'
    if re.search(r'fema|emergency', lp):
        included = True
    else:
        # Criterion 2: project name appears in any civic doc that also mentions 'fema' or 'emergency'
        bname = base_name(pname).lower()
        if bname and len(bname) >= 4:  # avoid overly short names
            for doc in civic_texts:
                if 'fema' in doc['ltext'] or 'emergency' in doc['ltext']:
                    if bname in doc['ltext']:
                        included = True
                        break
    if included:
        candidates.append(row)

# For each candidate, try to extract status information from civic docs
results = []
for row in candidates:
    pname = row['Project_Name']
    bname = base_name(pname)
    bname_l = bname.lower()
    status_inferred = 'unknown'
    status_snippet = None
    source_files = []
    # search docs for occurrences of base name
    for doc in civic_texts:
        if bname_l and bname_l in doc['ltext']:
            source_files.append(doc['filename'])
            # find first occurrence
            pos = doc['ltext'].find(bname_l)
            start = max(0, pos-200)
            end = min(len(doc['ltext']), pos+400)
            snippet = doc['text'][start:end]
            status_snippet = snippet.strip()
            # infer status from snippet using keywords
            s = snippet.lower()
            if 'not started' in s or 'not yet' in s and 'started' in s:
                status_inferred = 'not started'
            elif 'complete' in s or 'completed' in s or 'notice of completion' in s:
                status_inferred = 'completed'
            elif '(design)' in doc['text'].lower() or 'design' in s or 'complete design' in s or 'finalize the design' in s:
                status_inferred = 'design'
            elif 'construction' in s or 'begin construction' in s or 'under construction' in s:
                # prefer explicit completed or design if present; otherwise mark as 'in construction'
                status_inferred = 'in construction'
            # stop at first doc match
            break
    # If no doc match and name itself has FEMA/emergency, leave status unknown
    results.append({
        'Project_Name': pname,
        'Funding_Source': row['Funding_Source'],
        'Amount': row['Amount'],
        'Status_Inferred': status_inferred,
        'Status_Snippet': status_snippet,
        'Source_Files': source_files
    })

# Deduplicate by Project_Name (keep first)
seen = set()
final = []
for r in results:
    if r['Project_Name'] in seen:
        continue
    seen.add(r['Project_Name'])
    final.append(r)

print('__RESULT__:')
print(json.dumps(final, ensure_ascii=False))"""

env_args = {'var_call_bu8LPbUHDRNIbQ84TXKpVe55': 'file_storage/call_bu8LPbUHDRNIbQ84TXKpVe55.json', 'var_call_O0tyg822jhfLZAIPR1IgNBpH': 'file_storage/call_O0tyg822jhfLZAIPR1IgNBpH.json'}

exec(code, env_args)
