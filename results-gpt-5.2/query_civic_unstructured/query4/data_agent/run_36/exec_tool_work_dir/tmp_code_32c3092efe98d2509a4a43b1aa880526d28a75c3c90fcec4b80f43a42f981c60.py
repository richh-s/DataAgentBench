code = """import json, re
import pandas as pd

# Load civic docs (may be file path)
raw_docs = var_call_3q5JfbLhXNhD8MhXSU0bpBO8
if isinstance(raw_docs, str):
    with open(raw_docs, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = raw_docs

fund = var_call_CxeuNTyavwBzJpqFNvFH6isy
if isinstance(fund, str):
    with open(fund, 'r', encoding='utf-8') as f:
        fund = json.load(f)

fund_df = pd.DataFrame(fund)
if not fund_df.empty:
    fund_df['total_amount'] = fund_df['total_amount'].astype(float)

# Parse projects and schedules from docs
projects = {}
current_section = None
current_project = None

schedule_label_re = re.compile(r'^(Complete Design|Final Design|Advertise|Begin Construction|Begin construction|Complete Construction)\s*:\s*(.+)$', re.I)

for d in docs:
    text = d.get('text','')
    lines = [ln.strip() for ln in text.splitlines()]
    for ln in lines:
        if not ln:
            continue
        # section headers
        if re.search(r'^Capital Improvement Projects', ln, re.I):
            current_section = 'capital'
            continue
        if re.search(r'^Disaster Recovery Projects', ln, re.I):
            current_section = 'disaster'
            continue

        # project name heuristic: line with no colon, not bullets, not page, not agenda etc.
        if (':' not in ln and
            not re.match(r'^(\(cid:|Page\s+\d+|Agenda Item|To\s*:|Prepared by\s*:|Approved by\s*:|Date prepared\s*:|Meeting date\s*:|Subject\s*:|RECOMMENDED ACTION|DISCUSSION)', ln, re.I) and
            len(ln) >= 4 and len(ln) <= 120 and
            not re.match(r'^[\-\u2022\*]', ln)):
            # likely project name when followed by Updates/Schedule elsewhere; we accept and create/update
            current_project = ln
            if current_project not in projects:
                projects[current_project] = {'Project_Name': current_project, 'type': current_section, 'st': None, 'et': None}
            continue

        # schedule lines
        m = schedule_label_re.match(ln)
        if m and current_project:
            label = m.group(1).lower()
            val = m.group(2).strip()
            # assign start/end heuristics
            if 'begin construction' in label:
                projects[current_project]['st'] = val
            elif 'complete construction' in label:
                projects[current_project]['et'] = val
            elif 'advertise' in label and projects[current_project].get('st') is None:
                # if no begin construction, use advertise as proxy start
                projects[current_project]['st'] = val
            elif ('complete design' in label or 'final design' in label) and projects[current_project].get('st') is None:
                projects[current_project]['st'] = val

proj_df = pd.DataFrame(list(projects.values()))

# Filter for Spring 2022 start
if proj_df.empty:
    matched = proj_df
else:
    st = proj_df['st'].fillna('')
    matched = proj_df[st.str.contains(r'2022', case=False, regex=True) & st.str.contains(r'Spring', case=False, regex=True)]

# Join to funding by exact Project_Name
if matched.empty:
    n_projects = 0
    total_funding = 0
else:
    joined = matched.merge(fund_df, on='Project_Name', how='left')
    n_projects = int(joined['Project_Name'].nunique())
    total_funding = float(joined['total_amount'].fillna(0).sum())

out = {'projects_started_spring_2022': n_projects, 'total_funding_usd': int(round(total_funding))}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_3q5JfbLhXNhD8MhXSU0bpBO8': 'file_storage/call_3q5JfbLhXNhD8MhXSU0bpBO8.json', 'var_call_CxeuNTyavwBzJpqFNvFH6isy': 'file_storage/call_CxeuNTyavwBzJpqFNvFH6isy.json'}

exec(code, env_args)
