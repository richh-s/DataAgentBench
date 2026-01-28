code = """import json, re
import pandas as pd

# load funding rows
path_f = var_call_UxqmfWeRLCl4Ob5IcHAX4Xi2
with open(path_f, 'r', encoding='utf-8') as f:
    funding = json.load(f)

df_f = pd.DataFrame(funding)
df_f['Amount'] = pd.to_numeric(df_f['Amount'], errors='coerce').fillna(0).astype(int)

# load civic docs containing disaster section
path_docs = var_call_jwVeRgw1Ju7fnQfGQQLXxdpg
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

texts = [d.get('text','') for d in docs]

# Extract Disaster Recovery project blocks and find start dates (st) year 2022
# Heuristic: within disaster section, each project has a name line then 'Project Schedule' with 'Begin' or 'Start' containing year.

disaster_projects_started_2022 = set()

for text in texts:
    # locate disaster section
    m = re.search(r'Disaster Recovery Projects.*?(?=\n\s*(Capital Improvement Projects|$))', text, flags=re.IGNORECASE|re.DOTALL)
    if not m:
        # sometimes combined report; try find from 'Disaster Recovery Projects' to end
        m = re.search(r'Disaster Recovery Projects.*', text, flags=re.IGNORECASE|re.DOTALL)
    if not m:
        continue
    sec = m.group(0)

    # split by blank lines and look for pattern: name line followed by schedule lines
    # We'll scan for likely project headings: lines with Title Case and not bullets
    lines = [ln.strip() for ln in sec.splitlines()]
    # create indices of candidate headings: non-empty, not starting with '(' or 'cid', and not containing ':' and length<120
    cand = []
    for i,ln in enumerate(lines):
        if not ln: 
            continue
        if re.match(r'\(cid:|[\u2022\-\*])', ln):
            continue
        if ln.lower() in {'disaster recovery projects','disaster recovery projects (design)','disaster recovery projects (construction)','disaster recovery projects (not started)','project schedule','updates','estimated schedule','project description','discussion','recommended action'}:
            continue
        if 'agenda item' in ln.lower() or 'page ' in ln.lower():
            continue
        if len(ln) > 120:
            continue
        # headings often have no period at end
        cand.append(i)

    # For each candidate heading, look ahead up to 20 lines for Begin/Start and 2022
    for idx in cand:
        name = lines[idx]
        window = '\n'.join(lines[idx:idx+25])
        if re.search(r'\b(Begin|Start)\b.*2022', window, flags=re.IGNORECASE):
            # filter out obvious non-projects like Chair/Prepared by etc
            if re.search(r'\b(To|Prepared by|Approved by|Date prepared|Meeting date|Subject)\b', name, flags=re.IGNORECASE):
                continue
            disaster_projects_started_2022.add(name)

# Join to funding by exact project name
started_names = sorted(disaster_projects_started_2022)

# compute sum for matching names
match_df = df_f[df_f['Project_Name'].isin(started_names)]

total = int(match_df['Amount'].sum())

out = {
    'total_funding': total,
    'matched_projects_count': int(match_df['Project_Name'].nunique()),
    'matched_projects': sorted(match_df['Project_Name'].unique().tolist())
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_DQgvNaBjVrnO8a12rz6Frntv': ['Funding'], 'var_call_UxqmfWeRLCl4Ob5IcHAX4Xi2': 'file_storage/call_UxqmfWeRLCl4Ob5IcHAX4Xi2.json', 'var_call_jwVeRgw1Ju7fnQfGQQLXxdpg': 'file_storage/call_jwVeRgw1Ju7fnQfGQQLXxdpg.json'}

exec(code, env_args)
