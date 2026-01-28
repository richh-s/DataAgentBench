code = """import json, re
import pandas as pd

# load funding
path_f = var_call_1mO1zBqsDiMHvjH7DlP4LYVA
with open(path_f,'r') as f:
    funding = json.load(f)
df_f = pd.DataFrame(funding)
# normalize amount
df_f['Amount'] = pd.to_numeric(df_f['Amount'], errors='coerce').fillna(0).astype(int)

# load civic docs
path_d = var_call_0YuvyDk8s1YDWSMEFutJShlK
with open(path_d,'r') as f:
    docs = json.load(f)
texts = "\n".join(d.get('text','') for d in docs)

# Identify disaster projects and their start fields that include 2022.
# In these agenda reports, disaster projects are typically under a heading like:
# 'Disaster Recovery Projects (Design/Construction/Not Started)' and each project block may include 'Begin Construction:' or 'Start:' etc.

# We'll parse by sections after 'Disaster Recovery Projects' and capture project names lines followed by a schedule line containing 'Begin Construction:' or 'Start' with 2022.

disaster_blocks = []
for m in re.finditer(r"Disaster Recovery Projects[\s\S]{0,20000}", texts, flags=re.IGNORECASE):
    disaster_blocks.append(m.group(0))

proj_started_2022 = set()

# project names likely appear as standalone lines (not bullet) with title case, possibly with suffix in parentheses.
# We'll scan each block for known project names from Funding that are disaster-like (contain FEMA/CalOES/CalJPIA or appear near FEMA in text)

fund_projects = df_f['Project_Name'].dropna().astype(str).unique().tolist()

# pre-filter candidate projects by those that look disaster related in funding names
cand = [p for p in fund_projects if re.search(r"FEMA|CalOES|CalJPIA|Disaster", p, flags=re.IGNORECASE)]

for block in disaster_blocks if disaster_blocks else [texts]:
    # If we didn't find explicit blocks, fall back to whole text; but we'll still require nearby 'Disaster Recovery' or FEMA context.
    for p in cand:
        # find occurrences of project name and look ahead 500 chars for 2022 and a start indicator
        for mm in re.finditer(re.escape(p), block):
            window = block[mm.end():mm.end()+800]
            if re.search(r"(Begin\s+Construction|Start|ST\s*:|Project\s+Schedule)[^\n\r]{0,200}2022", window, flags=re.IGNORECASE):
                proj_started_2022.add(p)

# Also include non-suffixed base project names where text might list without suffix but still disaster section.
# We'll take any funding project that appears in disaster block and has 'Begin Construction' line with 2022 within 300 chars.
for block in disaster_blocks if disaster_blocks else []:
    for p in fund_projects:
        for mm in re.finditer(re.escape(p), block):
            window = block[mm.end():mm.end()+500]
            if re.search(r"(Begin\s+Construction|Start)[^\n\r]{0,120}2022", window, flags=re.IGNORECASE):
                # ensure disaster-related by being in disaster section
                proj_started_2022.add(p)

# Sum funding amounts for these projects
if proj_started_2022:
    total = int(df_f[df_f['Project_Name'].isin(list(proj_started_2022))]['Amount'].sum())
else:
    total = 0

out = {"total_funding": total, "num_projects": len(proj_started_2022), "projects": sorted(list(proj_started_2022))}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_MOqftnFibvUkFDBpZBPW0v1V': ['Funding'], 'var_call_1mO1zBqsDiMHvjH7DlP4LYVA': 'file_storage/call_1mO1zBqsDiMHvjH7DlP4LYVA.json', 'var_call_YcNxcpvNJ1ntUMcyfXH3rkSl': ['civic_docs'], 'var_call_0YuvyDk8s1YDWSMEFutJShlK': 'file_storage/call_0YuvyDk8s1YDWSMEFutJShlK.json'}

exec(code, env_args)
