code = """import json, re
# Load data from storage files
with open(var_call_0fUjBApHRNYQRbT9gTd4fnWS, 'r') as f:
    funding = json.load(f)
with open(var_call_agSZO2Qc3Ku1gCpY4STNohpM, 'r') as f:
    docs = json.load(f)

# Normalize funding amounts and prepare
for rec in funding:
    # ensure Amount is int
    try:
        rec['Amount'] = int(rec.get('Amount') if rec.get('Amount') is not None else 0)
    except:
        # remove non-digits
        s = re.sub(r"[^0-9]","", str(rec.get('Amount','0')))
        rec['Amount'] = int(s) if s else 0

park_keywords = ['park','playground','walkway','bench','play area','trail','plaza']

matches = []
total = 0

# For each funding record, search in civic docs for evidence it's park-related and completed in 2022
for rec in funding:
    pname = rec.get('Project_Name','')
    if not pname:
        continue
    pname_lower = pname.lower()
    found = False
    for doc in docs:
        text = doc.get('text','')
        text_lower = text.lower()
        # fuzzy find: exact substring
        idx = text_lower.find(pname_lower)
        if idx == -1:
            # try matching by partial name segments (take up to first 6 words)
            short = ' '.join(pname_lower.split()[:6])
            idx = text_lower.find(short) if short else -1
        if idx != -1:
            window_start = max(0, idx-500)
            window_end = min(len(text), idx+1500)
            window = text[window_start:window_end]
            wlow = window.lower()
            is_park = any(k in wlow for k in park_keywords)
            # completed in 2022: look for 'completed' and '2022' within window
            is_completed_2022 = ('completed' in wlow) and ('2022' in window)
            if is_park and is_completed_2022:
                found = True
                matches.append({'Project_Name': rec.get('Project_Name'), 'Amount': rec.get('Amount'), 'Funding_ID': rec.get('Funding_ID'), 'filename': doc.get('filename')})
                total += rec.get('Amount',0)
                break
    # also try matching by finding project headings like 'Trancas Canyon Park' even if funding name different

# Additionally, search for explicit park project mentions in docs completed in 2022 and join to funding by name inclusion
# Build set of project names mentioned in docs that are park-related and completed in 2022
park_completed_projects = set()
for doc in docs:
    text = doc.get('text','')
    text_lower = text.lower()
    # find all occurrences of 'construction was completed' or 'was completed' with 2022 nearby
    for m in re.finditer(r"([A-Z][^\n]{0,1000}?)(construction was completed|was completed|completed)[^\n]{0,1000}?2022", text, flags=re.IGNORECASE):
        context_start = max(0, m.start()-200)
        context_end = min(len(text), m.end()+200)
        context = text[context_start:context_end]
        # try to extract a project name from lines above the match: take up to 3 lines before
        prior = text[:m.start()]
        lines = prior.splitlines()
        last_lines = [ln.strip() for ln in lines[-6:] if ln.strip()]
        # candidate project lines: look for lines that look like titles (short, capitalized)
        for ln in reversed(last_lines):
            if len(ln) < 200 and len(ln.split())<=8:
                # add as candidate
                park_completed_projects.add(ln)
                break

# Try to match these candidate names to funding records
for pname in park_completed_projects:
    pname_lower = pname.lower()
    for rec in funding:
        if pname_lower in rec.get('Project_Name','').lower() or rec.get('Project_Name','').lower() in pname_lower:
            # ensure not already counted
            if rec.get('Funding_ID') not in [m['Funding_ID'] for m in matches]:
                matches.append({'Project_Name': rec.get('Project_Name'), 'Amount': rec.get('Amount'), 'Funding_ID': rec.get('Funding_ID'), 'matched_doc_project_line': pname})
                total += rec.get('Amount',0)

# Deduplicate matches by Funding_ID
unique = {}
for m in matches:
    fid = m.get('Funding_ID')
    if fid not in unique:
        unique[fid]=m

final_matches = list(unique.values())
final_total = sum(m['Amount'] for m in final_matches)

out = {'total_funding': final_total, 'matching_projects': final_matches}

import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_0fUjBApHRNYQRbT9gTd4fnWS': 'file_storage/call_0fUjBApHRNYQRbT9gTd4fnWS.json', 'var_call_agSZO2Qc3Ku1gCpY4STNohpM': 'file_storage/call_agSZO2Qc3Ku1gCpY4STNohpM.json'}

exec(code, env_args)
