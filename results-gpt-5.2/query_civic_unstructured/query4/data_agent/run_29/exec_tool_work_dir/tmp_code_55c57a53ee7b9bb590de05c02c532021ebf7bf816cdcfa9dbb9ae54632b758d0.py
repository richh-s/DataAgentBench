code = """import json, re, pandas as pd

# load mongo docs
p = var_call_LsFxrlemFokwe9uT8vEf3N2N
with open(p, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# load funding aggregation
pf = var_call_g33MN4t2mE4gZZMmehaPWi0s
with open(pf, 'r', encoding='utf-8') as f:
    fund = json.load(f)
fund_df = pd.DataFrame(fund)
if not fund_df.empty:
    fund_df['Total_Amount'] = pd.to_numeric(fund_df['Total_Amount'], errors='coerce').fillna(0).astype(int)

spring2022_projects = set()

# patterns for start schedule lines
start_line_re = re.compile(r'^(?:\s*\(cid:[^)]+\)\s*)?(?:\*\s*)?(?:Project\s+Schedule|Estimated\s+Schedule|Project\s+Timeline|Schedule)\b', re.I)
start_value_re = re.compile(r'\b(?:Start|Begin\s+Construction|Begin\s+Design|Kickoff|Commence)\s*:\s*(.+)$', re.I)

# also handle single line like 'Begin Construction: Spring 2022'
begin_line_re = re.compile(r'\bBegin\s+Construction\s*:\s*(.+)$', re.I)
start_line2_re = re.compile(r'\bStart\s*:\s*(.+)$', re.I)

# project header heuristic: line with no colon, not bullet, and titlecase-ish
stop_headers = set([
    'Capital Improvement Projects (Design)','Capital Improvement Projects (Construction)','Capital Improvement Projects (Not Started)',
    'Disaster Recovery Projects (Construction)','Disaster Recovery Projects (Design)','Disaster Recovery Projects (Not Started)',
    'Disaster Recovery Projects','Capital Improvement Projects'
])

for d in docs:
    text = d.get('text','') or ''
    lines = [ln.strip() for ln in text.splitlines()]
    current_project = None
    in_schedule = False
    for ln in lines:
        if not ln:
            continue
        # detect project header
        if ':' not in ln and len(ln) <= 120 and not ln.lower().startswith(('page ','agenda item')):
            # ignore known section headers
            if ln in stop_headers:
                in_schedule = False
                continue
            # many project titles appear as standalone lines; update current_project
            # Avoid generic words
            if len(ln.split())>=2 and not ln.lower().startswith(('updates','project description','discussion','recommended action')):
                current_project = ln
                in_schedule = False
                continue

        if start_line_re.search(ln):
            in_schedule = True
            continue

        if in_schedule and current_project:
            m = start_value_re.search(ln)
            if m:
                val = m.group(1).strip()
                if '2022' in val and 'spring' in val.lower():
                    spring2022_projects.add(current_project)
                continue

        # catch direct begin construction lines even if schedule header missed
        if current_project:
            m2 = begin_line_re.search(ln) or start_line2_re.search(ln)
            if m2:
                val = m2.group(1).strip()
                if '2022' in val and 'spring' in val.lower():
                    spring2022_projects.add(current_project)

# Join with funding
proj_list = sorted(spring2022_projects)
if len(proj_list)==0:
    out = {"spring_2022_project_count": 0, "total_funding": 0, "projects": []}
else:
    join_df = pd.DataFrame({'Project_Name': proj_list})
    merged = join_df.merge(fund_df, on='Project_Name', how='left')
    merged['Total_Amount'] = merged['Total_Amount'].fillna(0).astype(int)
    total = int(merged['Total_Amount'].sum())
    out = {"spring_2022_project_count": int(len(proj_list)), "total_funding": total, "projects": merged.to_dict(orient='records')}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_oGKkLTAqrX3yv6M0Y3GhajTM': ['Funding'], 'var_call_K7k9fbr5NW4TUhWbEyoJRYta': ['civic_docs'], 'var_call_LsFxrlemFokwe9uT8vEf3N2N': 'file_storage/call_LsFxrlemFokwe9uT8vEf3N2N.json', 'var_call_g33MN4t2mE4gZZMmehaPWi0s': 'file_storage/call_g33MN4t2mE4gZZMmehaPWi0s.json'}

exec(code, env_args)
