code = """import json, re

# Load tool-results stored as files
with open(var_call_w5WiviLNuqM8uC0FZH8mDfoo, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_2shR4Lt5stCYfxsgZWUvQECb, 'r', encoding='utf-8') as f:
    funding_records = json.load(f)

park_keywords = ['park', 'playground', 'walkway', 'benches', 'bench', 'bluffs', 'playground']
completed_indicators = ['completed', 'Construction was completed', 'Complete Construction', 'Complete Construction:', 'Complete Construction']

found_projects = set()

for doc in civic_docs:
    text = doc.get('text','')
    lines = text.splitlines()
    # heuristic 1: find lines mentioning completion in 2022, look above for park-related project name
    for i, line in enumerate(lines):
        low = line.lower()
        if '2022' in line and ('complete' in low or 'completed' in low or 'construction was completed' in low):
            # look up to 8 lines above for a park-related line
            for j in range(max(0, i-8), i+1):
                l = lines[j].strip()
                if any(pk in l.lower() for pk in park_keywords):
                    # clean l
                    proj = re.sub(r"\(cid:\d+\)", "", l).strip()
                    proj = re.sub(r"\s+", " ", proj)
                    if proj:
                        found_projects.add(proj)
                        break
    # heuristic 2: find lines mentioning park, check following lines for completed + 2022
    for i, line in enumerate(lines):
        if any(pk in line.lower() for pk in park_keywords):
            # consider this a candidate project name
            candidate = re.sub(r"\(cid:\d+\)", "", line).strip()
            candidate = re.sub(r"\s+", " ", candidate)
            # look next 8 lines
            window = " ".join(lines[i:i+9])
            if '2022' in window and 'complete' in window.lower():
                if candidate:
                    found_projects.add(candidate)

# Final cleaning: remove very short or generic lines
clean_projects = []
for p in found_projects:
    p2 = p.strip(' -:\n\t')
    if len(p2) > 3 and not re.match(r'^(updates|page|agenda|item)', p2.strip().lower()):
        clean_projects.append(p2)

# Now match funding records
# normalize comparison
funding_map = funding_records
matched_records = []
for fr in funding_map:
    pname = fr.get('Project_Name','')
    for proj in clean_projects:
        if not proj:
            continue
        # exact match or one contains the other (case-insensitive)
        if proj.lower() == pname.lower() or proj.lower() in pname.lower() or pname.lower() in proj.lower():
            # convert amount to int safely
            try:
                amount = int(fr.get('Amount',0))
            except:
                try:
                    amount = int(float(fr.get('Amount',0)))
                except:
                    amount = 0
            matched_records.append({'project_doc_name': proj, 'funding_project_name': pname, 'amount': amount})

# sum amounts
total = sum(r['amount'] for r in matched_records)

# prepare result
result = {'extracted_projects': sorted(clean_projects), 'matched_funding_records': matched_records, 'total_funding': total}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_w5WiviLNuqM8uC0FZH8mDfoo': 'file_storage/call_w5WiviLNuqM8uC0FZH8mDfoo.json', 'var_call_2shR4Lt5stCYfxsgZWUvQECb': 'file_storage/call_2shR4Lt5stCYfxsgZWUvQECb.json'}

exec(code, env_args)
