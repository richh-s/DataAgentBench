code = """import json, re
with open(var_call_JPc0AHZNJ473qRVXDXq8OJB7, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_IGVzk4aYxUvIhkPcDouVPXxQ, 'r', encoding='utf-8') as f:
    funding_rows = json.load(f)
funding = []
for r in funding_rows:
    name = r.get('Project_Name', '').strip()
    amt_raw = r.get('Amount', 0)
    try:
        amt = int(str(amt_raw).replace(',', '').strip())
    except:
        try:
            amt = int(float(str(amt_raw).strip()))
        except:
            amt = 0
    funding.append({'name': name, 'name_l': name.lower(), 'amount': amt})

def extract_design_projects_from_text(text):
    projects = []
    marker = 'Capital Improvement Projects (Design)'
    start = text.find(marker)
    if start == -1:
        return projects
    candidates = [
        'Capital Improvement Projects (Construction)',
        'Capital Improvement Projects (Not Started)'
    ]
    end_positions = [text.find(c, start+len(marker)) for c in candidates if text.find(c, start+len(marker))!=-1]
    end = min(end_positions) if end_positions else len(text)
    section = text[start+len(marker):end]
    lines = [ln.strip() for ln in section.splitlines()]
    for ln in lines:
        if not ln:
            continue
        low = ln.lower()
        if ln.startswith('(') or 'cid:' in low:
            continue
        if ':' in ln:
            skip_phrases = ['updates', 'project schedule', 'project description', 'estimated schedule', 'page', 'agenda']
            if any(sp in low for sp in skip_phrases):
                continue
        if re.search(r'complete design|advertise|begin construction|updates|project schedule|complete construction', low):
            continue
        if len(ln) < 6:
            continue
        if ln.endswith('.') or ln.endswith(':'):
            continue
        if len(ln.split()) > 12:
            continue
        projects.append(ln)
    seen = set()
    dedup = []
    for p in projects:
        pl = p.lower()
        if pl not in seen:
            seen.add(pl)
            dedup.append(p)
    return dedup

all_design = []
for doc in civic_docs:
    text = doc.get('text','')
    all_design.extend(extract_design_projects_from_text(text))
seen = set(); design_projects_unique = []
for p in all_design:
    pl = p.lower()
    if pl not in seen:
        seen.add(pl)
        design_projects_unique.append(p)

matched = {}
for proj in design_projects_unique:
    pl = proj.lower()
    max_amt = 0
    matched_any = False
    for f in funding:
        fn = f['name_l']
        if fn == pl or pl in fn or fn in pl:
            matched_any = True
            if f['amount'] > max_amt:
                max_amt = f['amount']
    if matched_any and max_amt > 50000:
        matched[proj] = max_amt

result = {'count': len(matched), 'projects': [{'Project_Name': k, 'Max_Funding_Amount': v} for k, v in matched.items()]}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_QtrJYdmqZO25uIQ3SftUGcBd': ['civic_docs'], 'var_call_ac6iPhPJz3RegHhG8ATcrZsH': ['Funding'], 'var_call_JPc0AHZNJ473qRVXDXq8OJB7': 'file_storage/call_JPc0AHZNJ473qRVXDXq8OJB7.json', 'var_call_IGVzk4aYxUvIhkPcDouVPXxQ': 'file_storage/call_IGVzk4aYxUvIhkPcDouVPXxQ.json'}

exec(code, env_args)
