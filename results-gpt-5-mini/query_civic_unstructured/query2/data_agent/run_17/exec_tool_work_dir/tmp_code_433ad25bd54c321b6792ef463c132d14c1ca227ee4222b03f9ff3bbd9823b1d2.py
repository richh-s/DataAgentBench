code = """import json, re

# Load civic docs results
path_civic = var_call_qq5H8yxp6vSjXz8DyOJq4vMt
with open(path_civic, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Load funding results
path_funding = var_call_MRy4mHtwIMauqNFgG2MkW8MK
with open(path_funding, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Normalize funding amounts and prepare list
for r in funding:
    try:
        r['Amount'] = int(r['Amount'])
    except:
        try:
            r['Amount'] = int(float(r['Amount']))
        except:
            r['Amount'] = 0

# Candidate park-related funding projects: those whose Project_Name contains 'park' or 'playground' or 'bluffs'
park_candidates = [r for r in funding if re.search(r'\bpark\b', r['Project_Name'], re.IGNORECASE) or re.search(r'playground', r['Project_Name'], re.IGNORECASE) or re.search(r'bluffs', r['Project_Name'], re.IGNORECASE)]

matched = []

# For each candidate, search civic_docs texts for evidence of completion in 2022
for proj in park_candidates:
    pname = proj['Project_Name']
    found = False
    for doc in civic_docs:
        text = doc.get('text','')
        # find all occurrences of project name (case-insensitive)
        for m in re.finditer(re.escape(pname), text, re.IGNORECASE):
            start = max(0, m.start()-400)
            end = min(len(text), m.end()+400)
            window = text[start:end].lower()
            # look for 'complete' or 'completed' or 'complete construction' nearby and '2022'
            if '2022' in window and ('complete' in window or 'completed' in window or 'complete construction' in window or 'construction was completed' in window or 'complete design' in window):
                found = True
                break
        if found:
            break
    if found:
        matched.append({'Project_Name': pname, 'Amount': proj['Amount']})

# Additionally, some park projects might be described in civic_docs but funding names differ slightly.
# Search civic_docs for project names that include 'park' and 'completed' and '2022', then try to match to funding by substring containment.
park_projects_in_docs = set()
for doc in civic_docs:
    text = doc.get('text','').lower()
    # find lines or segments mentioning 'park' and 'completed' and '2022'
    if 'park' in text and '2022' in text and 'completed' in text:
        # extract potential project names by regex for lines around 'park'
        for m in re.finditer(r'([A-Z][A-Za-z0-9\s\-\'"\(\)]+park[A-Za-z0-9\s\-\'"\(\)]*)', doc.get('text',''), re.IGNORECASE):
            seg = m.group(1).strip()
            if len(seg) < 200:
                park_projects_in_docs.add(seg)

# Try to match these to funding entries by substring
for projname in park_projects_in_docs:
    # try to find funding entries where projname is substring of Project_Name or vice versa
    for f in funding:
        if projname.lower() in f['Project_Name'].lower() or f['Project_Name'].lower() in projname.lower():
            # ensure not already added
            if not any(x['Project_Name']==f['Project_Name'] for x in matched):
                # verify the doc snippet containing projname also had completed and 2022
                # (we already ensured that by selection)
                matched.append({'Project_Name': f['Project_Name'], 'Amount': f['Amount']})

# Sum amounts
total = sum(x['Amount'] for x in matched)

result = {'total_funding': total, 'matched_projects': matched}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_h13harN4hIdf4SoYdUp1TJC9': ['civic_docs'], 'var_call_cRJrleGz2E7eW0b4Wfh42kvJ': ['Funding'], 'var_call_qq5H8yxp6vSjXz8DyOJq4vMt': 'file_storage/call_qq5H8yxp6vSjXz8DyOJq4vMt.json', 'var_call_MRy4mHtwIMauqNFgG2MkW8MK': 'file_storage/call_MRy4mHtwIMauqNFgG2MkW8MK.json'}

exec(code, env_args)
