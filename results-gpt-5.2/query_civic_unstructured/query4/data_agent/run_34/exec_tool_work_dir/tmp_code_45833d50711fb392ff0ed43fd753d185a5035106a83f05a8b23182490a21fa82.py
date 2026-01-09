code = """import json, re, pandas as pd

# Load civic docs
path_docs = var_call_YqTSuR3GXW6Jbj4mHL5L7T6j
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Choose latest status report doc that contains project schedule lines with seasons
# We'll scan texts for 'Capital Improvement Projects and Disaster Recovery Projects Status' and 'Project Schedule'
selected = None
for d in docs:
    t = d.get('text','')
    if 'Capital Improvement Projects' in t and 'Disaster Recovery Projects' in t and 'Project Schedule' in t:
        # prefer those around 2022 (FY 2021-2022 / 2022-2023) but any ok
        if selected is None or len(t) > len(selected.get('text','')):
            selected = d

projects = []
if selected is not None:
    text = selected['text']
    # split into blocks by blank lines around project names: heuristic using double newlines
    lines = [ln.strip() for ln in text.splitlines()]
    # project names appear as standalone lines without bullet chars and not headers
    # We'll detect a project name line followed by 'Updates:' within next 10 lines
    for i, ln in enumerate(lines):
        if not ln or ln.endswith(':'):
            continue
        if any(kw in ln for kw in ['Public Works Commission','Agenda Report','RECOMMENDED ACTION','DISCUSSION','Capital Improvement Projects','Disaster Recovery Projects','Page','Agenda Item','#','Prepared by','Approved by','Date prepared','Meeting date','Subject','Project Schedule','Estimated Schedule','Project Description','Updates','(cid']):
            continue
        # likely project name if next few lines contain 'Updates' or 'Project Description'
        window = '\n'.join(lines[i+1:i+12])
        if ('Updates' in window) or ('Project Description' in window):
            pname = ln
            # find schedule line for Begin Construction/Start/etc within next 30 lines
            window2 = '\n'.join(lines[i:i+40])
            # match begin construction season/year e.g. 'Begin Construction: Spring 2022'
            m = re.search(r'Begin Construction:\s*([A-Za-z]+)\s*(\d{4})', window2)
            if not m:
                m = re.search(r'Advertise:\s*([A-Za-z]+)\s*(\d{4})', window2)  # fallback
            st = None
            if m:
                st = f"{m.group(2)}-{m.group(1)}"
            projects.append({'Project_Name': pname, 'st': st})

# Determine those started in Spring 2022
spring2022 = [p for p in projects if p.get('st') == '2022-Spring']

# Load funding totals per project
path_fund = var_call_wwChxgxD7R9MbTUwO34qbypP
with open(path_fund, 'r', encoding='utf-8') as f:
    fund = json.load(f)
fund_map = {r['Project_Name']: int(r['Total_Amount']) for r in fund}

total_funding = sum(fund_map.get(p['Project_Name'], 0) for p in spring2022)
result = {'projects_started_spring_2022_count': len(spring2022), 'projects_started_spring_2022_total_funding': total_funding}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_YqTSuR3GXW6Jbj4mHL5L7T6j': 'file_storage/call_YqTSuR3GXW6Jbj4mHL5L7T6j.json', 'var_call_wwChxgxD7R9MbTUwO34qbypP': 'file_storage/call_wwChxgxD7R9MbTUwO34qbypP.json'}

exec(code, env_args)
