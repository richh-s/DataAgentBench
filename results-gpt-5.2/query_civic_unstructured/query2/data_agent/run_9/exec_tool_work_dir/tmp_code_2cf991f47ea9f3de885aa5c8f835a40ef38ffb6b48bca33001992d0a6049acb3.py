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

# Identify park-related projects completed in 2022 by scanning documents for each project name line and nearby completion info.
texts = [d.get('text','') for d in docs]
all_text = "\n".join(texts)

project_names = df_fund['Project_Name'].dropna().unique().tolist()

completed_2022_projects = set()

# heuristic: if a project name appears, look within next 200 chars for 'completed' and '2022' (or month in 2022)
for pn in project_names:
    if not pn or len(pn) < 4:
        continue
    # park-related by name keywords
    if not re.search(r'\bpark\b|playground|bluffs|skate', pn, flags=re.I):
        continue
    # search occurrences
    for m in re.finditer(re.escape(pn), all_text):
        start = m.start()
        window = all_text[start:start+300]
        if re.search(r'completed[^\n\.]{0,80}2022|completed[^\n\.]{0,80}(January|February|March|April|May|June|July|August|September|October|November|December)\s+2022', window, flags=re.I):
            completed_2022_projects.add(pn)
            break

# If still empty/limited, also accept if line contains 'Construction was completed' and '2022' and project name is in same paragraph.
if True:
    # split into paragraphs
    paras = re.split(r'\n\s*\n', all_text)
    for para in paras:
        if not re.search(r'completed\s+\w+\s+2022|completed\s+\w+\s*\d{4}|completed\s+November\s+2022|completed\s+December\s+2022', para, flags=re.I):
            continue
        if '2022' not in para:
            continue
        for pn in project_names:
            if not pn or len(pn) < 4:
                continue
            if not re.search(r'\bpark\b|playground|bluffs|skate', pn, flags=re.I):
                continue
            if pn in para:
                # ensure completed in 2022
                if re.search(r'completed\s+\w+\s+2022|completed\s+(January|February|March|April|May|June|July|August|September|October|November|December)\s+2022', para, flags=re.I):
                    completed_2022_projects.add(pn)

# compute total funding
mask = df_fund['Project_Name'].isin(sorted(completed_2022_projects))
total = int(df_fund.loc[mask, 'Amount'].sum())

out = {
    "total_funding": total,
    "completed_2022_park_related_projects": sorted(completed_2022_projects)
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_G9PPPAAnLCfzTegQL8L8MWn2': 'file_storage/call_G9PPPAAnLCfzTegQL8L8MWn2.json', 'var_call_OpiSgCFi4ICBYwei30tOcC07': 'file_storage/call_OpiSgCFi4ICBYwei30tOcC07.json'}

exec(code, env_args)
