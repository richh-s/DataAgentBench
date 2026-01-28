code = """import json, re, pandas as pd

# load funded project names (>50k)
path = var_call_pjyJCBqxjnhZGELe2LBDx1ot
with open(path,'r') as f:
    funded = json.load(f)
funded_names = {r['Project_Name'] for r in funded if r.get('Project_Name')}

# load civic docs
docs_path = var_call_yvMGi69Zrb1SVhNwovJE3Tun
with open(docs_path,'r') as f:
    docs = json.load(f)

status_projects = set()

# parse projects under 'Capital Improvement Projects (Design)'
for d in docs:
    text = d.get('text','')
    if 'Capital Improvement Projects (Design)' not in text:
        continue
    # take section from Design header until next 'Capital Improvement Projects (' or 'Disaster Recovery Projects'
    start = text.find('Capital Improvement Projects (Design)')
    sub = text[start:]
    # end markers
    end_positions = [p for p in [sub.find('Capital Improvement Projects (Construction)'),
                                sub.find('Capital Improvement Projects (Not Started)'),
                                sub.find('Disaster Recovery Projects'),
                                sub.find('Disaster Recovery Projects (')]
                     if p!=-1]
    if end_positions:
        sub = sub[:min(end_positions)]

    lines = [ln.strip() for ln in sub.splitlines()]
    # collect candidate project name lines: non-empty, not bullets, not headings, not schedule/update labels
    for ln in lines:
        if not ln: 
            continue
        if ln.lower().startswith(('capital improvement projects','project schedule','estimated schedule','updates','discussion','recommended action','page ')):
            continue
        if any(tok in ln for tok in ['(cid:', 'Agenda Item', 'Prepared by', 'Approved by', 'To:', 'Subject:']):
            continue
        if ln.startswith(('-', '•','','0','1','6','7')):
            continue
        if ':' in ln and len(ln.split())<=5:
            continue
        # heuristics: likely project name line if contains 'Project' or 'Plan' or 'Facility' or 'Park' or 'Road' etc and not a sentence
        if len(ln) > 4 and len(ln) < 120:
            # exclude sentences (contain period) and update text
            if '.' in ln:
                continue
            # must have at least 2 words
            if len(ln.split()) < 2:
                continue
            # filter out schedule items like 'Complete Design: Summer 2023'
            if re.search(r'^(Complete|Begin|Advertise|Final)\s', ln):
                continue
            # add
            status_projects.add(ln)

# intersect with funded project names
count = len(status_projects & funded_names)

print('__RESULT__:')
print(json.dumps({'count': count}))"""

env_args = {'var_call_okqKvXewzcFtP0avPdRpMEW1': [{'cnt': '276'}], 'var_call_yvMGi69Zrb1SVhNwovJE3Tun': 'file_storage/call_yvMGi69Zrb1SVhNwovJE3Tun.json', 'var_call_pjyJCBqxjnhZGELe2LBDx1ot': 'file_storage/call_pjyJCBqxjnhZGELe2LBDx1ot.json'}

exec(code, env_args)
