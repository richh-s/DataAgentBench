code = """import json, re
import pandas as pd

# load funding
path_f = var_call_1mO1zBqsDiMHvjH7DlP4LYVA
with open(path_f,'r') as f:
    funding = json.load(f)
df_f = pd.DataFrame(funding)
df_f['Amount'] = pd.to_numeric(df_f['Amount'], errors='coerce').fillna(0).astype(int)

# load civic docs
path_d = var_call_0YuvyDk8s1YDWSMEFutJShlK
with open(path_d,'r') as f:
    docs = json.load(f)
texts = "\n".join(d.get('text','') for d in docs)

# find disaster sections (best-effort)
pattern = r"Disaster Recovery Projects[\s\S]{0,20000}"
disaster_blocks = [m.group(0) for m in re.finditer(pattern, texts, flags=re.IGNORECASE)]

proj_started_2022 = set()

fund_projects = df_f['Project_Name'].dropna().astype(str).unique().tolist()

# candidate disaster-like projects by name
cand = [p for p in fund_projects if re.search(r"FEMA|CalOES|CalJPIA|Disaster", p, flags=re.IGNORECASE)]

blocks_to_scan = disaster_blocks if disaster_blocks else [texts]

for block in blocks_to_scan:
    for p in cand:
        for mm in re.finditer(re.escape(p), block):
            window = block[mm.end():mm.end()+800]
            if re.search(r"(Begin\s+Construction|Start|Project\s+Schedule)[^\n\r]{0,200}2022", window, flags=re.IGNORECASE):
                proj_started_2022.add(p)

# sum funding
total = int(df_f[df_f['Project_Name'].isin(list(proj_started_2022))]['Amount'].sum()) if proj_started_2022 else 0
out = {"total_funding": total, "num_projects": len(proj_started_2022), "projects": sorted(proj_started_2022)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_MOqftnFibvUkFDBpZBPW0v1V': ['Funding'], 'var_call_1mO1zBqsDiMHvjH7DlP4LYVA': 'file_storage/call_1mO1zBqsDiMHvjH7DlP4LYVA.json', 'var_call_YcNxcpvNJ1ntUMcyfXH3rkSl': ['civic_docs'], 'var_call_0YuvyDk8s1YDWSMEFutJShlK': 'file_storage/call_0YuvyDk8s1YDWSMEFutJShlK.json'}

exec(code, env_args)
