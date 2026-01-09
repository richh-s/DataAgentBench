code = """import json, re, pandas as pd

with open(var_call_1mO1zBqsDiMHvjH7DlP4LYVA,'r') as f:
    funding=json.load(f)
df=pd.DataFrame(funding)
df['Amount']=pd.to_numeric(df['Amount'], errors='coerce').fillna(0).astype(int)

with open(var_call_z2Qekco9lHo7XagX0PqaxbPV,'r') as f:
    docs=json.load(f)
texts='|'.join(d.get('text','') for d in docs)

fund_projects=df['Project_Name'].dropna().astype(str).unique().tolist()

cand=[p for p in fund_projects if re.search(r'FEMA|CalOES|CalJPIA|Disaster', p, flags=re.IGNORECASE)]

start_pat=re.compile(r'(Begin\s+Construction|Begin\s+Design|Start)[^\|]{0,120}2022|2022[^\|]{0,120}(Begin\s+Construction|Begin\s+Design|Start)', flags=re.IGNORECASE)

started=set()
for p in cand:
    for m in re.finditer(re.escape(p), texts):
        window=texts[m.end():m.end()+1500]
        if start_pat.search(window):
            started.add(p)

total=int(df[df['Project_Name'].isin(list(started))]['Amount'].sum())
print('__RESULT__:')
print(json.dumps({'total_funding': total, 'num_projects': len(started), 'projects': sorted(list(started))}))"""

env_args = {'var_call_MOqftnFibvUkFDBpZBPW0v1V': ['Funding'], 'var_call_1mO1zBqsDiMHvjH7DlP4LYVA': 'file_storage/call_1mO1zBqsDiMHvjH7DlP4LYVA.json', 'var_call_YcNxcpvNJ1ntUMcyfXH3rkSl': ['civic_docs'], 'var_call_0YuvyDk8s1YDWSMEFutJShlK': 'file_storage/call_0YuvyDk8s1YDWSMEFutJShlK.json', 'var_call_z2Qekco9lHo7XagX0PqaxbPV': 'file_storage/call_z2Qekco9lHo7XagX0PqaxbPV.json', 'var_call_ZthsKbieV1eqdO7yBF6vIdJR': {'n': 500}, 'var_call_igYpGVqfnS8uWdcfhdZ0AuSw': {'docs': 5, 'first_filename': 'malibucity_agenda__01262022-1835.txt', 'first_len': 16311}, 'var_call_9VMOQfkkfXtNvW28GMxBXEhj': {'has_disaster': True, 'len': 78968}}

exec(code, env_args)
