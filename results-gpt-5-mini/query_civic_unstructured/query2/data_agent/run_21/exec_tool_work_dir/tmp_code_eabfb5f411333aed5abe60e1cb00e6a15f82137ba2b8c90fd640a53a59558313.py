code = """import json, re
with open(var_call_w5WiviLNuqM8uC0FZH8mDfoo, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_2shR4Lt5stCYfxsgZWUvQECb, 'r', encoding='utf-8') as f:
    funding_records = json.load(f)

park_keywords = ['park', 'playground', 'walkway', 'benches', 'bench', 'bluffs', 'playground']
complete_terms = ['completed', 'construction was completed', 'complete construction', 'complete construction:', 'notice of completion', 'complete construction:']

def clean(s):
    s = re.sub(r"\(cid:\d+\)", "", s)
    s = s.replace('\t',' ').replace('\r',' ')
    return ' '.join(s.split())

extracted = set()
for doc in civic_docs:
    text = doc.get('text','')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        lowline = line.lower()
        # if this line mentions a park keyword, check nearby context for 2022 and completion
        if any(pk in lowline for pk in park_keywords):
            window = ' '.join(lines[max(0,i-8):min(len(lines), i+9)])
            lw = window.lower()
            if '2022' in lw and any(ct in lw for ct in complete_terms):
                extracted.add(clean(line))
        # also if this line mentions 2022 and completion, look upward for park keyword
        if '2022' in line and any(ct in lowline for ct in complete_terms):
            for j in range(max(0, i-8), i+1):
                if any(pk in lines[j].lower() for pk in park_keywords):
                    extracted.add(clean(lines[j]))
                    break

# Filter short/generic
projects = [p for p in sorted(extracted) if len(p) > 3 and not p.lower().startswith(('page','agenda','item','updates'))]

# Match with funding records
matched = []
for fr in funding_records:
    pname = fr.get('Project_Name','')
    pname_l = pname.lower()
    for proj in projects:
        pl = proj.lower()
        if pl == pname_l or pl in pname_l or pname_l in pl:
            # parse amount
            amt = fr.get('Amount', 0)
            try:
                amount = int(str(amt).replace(',',''))
            except:
                try:
                    amount = int(float(str(amt)))
                except:
                    amount = 0
            matched.append({'project_doc_name': proj, 'funding_project_name': pname, 'amount': amount})

total = sum(m['amount'] for m in matched)

result = {'extracted_projects': projects, 'matched_funding_records': matched, 'total_funding': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_w5WiviLNuqM8uC0FZH8mDfoo': 'file_storage/call_w5WiviLNuqM8uC0FZH8mDfoo.json', 'var_call_2shR4Lt5stCYfxsgZWUvQECb': 'file_storage/call_2shR4Lt5stCYfxsgZWUvQECb.json', 'var_call_UQeZLuXO6HMfdozF8MGZJz3e': {'civic_docs_count': 19, 'funding_records_count': 500}}

exec(code, env_args)
