code = """import json, re

def load_records(maybe_path):
    if isinstance(maybe_path, str) and maybe_path.endswith('.json'):
        with open(maybe_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path

funding = load_records(var_call_dQMDkEhraVToewND2NsG7Sq7)
docs = load_records(var_call_19w2pYQ1u1S8qDErvxa5Ejhw)

fund_projects = {r['Project_Name'] for r in funding}

def extract_design_capital_projects(text):
    # capture section text after heading
    pattern = r"Capital Improvement Projects \(Design\)(.*?)(?:Capital Improvement Projects \(|Disaster Recovery Projects|\Z)"
    m = re.search(pattern, text, flags=re.IGNORECASE | re.DOTALL)
    if not m:
        return []
    section = m.group(1)
    lines = [ln.strip() for ln in section.splitlines()]
    projects = []
    for ln in lines:
        if not ln:
            continue
        low = ln.lower()
        skip_phrases = ['updates:', 'project schedule', 'estimated schedule', 'complete design', 'advertise:', 'begin construction', 'agenda item', 'project description']
        if any(sp in low for sp in skip_phrases):
            continue
        if '(cid:' in low or low.startswith('page '):
            continue
        if ':' in ln:
            continue
        if len(ln) < 3 or len(ln) > 120:
            continue
        if not re.match(r'^[A-Za-z0-9]', ln):
            continue
        if not re.search(r'[A-Za-z]', ln):
            continue
        projects.append(ln)
    # dedupe preserve order
    out=[]
    seen=set()
    for p in projects:
        k=p.lower()
        if k not in seen:
            seen.add(k)
            out.append(p)
    return out

capital_design_projects=set()
for d in docs:
    for p in extract_design_capital_projects(d.get('text','')):
        capital_design_projects.add(p)

matched = sorted([p for p in capital_design_projects if p in fund_projects])

print('__RESULT__:')
print(json.dumps({'count': len(matched), 'projects': matched}))"""

env_args = {'var_call_c3HPNynpVC25T6F3gci1Kh8p': ['Funding'], 'var_call_oDAW5VDp7OxJ3eI1nHzkTxIC': ['civic_docs'], 'var_call_dQMDkEhraVToewND2NsG7Sq7': 'file_storage/call_dQMDkEhraVToewND2NsG7Sq7.json', 'var_call_19w2pYQ1u1S8qDErvxa5Ejhw': 'file_storage/call_19w2pYQ1u1S8qDErvxa5Ejhw.json'}

exec(code, env_args)
