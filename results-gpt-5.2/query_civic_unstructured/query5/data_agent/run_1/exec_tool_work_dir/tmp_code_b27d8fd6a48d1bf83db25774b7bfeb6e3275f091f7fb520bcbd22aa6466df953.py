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
project_names = list(fund_df['Project_Name'].dropna().unique())

pat_disaster_name = re.compile('\\b(FEMA|CalOES|CalJPIA|disaster|Woolsey|fire|emergency)\\b', re.IGNORECASE)
start_line_pat = re.compile('\\b(Begin|Start)\\b[^\\n]{0,120}2022', re.IGNORECASE)

start_2022 = set()

for d in docs:
    text = d.get('text') or ''
    if '2022' not in text:
        continue
    lower_text = text.lower()
    for pn in project_names:
        if pn in ('Discussion', 'Recommended Action'):
            continue
        if not pat_disaster_name.search(pn):
            continue
        pnl = pn.lower()
        pos = 0
        while True:
            idx = lower_text.find(pnl, pos)
            if idx == -1:
                break
            window = text[idx:idx+1200]
            if start_line_pat.search(window):
                start_2022.add(pn)
                break
            for line in window.splitlines()[:50]:
                if '2022' in line and re.search('\\b(begin|start)\\b', line, re.IGNORECASE):
                    start_2022.add(pn)
                    break
            if pn in start_2022:
                break
            pos = idx + len(pnl)

if len(start_2022) == 0:
    # very conservative fallback: treat as started in 2022 if name contains FEMA/CalOES/CalJPIA and doc has any begin/start 2022
    for d in docs:
        text = d.get('text') or ''
        if not start_line_pat.search(text):
            continue
        tl = text.lower()
        for pn in project_names:
            if pat_disaster_name.search(pn) and pn.lower() in tl:
                start_2022.add(pn)

subset = fund_df[fund_df['Project_Name'].isin(start_2022)]

total = int(subset['Amount'].sum())

print('__RESULT__:')
print(json.dumps({'total_funding': total, 'n_projects': int(subset['Project_Name'].nunique())}))"""

env_args = {'var_call_DxZXrgir7bSPofq0krrauG1m': 'file_storage/call_DxZXrgir7bSPofq0krrauG1m.json', 'var_call_JfAXMaifEjUuzNF65e2KwdVd': 'file_storage/call_JfAXMaifEjUuzNF65e2KwdVd.json', 'var_call_TCTs3cGEi5kICAZ0yDI5sy91': ['civic_docs'], 'var_call_umEJ4GpybYpolnXPUAjvCwXZ': ['Funding'], 'var_call_31KAvYQlBKpc4NWlA31swVWY': {'ok': True}, 'var_call_SJnV9u6cAf5Qujvm4JKQkVV2': {'compiled': True}}

exec(code, env_args)
