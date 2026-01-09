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

# helper to find projects with Begin Construction: Spring 2022 (or Spring 2022)
# Parse sections as: project name line, followed by up to next blank-ish line? We'll do regex capturing.
pattern = re.compile(r"\n(?P<name>[^\n]{3,120}?)\n\s*(?:\(cid:190\))?.*?Project Schedule:.*?(?:\n\s*(?:\(cid:131\))?\s*Begin Construction:\s*(?P<begin>[^\n]+))?", re.DOTALL)

# more robust: iterate lines and detect 'Begin Construction:' then take nearest preceding non-empty line as name.
projects_begin_spring2022 = set()
for d in docs:
    text = d.get('text','')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        m = re.search(r"Begin Construction:\s*(.+)", line)
        if not m:
            continue
        begin = m.group(1).strip()
        if 'Spring 2022' not in begin and 'Spring, 2022' not in begin and '2022 Spring' not in begin:
            continue
        # find project name above
        j = i-1
        name = None
        while j >= 0:
            cand = lines[j].strip()
            if cand == '' or cand.startswith('(') or cand.lower().startswith('project schedule') or cand.lower().startswith('updates') or cand.lower().startswith('estimated schedule') or cand.lower().startswith('project description'):
                j -= 1
                continue
            # stop at headings
            if 'Capital Improvement Projects' in cand or 'Disaster Recovery Projects' in cand or 'Agenda Item' in cand or cand.startswith('Page '):
                break
            # choose first plausible as name
            if 3 <= len(cand) <= 120 and not cand.endswith(':') and not cand.lower().startswith('complete') and not cand.lower().startswith('advertise'):
                name = cand
                break
            j -= 1
        if name:
            projects_begin_spring2022.add(name)

# join to funding totals by exact Project_Name
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
