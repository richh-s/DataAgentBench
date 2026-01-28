code = """import json, re, pandas as pd

path_funding = var_call_03eErQ7onovmP9Kz16H3wjuq
with open(path_funding, 'r', encoding='utf-8') as f:
    funding = json.load(f)
fund_df = pd.DataFrame(funding)
fund_df['Amount'] = pd.to_numeric(fund_df['Amount'], errors='coerce').fillna(0).astype('int64')

path_docs = var_call_g8ackhFeG3EyF28ZiUZ6nNF4
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

def extract_projects_from_text(text):
    lines = [ln.strip() for ln in text.splitlines()]
    projects = []
    current_section = None
    for i, ln in enumerate(lines):
        if re.search(r'Disaster\s+Recovery\s+Projects', ln, flags=re.I):
            current_section = 'disaster'
        elif re.search(r'Capital\s+Improvement\s+Projects', ln, flags=re.I):
            current_section = 'capital'

        if not ln or len(ln) > 120 or not re.search(r'[A-Za-z]', ln):
            continue
        if re.match(r'^(To:|Prepared by:|Approved by:|Date prepared:|Meeting date:|Subject:|RECOMMENDED ACTION|DISCUSSION:|Page\s+\d+|Agenda Item)', ln, flags=re.I):
            continue
        if re.match(r'^\(cid:', ln, flags=re.I):
            continue
        if re.match(r'^(Updates:|Project Schedule|Estimated Schedule|Project Description|Complete Design|Advertise|Begin Construction|Begin construction|Complete Construction|Final Design)', ln, flags=re.I):
            continue

        window = "\\n".join(lines[i:i+20])
        if re.search(r'(Updates:|Project Description:|Project Schedule|Estimated Schedule)', window, flags=re.I):
            proj = ln
            nearby = window
            disaster = (current_section == 'disaster') or bool(re.search(r'FEMA|CalOES|CalJPIA|Woolsey|Disaster', proj + ' ' + nearby, flags=re.I))

            started_2022 = False
            m = re.search(r'Begin\s+Construction\s*:\s*([^\n\r]+)', nearby, flags=re.I)
            if not m:
                m = re.search(r'Begin\s+construction\s*:\s*([^\n\r]+)', nearby, flags=re.I)
            if m and '2022' in m.group(1):
                started_2022 = True
            if not started_2022 and re.search(r'Begin\s+Construction\s*:\s*.*\b2022\b', nearby, flags=re.I):
                started_2022 = True

            projects.append({'Project_Name': proj, 'disaster': bool(disaster), 'started_2022': bool(started_2022)})
    return projects

all_projects = []
for d in docs:
    all_projects.extend(extract_projects_from_text(d.get('text','')))

proj_df = pd.DataFrame(all_projects)
if not proj_df.empty:
    proj_df = proj_df.drop_duplicates(subset=['Project_Name'])

sel = proj_df[(proj_df['disaster']) & (proj_df['started_2022'])] if not proj_df.empty else pd.DataFrame(columns=['Project_Name'])
merged = sel.merge(fund_df, on='Project_Name', how='inner')

total = int(merged['Amount'].sum())

out = {'total_funding_disaster_projects_started_2022': total, 'matched_projects_count': int(merged['Project_Name'].nunique())}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Kk5OB2Mqpj27bh4OCdarIeqv': ['Funding'], 'var_call_03eErQ7onovmP9Kz16H3wjuq': 'file_storage/call_03eErQ7onovmP9Kz16H3wjuq.json', 'var_call_g8ackhFeG3EyF28ZiUZ6nNF4': 'file_storage/call_g8ackhFeG3EyF28ZiUZ6nNF4.json'}

exec(code, env_args)
