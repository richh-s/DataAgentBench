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

projects = []
current = None
in_sections = False

# project heading: fairly permissive; exclude obvious non-project lines later
proj_heading_re = re.compile(r"^[A-Z0-9][A-Za-z0-9&\-\u2019'\(\)\./,: ]{3,}$")
begin_re = re.compile(r"^\s*(?:\(?(?:cid:\d+)?\)?\s*)?Begin Construction\s*:\s*(.+)\s*$", re.IGNORECASE)

for d in docs:
    for raw_line in d.get('text','').splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if 'Capital Improvement Projects' in line or 'Disaster Recovery Projects' in line:
            in_sections = True
            continue
        if not in_sections:
            continue

        # treat heading
        if proj_heading_re.match(line) and len(line) <= 140:
            bad_starts = ('Page ', 'Agenda Item', 'Public Works', 'To:', 'Prepared by:', 'Approved by:', 'Date prepared', 'Meeting date', 'Subject:')
            bad_exact = {'Discussion','Recommended Action','RECOMMENDED ACTION','DISCUSSION','Capital Improvement Projects (Design)','Capital Improvement Projects (Construction)','Capital Improvement Projects (Not Started)','Disaster Recovery Projects (Design)','Disaster Recovery Projects (Construction)','Disaster Recovery Projects (Not Started)'}
            if line in bad_exact or line.startswith(bad_starts) or 'Project Schedule' in line or 'Estimated Schedule' in line or 'Project Updates' in line or 'Project Description' in line or 'Updates:' in line:
                continue
            current = {'Project_Name': line, 'begin': None}
            projects.append(current)
            continue

        m = begin_re.match(line)
        if m and current is not None:
            current['begin'] = m.group(1).strip()

spring2022 = sorted({p['Project_Name'] for p in projects if p.get('begin') and 'spring' in p['begin'].lower() and '2022' in p['begin'].lower()})

sel = fund_df[fund_df['Project_Name'].isin(spring2022)].copy() if spring2022 else fund_df.head(0).copy()

out = {
    'projects_started_spring_2022_count': int(len(spring2022)),
    'total_funding_usd': int(sel['total_amount'].sum()) if not sel.empty else 0,
    'projects_started_spring_2022': spring2022,
    'matched_projects_with_funding_count': int(sel['Project_Name'].nunique()) if not sel.empty else 0
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_OkBM9nRKJWllRYZdF1owa9C7': 'file_storage/call_OkBM9nRKJWllRYZdF1owa9C7.json', 'var_call_5jgLED9yFbAt2JE425ttvTwU': 'file_storage/call_5jgLED9yFbAt2JE425ttvTwU.json'}

exec(code, env_args)
