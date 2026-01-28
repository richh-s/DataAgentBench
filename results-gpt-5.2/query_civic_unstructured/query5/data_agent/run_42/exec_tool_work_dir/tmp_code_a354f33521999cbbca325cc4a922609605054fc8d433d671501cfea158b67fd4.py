code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

docs = load_records(var_call_gzsZiU7wXQyH4mWQvV7OHFPc)
fund = load_records(var_call_RJmqRBDb3cvzpVjDNrgMt7U5)

projects = []

st_re = re.compile(r'^(?:\(cid:131\)\s*)?(?:Begin Construction|Start|Construction Start|Begin|Kickoff)\s*:\s*(.+)$', re.I)
alt_re = re.compile(r'^(?:\(cid:131\)\s*)?(?:Complete Design|Advertise|Final Design|Preliminary Design)\s*:\s*(.+)$', re.I)

def norm_name(s):
    s = re.sub(r'\s+', ' ', s).strip()
    return s

for d in docs:
    text = d.get('text','') or ''
    if 'Disaster Recovery Projects' not in text:
        continue
    lines = [ln.rstrip() for ln in text.splitlines()]
    in_disaster = False
    current = None
    for ln in lines:
        ls = ln.strip()
        if re.match(r'^Disaster Recovery Projects', ls):
            in_disaster = True
            current = None
            continue
        if in_disaster and re.match(r'^Capital Improvement Projects', ls):
            in_disaster = False
            current = None
            continue
        if not in_disaster or not ls:
            continue
        if ls.lower().startswith('page ') or ls.lower().startswith('agenda item'):
            continue
        if ls.startswith('(cid:'):
            m = st_re.match(ls)
            if m and current is not None:
                projects.append({'Project_Name': current, 'st': norm_name(m.group(1))})
            else:
                m2 = alt_re.match(ls)
                if m2 and current is not None:
                    projects.append({'Project_Name': current, 'st': norm_name(m2.group(1))})
            continue
        if not ls.endswith(':') and ls not in ['Discussion','Recommended Action','RECOMMENDED ACTION']:
            if len(ls) <= 160 and re.search(r'(Project|Repairs|Repair|Improvements|Improvement|Slope|Culvert|Bridge|Drain|Storm|Warning|Fire|FEMA|CalOES)', ls, re.I):
                current = norm_name(ls)

started_2022 = {p['Project_Name'] for p in projects if p.get('st') and '2022' in p['st']}

fund_df = pd.DataFrame(fund)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'])
matched = fund_df[fund_df['Project_Name'].isin(started_2022)]

out = {
    'total_funding': int(matched['total_amount'].sum()),
    'num_projects': int(matched.shape[0]),
    'projects': matched.sort_values('Project_Name')[['Project_Name','total_amount']].to_dict(orient='records'),
    'started_2022_projects': sorted(started_2022)
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_mImfOvDqjEWwtbOEFHa6RwO8': ['Funding'], 'var_call_zek2GZ6YL608W3ghopgfCLDJ': ['civic_docs'], 'var_call_gzsZiU7wXQyH4mWQvV7OHFPc': 'file_storage/call_gzsZiU7wXQyH4mWQvV7OHFPc.json', 'var_call_RJmqRBDb3cvzpVjDNrgMt7U5': 'file_storage/call_RJmqRBDb3cvzpVjDNrgMt7U5.json'}

exec(code, env_args)
