code = """import json, re

# Load the large results from previous query_db calls
with open(var_call_6J4006sO6RTov6u6Nm05aSqk, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_u6kbbjywWr5opYq5xQBe7hrb, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Concatenate all civic document texts into one large text for searching
all_text = "\n".join([d.get('text','') for d in civic_docs])
all_text_lower = all_text.lower()

park_funding_records = [r for r in funding if 'park' in r.get('Project_Name','').lower()]

matched = []
for r in park_funding_records:
    pname = r.get('Project_Name','')
    pname_lower = pname.lower()
    amount_str = r.get('Amount', '0')
    try:
        amount = int(amount_str)
    except:
        # remove non-digits
        amount = int(re.sub(r"[^0-9]", "", amount_str) or 0)

    found = False
    # search for exact substring occurrences of the project name in the civic texts
    for m in re.finditer(re.escape(pname_lower), all_text_lower):
        i = m.start()
        j = m.end()
        window = all_text_lower[max(0, i-200): min(len(all_text_lower), j+200)]
        if 'completed' in window and '2022' in window:
            matched.append({'Project_Name': pname, 'Amount': amount})
            found = True
            break
    if found:
        continue
    # If not found by exact match, try partial heuristics: search for key words (e.g., main name tokens)
    tokens = [t for t in re.split(r"[^a-z0-9]+", pname_lower) if t and len(t)>3]
    for t in tokens:
        for m in re.finditer(re.escape(t), all_text_lower):
            i = m.start()
            j = m.end()
            window = all_text_lower[max(0, i-200): min(len(all_text_lower), j+200)]
            if 'park' in window and 'completed' in window and '2022' in window:
                matched.append({'Project_Name': pname, 'Amount': amount})
                found = True
                break
        if found:
            break

# Deduplicate matched by Project_Name
unique = {}
for rec in matched:
    unique[rec['Project_Name']] = unique.get(rec['Project_Name'], 0) + rec['Amount']

total = sum(unique.values())

result = {'total_funding_for_parks_completed_in_2022': total, 'matched_projects': [{'Project_Name': k, 'Amount': v} for k,v in unique.items()]}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_6J4006sO6RTov6u6Nm05aSqk': 'file_storage/call_6J4006sO6RTov6u6Nm05aSqk.json', 'var_call_u6kbbjywWr5opYq5xQBe7hrb': 'file_storage/call_u6kbbjywWr5opYq5xQBe7hrb.json'}

exec(code, env_args)
