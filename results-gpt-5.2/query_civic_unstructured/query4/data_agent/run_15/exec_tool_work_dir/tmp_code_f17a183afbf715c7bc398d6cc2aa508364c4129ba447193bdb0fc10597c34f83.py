code = """import json, re, pandas as pd

# load civic docs
path_docs = var_call_SSZmptyxIbYw1XWwfIPLXVpE
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# load funding totals
path_fund = var_call_GraUd7Ag9ux7CHFKSfpEMYu6
with open(path_fund, 'r', encoding='utf-8') as f:
    fund = json.load(f)

df_fund = pd.DataFrame(fund)
if not df_fund.empty:
    df_fund['Total_Amount'] = pd.to_numeric(df_fund['Total_Amount'], errors='coerce').fillna(0).astype(int)

projects_begin_spring2022 = set()
for d in docs:
    text = d.get('text','')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        m = re.search(r'Begin Construction:\s*(.+)', line)
        if not m:
            continue
        begin = m.group(1).strip()
        if ('Spring 2022' not in begin) and ('Spring, 2022' not in begin) and ('2022-Spring' not in begin):
            continue
        j = i-1
        name = None
        while j >= 0:
            cand = lines[j].strip()
            if cand == '' or cand.startswith('('):
                j -= 1
                continue
            low = cand.lower()
            if low.startswith('project schedule') or low.startswith('estimated schedule') or low.startswith('updates') or low.startswith('project description'):
                j -= 1
                continue
            if ('capital improvement projects' in low) or ('disaster recovery projects' in low) or ('agenda item' in low) or cand.startswith('Page '):
                break
            if 3 <= len(cand) <= 140 and (not cand.endswith(':')):
                if not (low.startswith('complete') or low.startswith('advertise') or low.startswith('final design') or low.startswith('begin construction')):
                    name = cand
                    break
            j -= 1
        if name:
            projects_begin_spring2022.add(name)

if projects_begin_spring2022:
    df_sel = pd.DataFrame({'Project_Name': sorted(projects_begin_spring2022)})
    df_join = df_sel.merge(df_fund, on='Project_Name', how='left')
    df_join['Total_Amount'] = df_join['Total_Amount'].fillna(0).astype(int)
    total_funding = int(df_join['Total_Amount'].sum())
    count_projects = int(df_sel.shape[0])
else:
    count_projects = 0
    total_funding = 0

result = {'projects_started_spring_2022_count': count_projects, 'total_funding_amount': total_funding, 'projects': sorted(projects_begin_spring2022)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_SSZmptyxIbYw1XWwfIPLXVpE': 'file_storage/call_SSZmptyxIbYw1XWwfIPLXVpE.json', 'var_call_GraUd7Ag9ux7CHFKSfpEMYu6': 'file_storage/call_GraUd7Ag9ux7CHFKSfpEMYu6.json'}

exec(code, env_args)
