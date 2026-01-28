code = """import json, re, pandas as pd

path_docs = var_call_SSZmptyxIbYw1XWwfIPLXVpE
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

path_fund = var_call_GraUd7Ag9ux7CHFKSfpEMYu6
with open(path_fund, 'r', encoding='utf-8') as f:
    fund = json.load(f)

df_fund = pd.DataFrame(fund)
df_fund['Total_Amount'] = pd.to_numeric(df_fund['Total_Amount'], errors='coerce').fillna(0).astype(int)

# known project names set for validation
known = set(df_fund['Project_Name'].astype(str).tolist())

projects = set()
for d in docs:
    lines = d.get('text','').splitlines()
    for i, line in enumerate(lines):
        m = re.search(r'Begin Construction:\s*(.+)', line)
        if not m:
            continue
        begin = m.group(1).strip()
        if ('Spring 2022' not in begin) and ('Spring, 2022' not in begin) and ('2022-Spring' not in begin):
            continue
        # scan up to 25 lines above for an exact match to known project names
        name = None
        for j in range(i-1, max(-1, i-26), -1):
            cand = lines[j].strip()
            if cand in known:
                name = cand
                break
        if name:
            projects.add(name)

# compute totals
if projects:
    df_sel = pd.DataFrame({'Project_Name': sorted(projects)})
    df_join = df_sel.merge(df_fund, on='Project_Name', how='left')
    total_funding = int(df_join['Total_Amount'].sum())
    count_projects = int(df_sel.shape[0])
else:
    count_projects = 0
    total_funding = 0

result = {'projects_started_spring_2022_count': count_projects, 'total_funding_amount': total_funding, 'projects': sorted(projects)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_SSZmptyxIbYw1XWwfIPLXVpE': 'file_storage/call_SSZmptyxIbYw1XWwfIPLXVpE.json', 'var_call_GraUd7Ag9ux7CHFKSfpEMYu6': 'file_storage/call_GraUd7Ag9ux7CHFKSfpEMYu6.json', 'var_call_uOoJ6qJLXemF7CfaWHynOGJA': {'projects_started_spring_2022_count': 10, 'total_funding_amount': 87000, 'projects': ['Fire.', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'anticipated to have a final design by March 2022. The project will be', 'beginning in Spring 2022.', 'is finalizing the bid documents.', 'scheduled for the April 11, 2022 Council meeting.', 'sending this project out to bid during the Spring of 2022.', 'that was damaged by the Woolsey Fire.', 'timber with non-combustible materials.']}}

exec(code, env_args)
