code = """import json, re
import pandas as pd

# Load civic docs
path_docs = var_call_OkBM9nRKJWllRYZdF1owa9C7
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Load funding totals per project
path_fund = var_call_5jgLED9yFbAt2JE425ttvTwU
with open(path_fund, 'r', encoding='utf-8') as f:
    fund = json.load(f)
fund_df = pd.DataFrame(fund)
if not fund_df.empty:
    fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)

# Parse project blocks and find those with Begin Construction: Spring 2022
projects = []
current = None
in_capital_or_disaster = False

proj_heading_re = re.compile(r'^[A-Z0-9][A-Za-z0-9&\-\u2019\'\(\)\./,: ]{3,}$')
begin_re = re.compile(r'^\s*\(?(?:cid:\d+)?\)?\s*Begin Construction\s*:\s*(.+)\s*$', re.IGNORECASE)

for d in docs:
    text = d.get('text','')
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        # section markers
        if 'Capital Improvement Projects' in line or 'Disaster Recovery Projects' in line:
            in_capital_or_disaster = True
            continue
        if not in_capital_or_disaster:
            continue
        # detect heading lines (project name)
        if 'Project Schedule' in line or 'Estimated Schedule' in line or 'Project Description' in line or 'Updates' in line:
            continue
        if proj_heading_re.match(line) and len(line) <= 120:
            # avoid generic headings
            bad = {'Discussion','Recommended Action','RECOMMENDED ACTION','DISCUSSION','Agenda Report','Public Works Commission','Agenda Item # 4.B.'}
            if line in bad:
                continue
            # start new project
            current = {'Project_Name': line, 'begin': None}
            projects.append(current)
            continue
        m = begin_re.match(line)
        if m and current is not None:
            current['begin'] = m.group(1).strip()

# Filter for Spring 2022 begin
spring2022 = []
for p in projects:
    b = p.get('begin')
    if not b:
        continue
    b_norm = b.lower()
    if 'spring' in b_norm and '2022' in b_norm:
        spring2022.append(p['Project_Name'])

# Deduplicate
spring2022 = sorted(set(spring2022))

# Join with funding totals (exact match)
if spring2022:
    sel = fund_df[fund_df['Project_Name'].isin(spring2022)].copy()
    count = len(spring2022)
    total = int(sel['total_amount'].sum())
else:
    count = 0
    total = 0

out = {'projects_started_spring_2022_count': count, 'total_funding_usd': total, 'matched_projects_with_funding_count': int(fund_df[fund_df['Project_Name'].isin(spring2022)]['Project_Name'].nunique())}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_OkBM9nRKJWllRYZdF1owa9C7': 'file_storage/call_OkBM9nRKJWllRYZdF1owa9C7.json', 'var_call_5jgLED9yFbAt2JE425ttvTwU': 'file_storage/call_5jgLED9yFbAt2JE425ttvTwU.json'}

exec(code, env_args)
