code = """import json, re
import pandas as pd

# Load funding
funding_src = var_call_ORRyLjnXShWqH1TOfUUzxRhm
if isinstance(funding_src, str) and funding_src.endswith('.json'):
    with open(funding_src,'r') as f:
        funding = json.load(f)
else:
    funding = funding_src
fund_df = pd.DataFrame(funding)
if not fund_df.empty:
    fund_df['Amount'] = pd.to_numeric(fund_df['Amount'], errors='coerce').fillna(0)

# Load docs
docs_src = var_call_6SWUtuVGucrjULNBfokAhWqi
if isinstance(docs_src, str) and docs_src.endswith('.json'):
    with open(docs_src,'r') as f:
        docs = json.load(f)
else:
    docs = docs_src

# Identify disaster recovery project entries with start date in 2022.
# Heuristic: In status reports, Disaster Recovery Projects section and project lines following it.
# Extract schedule lines containing 'Begin Construction' or 'Start' with 2022 or '2022-' etc.

project_info = {}  # name -> {'is_disaster':bool, 'start_2022':bool}

for d in docs:
    text = d.get('text','') or ''
    # normalize
    t = text.replace('\r','')
    # Split into lines for scanning
    lines = [ln.strip() for ln in t.split('\n')]
    in_disaster = False
    current_project = None
    for ln in lines:
        if re.search(r'Disaster\s+Recovery\s+Projects', ln, re.I):
            in_disaster = True
            current_project = None
            continue
        if re.search(r'Capital\s+Improvement\s+Projects', ln, re.I):
            # leaving disaster section when capital section appears after
            if in_disaster:
                in_disaster = False
                current_project = None
            continue
        # project name lines: often plain text not starting with special chars and not too long
        if in_disaster:
            # detect project header: line with letters and maybe parentheses, no colon, not bullet words
            if ln and len(ln) < 120 and ':' not in ln and not re.match(r'^(Updates|Project Schedule|Estimated Schedule|Project Description|Page \d+|Agenda Item|RECOMMENDED ACTION|DISCUSSION)\b', ln, re.I):
                # avoid schedule entries
                if not re.search(r'Complete|Advertise|Begin Construction|Final Design|Design', ln, re.I):
                    current_project = ln
                    if current_project not in project_info:
                        project_info[current_project] = {'is_disaster': True, 'start_2022': False}
                    else:
                        project_info[current_project]['is_disaster'] = True
                    continue
            if current_project:
                if '2022' in ln and re.search(r'\b(Begin\s+Construction|Start|Begin\s+Design|Construction\s+Start)\b', ln, re.I):
                    project_info[current_project]['start_2022'] = True

# Additionally, if project name itself contains (FEMA/CalOES/CalJPIA/CalOES) treat as disaster.
for name in list(project_info.keys()):
    if re.search(r'\((FEMA|CalOES|CalJPIA)', name, re.I):
        project_info[name]['is_disaster'] = True

# Create list of disaster projects started 2022
started_2022 = {n for n,v in project_info.items() if v.get('is_disaster') and v.get('start_2022')}

# Fallback heuristic: if no explicit start found, approximate by scanning for 'Project Schedule' under disaster project and any line containing '2022' in first schedule block
if len(started_2022)==0:
    for d in docs:
        t = (d.get('text','') or '').replace('\r','')
        if 'Disaster Recovery Projects' not in t:
            continue
        lines = [ln.strip() for ln in t.split('\n')]
        in_disaster=False
        current=None
        in_schedule=False
        for ln in lines:
            if re.search(r'Disaster\s+Recovery\s+Projects', ln, re.I):
                in_disaster=True; current=None; in_schedule=False; continue
            if re.search(r'Capital\s+Improvement\s+Projects', ln, re.I) and in_disaster:
                in_disaster=False; current=None; in_schedule=False; continue
            if in_disaster:
                if ln and len(ln)<120 and ':' not in ln and not re.match(r'^(Updates|Project Schedule|Estimated Schedule|Project Description|Page \d+|Agenda Item)\b', ln, re.I):
                    if not re.search(r'Complete|Advertise|Begin Construction|Final Design|Design', ln, re.I):
                        current=ln; in_schedule=False
                        project_info.setdefault(current, {'is_disaster': True, 'start_2022': False})
                        continue
                if re.match(r'^(Project Schedule|Estimated Schedule)\b', ln, re.I):
                    in_schedule=True
                    continue
                if current and in_schedule and '2022' in ln:
                    project_info[current]['start_2022']=True
    started_2022 = {n for n,v in project_info.items() if v.get('is_disaster') and v.get('start_2022')}

# Join with funding. Project_Name match exact.
if fund_df.empty:
    total = 0
else:
    total = fund_df[fund_df['Project_Name'].isin(started_2022)]['Amount'].sum()

out = {'total_funding_usd': int(total), 'matched_projects_count': int(fund_df['Project_Name'].isin(started_2022).sum()), 'started_2022_disaster_projects': sorted(list(started_2022))}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_ORRyLjnXShWqH1TOfUUzxRhm': 'file_storage/call_ORRyLjnXShWqH1TOfUUzxRhm.json', 'var_call_6SWUtuVGucrjULNBfokAhWqi': 'file_storage/call_6SWUtuVGucrjULNBfokAhWqi.json'}

exec(code, env_args)
