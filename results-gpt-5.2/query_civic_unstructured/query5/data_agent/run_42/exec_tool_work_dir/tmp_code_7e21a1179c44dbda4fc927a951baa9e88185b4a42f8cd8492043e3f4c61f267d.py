code = """import json, re, pandas as pd

def load_records(var):
    if isinstance(var, str) and var.endswith('.json'):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

docs = load_records(var_call_gzsZiU7wXQyH4mWQvV7OHFPc)
fund = load_records(var_call_RJmqRBDb3cvzpVjDNrgMt7U5)

# Parse projects from docs: focus on Disaster Recovery Projects section; capture schedule lines.
projects = []  # {Project_Name, type, st}

# Patterns
proj_line_re = re.compile(r'^(?!\s)([A-Za-z0-9].{2,120}?)\s*$')
st_re = re.compile(r'^(?:\(cid:131\)\s*)?(?:Begin Construction|Start|Construction Start|Begin|Kickoff)\s*:\s*(.+)$', re.I)
alt_st_re = re.compile(r'^(?:\(cid:131\)\s*)?(?:Complete Design|Advertise|Final Design|Preliminary Design)\s*:\s*(.+)$', re.I)

def norm_name(s):
    s = re.sub(r'\s+', ' ', s).strip()
    s = s.replace('\u2019', "'")
    return s

for d in docs:
    text = d.get('text','')
    if 'Disaster Recovery Projects' not in text:
        continue
    lines = [ln.rstrip() for ln in text.splitlines()]
    in_disaster = False
    current = None
    seen_schedule = False
    for ln in lines:
        l = ln.strip('\n')
        if re.search(r'^Disaster Recovery Projects', l):
            in_disaster = True
            current = None
            seen_schedule = False
            continue
        if in_disaster and re.search(r'^Capital Improvement Projects', l):
            in_disaster = False
            current = None
            continue
        if not in_disaster:
            continue
        ls = l.strip()
        if not ls:
            continue
        # detect a project name line: not bullet updates/schedule headers
        if ls in ['Updates:', 'Project Updates:', 'Project Schedule:', 'Estimated Schedule:', 'Project Description:', '(cid:190) Updates:', '(cid:190) Project Schedule:', '(cid:190) Estimated Schedule:']:
            continue
        if ls.startswith('(cid:'):
            # bullet line, might contain schedule
            m = st_re.match(ls)
            if m and current is not None:
                st = norm_name(m.group(1))
                projects.append({'Project_Name': current, 'type':'disaster', 'st': st})
            continue
        # project name candidate: ignore page headers
        if ls.lower().startswith('page ') or ls.lower().startswith('agenda item'):
            continue
        # if line ends with 'Project' or contains 'Repairs' etc and next lines have bullets; accept.
        if len(ls) <= 140 and not ls.endswith(':'):
            # heuristic: treat as project header if previous not in a project or previous was schedule/update header
            # and line is not just generic words
            if ls not in ['Discussion','Recommended Action'] and not re.match(r'^(cid:|\(cid)', ls):
                # many headers include words like Project, Repairs, Improvements, Culvert, etc.
                if re.search(r'(Project|Repairs|Repair|Improvements|Improvement|Slope|Culvert|Bridge|Drain|Storm|Warning|Fire|FEMA|CalOES)', ls, re.I):
                    current = norm_name(ls)
                    seen_schedule = False
                    continue

# Determine which disaster projects started in 2022 using st containing '2022'
started_2022 = {p['Project_Name'] for p in projects if p.get('st') and '2022' in p['st']}

# If no explicit begin construction lines, fallback: treat projects with any schedule date in 2022 within disaster section.
if not started_2022:
    # broader parse: in disaster section, for each current project capture any schedule value lines and test for 2022
    started_2022 = set()
    for d in docs:
        text = d.get('text','')
        if 'Disaster Recovery Projects' not in text:
            continue
        lines = [ln.rstrip() for ln in text.splitlines()]
        in_disaster = False
        current = None
        for ln in lines:
            ls = ln.strip()
            if re.search(r'^Disaster Recovery Projects', ls):
                in_disaster = True
                current = None
                continue
            if in_disaster and re.search(r'^Capital Improvement Projects', ls):
                in_disaster = False
                current = None
                continue
            if not in_disaster or not ls:
                continue
            if ls.startswith('(cid:'):
                m = st_re.match(ls) or alt_st_re.match(ls)
                if m and current is not None and '2022' in m.group(1):
                    started_2022.add(current)
                continue
            if ls.lower().startswith('page ') or ls.lower().startswith('agenda item'):
                continue
            if len(ls) <= 140 and not ls.endswith(':') and ls not in ['Discussion','Recommended Action']:
                if re.search(r'(Project|Repairs|Repair|Improvements|Improvement|Slope|Culvert|Bridge|Drain|Storm|Warning|Fire|FEMA|CalOES)', ls, re.I):
                    current = norm_name(ls)

fund_df = pd.DataFrame(fund)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'])

# Disaster-related projects: from funding names containing FEMA/CalOES/CalJPIA or those in started_2022 set.
# But question asks disaster-related projects that started in 2022. We'll use started_2022 set and join with funding.
matched = fund_df[fund_df['Project_Name'].isin(started_2022)]

total = int(matched['total_amount'].sum())

out = {
    'total_funding': total,
    'num_projects': int(matched.shape[0]),
    'projects': matched.sort_values('Project_Name')[['Project_Name','total_amount']].to_dict(orient='records')
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_mImfOvDqjEWwtbOEFHa6RwO8': ['Funding'], 'var_call_zek2GZ6YL608W3ghopgfCLDJ': ['civic_docs'], 'var_call_gzsZiU7wXQyH4mWQvV7OHFPc': 'file_storage/call_gzsZiU7wXQyH4mWQvV7OHFPc.json', 'var_call_RJmqRBDb3cvzpVjDNrgMt7U5': 'file_storage/call_RJmqRBDb3cvzpVjDNrgMt7U5.json'}

exec(code, env_args)
