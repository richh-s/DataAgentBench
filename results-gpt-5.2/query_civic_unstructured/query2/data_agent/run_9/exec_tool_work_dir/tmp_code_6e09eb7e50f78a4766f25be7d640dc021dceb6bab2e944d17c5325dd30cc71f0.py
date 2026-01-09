code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

docs = load_records(var_call_G9PPPAAnLCfzTegQL8L8MWn2)
fund = load_records(var_call_OpiSgCFi4ICBYwei30tOcC07)

df_fund = pd.DataFrame(fund)
df_fund['Amount'] = pd.to_numeric(df_fund['Amount'], errors='coerce').fillna(0).astype(int)

all_text = "\n".join([d.get('text','') for d in docs])
project_names = df_fund['Project_Name'].dropna().unique().tolist()

park_kw = re.compile(r'\bpark\b|playground|bluffs|skate', re.I)
completed_2022_kw = re.compile(r'completed.*2022', re.I)

completed_2022_projects = set()

for pn in project_names:
    if not pn or len(pn) < 4:
        continue
    if not park_kw.search(pn):
        continue
    for m in re.finditer(re.escape(pn), all_text):
        window = all_text[m.start():m.start()+250]
        if completed_2022_kw.search(window):
            completed_2022_projects.add(pn)
            break

# refine: ensure month-year pattern or explicit 2022 after completed within window
months = '(January|February|March|April|May|June|July|August|September|October|November|December)'
completed_month_2022 = re.compile('completed[^\n\.]{0,80}'+months+'\\s+2022|Construction was completed[^\n\.]{0,80}'+months+'\\s+2022|completed[^\n\.]{0,80}2022', re.I)

final_projects = set()
for pn in completed_2022_projects:
    for m in re.finditer(re.escape(pn), all_text):
        window = all_text[m.start():m.start()+400]
        if completed_month_2022.search(window):
            final_projects.add(pn)
            break

mask = df_fund['Project_Name'].isin(sorted(final_projects))
total = int(df_fund.loc[mask, 'Amount'].sum())

out = {"total_funding": total, "projects": sorted(final_projects)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_G9PPPAAnLCfzTegQL8L8MWn2': 'file_storage/call_G9PPPAAnLCfzTegQL8L8MWn2.json', 'var_call_OpiSgCFi4ICBYwei30tOcC07': 'file_storage/call_OpiSgCFi4ICBYwei30tOcC07.json'}

exec(code, env_args)
