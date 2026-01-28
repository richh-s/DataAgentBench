code = """import json, re
import pandas as pd

funding_src = var_call_ORRyLjnXShWqH1TOfUUzxRhm
if isinstance(funding_src, str) and funding_src.endswith('.json'):
    with open(funding_src, 'r') as f:
        funding = json.load(f)
else:
    funding = funding_src
fund_df = pd.DataFrame(funding)
if not fund_df.empty:
    fund_df['Amount'] = pd.to_numeric(fund_df['Amount'], errors='coerce').fillna(0)

docs_src = var_call_6SWUtuVGucrjULNBfokAhWqi
if isinstance(docs_src, str) and docs_src.endswith('.json'):
    with open(docs_src, 'r') as f:
        docs = json.load(f)
else:
    docs = docs_src

# Build regex patterns without using backslash-escaped sequences to avoid string issues
re_disaster_hdr = re.compile('Disaster\\s+Recovery\\s+Projects', re.I)
re_capital_hdr = re.compile('Capital\\s+Improvement\\s+Projects', re.I)
re_skip_line = re.compile('^(Updates|Project Schedule|Estimated Schedule|Project Description|Page\\s+\\d+|Agenda Item|RECOMMENDED ACTION|DISCUSSION)\\b', re.I)
re_not_project = re.compile('Complete|Advertise|Begin Construction|Final Design|Design', re.I)
re_start = re.compile('\\b(Begin\\s+Construction|Start|Begin\\s+Design|Construction\\s+Start)\\b', re.I)
re_paren_disaster = re.compile('\\((FEMA|CalOES|CalJPIA)', re.I)

project_info = {}

for d in docs:
    text = d.get('text', '') or ''
    t = text.replace('\r', '')
    lines = [ln.strip() for ln in t.split('\n')]
    in_disaster = False
    current_project = None

    for ln in lines:
        if re_disaster_hdr.search(ln):
            in_disaster = True
            current_project = None
            continue
        if re_capital_hdr.search(ln):
            if in_disaster:
                in_disaster = False
                current_project = None
            continue

        if not in_disaster:
            continue

        if ln and len(ln) < 120 and (':' not in ln) and (not re_skip_line.match(ln)):
            if not re_not_project.search(ln):
                current_project = ln
                project_info.setdefault(current_project, {'is_disaster': True, 'start_2022': False})
                project_info[current_project]['is_disaster'] = True
                continue

        if current_project and ('2022' in ln) and re_start.search(ln):
            project_info[current_project]['start_2022'] = True

for name in list(project_info.keys()):
    if re_paren_disaster.search(name):
        project_info[name]['is_disaster'] = True

started_2022 = {n for n, v in project_info.items() if v.get('is_disaster') and v.get('start_2022')}

# If none found via explicit start markers, fall back to any schedule line containing 2022 under disaster section
if len(started_2022) == 0:
    re_sched = re.compile('^(Project Schedule|Estimated Schedule)\\b', re.I)
    re_skip2 = re.compile('^(Updates|Project Schedule|Estimated Schedule|Project Description|Page\\s+\\d+|Agenda Item)\\b', re.I)
    for d in docs:
        t = (d.get('text', '') or '').replace('\r', '')
        if 'Disaster Recovery Projects' not in t:
            continue
        lines = [ln.strip() for ln in t.split('\n')]
        in_disaster = False
        current = None
        in_schedule = False
        for ln in lines:
            if re_disaster_hdr.search(ln):
                in_disaster = True
                current = None
                in_schedule = False
                continue
            if re_capital_hdr.search(ln) and in_disaster:
                in_disaster = False
                current = None
                in_schedule = False
                continue
            if not in_disaster:
                continue
            if ln and len(ln) < 120 and (':' not in ln) and (not re_skip2.match(ln)):
                if not re_not_project.search(ln):
                    current = ln
                    in_schedule = False
                    project_info.setdefault(current, {'is_disaster': True, 'start_2022': False})
                    continue
            if re_sched.match(ln):
                in_schedule = True
                continue
            if current and in_schedule and ('2022' in ln):
                project_info[current]['start_2022'] = True

    started_2022 = {n for n, v in project_info.items() if v.get('is_disaster') and v.get('start_2022')}

if fund_df.empty:
    total = 0
    matched = 0
else:
    mask = fund_df['Project_Name'].isin(started_2022)
    total = float(fund_df.loc[mask, 'Amount'].sum())
    matched = int(mask.sum())

out = {
    'total_funding_usd': int(total),
    'matched_projects_count': matched,
    'started_2022_disaster_projects': sorted(list(started_2022))
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_ORRyLjnXShWqH1TOfUUzxRhm': 'file_storage/call_ORRyLjnXShWqH1TOfUUzxRhm.json', 'var_call_6SWUtuVGucrjULNBfokAhWqi': 'file_storage/call_6SWUtuVGucrjULNBfokAhWqi.json'}

exec(code, env_args)
