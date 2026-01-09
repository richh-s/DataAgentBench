code = """import json, re, pandas as pd

funding_src = var_call_DxZXrgir7bSPofq0krrauG1m
if isinstance(funding_src, str) and funding_src.endswith('.json'):
    with open(funding_src, 'r', encoding='utf-8') as f:
        funding = json.load(f)
else:
    funding = funding_src

docs_src = var_call_JfAXMaifEjUuzNF65e2KwdVd
if isinstance(docs_src, str) and docs_src.endswith('.json'):
    with open(docs_src, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = docs_src

fund_df = pd.DataFrame(funding)
fund_df['Project_Name'] = fund_df['Project_Name'].astype(str)
fund_df['Amount'] = pd.to_numeric(fund_df['Amount'], errors='coerce').fillna(0).astype(int)

# disaster-related projects by name keyword
pat_disaster = re.compile('\\b(FEMA|CalOES|CalJPIA|disaster|Woolsey|fire|emergency)\\b', re.IGNORECASE)
disaster_projects = set(fund_df.loc[fund_df['Project_Name'].str.contains(pat_disaster, regex=True, na=False), 'Project_Name'])

# determine which of these started in 2022 from docs: if doc contains project name AND within doc there is any 'Begin'/'Start' line with 2022
beg2022 = re.compile('\\b(Begin|Start)\\b[^\\n]{0,120}2022', re.IGNORECASE)

started_2022 = set()
for d in docs:
    text = d.get('text') or ''
    if '2022' not in text:
        continue
    if not beg2022.search(text):
        continue
    tl = text.lower()
    for pn in disaster_projects:
        if pn.lower() in tl:
            started_2022.add(pn)

# if still empty, broaden to any line containing 2022 and (Begin Construction|Start)
if len(started_2022)==0:
    broad = re.compile('2022', re.IGNORECASE)
    for d in docs:
        text = d.get('text') or ''
        if '2022' not in text:
            continue
        # check per project window for line with begin/start and 2022 maybe separated by newline
        tl = text.lower()
        for pn in disaster_projects:
            p = pn.lower()
            idx = tl.find(p)
            if idx==-1:
                continue
            window = text[idx:idx+1500]
            if re.search('\\b(begin|start)\\b', window, re.IGNORECASE) and '2022' in window:
                started_2022.add(pn)

subset = fund_df[fund_df['Project_Name'].isin(started_2022)]
total = int(subset['Amount'].sum())

print('__RESULT__:')
print(json.dumps({'total_funding': total, 'n_projects': int(subset['Project_Name'].nunique()), 'projects': sorted(list(started_2022))[:50]}))"""

env_args = {'var_call_DxZXrgir7bSPofq0krrauG1m': 'file_storage/call_DxZXrgir7bSPofq0krrauG1m.json', 'var_call_JfAXMaifEjUuzNF65e2KwdVd': 'file_storage/call_JfAXMaifEjUuzNF65e2KwdVd.json', 'var_call_TCTs3cGEi5kICAZ0yDI5sy91': ['civic_docs'], 'var_call_umEJ4GpybYpolnXPUAjvCwXZ': ['Funding'], 'var_call_31KAvYQlBKpc4NWlA31swVWY': {'ok': True}, 'var_call_SJnV9u6cAf5Qujvm4JKQkVV2': {'compiled': True}, 'var_call_XoRyC4xNZGy1G0tpGAUQ45o2': {'total_funding': 0, 'n_projects': 0}}

exec(code, env_args)
