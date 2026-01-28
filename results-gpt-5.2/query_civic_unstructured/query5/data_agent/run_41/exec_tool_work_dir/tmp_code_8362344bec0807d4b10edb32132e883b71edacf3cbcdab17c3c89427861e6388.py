code = """import json, re
import pandas as pd

# Load funding
with open(var_call_1mO1zBqsDiMHvjH7DlP4LYVA, 'r') as f:
    funding = json.load(f)
df_f = pd.DataFrame(funding)
df_f['Amount'] = pd.to_numeric(df_f['Amount'], errors='coerce').fillna(0).astype(int)

# Load 2022 docs
with open(var_call_z2Qekco9lHo7XagX0PqaxbPV, 'r') as f:
    docs2022 = json.load(f)
texts = "\n".join(d.get('text','') for d in docs2022)

# Candidate projects: disaster-related by name markers
fund_projects = df_f['Project_Name'].dropna().astype(str).unique().tolist()
cand = [p for p in fund_projects if re.search(r"FEMA|CalOES|CalJPIA|Disaster", p, flags=re.IGNORECASE)]

# Determine which of these started in 2022 based on 'Begin Construction' or 'Begin Design' etc with 2022 near
start_pat = re.compile(r"(Begin\s+Construction|Begin\s+Design|Start)[^\n\r]{0,80}2022|2022[^\n\r]{0,80}(Begin\s+Construction|Begin\s+Design|Start)", flags=re.IGNORECASE)

proj_started_2022 = set()
for p in cand:
    for mm in re.finditer(re.escape(p), texts):
        window = texts[mm.end():mm.end()+1200]
        if start_pat.search(window):
            proj_started_2022.add(p)

# Sum funding
total = int(df_f[df_f['Project_Name'].isin(list(proj_started_2022))]['Amount'].sum())

print('__RESULT__:')
print(json.dumps({'total_funding': total, 'num_projects': len(proj_started_2022), 'projects': sorted(list(proj_started_2022))}))"""

env_args = {'var_call_MOqftnFibvUkFDBpZBPW0v1V': ['Funding'], 'var_call_1mO1zBqsDiMHvjH7DlP4LYVA': 'file_storage/call_1mO1zBqsDiMHvjH7DlP4LYVA.json', 'var_call_YcNxcpvNJ1ntUMcyfXH3rkSl': ['civic_docs'], 'var_call_0YuvyDk8s1YDWSMEFutJShlK': 'file_storage/call_0YuvyDk8s1YDWSMEFutJShlK.json', 'var_call_z2Qekco9lHo7XagX0PqaxbPV': 'file_storage/call_z2Qekco9lHo7XagX0PqaxbPV.json'}

exec(code, env_args)
