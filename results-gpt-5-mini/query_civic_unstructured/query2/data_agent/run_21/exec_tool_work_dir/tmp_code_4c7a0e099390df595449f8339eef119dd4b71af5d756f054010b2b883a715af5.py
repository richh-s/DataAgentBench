code = """import json

with open(var_call_w5WiviLNuqM8uC0FZH8mDfoo, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_2shR4Lt5stCYfxsgZWUvQECb, 'r', encoding='utf-8') as f:
    funding_records = json.load(f)

park_keywords = ['park', 'playground', 'walkway', 'benches', 'bench', 'bluffs']
complete_terms = ['completed', 'construction was completed', 'complete construction', 'notice of completion', 'complete']

def remove_cid_tokens(s):
    while True:
        idx = s.find('(cid:')
        if idx == -1:
            break
        end = s.find(')', idx)
        if end == -1:
            s = s[:idx]
            break
        s = s[:idx] + s[end+1:]
    return s

def clean(s):
    s = s.replace('\t', ' ').replace('\r', ' ')
    s = remove_cid_tokens(s)
    return ' '.join(s.split())

extracted = set()
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        low = line.lower()
        # if this line mentions park keyword, check nearby window
        if any(pk in low for pk in park_keywords):
            start = max(0, i-8)
            end = min(len(lines), i+9)
            window = ' '.join(lines[start:end]).lower()
            if '2022' in window and any(ct in window for ct in complete_terms):
                extracted.add(clean(line))
        # if this line mentions 2022 and completion, look upward for park keyword
        if '2022' in line and any(ct in low for ct in complete_terms):
            for j in range(max(0, i-8), i+1):
                if any(pk in lines[j].lower() for pk in park_keywords):
                    extracted.add(clean(lines[j]))
                    break

projects = [p for p in sorted(extracted) if len(p) > 3 and not p.lower().startswith(('page','agenda','item','updates'))]

# match to funding
matched = []
for fr in funding_records:
    pname = fr.get('Project_Name', '')
    pname_l = pname.lower()
    for proj in projects:
        pl = proj.lower()
        if pl == pname_l or pl in pname_l or pname_l in pl:
            amt_raw = fr.get('Amount', 0)
            try:
                amount = int(str(amt_raw).replace(',', ''))
            except:
                try:
                    amount = int(float(str(amt_raw)))
                except:
                    amount = 0
            matched.append({'project_doc_name': proj, 'funding_project_name': pname, 'amount': amount})

total = sum(m['amount'] for m in matched)

result = {'extracted_projects': projects, 'matched_funding_records': matched, 'total_funding': total}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_w5WiviLNuqM8uC0FZH8mDfoo': 'file_storage/call_w5WiviLNuqM8uC0FZH8mDfoo.json', 'var_call_2shR4Lt5stCYfxsgZWUvQECb': 'file_storage/call_2shR4Lt5stCYfxsgZWUvQECb.json', 'var_call_UQeZLuXO6HMfdozF8MGZJz3e': {'civic_docs_count': 19, 'funding_records_count': 500}}

exec(code, env_args)
