code = """import json

with open(var_call_w5WiviLNuqM8uC0FZH8mDfoo, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_2shR4Lt5stCYfxsgZWUvQECb, 'r', encoding='utf-8') as f:
    funding_records = json.load(f)

park_keywords = ['park', 'playground', 'walkway', 'benches', 'bench', 'bluffs', 'playground']
completed_terms = ['completed', 'complete', 'notice of completion', 'complete construction', 'complete construction:']

def clean_text(s):
    s = s.replace('\t', ' ').replace('\r', ' ').strip()
    # remove cid tokens
    while '(cid:' in s:
        start = s.find('(cid:')
        end = s.find(')', start)
        if end != -1:
            s = s[:start] + s[end+1:]
        else:
            s = s[:start]
    return ' '.join(s.split())

found_projects = set()
for doc in civic_docs:
    text = doc.get('text','')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        low = line.lower()
        if '2022' in line and any(term in low for term in completed_terms):
            # search upward up to 10 lines for park keyword
            for j in range(max(0, i-10), i+1):
                candidate = lines[j].strip()
                if any(pk in candidate.lower() for pk in park_keywords):
                    candidate = clean_text(candidate)
                    if len(candidate) > 3:
                        found_projects.add(candidate)
                        break
    # second pass: find park lines then check following lines for completed+2022
    for i, line in enumerate(lines):
        if any(pk in line.lower() for pk in park_keywords):
            candidate = clean_text(line)
            window = ' '.join(lines[i:i+9]).lower()
            if '2022' in window and any(term in window for term in completed_terms):
                if len(candidate) > 3:
                    found_projects.add(candidate)

# Normalize found project names
clean_projects = []
for p in sorted(found_projects):
    pp = p.strip(' -:\n\t')
    if len(pp) > 3 and not pp.lower().startswith(('updates','page','agenda','item')):
        clean_projects.append(pp)

# match funding records
matched = []
for fr in funding_records:
    pname = fr.get('Project_Name','')
    for proj in clean_projects:
        if not proj:
            continue
        pl = proj.lower()
        nl = pname.lower()
        if pl == nl or pl in nl or nl in pl:
            try:
                amt = int(fr.get('Amount') if fr.get('Amount') is not None else 0)
            except:
                try:
                    amt = int(float(fr.get('Amount')))
                except:
                    amt = 0
            matched.append({'project_doc_name': proj, 'funding_project_name': pname, 'amount': amt})

total = sum(m['amount'] for m in matched)

result = {'extracted_projects': clean_projects, 'matched_funding_records': matched, 'total_funding': total}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_w5WiviLNuqM8uC0FZH8mDfoo': 'file_storage/call_w5WiviLNuqM8uC0FZH8mDfoo.json', 'var_call_2shR4Lt5stCYfxsgZWUvQECb': 'file_storage/call_2shR4Lt5stCYfxsgZWUvQECb.json'}

exec(code, env_args)
