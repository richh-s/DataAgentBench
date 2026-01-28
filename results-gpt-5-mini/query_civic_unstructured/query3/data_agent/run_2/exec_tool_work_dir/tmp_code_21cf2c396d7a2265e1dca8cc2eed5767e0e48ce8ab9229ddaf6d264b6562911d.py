code = """import json
import re

# Load funding data
path_funding = var_call_51uSuFk7C0eKQtq87NGdSzGT
if isinstance(path_funding, str):
    with open(path_funding, 'r', encoding='utf-8') as f:
        funding = json.load(f)
else:
    funding = path_funding

# Load civic docs
path_docs = var_call_gWIVvlDnNeNO28YeN24U8bSs
if isinstance(path_docs, str):
    with open(path_docs, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = path_docs

# Normalize funding entries
for f in funding:
    # Ensure consistent types
    f['Project_Name'] = f.get('Project_Name','')
    f['Funding_Source'] = f.get('Funding_Source','')
    # Amount as int if possible
    try:
        f['Amount'] = int(f.get('Amount'))
    except:
        try:
            f['Amount'] = int(float(f.get('Amount')))
        except:
            f['Amount'] = None

# Collect relevant funding records: those whose Project_Name contains 'FEMA' or 'emergency' (case-insensitive)
re_fema = re.compile(r'fema', re.I)
re_emergency = re.compile(r'emergency', re.I)
selected = []

# Helper to strip parenthetical suffixes
def base_name(name):
    return re.sub(r"\s*\([^)]*\)", '', name).strip()

# Precompute doc texts
doc_texts = [d.get('text','') for d in docs]

for rec in funding:
    name = rec['Project_Name']
    if re_fema.search(name) or re_emergency.search(name):
        selected.append(rec)
        continue
    # Otherwise check if project name (or base name) appears in any of the civic docs that contain FEMA/emergency
    bname = base_name(name)
    if not bname:
        continue
    found = False
    for text in doc_texts:
        if re.search(re.escape(bname), text, re.I):
            # consider this related
            selected.append(rec)
            found = True
            break
    # Also check if funding source or other hints mention FEMA? skip

# Deduplicate selected by Project_Name
uniq = {}
for r in selected:
    uniq[r['Project_Name']] = r
selected = list(uniq.values())

# Determine status by searching civic docs around matches
results = []

for rec in selected:
    pname = rec['Project_Name']
    bname = base_name(pname)
    status = None
    matched = False
    for text in doc_texts:
        # search for full project name first, then base name
        for target in [pname, bname]:
            if not target:
                continue
            m = re.search(re.escape(target), text, re.I)
            if m:
                matched = True
                start = max(0, m.start()-200)
                end = min(len(text), m.end()+200)
                window = text[start:end]
                # decide status
                if re.search(r'\bdesign\b', window, re.I) or 'Capital Improvement Projects (Design)'.lower() in text.lower():
                    status = 'design'
                if status is None and re.search(r'completed|complete construction|construction was completed|Notice of completion', window, re.I):
                    status = 'completed'
                if status is None and re.search(r'not started|Not Started|not begun|identified but not begun', window, re.I):
                    status = 'not started'
                # If still None, look for construction phrases -> map to design if under 'Design' section else unknown
                if status is None and re.search(r'under construction|begin construction|begin construction:', window, re.I):
                    # If text has 'Construction' section header near the match, mark completed; else mark design
                    if 'Capital Improvement Projects (Construction)'.lower() in text.lower():
                        status = 'completed'
                    else:
                        status = 'design'
                # If still None but document contained FEMA/emergency, set unknown
                if status is None:
                    # try broader context
                    if re_emergency.search(text) or re_fema.search(text):
                        status = 'unknown'
                    else:
                        status = 'unknown'
                break
        if matched:
            break
    if not matched:
        status = 'unknown'
    results.append({
        'Project_Name': pname,
        'Funding_Source': rec.get('Funding_Source'),
        'Amount': rec.get('Amount'),
        'Status': status
    })

# Sort results by Project_Name
results = sorted(results, key=lambda x: x['Project_Name'].lower())

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_gWIVvlDnNeNO28YeN24U8bSs': 'file_storage/call_gWIVvlDnNeNO28YeN24U8bSs.json', 'var_call_51uSuFk7C0eKQtq87NGdSzGT': 'file_storage/call_51uSuFk7C0eKQtq87NGdSzGT.json'}

exec(code, env_args)
