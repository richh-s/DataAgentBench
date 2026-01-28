code = """import re, json, pandas as pd, os, textwrap

# Load full civic docs
path_docs = var_call_Oryz0IW27dW9NvyP6VVPLu4l
with open(path_docs, 'r') as f:
    docs = json.load(f)
texts = [d['text'] for d in docs]
full_text = '\n'.join(texts)

# Heuristic: project lines often capitalized and followed by schedule lines.
# We will extract project name and any "Begin Construction" or similar with a date containing a year.

projects = []
current_project = None
for line in full_text.split('\n'):
    line_stripped = line.strip()
    if not line_stripped:
        continue
    # Detect project name line: not too long, title-style, contains keywords like 'Project', 'Road', 'Park', etc.
    if re.search(r'Project|Road|Park|Improvements|Repairs|Facility|Bridge|Canyon|Median|Playground|Signals', line_stripped) and len(line_stripped) < 120 and not line_stripped.startswith('('):
        current_project = line_stripped
        continue
    if current_project:
        m = re.search(r'(Begin Construction|Construction Start|Start of Construction|Project Start)[:\s]+([^\n]+)', line_stripped, re.IGNORECASE)
        if m:
            date_str = m.group(2).strip()
            projects.append({'Project_Name': current_project, 'st': date_str})
        m2 = re.search(r'(Start|Begin)\s+(Design|Planning)[:\s]+([^\n]+)', line_stripped, re.IGNORECASE)
        if m2 and not any(p['Project_Name']==current_project for p in projects):
            projects.append({'Project_Name': current_project, 'st': m2.group(3).strip()})

# Also capture explicit seasonal or month-year mentions near project names like "2022" and a Spring month
seasonal_projects = []
for proj in projects:
    st = proj['st']
    if not isinstance(st,str):
        continue
    # Normalize Spring 2022
    if ('2022' in st) and (re.search(r'Spring|March|April|May', st, re.IGNORECASE)):
        seasonal_projects.append(proj)

# Load funding table
path_fund = var_call_ifSQ1lHS8eMKbm2pSnCVnze4
with open(path_fund, 'r') as f:
    funding = json.load(f)

fund_df = pd.DataFrame(funding)
proj_df = pd.DataFrame(seasonal_projects)

if proj_df.empty:
    result = {'project_count': 0, 'total_funding': 0}
else:
    merged = fund_df.merge(proj_df, on='Project_Name', how='inner')
    merged['Amount'] = pd.to_numeric(merged['Amount'], errors='coerce').fillna(0)
    result = {'project_count': int(merged['Project_Name'].nunique()), 'total_funding': int(merged['Amount'].sum())}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_Oryz0IW27dW9NvyP6VVPLu4l': 'file_storage/call_Oryz0IW27dW9NvyP6VVPLu4l.json', 'var_call_ifSQ1lHS8eMKbm2pSnCVnze4': 'file_storage/call_ifSQ1lHS8eMKbm2pSnCVnze4.json'}

exec(code, env_args)
