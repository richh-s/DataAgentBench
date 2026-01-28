code = """import json
import re

# Load data from storage file paths
with open(var_call_QNC7P8mjljZASGfnnZi9S4PP, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_jifqAMOUNn9PorNbe5w6A4Vg, 'r', encoding='utf-8') as f:
    funding = json.load(f)

texts = [d.get('text','') for d in civic_docs]

# Find candidate park-related project names
candidates = set()
for text in texts:
    # find phrases containing 'Park' or 'playground' up to line breaks
    for m in re.finditer(r'([A-Za-z0-9\-\'"\(\) &,./]+?(?:Park|park|Playground|playground)[A-Za-z0-9\-\'"\(\) &,./]{0,80})', text):
        name = m.group(1).strip()
        # normalize whitespace and remove trailing punctuation
        name = re.sub(r'\s+', ' ', name).strip(' \n\r\t:')
        # check if 'completed' and '2022' appear near the occurrence (within 300 chars after)
        start = m.start()
        window = text[start:start+400]
        if re.search(r'completed', window, re.IGNORECASE) and re.search(r'2022', window, re.IGNORECASE):
            candidates.add(name)
    # also catch lines where project name is on its own line and followed by updates later
    # capture lines with 'Park' then search within next 800 chars
    for line in text.split('\n'):
        if 'park' in line.lower() or 'playground' in line.lower():
            snippet = line.strip()
            if len(snippet) > 2:
                idx = text.find(line)
                if idx != -1:
                    window = text[idx:idx+800]
                    if re.search(r'completed', window, re.IGNORECASE) and re.search(r'2022', window, re.IGNORECASE):
                        # use the line as candidate
                        name = re.sub(r'\s+', ' ', snippet).strip(' \n\r\t:')
                        candidates.add(name)

# Also include explicit project headings that are park-related anywhere in document if completed 2022
# Convert funding list project names to compare
fund_names = [f.get('Project_Name','') for f in funding]

matched_fund_records = []
matched_projects = set()
for cand in candidates:
    # Try to match cand to funding Project_Name by exact or substring match
    cand_low = cand.lower()
    for rec in funding:
        pname = rec.get('Project_Name','')
        if pname.lower() == cand_low or cand_low in pname.lower() or pname.lower() in cand_low:
            matched_fund_records.append(rec)
            matched_projects.add(pname)

# As a fallback, look for funding projects whose names contain 'park' and appear completed 2022 in the docs anywhere
if not matched_fund_records:
    # find all funding recs with 'park' and check if their names appear near 'completed' and '2022' in docs
    for rec in funding:
        pname = rec.get('Project_Name','')
        if 'park' in pname.lower() or 'playground' in pname.lower():
            # search pname in civic texts and check completed & 2022 proximity
            for text in texts:
                idx = text.lower().find(pname.lower())
                if idx != -1:
                    window = text[idx:idx+400]
                    if re.search(r'completed', window, re.IGNORECASE) and re.search(r'2022', window, re.IGNORECASE):
                        matched_fund_records.append(rec)
                        matched_projects.add(pname)
                        break

# Compute total funding
total = 0
matched_details = []
for rec in matched_fund_records:
    amt = rec.get('Amount')
    try:
        val = int(str(amt))
    except:
        try:
            val = int(float(str(amt)))
        except:
            val = 0
    total += val
    matched_details.append({'Project_Name': rec.get('Project_Name',''), 'Amount': val})

# Prepare result string
if matched_details:
    msg = f"Total funding for park-related projects completed in 2022: ${total}"
else:
    msg = "Total funding for park-related projects completed in 2022: $0"

import json as _json
print("__RESULT__:")
print(_json.dumps(msg))"""

env_args = {'var_call_hrawrctsouX7uyMEWqR3rdZM': ['civic_docs'], 'var_call_vr3n5PyiecSjEweMrZb1UBzg': ['Funding'], 'var_call_QNC7P8mjljZASGfnnZi9S4PP': 'file_storage/call_QNC7P8mjljZASGfnnZi9S4PP.json', 'var_call_jifqAMOUNn9PorNbe5w6A4Vg': 'file_storage/call_jifqAMOUNn9PorNbe5w6A4Vg.json'}

exec(code, env_args)
