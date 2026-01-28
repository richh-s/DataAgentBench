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

texts = [d.get('text','') for d in docs]
all_text = "\n".join(texts)

project_names = df_fund['Project_Name'].dropna().unique().tolist()

completed_2022_projects = set()

park_kw = re.compile(r'\bpark\b|playground|bluffs|skate', flags=re.I)
completed_2022_kw = re.compile(r'completed[^\n\.]{0,80}2022|completed[^\n\.]{0,80}(January|February|March|April|May|June|July|August|September|October|November|December)\\s+2022', flags=re.I)

for pn in project_names:
    if not pn or len(pn) < 4:
        continue
    if not park_kw.search(pn):
        continue
    for m in re.finditer(re.escape(pn), all_text):
        window = all_text[m.start():m.start()+300]
        if completed_2022_kw.search(window):
            completed_2022_projects.add(pn)
            break

paras = re.split(r'\n\s*\n', all_text)
para_completed_2022 = re.compile(r'completed\\s+(January|February|March|April|May|June|July|August|September|October|November|December)\\s+2022', flags=re.I)
for para in paras:
    if '2022' not in para:
        continue
    if not para_completed_2022.search(para):
        continue
    for pn in project_names:
        if not pn or len(pn) < 4:
            continue
        if not park_kw.search(pn):
            continue
        if pn in para:
            completed_2022_projects.add(pn)

mask = df_fund['Project_Name'].isin(sorted(completed_2022_projects))
total = int(df_fund.loc[mask, 'Amount'].sum())

out = {"total_funding": total, "projects": sorted(completed_2022_projects)}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_G9PPPAAnLCfzTegQL8L8MWn2': 'file_storage/call_G9PPPAAnLCfzTegQL8L8MWn2.json', 'var_call_OpiSgCFi4ICBYwei30tOcC07': 'file_storage/call_OpiSgCFi4ICBYwei30tOcC07.json'}

exec(code, env_args)
