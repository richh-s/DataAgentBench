code = """import json,re

with open(var_call_6J4006sO6RTov6u6Nm05aSqk, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_u6kbbjywWr5opYq5xQBe7hrb, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Prepare lowercased civic docs texts
for d in civic_docs:
    d['text_lower'] = d.get('text','').lower()

park_funding_records = [r for r in funding if 'park' in r.get('Project_Name','').lower()]

matched = []
for r in park_funding_records:
    pname = r.get('Project_Name','')
    pname_lower = pname.lower()
    try:
        amount = int(r.get('Amount') or 0)
    except:
        amount = int(re.sub(r'[^0-9]', '', r.get('Amount') or '0') or 0)

    found = False
    # search in each civic doc
    for d in civic_docs:
        txt = d['text_lower']
        if '2022' in txt and 'completed' in txt:
            if pname_lower in txt:
                matched.append({'Project_Name': pname, 'Amount': amount})
                found = True
                break
            # fallback: check tokens and presence of 'park'
            tokens = [t for t in re.split(r'[^a-z0-9]+', pname_lower) if t and len(t)>3]
            if 'park' in txt:
                token_hits = sum(1 for t in tokens if t in txt)
                if token_hits >= 1:
                    matched.append({'Project_Name': pname, 'Amount': amount})
                    found = True
                    break
    # end docs loop

# aggregate unique by project name (sum amounts if duplicates)
unique = {}
for rec in matched:
    unique[rec['Project_Name']] = unique.get(rec['Project_Name'], 0) + rec['Amount']

total = sum(unique.values())

result = {'total_funding_for_parks_completed_in_2022': total, 'matched_projects': [{'Project_Name': k, 'Amount': v} for k,v in unique.items()]}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_6J4006sO6RTov6u6Nm05aSqk': 'file_storage/call_6J4006sO6RTov6u6Nm05aSqk.json', 'var_call_u6kbbjywWr5opYq5xQBe7hrb': 'file_storage/call_u6kbbjywWr5opYq5xQBe7hrb.json'}

exec(code, env_args)
