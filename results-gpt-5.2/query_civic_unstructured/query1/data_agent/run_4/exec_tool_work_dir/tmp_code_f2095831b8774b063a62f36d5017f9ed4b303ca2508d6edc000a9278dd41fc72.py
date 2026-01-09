code = """import json, re
import pandas as pd

def load_records(maybe_path):
    if isinstance(maybe_path, str) and maybe_path.endswith('.json'):
        with open(maybe_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path

funding = load_records(var_call_dQMDkEhraVToewND2NsG7Sq7)
docs = load_records(var_call_19w2pYQ1u1S8qDErvxa5Ejhw)

fund_projects = {r['Project_Name'] for r in funding}

def extract_design_capital_projects(text):
    # Find section between 'Capital Improvement Projects (Design)' and next 'Capital Improvement Projects (' or 'Disaster Recovery Projects'
    m = re.search(r'Capital Improvement Projects \(Design\)(.*?)(?:\n\s*Capital Improvement Projects \(|\n\s*Disaster Recovery Projects|\Z)', text, flags=re.IGNORECASE|re.DOTALL)
    if not m:
        return []
    section = m.group(1)
    lines = [ln.strip() for ln in section.splitlines()]
    projects = []
    for ln in lines:
        if not ln:
            continue
        # skip bullets/updates/schedule/page headers
        if any(k in ln.lower() for k in ['updates:', 'project schedule', 'estimated schedule', 'complete design', 'advertise:', 'begin construction', 'page ', 'agenda item', '(cid:', 'project description']):
            continue
        # project names tend to be standalone lines without colon and not too long
        if ':' in ln:
            continue
        # avoid generic headings
        if re.fullmatch(r'capital improvement projects.*', ln, flags=re.IGNORECASE):
            continue
        if len(ln) < 3 or len(ln) > 120:
            continue
        # keep if starts with letter/number and contains at least one alpha
        if not re.match(r'^[A-Za-z0-9]', ln):
            continue
        if not re.search(r'[A-Za-z]', ln):
            continue
        # de-duplicate consecutive
        if projects and projects[-1].lower() == ln.lower():
            continue
        projects.append(ln)
    return projects

capital_design_projects = set()
for d in docs:
    for p in extract_design_capital_projects(d.get('text','')):
        capital_design_projects.add(p)

# intersection with funded >50k projects (exact match)
count = sum(1 for p in capital_design_projects if p in fund_projects)

print('__RESULT__:')
print(json.dumps({'count': int(count), 'projects': sorted([p for p in capital_design_projects if p in fund_projects])}))"""

env_args = {'var_call_c3HPNynpVC25T6F3gci1Kh8p': ['Funding'], 'var_call_oDAW5VDp7OxJ3eI1nHzkTxIC': ['civic_docs'], 'var_call_dQMDkEhraVToewND2NsG7Sq7': 'file_storage/call_dQMDkEhraVToewND2NsG7Sq7.json', 'var_call_19w2pYQ1u1S8qDErvxa5Ejhw': 'file_storage/call_19w2pYQ1u1S8qDErvxa5Ejhw.json'}

exec(code, env_args)
