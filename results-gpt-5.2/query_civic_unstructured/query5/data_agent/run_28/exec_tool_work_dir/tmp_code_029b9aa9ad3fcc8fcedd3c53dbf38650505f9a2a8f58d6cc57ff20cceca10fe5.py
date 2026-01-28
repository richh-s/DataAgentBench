code = """import json, re
import pandas as pd

# Load funding records
fp = var_call_E3A3KNZAloQm34K4K1JvVvyY
with open(fp, 'r') as f:
    funding = json.load(f)
df_f = pd.DataFrame(funding)
df_f['Amount'] = pd.to_numeric(df_f['Amount'], errors='coerce').fillna(0).astype(int)

# Load 2022 civic docs
dp = var_call_JESPpTsMF7CJnZLezqHiSbmp
with open(dp, 'r') as f:
    docs = json.load(f)

# Heuristic: project started in 2022 if a line near the project contains
# 'Begin Construction:' or 'Begin Design:' or 'Award Contract and Begin Construction:' with '2022'
# and the project is in Disaster section (Disaster Projects (Design/Construction/Not Started/Completed))

def extract_disaster_projects_started_2022(text):
    lines = [ln.strip() for ln in text.splitlines()]
    started = set()
    in_disaster = False
    current_project = None
    for i, ln in enumerate(lines):
        if re.search(r'^Disaster Projects', ln):
            in_disaster = True
            current_project = None
            continue
        if in_disaster and re.search(r'^(Capital Improvement Projects|Page \d+ of \d+|Agenda Item)', ln):
            # don't exit on page markers; but if Capital starts again, exit
            if ln.startswith('Capital Improvement Projects'):
                in_disaster = False
            continue
        if not in_disaster:
            continue
        # Identify potential project title lines: non-empty and not bullet/label
        if ln and not ln.startswith('(cid') and not re.match(r'^(Updates:|Project Schedule|Estimated Schedule|Project Description|\u2022|RECOMMENDED ACTION|DISCUSSION:)', ln):
            # project titles often have parentheses and no colon
            if len(ln) < 120 and not ln.endswith(':') and not re.search(r'\b(cid:|Page|To:|Prepared by:|Approved by:|Date prepared:|Meeting date:|Subject:)\b', ln):
                # when a new title appears, set current_project
                # avoid schedule lines
                if not re.match(r'^(Complete|Begin|Advertise|Award|Final|Design:)', ln):
                    current_project = ln
        # Check begin lines
        if current_project and re.search(r'^(Begin Construction|Begin Design|Award Contract and Begin Construction):', ln):
            if '2022' in ln:
                started.add(current_project)
        # Also check within next 2 lines after 'Project Schedule' for begin
        if current_project and re.search(r'^(Begin Construction|Begin Design|Award Contract and Begin Construction)', ln) and '2022' in ln:
            started.add(current_project)
    return started

started_projects = set()
for d in docs:
    started_projects |= extract_disaster_projects_started_2022(d.get('text',''))

# Filter to disaster-related by name heuristic as backup (FEMA/CalOES/CalJPIA)
# but main is being in Disaster section.

started_list = sorted(started_projects)

# Join to funding on exact Project_Name
fund_started = df_f[df_f['Project_Name'].isin(started_list)]

result = {
    'total_funding_amount_usd': int(fund_started['Amount'].sum()),
    'num_disaster_projects_started_2022_with_funding_match': int(fund_started['Project_Name'].nunique()),
    'matched_projects': fund_started.groupby('Project_Name', as_index=False)['Amount'].sum().sort_values('Project_Name').to_dict(orient='records'),
    'extracted_disaster_projects_started_2022': started_list,
    'num_extracted_disaster_projects_started_2022': len(started_list)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_cguj2JY470StqtvTJdpADgC5': ['Funding'], 'var_call_E3A3KNZAloQm34K4K1JvVvyY': 'file_storage/call_E3A3KNZAloQm34K4K1JvVvyY.json', 'var_call_JESPpTsMF7CJnZLezqHiSbmp': 'file_storage/call_JESPpTsMF7CJnZLezqHiSbmp.json'}

exec(code, env_args)
